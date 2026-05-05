#!/usr/bin/env python3
"""
build_excel.py — wiki/exports/usecases.json + companies.json → 단일 Excel 워크북

산출물: wiki/exports/hr-ai-usecase-collection.xlsx
시트 4개:
  1. 개요          — README + schema reference + 사용법
  2. Use Cases     — 115행 × 25컬럼 (메인 데이터, AutoFilter, conditional formatting)
  3. AI 기술 분포   — long-format (use_case × subtype), Pivot Table용
  4. Companies     — 20행 × 9컬럼 (기업별 holistic view)
"""
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo


BASE = Path(__file__).parent.parent
UC_JSON = BASE / "wiki" / "exports" / "usecases.json"
CO_JSON = BASE / "wiki" / "exports" / "companies.json"
OUT = BASE / "wiki" / "exports" / "hr-ai-usecase-collection.xlsx"


# ── Korean label mappings (build_html_v6.py와 동일) ──
KR_CATEGORY = {
    "Talent Acquisition": "채용",
    "Onboarding & Transitions": "온보딩·이동",
    "Learning & Development": "학습·육성",
    "Performance & Talent Management": "성과·인재관리",
    "Total Rewards": "보상·복리후생",
    "Employee Experience & HR Ops": "EX·HR운영",
    "Strategic Workforce & Governance": "전략기획·거버넌스",
}
KR_STAGE = {
    "production": "운영",
    "pilot": "파일럿",
    "announced": "발표·계획",
    "sunset": "종료",
    "stub": "stub",
}
KR_FREQUENCY = {"daily": "일", "monthly": "월", "annual": "연", "adhoc": "수시"}
TECH_LABEL = {
    "generative": "생성형",
    "predictive": "판별·예측",
    "recognition": "인식",
    "decision-optimization": "의사결정·최적화",
    "automation": "자동화",
}
SUB_LABEL = {
    "text-generation": "텍스트 생성",
    "summarization-qa": "요약·재작성·QA",
    "multimodal": "멀티모달",
    "information-extraction": "정보 추출",
    "prediction": "예측",
    "clustering-classification": "군집·분류",
    "recommendation-ranking": "추천·랭킹",
    "ocr": "OCR",
    "speech-recognition": "음성 인식",
    "optimization": "최적화",
    "rpa": "RPA",
}
KR_REGION = {
    "kr": "🇰🇷 KR",
    "na": "N. America",
    "eu": "Europe",
    "apac": "APAC",
    "global": "Global",
}


# ── Styles ──
HEADER_FILL = PatternFill("solid", fgColor="2F4858")
HEADER_FONT = Font(name="맑은 고딕", size=12, bold=True, color="FFFFFF")
HEADER_ALIGN = Alignment(horizontal="center", vertical="center", wrap_text=True)
BODY_FONT = Font(name="맑은 고딕", size=11)
BODY_ALIGN = Alignment(horizontal="left", vertical="top", wrap_text=True)
BORDER_THIN = Border(
    left=Side(style="thin", color="E5E5E5"),
    right=Side(style="thin", color="E5E5E5"),
    top=Side(style="thin", color="E5E5E5"),
    bottom=Side(style="thin", color="E5E5E5"),
)
COVER_TITLE_FONT = Font(name="맑은 고딕", size=20, bold=True, color="2F4858")
COVER_SECTION_FONT = Font(name="맑은 고딕", size=12, bold=True, color="2F4858")

# 가독성 보조 fill
ZEBRA_FILL = PatternFill("solid", fgColor="F8F9FA")  # 짝수 row 옅은 회색
NO_FILL = PatternFill(fill_type=None)

# HR 카테고리별 색상 (7개) — 파스텔 톤, 시각 부담 적음
CATEGORY_FILL = {
    "Talent Acquisition":              PatternFill("solid", fgColor="DBE9F4"),  # 옅은 파랑
    "Onboarding & Transitions":        PatternFill("solid", fgColor="D4EDE0"),  # 옅은 청록
    "Learning & Development":          PatternFill("solid", fgColor="E5DAF0"),  # 옅은 보라
    "Performance & Talent Management": PatternFill("solid", fgColor="FCE4CB"),  # 옅은 주황
    "Total Rewards":                   PatternFill("solid", fgColor="DCEFC8"),  # 옅은 녹
    "Employee Experience & HR Ops":    PatternFill("solid", fgColor="DDDCF1"),  # 옅은 인디고
    "Strategic Workforce & Governance":PatternFill("solid", fgColor="F4D5DB"),  # 옅은 핑크
}
# AI 기술 체크 표시 (✓ 대신 ●) + 강조 fill
TECH_PARENT_CHECK_FILL = PatternFill("solid", fgColor="C5B5DB")  # 보라
TECH_SUB_CHECK_FILL = PatternFill("solid", fgColor="DDD3EC")     # 옅은 보라
CHECK_MARK = "●"

# 시트 탭 색
TAB_COLOR = {
    "개요":       "2F4858",
    "Use Cases": "1B6E3E",
    "AI 기술 분포": "5B3A8C",
    "Companies": "C2562D",
}


