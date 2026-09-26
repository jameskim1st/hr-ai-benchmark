#!/usr/bin/env python3
"""
wiki/usecases/*.md → JSON 추출 스크립트
HTML 산출물에 임베딩할 데이터를 생성합니다.
"""

import os
import re
import json
import yaml
from pathlib import Path

USECASES_DIR = Path(__file__).parent.parent / "wiki" / "usecases"
OUTPUT_PATH = Path(__file__).parent.parent / "wiki" / "exports" / "usecases.json"


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """YAML frontmatter와 body를 분리합니다."""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1])
                body = parts[2].strip()
                return fm or {}, body
            except yaml.YAMLError:
                pass
    return {}, content


def extract_section(body: str, heading: str, max_lines: int = 5) -> str:
    """특정 ## 헤딩 아래의 첫 max_lines 줄을 추출합니다."""
    pattern = rf"^##\s+{re.escape(heading)}.*$"
    match = re.search(pattern, body, re.MULTILINE | re.IGNORECASE)
    if not match:
        # 부분 매칭 시도 (예: "Problem" → "Problem / Why (도입 배경)")
        pattern = rf"^##\s+.*{re.escape(heading)}.*$"
        match = re.search(pattern, body, re.MULTILINE | re.IGNORECASE)
    if not match:
        return ""

    start = match.end()
    lines = body[start:].split("\n")
    result = []
    for line in lines[1:]:  # 헤딩 다음 줄부터
        if line.startswith("## ") or line.startswith("# "):
            break
        if line.strip():
            result.append(line.strip())
        if len(result) >= max_lines:
            break
    return "\n".join(result)


def extract_summary_line(body: str) -> str:
    """기대효과 요약 라인을 추출합니다."""
    match = re.search(r"###\s+기대효과 요약\s*\n(.+)", body)
    if match:
        return match.group(1).strip()
    return ""


def extract_mermaid_blocks(body: str, max_blocks: int = 3) -> list[str]:
    """Mermaid 코드 블록을 추출합니다."""
    pattern = r"```mermaid\s*\n(.*?)```"
    matches = re.findall(pattern, body, re.DOTALL)
    return [m.strip() for m in matches[:max_blocks]]


def extract_consulting_angle(body: str, max_lines: int = 3) -> str:
    """Consulting Angle 섹션의 첫 줄들을 추출합니다."""
    return extract_section(body, "Consulting Angle", max_lines)


def process_file(filepath: Path) -> dict | None:
    """단일 markdown 파일을 처리합니다."""
    content = filepath.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(content)

    if not fm.get("title"):
        return None

    # frontmatter 필드 추출
    data = {
        "slug": fm.get("slug", filepath.stem),
        "title": fm.get("title", ""),
        "primary_category": fm.get("primary_category", ""),
        "subcategory": fm.get("subcategory", ""),
        "company": fm.get("company", ""),
        "industry": fm.get("industry", []),
        "region": fm.get("region", []),
        "vendor": fm.get("vendor", []),
        "vendor_type": fm.get("vendor_type", []),
        "confidence": fm.get("confidence", 0),
        "stage": fm.get("stage", ""),
        "tags": fm.get("tags", []),
        "first_seen": str(fm.get("first_seen", "")),
        "last_confirmed": str(fm.get("last_confirmed", "")),
    }

    # body에서 추출
    data["summary"] = extract_section(body, "Summary", 3)
    data["problem"] = extract_section(body, "Problem", 4)
    data["impact_summary"] = extract_summary_line(body)
    data["mermaid"] = extract_mermaid_blocks(body, 3)
    data["consulting"] = extract_consulting_angle(body, 3)

    # industry/region/vendor를 항상 리스트로
    for field in ["industry", "region", "vendor", "vendor_type", "tags"]:
        if isinstance(data[field], str):
            data[field] = [data[field]]
        elif not isinstance(data[field], list):
            data[field] = []

    # confidence를 float로
    try:
        data["confidence"] = float(data["confidence"])
    except (ValueError, TypeError):
        data["confidence"] = 0.0

    return data


def main():
    files = sorted(USECASES_DIR.glob("*.md"))
    print(f"Processing {len(files)} files from {USECASES_DIR}")

    usecases = []
    for f in files:
        result = process_file(f)
        if result:
            usecases.append(result)
            print(f"  OK {f.stem} (conf: {result['confidence']}, cat: {result['primary_category']})")
        else:
            print(f"  SKIP {f.stem} (no title)")

    # confidence 내림차순 정렬
    usecases.sort(key=lambda x: -x["confidence"])

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(usecases, f, ensure_ascii=False, indent=2)

    print(f"\nDONE: {len(usecases)} use cases -> {OUTPUT_PATH}")
    print(f"   File size: {OUTPUT_PATH.stat().st_size / 1024:.1f} KB")

    # 통계
    categories = {}
    for uc in usecases:
        cat = uc["primary_category"]
        categories[cat] = categories.get(cat, 0) + 1
    print("\nCategory distribution:")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"   {cat}: {count}")

    kr_count = sum(1 for uc in usecases if "kr" in uc.get("region", []))
    mermaid_count = sum(1 for uc in usecases if uc.get("mermaid"))
    print(f"\nKR cases: {kr_count}")
    print(f"Cases with Mermaid: {mermaid_count}")
    avg_conf = sum(uc["confidence"] for uc in usecases) / len(usecases) if usecases else 0
    print(f"Avg confidence: {avg_conf:.2f}")


if __name__ == "__main__":
    main()
