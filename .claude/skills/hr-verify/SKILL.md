---
name: hr-verify
description: 특정 use case 페이지 또는 자유 형식 주장("Gloat가 Mastercard $21M 절감")을 raw 스냅샷·원문·독립 소스와 대조해 확인/표기 오류/근거 없음/supersede 판정을 받는다. PwC 자료 fact-check처럼 클라이언트 자료 검증에 사용.
argument-hint: "<usecase-slug | \"주장 문장\"> [--fix]"
---

# /hr-verify

대상: `$ARGUMENTS`

1. 대상이 슬러그면 `python scripts/check_quotes.py <slug>`를 먼저 실행해 수치 근거 현황을 본다.
2. `hr-verifier` 서브에이전트(Agent tool, `subagent_type: hr-verifier`)에 대상과 함께 다음을 넘긴다: 페이지 경로, `sources:`의 source 페이지 경로, 각 `raw:` 경로. 자유 형식 주장이면 관련 use case를 `grep -ril`로 찾아 같이 넘긴다.
3. 결과 표(주장 | 판정 | 인용 | 출처)를 사용자에게 그대로 보여주고, 판정 요약과 **권고 수정**을 붙인다.
4. `--fix`가 있을 때만: ❌ 근거 없음 문장을 `_미공개 (not disclosed)_`로, ⚠️ 표기 오류는 접두사·hedging을 복원, 🔁 supersede는 `[!contradiction]` 콜아웃(`상태: superseded`)과 함께 본문 재작성. 수정 후 `python scripts/grade.py && python scripts/lint.py --quick <file>`. `wiki/log.md`에 `## [YYYY-MM-DD] verify | <slug> | 확인 n / 표기오류 n / 근거없음 n / supersede n` append.
5. 클라이언트 자료(제안서·벤더 deck)를 검증한 경우, 결과를 `wiki/syntheses/verify-<topic>-YYYY-MM-DD.md`에 저장하고 frontmatter `visibility: internal`을 붙인다 (export 제외).

원칙: "인용이 있다"는 "참이다"가 아니다. 판정 표에 이 문장을 항상 포함한다. 검색으로 못 찾은 것은 못 찾았다고 쓴다.
