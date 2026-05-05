---
description: 두 개 이상의 벤더·회사·use case를 비교해 syntheses 페이지로 저장
argument-hint: <entityA> vs <entityB> [vs <entityC>...]
---

# /hr-compare

지정한 엔티티(벤더·회사·use case)를 wiki 데이터만으로 비교해 비교표·분석 페이지를 만듭니다.
컨설팅 프로젝트의 벤더 선정·벤치마크 슬라이드 준비에 사용.

**입력**: `$ARGUMENTS` (예: `Workday vs SAP SuccessFactors vs Oracle HCM`)

## 실행 절차

1. **엔티티 resolve**
   - 각 이름을 `wiki/vendors/`·`wiki/companies/`·`wiki/usecases/`에서 검색
   - 못 찾으면 사용자에게 정확한 wiki slug 확인 요청 (자동 생성 금지)
   - 페이지가 있지만 내용이 stub이면 경고 — 비교 품질이 낮아질 것을 고지

2. **비교 축 자동 결정**
   - 벤더끼리 → Functional coverage (어떤 카테고리 지원), 주요 고객, 차별화, AI 기능, 알려진 한계, pricing 신호, 통합성
   - 회사 사례끼리 → Problem, Solution, Vendor/Tech stack, Metrics, Timeline, 교훈
   - use case끼리 → Approach, Architecture, Metrics, Governance, 적용 가능 산업

3. **비교 본문 구성**
   - 한 페이지 맨 위에 **한 눈 비교표**(markdown table)
   - 각 축별 1~3줄 분석 + citation `[[wikilink]]`
   - 모순·불확실한 축은 "데이터 부족"으로 솔직하게 표시 (추측 금지)

4. **Consulting Angle 섹션**
   - 어떤 상황·산업·규모에서 각 선택지가 우세한가
   - 이 비교로 **어떤 클라이언트 질문에 답할 수 있는가**
   - 빠진 데이터가 있다면 `/hr-autoresearch` 제안

5. **저장**
   - 경로: `wiki/syntheses/compare-<slug1>-vs-<slug2>[-vs-<slug3>]-YYYY-MM-DD.md`
   - Frontmatter: `type: comparison, entities, generated_at, sufficient_data (true|partial|false)`
   - `wiki/index.md` Syntheses 섹션에 엔트리 추가
   - `wiki/log.md` append: `## [YYYY-MM-DD] compare | <entities> | sufficient_data: <status>`

6. **Report**
   - 비교표 한 눈 버전 + Consulting Angle 2~3줄만 표시
   - 부족한 데이터가 있으면 명시적으로 경고

## 원칙
- **Wiki에 없는 정보는 만들지 않는다**. 부족하면 부족하다고 말하고 autoresearch를 제안.
- 벤더 비교는 marketing 주장을 그대로 옮기지 않는다 — Tier 1·2 소스 주장을 우선 인용.
