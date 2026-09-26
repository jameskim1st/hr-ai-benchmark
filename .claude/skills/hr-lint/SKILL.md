---
name: hr-lint
description: wiki 건강 점검. 결정론적 lint.py 결과를 먼저 읽고, LLM은 모순·낡음·품질 판단만 덧붙인다. 자동 수정 없음 — 권고 목록만.
argument-hint: "[--strong] [--report]"
---

# /hr-lint

결정론적 점검 결과 (방금 실행된 `scripts/lint.py`):

!`python scripts/lint.py`

Grounding 검사 요약 (수치가 raw 스냅샷에 있는지):

!`python scripts/check_quotes.py | head -25`

## 네가 할 일

1. 위 결과를 **그대로 신뢰**한다. 링크·frontmatter·날짜·근거 등급은 스크립트 판정이 최종이다. 다시 세지 않는다.
2. LLM 판단이 필요한 항목만 추가로 본다 (`.claude/rules/protocols.md` Lint Protocol 참조):
   - `unresolved-contradiction` 페이지: 두 주장·날짜·출처를 읽고 supersession 가능 여부(최신·권위 우선) 판단
   - `ungrounded-bcd` 상위 10건: 실제로 소스에 없는 서술인지 페이지를 열어 확인하고, `_미공개_`로 바꿀 문장을 인용
   - `banned-word` 상위 10건: 리라이트 문장 제안
   - `possible-duplicate`: 병합 여부 판단
   - check_quotes ⚠️ 페이지 상위 5건: 어떤 수치가 어느 소스에서 왔어야 하는지
3. `$ARGUMENTS`에 `--strong`이 있으면 evidence_grade A·B 페이지 10건을 무작위로 골라 `hr-verifier` 서브에이전트(Agent tool, subagent_type: hr-verifier)에 검증을 맡기고 결과를 요약한다.
4. `$ARGUMENTS`에 `--report`가 있으면 `python scripts/lint.py --write-report`를 실행해 `wiki/syntheses/lint-YYYY-MM-DD.md`를 만들고, 네 LLM 판단을 그 파일 끝에 `## LLM 판단` 섹션으로 append한다. `wiki/log.md`에 `## [YYYY-MM-DD] lint | critical: N, warning: M, info: K` 한 줄을 append한다.
5. 사용자에게 보고: critical/warning/info 수, **사람 승인이 필요한 수정 목록**(페이지·문장·제안), 다음 액션 3개.

## 금지
- 페이지를 직접 고치지 않는다. 사용자가 "고쳐"라고 하면 그때 한 건씩 수정하고, 수정 후 `python scripts/lint.py --quick <file>`로 확인한다.
- raw/ 는 절대 수정하지 않는다.
