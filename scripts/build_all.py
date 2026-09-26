#!/usr/bin/env python3
"""
build_all.py — export 파이프라인 일괄 실행

  python scripts/build_all.py

순서:
  1. python scripts/extract_v3.py (internal 제외)
  1.5 python scripts/lint.py --json → `internal-in-export` 가 있으면 중단 (방어)   → wiki/exports/usecases.json · enterprise_ai.json · companies.json
  2. python scripts/build_html_v6.py → wiki/exports/hr-ai-usecase-collection.html
  3. python scripts/build_excel.py   → wiki/exports/hr-ai-usecase-collection.xlsx

각 단계의 stdout 요약을 출력하고, 어느 단계든 실패하면 non-zero 로 종료한다.
lint 단계에서 `internal-in-export` 가 나오면 현재 wiki/exports/usecases.json 에 visibility=internal
페이지가 포함돼 있다는 뜻이다 → `python scripts/extract_v3.py` 를 먼저 단독 실행해 깨끗한 JSON을 만든 뒤 재실행.
"""
import json
import os
import subprocess
import sys
import time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(BASE, "scripts")
PY = sys.executable

ENV = dict(os.environ)
ENV["PYTHONIOENCODING"] = "utf-8"
ENV["PYTHONUTF8"] = "1"


def run(script, *args, capture=True):
    """scripts/<script> 실행 → (returncode, stdout, stderr)."""
    cmd = [PY, os.path.join(SCRIPTS, script), *args]
    p = subprocess.run(cmd, cwd=BASE, env=ENV, capture_output=capture, text=True, encoding="utf-8", errors="replace")
    return p.returncode, (p.stdout or ""), (p.stderr or "")


def banner(title):
    print(f"\n=== {title} " + "=" * max(0, 60 - len(title)))


def lint_gate():
    banner("0. lint gate (internal-in-export)")
    t0 = time.time()
    rc, out, err = run("lint.py", "--json")
    if rc != 0 and not out.strip():
        print(f"[FAIL] lint.py exited {rc} without JSON output")
        print(err.strip()[-2000:])
        return False
    try:
        data = json.loads(out)
    except json.JSONDecodeError as e:
        print(f"[FAIL] lint.py --json output is not JSON: {e}")
        print(out.strip()[-1500:])
        return False
    findings = data.get("findings") or []
    leaks = [f for f in findings if f.get("code") == "internal-in-export"]
    counts = data.get("counts") or {}
    print(f"lint: critical {counts.get('C', 0)} · warning {counts.get('W', 0)} · info {counts.get('I', 0)}  ({time.time() - t0:.1f}s)")
    if leaks:
        print("[ABORT] visibility=internal 페이지가 현재 export에 포함되어 있습니다:")
        for f in leaks:
            print(f"  - {f.get('page')}: {f.get('detail')}")
        print("  → `python scripts/extract_v3.py` 를 먼저 단독 실행해 export를 재생성한 뒤 build_all.py 를 다시 실행하세요.")
        return False
    print("internal-in-export: none")
    return True


def step(n, title, script):
    banner(f"{n}. {title}")
    t0 = time.time()
    rc, out, err = run(script)
    if out.strip():
        print(out.rstrip())
    if rc != 0:
        print(f"[FAIL] {script} exited {rc}  ({time.time() - t0:.1f}s)")
        if err.strip():
            print(err.strip()[-3000:])
        return False
    if err.strip():
        # 경고성 stderr 는 참고용으로 마지막 몇 줄만
        tail = err.strip().splitlines()[-5:]
        print("[stderr] " + " | ".join(tail))
    print(f"[OK] {script}  ({time.time() - t0:.1f}s)")
    return True


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    t_all = time.time()
    if not lint_gate():
        return 2
    steps = [
        (1, "extract (wiki → JSON)", "extract_v3.py"),
        (2, "build HTML", "build_html_v6.py"),
        (3, "build Excel", "build_excel.py"),
    ]
    for n, title, script in steps:
        if not step(n, title, script):
            print(f"\n[build_all] FAILED at step {n} ({script}) — 이후 단계는 실행하지 않음")
            return 1
    banner("done")
    for fn in ("usecases.json", "enterprise_ai.json", "companies.json",
               "hr-ai-usecase-collection.html", "hr-ai-usecase-collection.xlsx"):
        p = os.path.join(BASE, "wiki", "exports", fn)
        if os.path.exists(p):
            print(f"  {fn:<34}{os.path.getsize(p) / 1024:>8.0f} KB")
        else:
            print(f"  {fn:<34}   (missing)")
    print(f"[build_all] OK in {time.time() - t_all:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