# ── Utility ──
def strip_html(s, max_len=None, prettify=True, target_line_len=80):
    """HTML 태그 제거 → plain text. <br>·</li>는 줄바꿈으로, 다중 공백 collapse.
    em-dash도 제거 (사용자 요청). max_len은 절대 한도 (Excel 32k 안전판) — 기본 잘림 비활성.
    prettify=True 시 문장·절 경계에 \n 자동 삽입 (Excel wrap_text 가독성 보강)."""
    if not s:
        return ""
    # <br>·</li>·</p> → 줄바꿈
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.IGNORECASE)
    s = re.sub(r"</li>", "\n", s, flags=re.IGNORECASE)
    s = re.sub(r"</p>", "\n", s, flags=re.IGNORECASE)
    s = re.sub(r"<li>", "• ", s, flags=re.IGNORECASE)
    # <ul>/<ol> opening tags → 빈 줄 (bullet 그룹 시작 시각화)
    s = re.sub(r"<ul[^>]*>", "", s, flags=re.IGNORECASE)
    s = re.sub(r"<ol[^>]*>", "", s, flags=re.IGNORECASE)
    s = re.sub(r"</ul>", "", s, flags=re.IGNORECASE)
    s = re.sub(r"</ol>", "", s, flags=re.IGNORECASE)
    # 나머지 태그 제거
    s = re.sub(r"<[^>]+>", "", s)
    # HTML entity
    s = s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&nbsp;", " ")
    # 다중 공백·다중 줄바꿈 정리
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n[ \t]*\n[ \t]*\n+", "\n\n", s)
    s = s.strip()
    # em-dash 제거 (사용자 요청), 줄별로 처리 (\n 보존)
    lines = s.split('\n')
    lines = [_remove_emdash_line(l) for l in lines]
    s = '\n'.join(lines)
    # max_len은 명시적으로 지정한 경우에만 잘림 적용 (기본은 잘림 X)
    if max_len and len(s) > max_len:
        s = s[: max_len - 1] + "…"
    # prettify: 긴 문장에 자동 \n 삽입 (Excel 가독성)
    if prettify:
        s = prettify_for_excel(s, target_line_len=target_line_len)
    return s


def _remove_emdash_line(line):
    """단일 line에서 em-dash 제거 (build_excel.remove_emdash와 동일)."""
    line = re.sub(r' +— +', ': ', line)
    line = re.sub(r' —|— ', ':', line)
    line = line.replace('—', ' ')
    line = re.sub(r'  +', ' ', line)
    return line.strip()


def prettify_for_excel(s, target_line_len=80):
    """Excel cell 가독성: 긴 paragraph에 자동 \n 삽입.
    - 기존 \n 보존
    - 줄이 target_line_len보다 길면 문장 종결(. ! ? 。) → 콜론(:) → 쉼표(, ·) 순으로 분할
    - 분할 못 하면 hard wrap (80자 단위)
    - wrap_text=True는 컬럼 폭 기준 wrap만 가능 → \n으로 logical break 부여."""
    if not s:
        return s
    out_lines = []
    for line in s.split('\n'):
        line = line.rstrip()
        if len(line) <= target_line_len:
            out_lines.append(line)
            continue
        # 1) 문장 종결 split (마침표·물음표·느낌표 + 공백)
        parts = re.split(r'(?<=[\.\!\?。])\s+', line)
        if len(parts) > 1:
            for p in parts:
                if len(p) <= target_line_len:
                    out_lines.append(p)
                else:
                    # 재귀 분할
                    out_lines.extend(_split_long(p, target_line_len))
            continue
        # 2) 단일 긴 문장 → 콜론·쉼표·중점 split
        out_lines.extend(_split_long(line, target_line_len))
    return '\n'.join(out_lines)


def _split_long(line, target_line_len):
    """단일 긴 line을 부드럽게 분할."""
    # 콜론(:) 뒤
    parts = re.split(r'(?<=[:：])\s+', line)
    if len(parts) > 1 and all(len(p) <= target_line_len * 1.5 for p in parts):
        return parts
    # 쉼표·중점·세미콜론 뒤
    parts = re.split(r'(?<=[,;·])\s+', line)
    if len(parts) > 1 and all(len(p) <= target_line_len * 1.5 for p in parts):
        return parts
    # → 화살표 뒤
    parts = re.split(r'(?<=→)\s+', line)
    if len(parts) > 1 and all(len(p) <= target_line_len * 1.5 for p in parts):
        return parts
    # 마지막 수단: hard wrap (단어 경계 유지)
    out = []
    cur = ''
    for word in line.split(' '):
        if not cur:
            cur = word
        elif len(cur) + 1 + len(word) <= target_line_len:
            cur += ' ' + word
        else:
            out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


def join_kr(items, mapping=None, sep=", "):
    """list → KR label join. mapping=None 이면 raw 값 사용."""
    if not items:
        return ""
    if isinstance(items, str):
        items = [items]
    if mapping:
        return sep.join(mapping.get(x, x) for x in items)
    return sep.join(str(x) for x in items)


def join_dict_kr(d, target_line_len=40):
    """{key: value} dict → 'key: value' 줄바꿈 join. value도 prettify로 줄바꿈 보강."""
    if not d:
        return ""
    items = []
    for k, v in d.items():
        # value에서 HTML strip + prettify
        v_clean = strip_html(str(v), prettify=True, target_line_len=target_line_len)
        # bullet item — 첫 줄은 "• key: value"; 이후 줄은 들여쓰기
        v_lines = v_clean.split('\n')
        if len(v_lines) <= 1:
            items.append(f"• {k}: {v_clean}")
        else:
            first = f"• {k}: {v_lines[0]}"
            rest = "\n".join(f"  {ln}" for ln in v_lines[1:])
            items.append(first + "\n" + rest)
    return "\n".join(items)


