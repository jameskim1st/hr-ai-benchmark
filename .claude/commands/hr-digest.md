---
description: 지정 기간(기본 weekly) 동안 추가·변경된 use case를 요약해 syntheses 페이지로 생성
argument-hint: [weekly | monthly | YYYY-MM-DD..YYYY-MM-DD]
---

# /hr-digest

기간 내 wiki 변경사항을 정리한 digest를 만듭니다. 컨설팅 프로젝트 준비·주간 리뷰에 사용.

**기간**: `$ARGUMENTS` (미지정 시 `weekly` = 최근 7일)

## 실행 절차

1. **범위 확정**
   - `weekly` → 오늘 기준 -7일
   - `monthly` → 오늘 기준 -30일
   - `YYYY-MM-DD..YYYY-MM-DD` → 명시 범위
   - `wiki/log.md`를 grep해서 해당 기간의 ingest·manual-edit 엔트리 수집

2. **변경사항 집계**
   - 신규 use case (grouped by 대그룹)
   - 업데이트된 use case (confidence 변동, stage 변화, new contradiction 등)
   - 신규 vendor·company 페이지
   - 해결된·신규 발생한 contradiction

3. **트렌드 관찰**
   - 이번 기간 가장 많이 언급된 vendor Top 5
   - 가장 많이 언급된 industry / region
   - 카테고리 커버리지 변화 (어떤 대/중그룹에 use case가 새로 찼는가)

4. **Consulting picks**
   - confidence ≥ 0.7이면서 최근 업데이트된 use case 중 "바로 제안서에 쓸 수 있는" 3~5건 선별
   - 각 건에 대해 1줄 사용 제안 ("제약 업계 제안서의 onboarding 섹션에 활용 가능" 등)

5. **Syntheses 페이지 생성**
   - 경로: `wiki/syntheses/digest-<period>-YYYY-MM-DD.md`
     - weekly: `digest-weekly-YYYY-Www.md`
     - monthly: `digest-monthly-YYYY-MM.md`
     - range: `digest-range-<start>-to-<end>.md`
   - Frontmatter: `type: digest, period, generated_at, usecases_new, usecases_updated`
   - 섹션: Executive Summary / By Category / Vendor & Industry Signals / Consulting Picks / Open Questions

6. **Log 기록**
   - `wiki/log.md`에 append: `## [YYYY-MM-DD] digest | <period> | new: X, updated: Y`

7. **Report**
   - 사용자에게 digest 경로 + Executive Summary 3줄 + Consulting Picks 목록만 표시

## 원칙
- Digest는 wiki의 기존 페이지만 사용한다 — 새 리서치·추측 금지 (그건 `/hr-autoresearch`의 일).
- 모든 주장에 `[[wikilink]]` citation 필수.
