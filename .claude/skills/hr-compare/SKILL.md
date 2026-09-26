---
name: hr-compare
description: 두 개 이상의 벤더·회사·use case를 wiki 데이터만으로 비교해 syntheses 페이지로 저장 (벤더 선정·벤치마크 슬라이드용).
argument-hint: "<entityA> vs <entityB> [vs <entityC>...]"
---

# /hr-compare

입력: `$ARGUMENTS` (예: `Workday vs SAP SuccessFactors`, `Paradox vs HireVue`, `moderna-ask-hr-routing vs ibm-askhr-watsonx`)

## 절차
1. **엔티티 resolve** — 각 이름을 `wiki/vendors/`·`wiki/companies/`·`wiki/usecases/`에서 `grep -ril`로 찾는다. 못 찾으면 사용자에게 정확한 슬러그를 묻는다 (자동 생성 금지). `depth: stub`이면 비교 품질이 낮다고 고지한다.
2. **비교 축** — 벤더끼리: 기능 커버리지(대그룹), 주요 고객(use case 페이지 기준), AI 기능, evidence_grade 분포, 알려진 한계, 통합성. 회사끼리: Problem·Solution·Vendor/Stack·Metrics·Timeline·교훈. use case끼리: Approach·Architecture(A~E)·Metrics·Governance·적용 산업.
3. **본문** — 맨 위 한 눈 비교표, 축별 1~3줄 분석 + `[[wikilink]]`, 데이터 부족 축은 "데이터 부족"으로 표기(추측 금지). 각 수치에 evidence_grade와 ⚠️ 벤더 주장/자사 보고 표기를 그대로 옮긴다.
4. **Consulting Angle** — 어떤 상황·산업·규모에서 각 선택지가 우세한가, 이 비교로 답할 수 있는 클라이언트 질문, 빠진 데이터가 있으면 `/hr-research` 제안. 한국 적용 시사점(법규·노조·언어·국내 지원) 포함.
5. **저장** — `wiki/syntheses/compare-<slugA>-vs-<slugB>-YYYY-MM-DD.md`, frontmatter `type: comparison, entities, generated_at, sufficient_data (true|partial|false)`. `wiki/log.md`에 `## [YYYY-MM-DD] compare | <entities> | sufficient_data: <status>` append.
6. **보고** — 비교표 + Consulting Angle 2~3줄. 부족한 데이터는 명시.

원칙: wiki에 없는 정보는 만들지 않는다. 벤더 마케팅 주장을 그대로 옮기지 않는다.