def join_steps(steps):
    """process_steps list → 번호 매김 줄바꿈."""
    if not steps:
        return ""
    return "\n".join(f"{i+1}. {s}" for i, s in enumerate(steps))


# ── Sheet 1: 개요 ──
def build_cover_sheet(wb, ucs, cos):
    ws = wb.create_sheet("개요", 0)
    ws.column_dimensions["A"].width = 22
    ws.column_dimensions["B"].width = 90

    today = date.today().isoformat()
    n_uc = len(ucs)
    n_co = len(cos)
    n_kr = sum(1 for u in ucs if "kr" in (u.get("region") or []))
    avg_conf = sum(u["confidence"] for u in ucs) / n_uc if n_uc else 0
    n_high = sum(1 for u in ucs if u["confidence"] >= 0.5)
    n_mid = sum(1 for u in ucs if 0.3 <= u["confidence"] < 0.5)

    rows = [
        ("HR AI Use Case Collection (Excel)", ""),
        ("산출일자", today),
        ("데이터 규모", f"{n_uc} use cases · {n_co} companies · 7 HR 카테고리 · 5×13 AI 기술 axis"),
        ("한국 사례", f"{n_kr}건"),
        ("평균 신뢰도", f"{avg_conf:.2f}"),
        ("고신뢰도 (≥0.50)", f"{n_high}건 — 제안서 즉시 인용 가능"),
        ("중신뢰도 (0.30~0.49)", f"{n_mid}건 — 참고 사례"),
        ("GitHub", "https://github.com/jameskim1st/hr-ai-benchmark"),
        ("", ""),
        ("【 시트 구성 】", ""),
        ("개요", "본 시트 — 산출물 개요·스키마·사용법"),
        ("Use Cases", f"메인 데이터 ({n_uc}행 × 25컬럼). AutoFilter·정렬·copy/paste용."),
        ("AI 기술 분포", "long-format (use_case × subtype). Insert→Pivot Table로 즉시 heatmap 생성."),
        ("Companies", f"기업별 holistic view ({n_co}행)."),
        ("", ""),
        ("【 신뢰도 의미 】", ""),
        ("0.70+", "여러 독립 소스로 교차 검증 — 제안서에 'reference case'로 인용"),
        ("0.40~0.69", "일부 검증 + 일부 벤더 주장 — '참고 사례'로 활용"),
        ("0.20~0.39", "대부분 벤더 주장 또는 단일 소스 — '시장 동향' 수준"),
        ("<0.20", "stub — 인용 금지"),
        ("", ""),
        ("【 HR 7 카테고리 】", ""),
    ]
    for en, kr in KR_CATEGORY.items():
        rows.append((kr, en))
    rows.extend([
        ("", ""),
        ("【 AI 기술 5 대분류 】", ""),
    ])
    for en, kr in TECH_LABEL.items():
        rows.append((kr, f"({en})"))
    rows.extend([
        ("", ""),
        ("【 AI 기술 13 소분류 】", ""),
    ])
    for en, kr in SUB_LABEL.items():
        rows.append((f"  • {kr}", f"({en})"))
    rows.extend([
        ("", ""),
        ("【 사용법 】", ""),
        ("필터", "Use Cases 시트 → 헤더 행 dropdown 클릭 → 산업·지역·AI 기술 등 필터링"),
        ("정렬", "헤더 행 우클릭 → 정렬 (신뢰도 내림차순 권장)"),
        ("피벗 테이블", "AI 기술 분포 시트 → Insert → PivotTable → 행 'AI 기술 (소)' · 열 'HR 대분류' · 값 COUNT → heatmap"),
        ("색상 의미", "신뢰도: 녹(≥0.50) / 노(0.30~0.49) / 빨(<0.30). 지역 KR: 옅은 노란 배경"),
        ("출처 추적", "각 use case의 상세 source는 wiki/usecases/<slug>.md (GitHub)"),
        ("", ""),
        ("【 표기 규칙 】", ""),
        ("✅ Fact", "독립 Tier 1·2 소스에서 확인된 사실"),
        ("⚠️ 벤더 주장", "벤더 마케팅·자사 보고 — 독립 검증 없음"),
        ("⚠️ 자사 보고", "도입 기업이 자사 사례로 공개 — 과장 동기 있음"),
        ("_미공개_", "공개 소스에 정보 없음 (추측 금지)"),
    ])

    for r, (col_a, col_b) in enumerate(rows, start=1):
        ws.cell(row=r, column=1, value=col_a)
        ws.cell(row=r, column=2, value=col_b)

    # Title 셀 스타일
    ws.cell(row=1, column=1).font = COVER_TITLE_FONT
    ws.merge_cells("A1:B1")
    ws.cell(row=1, column=1).alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 36

    # 섹션 헤더 굵게 + 옅은 배경
    section_fill = PatternFill("solid", fgColor="EEF2F6")
    for r, (col_a, _) in enumerate(rows, start=1):
        if col_a.startswith("【"):
            ws.cell(row=r, column=1).font = COVER_SECTION_FONT
            ws.cell(row=r, column=1).fill = section_fill
            ws.cell(row=r, column=2).fill = section_fill
            ws.row_dimensions[r].height = 24

    # body 정렬 + font 11
    body_font_cover = Font(name="맑은 고딕", size=11)
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
            if not cell.font.bold:  # 섹션 header 제외
                cell.font = body_font_cover

    # 일반 row 높이 살짝 (가독성)
    for r in range(2, len(rows) + 1):
        if ws.row_dimensions[r].height is None:
            ws.row_dimensions[r].height = 20

    # 시트 탭 색
    ws.sheet_properties.tabColor = TAB_COLOR.get("개요", "2F4858")


