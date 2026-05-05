---
description: wiki 건강 점검 (stale·low-confidence·orphan·broken link·미해결 contradiction·카테고리 커버리지)
argument-hint: [--fix]
---

# /hr-lint

[CLAUDE.md](../../CLAUDE.md) **§7 Lint Protocol**에 따라 wiki 상태를 점검합니다.

**옵션**: `$ARGUMENTS` — `--fix` 지정 시 자동 수정 가능한 항목(frontmatter 재계산, broken link stub 생성 등)까지 수행.

## 점검 항목

1. **Stale claims** — `last_confirmed`가 12개월 경과한 use case
2. **Low confidence** — `confidence < 0.4` 페이지
3. **Orphan pages** — 어떤 다른 페이지에서도 `[[wikilink]]`되지 않은 페이지 (sources/는 예외)
4. **Broken links** — 존재하지 않는 페이지로의 `[[wikilink]]`
5. **Missing entities** — 본문에서 언급되었지만 `[[wikilink]]`로 연결되지 않은 유명 회사·벤더
6. **Unresolved contradictions** — `[!contradiction]` 중 `상태: unresolved`인 전수
7. **Category coverage gaps** — 대/중그룹 중 use case 0건인 곳 (리서치 공백 신호)
8. **Tier imbalance** — Tier 3·4 소스에만 의존(Tier 1·2 출처 0건)하는 use case
9. **Solution Architecture 품질** (★ critical)
   - A~E(Process / System / Data / Model / Org) 중 3개 이상 `_미공개_`인데 stub 표시 없는 페이지
   - 본문에 **추측성 금지어** 포함 여부 검사: `아마도`, `추정`, `보통`, `일반적으로`, `대개`, `대체로`, `통상`, `likely`, `probably`, `typically`, `generally`, `most likely`
   - **Unverified 벤더 주장**: 벤더/자사 소스(Tier 3)에서 나온 수치·단언이 `⚠️ 벤더 주장:` 접두사 없이 본문에 직접 쓰여 있는 경우
   - **Citation 커버리지**: Solution Architecture 섹션의 구체적 주장(시스템명·모델명·수치·팀 규모) 중 인접 `[[sources/xxx]]`가 없는 문장
   - **Mermaid 다이어그램 누락**: Solution Architecture의 A~E 중 3개 이상이 Fact로 채워져 있는데 도식이 0개인 페이지
10. **Missing Consulting Angle** — `## Consulting Angle` 섹션이 비어 있거나 `consulting_angle_status: pending`인 use case
11. **Frontmatter 불일치** — 필수 필드 누락, 태그 오탈자, primary_category가 taxonomy에 없는 값 등

## 실행 절차

1. 모든 점검을 돌리며 결과를 수집
2. 심각도 분류: `critical` (broken link, missing field) / `warning` (stale, low confidence) / `info` (coverage gap)
3. `wiki/syntheses/lint-YYYY-MM-DD.md` 생성:
   - 섹션별로 해당 페이지 리스트 + 권장 조치
   - 각 페이지는 `[[wikilink]]`로 연결
4. `--fix` 모드:
   - Confidence 자동 재계산 (CLAUDE.md §4 공식)
   - Broken link 대상 stub 페이지 생성
   - Missing 축 태그 중 추론 가능한 것만 채움 (industry/region 등은 본문에서 추론)
   - 자동 수정한 항목은 log에 기록
5. **자동 수정 금지 항목**: contradiction 해결, Consulting Angle 작성, stale 재확인 → 사용자 승인 필요
6. `wiki/log.md`에 append: `## [YYYY-MM-DD] lint | critical: N, warning: M, info: K | auto-fixed: X`

## Report 형식

```
🔴 Critical (N)
  - [[usecases/xxx]] — broken link to [[vendors/yyy]]
  ...

🟡 Warning (M)
  - [[usecases/xxx]] — last_confirmed 14개월 전, 재확인 필요
  ...

🔵 Info (K)
  - Category coverage gap: "Total Rewards → Payroll → 가압류" use case 0건
  ...

Next actions:
  1. ...
  2. ...
```
