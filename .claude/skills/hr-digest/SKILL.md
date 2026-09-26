---
name: hr-digest
description: 지정 기간(기본 weekly)의 wiki 변경사항·trend·Consulting picks를 syntheses 페이지로 생성. 새 리서치·추측 없음, wiki 데이터만.
argument-hint: "[weekly | monthly | YYYY-MM-DD..YYYY-MM-DD]"
---

# /hr-digest

기간: `$ARGUMENTS` (미지정 = `weekly`, 최근 7일)

최근 log 엔트리:

!`grep -n '^## \[' wiki/log.md | head -20`

최근 graded_at 기준 변경 페이지:

!`grep -l "graded_at: $(date +%Y-%m)" wiki/usecases/*.md 2>/dev/null | wc -l`

## 절차
1. 범위 확정: weekly = 오늘-7일, monthly = 오늘-30일, 범위 지정 시 그대로. `wiki/log.md`에서 해당 기간 `ingest|verify|research|refactor|manual-edit` 엔트리를 수집한다.
2. 변경 집계: 신규 use case(대그룹별), 갱신 use case(evidence_grade·depth·stage 변화, 새 contradiction), 신규 vendor·company, 해결/신규 contradiction. frontmatter의 `graded_at`, `last_confirmed`, `ingested_at`을 grep해서 확인한다.
3. 트렌드: 기간 내 가장 많이 언급된 vendor Top 5, industry/region, 카테고리 커버리지 변화, `freshness: stale`로 넘어간 페이지 수.
4. Consulting picks: `evidence_grade: A` 또는 `B` + `depth: full` + 최근 갱신 중 "바로 제안서에 쓸 수 있는" 3~5건, 각 1줄 활용 제안.
5. Open questions: 미해결 contradiction, check_quotes ⚠️ 상위 페이지, 승인 대기 research 후보.
6. 저장: `wiki/syntheses/digest-<period>-YYYY-MM-DD.md` (weekly: `digest-weekly-YYYY-Www.md`). frontmatter `type: digest, period, generated_at, usecases_new, usecases_updated`. 섹션: Executive Summary / By Category / Vendor & Industry Signals / Consulting Picks / Open Questions. 모든 주장에 `[[wikilink]]`.
7. `wiki/log.md`에 `## [YYYY-MM-DD] digest | <period> | new: X, updated: Y` append. 사용자에게 Executive Summary 3줄 + Consulting Picks만 보고.

원칙: wiki에 없는 정보는 만들지 않는다. 필요한 리서치는 `/hr-research`를 제안한다.