# ── Sheet 2: Use Cases ──
# 사용자 spec: HR 모듈·사례명·기업명·개요·Pain Point·Process Flow·System·Input·Output·Model·Impact + AI 기술 분류 18 체크박스
# AI 기술 분류 column 순서 (parent_id, kr_label) — 5 대분류
TECH_PARENT_COLS = [
    ("generative", "생성형"),
    ("predictive", "판별·예측"),
    ("recognition", "인식"),
    ("decision-optimization", "의사결정·최적화"),
    ("automation", "자동화"),
]
# 13 소분류
TECH_SUB_COLS = [
    ("text-generation", "텍스트 생성"),
    ("summarization-qa", "요약·재작성·QA"),
    ("multimodal", "멀티모달"),
    ("information-extraction", "정보 추출"),
    ("prediction", "예측"),
    ("clustering-classification", "군집·분류"),
    ("recommendation-ranking", "추천·랭킹"),
    ("ocr", "OCR"),
    ("speech-recognition", "음성 인식"),
    ("optimization", "최적화"),
    ("rpa", "RPA"),
]

# 메인 본문 column (필수, 사용자 spec 순서)
USECASE_MAIN_COLS = [
    ("번호", 5),
    ("HR 모듈", 22),                  # primary_category KR
    ("사례명", 50),                    # title
    ("기업명", 25),                    # company
    ("개요", 70),                      # summary (full, bullet/줄바꿈 보존)
    ("Pain Point", 55),                # problem
    ("Process Flow", 75),              # before → after combined
    ("System", 38),                    # system dict
    ("Input", 38),                     # data dict (input data sources)
    ("Output", 45),                    # NEW frontmatter field
    ("Model", 38),                     # model dict
    ("📊 Impact (Before → After)", 60), # impact_summary + before/after
]

# 보조 column (사용자 추천 + recommended)
USECASE_AUX_COLS = [
    ("HR 중분류", 22),
    ("벤더", 22),
    ("벤더 유형", 16),
    ("산업", 18),
    ("지역", 12),
    ("단계", 10),
    ("빈도", 8),
    ("신뢰도", 8),
    ("Consulting Angle", 70),
    ("태그", 28),
    ("출처1", 50),
    ("출처2", 50),
    ("출처3", 50),
    ("slug", 32),
]


GITHUB_BASE = "https://github.com/jameskim1st/hr-ai-benchmark/blob/main"


def remove_emdash(s):
    """em-dash 제거 — 사용자 요청. ': '·' '·'' 등으로 치환.
    한국어 문맥상 콜론·쉼표·공백 적절 매핑."""
    if not s:
        return s
    # " — " (전후 공백) → ": " (가장 흔한 패턴)
    s = re.sub(r' +— +', ': ', s)
    # " —" 또는 "— " → ":"
    s = re.sub(r' —|— ', ':', s)
    # 단독 "—" → " "
    s = s.replace('—', ' ')
    # 다중 공백 정리
    s = re.sub(r'  +', ' ', s)
    # ":: " 같은 중복 정리
    s = re.sub(r': :', ':', s)
    return s.strip()


def parse_source(src_str):
    """Source 문자열 파싱 → (display_text, url).
    외부 URL만 반환. 'sources/<slug>.md' (wiki internal)은 제외 (빈 tuple).
    예: 'McKinsey: JPM... https://www.mckinsey.com/...' → ('McKinsey: JPM...', 'https://...')
    """
    if not src_str:
        return ("", "")
    s = src_str.strip()
    # 'sources/<slug>.md' wiki internal — skip
    if re.match(r"sources/[\w-]+(?:\.md)?\s*$", s):
        return ("", "")
    # URL 추출 (http:// 또는 https://)
    m = re.search(r"(https?://[^\s\)]+)", s)
    if m:
        url = m.group(1)
        # display = URL 제외 부분 (앞 텍스트)
        text_part = s.replace(url, "").strip().rstrip("(").strip()
        if not text_part:
            text_part = url
        return (remove_emdash(text_part)[:80], url)
    # 기타 (URL 없는 plain citation) — display only, no link
    return (remove_emdash(s)[:80], "")


def select_external_sources(sources_list, max_n=3):
    """sources list에서 외부 URL을 가진 것만 골라 max_n개 반환.
    URL 없는 것도 backfill (display text만)."""
    parsed = []
    for s in (sources_list or []):
        text, url = parse_source(s)
        if not text and not url:
            continue  # wiki internal — skip
        parsed.append((text, url))
        if len(parsed) >= max_n:
            break
    while len(parsed) < max_n:
        parsed.append(("", ""))
    return parsed


def has_subtype(u, sub_id):
    """Use case가 특정 subtype을 사용하는지."""
    return sub_id in (u.get("ai_tech_subtype") or [])


def has_type(u, type_id):
    """Use case가 특정 type을 사용하는지."""
    return type_id in (u.get("ai_tech_type") or [])


def build_process_flow(u, target_line_len=75):
    """Process Before → After를 단일 셀로 결합."""
    before = strip_html(u.get("process_before"), prettify=True, target_line_len=target_line_len)
    after_steps = u.get("process_steps") or []
    parts = []
    if before:
        parts.append(f"[Before]\n{before}")
    if after_steps:
        # 각 step도 길면 prettify
        steps_lines = []
        for i, s in enumerate(after_steps):
            s_pretty = prettify_for_excel(s, target_line_len=target_line_len)
            s_lines = s_pretty.split('\n')
            if len(s_lines) <= 1:
                steps_lines.append(f"{i+1}. {s_pretty}")
            else:
                steps_lines.append(f"{i+1}. {s_lines[0]}")
                for ln in s_lines[1:]:
                    steps_lines.append(f"   {ln}")
        parts.append("[After]\n" + "\n".join(steps_lines))
    return "\n\n".join(parts) if parts else ""


def build_impact(u, target_line_len=60):
    """Impact 요약 — impact_summary 위주."""
    return strip_html(u.get("impact_summary"), prettify=True, target_line_len=target_line_len)


def build_usecases_sheet(wb, ucs):
    ws = wb.create_sheet("Use Cases")

    # 전체 column 구성: MAIN + AI 기술 18개 + AUX
    all_cols = list(USECASE_MAIN_COLS)
    # AI 기술 5 대분류 (체크박스, 폭 11)
    for type_id, kr in TECH_PARENT_COLS:
        all_cols.append((kr, 11))
    # AI 기술 13 소분류 (체크박스, 폭 12)
    for sub_id, kr in TECH_SUB_COLS:
        all_cols.append((f"  · {kr}", 12))
    # 보조 column
    all_cols.extend(USECASE_AUX_COLS)

    # AI tech 부분 시작·끝 컬럼 인덱스 (조건부 서식·헤더 색상용)
    n_main = len(USECASE_MAIN_COLS)
    n_parent = len(TECH_PARENT_COLS)
    n_sub = len(TECH_SUB_COLS)
    parent_start = n_main + 1
    parent_end = n_main + n_parent
    sub_start = parent_end + 1
    sub_end = parent_end + n_sub
    aux_start = sub_end + 1

    # Header
    headers = [c[0] for c in all_cols]
    tech_parent_fill = PatternFill("solid", fgColor="6B5B95")  # 보라
    tech_sub_fill = PatternFill("solid", fgColor="9B8AB8")     # 옅은 보라
    for i, h in enumerate(headers, start=1):
        cell = ws.cell(row=1, column=i, value=h)
        # AI 기술 영역은 별도 색
        if parent_start <= i <= parent_end:
            cell.fill = tech_parent_fill
        elif sub_start <= i <= sub_end:
            cell.fill = tech_sub_fill
        else:
            cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = HEADER_ALIGN
        cell.border = BORDER_THIN
    ws.row_dimensions[1].height = 44

    # 정렬: confidence 내림차순
    ucs_sorted = sorted(ucs, key=lambda u: -u.get("confidence", 0))

    # Body
    # HR 모듈 column index (1-based) — main의 2번째
    hr_module_col_idx = 2
    # 신뢰도 column index (aux의 8번째)
    confidence_col_idx_local = aux_start + 7

    # 동적 row 높이 계산용
    row_heights = []

    for row_idx, u in enumerate(ucs_sorted, start=2):
        region_kr = ", ".join(KR_REGION.get(r, r) for r in (u.get("region") or []))
        company = u.get("company", "") if isinstance(u.get("company"), str) else ""
        primary_cat_en = u.get("primary_category", "")
        cat_kr = KR_CATEGORY.get(primary_cat_en, primary_cat_en)
        cat_fill = CATEGORY_FILL.get(primary_cat_en)
        # zebra: 짝수 data row (data row 2,4,6.. = row_idx 3,5,7..)
        is_zebra = (row_idx % 2 == 1)
        zebra_fill = ZEBRA_FILL if is_zebra else None

        # MAIN columns (사용자 spec 순서) — 잘림 없이 full text + prettify로 자동 \n 삽입
        # target_line_len = 컬럼 폭 매칭 (한글 1.7 chars/cell)
        summary_txt = strip_html(u.get("summary"), prettify=True, target_line_len=70)
        problem_txt = strip_html(u.get("problem"), prettify=True, target_line_len=55)
        process_txt = build_process_flow(u, target_line_len=75)
        system_txt = join_dict_kr(u.get("system"), target_line_len=38)
        input_txt = join_dict_kr(u.get("data"), target_line_len=38)
        output_txt = strip_html(u.get("output"), prettify=True, target_line_len=45)
        model_txt = join_dict_kr(u.get("model"), target_line_len=38)
        impact_txt = build_impact(u, target_line_len=60)
        consulting_txt = strip_html(u.get("consulting"), prettify=True, target_line_len=70)

        main_values = [
            row_idx - 1,
            cat_kr,
            u.get("title", ""),
            company,
            summary_txt,
            problem_txt,
            process_txt,
            system_txt,
            input_txt,
            output_txt,
            model_txt,
            impact_txt,
        ]
        # AI 기술 5 대분류 체크박스 (● 사용)
        tech_parent_values = [
            CHECK_MARK if has_type(u, type_id) else "" for type_id, _ in TECH_PARENT_COLS
        ]
        # AI 기술 13 소분류 체크박스
        tech_sub_values = [
            CHECK_MARK if has_subtype(u, sub_id) else "" for sub_id, _ in TECH_SUB_COLS
        ]
        # 출처 1~3
        parsed_sources = select_external_sources(u.get("sources"), max_n=3)

        # AUX columns
        aux_values = [
            u.get("subcategory", ""),
            join_kr(u.get("vendor")),
            join_kr(u.get("vendor_type")),
            join_kr(u.get("industry")),
            region_kr,
            KR_STAGE.get(u.get("stage", ""), u.get("stage", "")),
            KR_FREQUENCY.get(u.get("frequency", ""), u.get("frequency", "")),
            float(u.get("confidence", 0)),
            consulting_txt,
            join_kr(u.get("tags")),
            parsed_sources[0][0],
            parsed_sources[1][0],
            parsed_sources[2][0],
            u.get("slug", ""),
        ]

        all_values = main_values + tech_parent_values + tech_sub_values + aux_values

        src_col_indices = [aux_start + 10, aux_start + 11, aux_start + 12]

        for col_idx, v in enumerate(all_values, start=1):
            # em-dash 제거
            if isinstance(v, str):
                v = '\n'.join(_remove_emdash_line(l) for l in v.split('\n'))
            cell = ws.cell(row=row_idx, column=col_idx, value=v)
            cell.font = BODY_FONT
            cell.border = BORDER_THIN

            # AI 기술 체크박스 영역
            if parent_start <= col_idx <= sub_end:
                cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=False)
                if v == CHECK_MARK:
                    if col_idx <= parent_end:
                        cell.fill = TECH_PARENT_CHECK_FILL
                        cell.font = Font(name="맑은 고딕", size=12, bold=True, color="3F2A6E")
                    else:
                        cell.fill = TECH_SUB_CHECK_FILL
                        cell.font = Font(name="맑은 고딕", size=11, bold=True, color="5B3A8C")
                else:
                    if zebra_fill:
                        cell.fill = zebra_fill
            # HR 모듈 column — 카테고리별 색상 + bold
            elif col_idx == hr_module_col_idx:
                cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
                cell.font = Font(name="맑은 고딕", size=11, bold=True, color="2F4858")
                if cat_fill:
                    cell.fill = cat_fill
            # 번호 column — 가운데 + 회색
            elif col_idx == 1:
                cell.alignment = Alignment(horizontal="center", vertical="center")
                cell.font = Font(name="맑은 고딕", size=10, color="999999")
                if zebra_fill:
                    cell.fill = zebra_fill
            # 신뢰도 column — 우측 정렬 + 굵게 + 숫자 포맷
            elif col_idx == confidence_col_idx_local:
                cell.alignment = Alignment(horizontal="center", vertical="center")
                cell.font = Font(name="맑은 고딕", size=11, bold=True)
                cell.number_format = "0.00"
                # 신뢰도 conditional formatting이 fill 덮어씀 — zebra 적용 X
            # 일반 텍스트 column
            else:
                cell.alignment = BODY_ALIGN
                if zebra_fill:
                    cell.fill = zebra_fill

        # 출처 hyperlink
        for i, col_idx in enumerate(src_col_indices):
            url = parsed_sources[i][1]
            if url:
                cell = ws.cell(row=row_idx, column=col_idx)
                cell.hyperlink = url
                cell.font = Font(name="맑은 고딕", size=10, color="0563C1", underline="single")

        # 동적 row 높이 — 가장 긴 셀의 line count + wrap 추정
        # 각 셀의 실제 표시 line 수를 측정하여 최댓값 사용
        cell_max_lines = 1
        for txt, col_w in [
            (summary_txt, 70), (problem_txt, 55), (process_txt, 75),
            (system_txt, 38), (input_txt, 38), (output_txt, 45),
            (model_txt, 38), (impact_txt, 60), (consulting_txt, 70),
        ]:
            if not txt:
                continue
            # 이 셀이 차지하는 line 수 = 줄별 wrap line 합
            cell_lines = 0
            for line in txt.split('\n'):
                if not line.strip():
                    cell_lines += 1
                    continue
                # 한글 평균 1.7 chars/cell-width, +0.7 안전 buffer
                cell_lines += max(1, int(len(line) / (col_w * 1.6)) + 1)
            cell_max_lines = max(cell_max_lines, cell_lines)
        # line 당 ~16pt + 8pt padding. 최소 60, 최대 600pt (잘림 방지 우선)
        height = max(60, min(600, cell_max_lines * 16 + 8))
        row_heights.append(height)

    # Column widths
    for i, (_, w) in enumerate(all_cols, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w

    # Freeze: 1행 + 사례명까지 좌측 고정 (번호·HR모듈·사례명까지 = D2)
    ws.freeze_panes = "D2"

    # AutoFilter
    last_col = get_column_letter(len(all_cols))
    last_row = len(ucs_sorted) + 1
    ws.auto_filter.ref = f"A1:{last_col}{last_row}"

    # Conditional formatting: 신뢰도 (AUX의 8번째 = aux_start + 7)
    conf_col_idx = aux_start + 7
    conf_col = get_column_letter(conf_col_idx)
    conf_range = f"{conf_col}2:{conf_col}{last_row}"
    ws.conditional_formatting.add(
        conf_range,
        CellIsRule(operator="greaterThanOrEqual", formula=["0.5"],
                   fill=PatternFill("solid", fgColor="C6EFCE")),
    )
    ws.conditional_formatting.add(
        conf_range,
        CellIsRule(operator="between", formula=["0.3", "0.499"],
                   fill=PatternFill("solid", fgColor="FFEB9C")),
    )
    ws.conditional_formatting.add(
        conf_range,
        CellIsRule(operator="lessThan", formula=["0.3"],
                   fill=PatternFill("solid", fgColor="FFC7CE")),
    )

    # 지역 column에 KR 포함 시 옅은 노란 배경 (AUX의 5번째 = aux_start + 4)
    region_col_idx = aux_start + 4
    region_col = get_column_letter(region_col_idx)
    region_range = f"{region_col}2:{region_col}{last_row}"
    ws.conditional_formatting.add(
        region_range,
        FormulaRule(formula=[f'ISNUMBER(SEARCH("KR",{region_col}2))'],
                    fill=PatternFill("solid", fgColor="FFF8DC")),
    )

    # Row height — 동적 (content 길이 기반)
    for i, h in enumerate(row_heights):
        ws.row_dimensions[i + 2].height = h

    # 시트 탭 색
    ws.sheet_properties.tabColor = TAB_COLOR.get("Use Cases", "1B6E3E")


# ── Sheet 3: AI 기술 분포 (long-format) ──
TECH_LONG_COLS = [
    ("사례명", 50),
    ("기업", 25),
    ("HR 대분류", 18),
    ("AI 기술 (대)", 18),
    ("AI 기술 (소)", 22),
    ("신뢰도", 10),
    ("지역", 14),
]


def build_tech_long_sheet(wb, ucs):
    ws = wb.create_sheet("AI 기술 분포")

    # Header
    for i, (h, _) in enumerate(TECH_LONG_COLS, start=1):
        cell = ws.cell(row=1, column=i, value=h)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = HEADER_ALIGN
        cell.border = BORDER_THIN
    ws.row_dimensions[1].height = 36

    # 시트 탭 색
    ws.sheet_properties.tabColor = TAB_COLOR.get("AI 기술 분포", "5B3A8C")

    # SUB → parent type mapping for long-format
    SUB_PARENT = {
        "text-generation": "generative", "summarization-qa": "generative",
        "multimodal": "generative", "information-extraction": "generative",
        "prediction": "predictive", "clustering-classification": "predictive",
        "recommendation-ranking": "predictive",
        "ocr": "recognition", "speech-recognition": "recognition",
        "optimization": "decision-optimization", "rpa": "automation",
    }

    # Long-format: use_case × subtype (subtype 없으면 type만으로 1행)
    rows_data = []
    for u in ucs:
        sub_list = u.get("ai_tech_subtype") or []
        types_list = u.get("ai_tech_type") or []
        region_kr = ", ".join(KR_REGION.get(r, r) for r in (u.get("region") or []))
        company = u.get("company", "") if isinstance(u.get("company"), str) else ""
        cat_kr = KR_CATEGORY.get(u.get("primary_category", ""), u.get("primary_category", ""))

        if sub_list:
            for sub in sub_list:
                parent = SUB_PARENT.get(sub, "")
                rows_data.append([
                    u.get("title", ""),
                    company,
                    cat_kr,
                    TECH_LABEL.get(parent, parent),
                    SUB_LABEL.get(sub, sub),
                    float(u.get("confidence", 0)),
                    region_kr,
                ])
        elif types_list:
            for t in types_list:
                rows_data.append([
                    u.get("title", ""),
                    company,
                    cat_kr,
                    TECH_LABEL.get(t, t),
                    "",
                    float(u.get("confidence", 0)),
                    region_kr,
                ])
        # types_list 비어있으면 (governance/regulation page) 제외

    # 정렬: 대분류 → 소분류 → 신뢰도
    rows_data.sort(key=lambda r: (r[3], r[4], -r[5]))

    for row_idx, vals in enumerate(rows_data, start=2):
        is_zebra = (row_idx % 2 == 1)
        for col_idx, v in enumerate(vals, start=1):
            cell = ws.cell(row=row_idx, column=col_idx, value=v)
            cell.font = BODY_FONT
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
            cell.border = BORDER_THIN
            # 신뢰도 column (6)은 conditional formatting이 fill 덮어씀 — zebra X
            if is_zebra and col_idx != 6:
                cell.fill = ZEBRA_FILL
            # 신뢰도 column 우측 정렬·숫자 포맷
            if col_idx == 6:
                cell.alignment = Alignment(horizontal="center", vertical="center")
                cell.font = Font(name="맑은 고딕", size=11, bold=True)
                cell.number_format = "0.00"

    # Column widths
    for i, (_, w) in enumerate(TECH_LONG_COLS, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w

    # Freeze + AutoFilter
    ws.freeze_panes = "A2"
    last_col = get_column_letter(len(TECH_LONG_COLS))
    last_row = len(rows_data) + 1
    ws.auto_filter.ref = f"A1:{last_col}{last_row}"

    # 신뢰도 conditional formatting (6번째 컬럼 = F)
    conf_col = get_column_letter(6)
    conf_range = f"{conf_col}2:{conf_col}{last_row}"
    ws.conditional_formatting.add(conf_range, CellIsRule(operator="greaterThanOrEqual", formula=["0.5"], fill=PatternFill("solid", fgColor="C6EFCE")))
    ws.conditional_formatting.add(conf_range, CellIsRule(operator="between", formula=["0.3", "0.499"], fill=PatternFill("solid", fgColor="FFEB9C")))
    ws.conditional_formatting.add(conf_range, CellIsRule(operator="lessThan", formula=["0.3"], fill=PatternFill("solid", fgColor="FFC7CE")))


# ── Sheet 4: Companies ──
COMPANY_COLS = [
    ("기업명", 25),
    ("산업", 25),
    ("지역", 14),
    ("직원 규모", 12),
    ("Use Case 수", 12),
    ("평균 신뢰도", 12),
    ("설명", 60),
    ("HR AI 전략", 80),
    ("Consulting Angle", 80),
]


def build_companies_sheet(wb, ucs, cos):
    ws = wb.create_sheet("Companies")

    # Header
    for i, (h, _) in enumerate(COMPANY_COLS, start=1):
        cell = ws.cell(row=1, column=i, value=h)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = HEADER_ALIGN
        cell.border = BORDER_THIN
    ws.row_dimensions[1].height = 36

    # 시트 탭 색
    ws.sheet_properties.tabColor = TAB_COLOR.get("Companies", "C2562D")

    # Compute use case count + avg confidence per company (slug 매칭)
    uc_by_company_name = defaultdict(list)
    for u in ucs:
        co = u.get("company", "") if isinstance(u.get("company"), str) else ""
        if co:
            uc_by_company_name[co].append(u)

    # Body
    for row_idx, c in enumerate(cos, start=2):
        name = c.get("name", "")
        # 기업명 매칭 (정확 일치 또는 partial)
        related = uc_by_company_name.get(name, [])
        if not related:
            for cn, ucs_list in uc_by_company_name.items():
                if name.lower() in cn.lower() or cn.lower() in name.lower():
                    related.extend(ucs_list)
        n_cases = len(related)
        avg_conf = sum(u.get("confidence", 0) for u in related) / n_cases if n_cases else 0

        region_kr = ", ".join(KR_REGION.get(r, r) for r in (c.get("region") or []))

        # HR AI 전략에서 Dataview 코드블록 제거
        strategy_raw = c.get("strategy", "")
        strategy_clean = re.sub(r"```dataview[\s\S]*?```", "", strategy_raw)

        values = [
            name,
            join_kr(c.get("industry")),
            region_kr,
            c.get("size", ""),
            n_cases,
            round(avg_conf, 2) if n_cases else "",
            strip_html(c.get("description"), 400),
            strip_html(strategy_clean, 600),
            strip_html(c.get("consulting"), 600),
        ]
        is_zebra = (row_idx % 2 == 1)
        for col_idx, v in enumerate(values, start=1):
            cell = ws.cell(row=row_idx, column=col_idx, value=v)
            cell.font = BODY_FONT
            cell.alignment = BODY_ALIGN
            cell.border = BORDER_THIN
            # 평균 신뢰도 column (6)은 conditional formatting이 fill 덮어씀 — zebra X
            if is_zebra and col_idx != 6:
                cell.fill = ZEBRA_FILL
            # 기업명 (1) — bold + 약간 더 큰 font
            if col_idx == 1:
                cell.font = Font(name="맑은 고딕", size=12, bold=True, color="2F4858")
                cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
            # Use Case 수 (5) — 가운데 정렬
            elif col_idx == 5:
                cell.alignment = Alignment(horizontal="center", vertical="center")
                cell.font = Font(name="맑은 고딕", size=12, bold=True, color="2F4858")
            # 평균 신뢰도 (6)
            elif col_idx == 6:
                cell.alignment = Alignment(horizontal="center", vertical="center")
                cell.font = Font(name="맑은 고딕", size=11, bold=True)
                if isinstance(v, (int, float)):
                    cell.number_format = "0.00"

    # Column widths
    for i, (_, w) in enumerate(COMPANY_COLS, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w

    # Freeze + AutoFilter
    ws.freeze_panes = "B2"
    last_col = get_column_letter(len(COMPANY_COLS))
    last_row = len(cos) + 1
    ws.auto_filter.ref = f"A1:{last_col}{last_row}"

    # Avg confidence conditional formatting (6번째 컬럼 = F)
    conf_col = get_column_letter(6)
    conf_range = f"{conf_col}2:{conf_col}{last_row}"
    ws.conditional_formatting.add(conf_range, CellIsRule(operator="greaterThanOrEqual", formula=["0.5"], fill=PatternFill("solid", fgColor="C6EFCE")))
    ws.conditional_formatting.add(conf_range, CellIsRule(operator="between", formula=["0.3", "0.499"], fill=PatternFill("solid", fgColor="FFEB9C")))
    ws.conditional_formatting.add(conf_range, CellIsRule(operator="lessThan", formula=["0.3"], fill=PatternFill("solid", fgColor="FFC7CE")))

    # Row height
    for r in range(2, last_row + 1):
        ws.row_dimensions[r].height = 100


# ── Main ──
def main():
    with open(UC_JSON, encoding="utf-8") as f:
        ucs = json.load(f)
    with open(CO_JSON, encoding="utf-8") as f:
        cos = json.load(f)

    wb = Workbook()
    # Workbook은 기본 'Sheet' 1개로 생성됨 — 제거
    wb.remove(wb.active)

    build_cover_sheet(wb, ucs, cos)
    build_usecases_sheet(wb, ucs)
    build_tech_long_sheet(wb, ucs)
    build_companies_sheet(wb, ucs, cos)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT)
    size_kb = OUT.stat().st_size / 1024
    print(f"Excel: 4 sheets, {len(ucs)} use cases, {len(cos)} companies -> {size_kb:.0f}KB")


if __name__ == "__main__":
    main()
