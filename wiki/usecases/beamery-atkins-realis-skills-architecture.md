---
title: "AtkinsRéalis — Beamery 기반 Skills Architecture"
slug: beamery-atkins-realis-skills-architecture
primary_category: Strategic Workforce & Governance
subcategory: Workforce Planning
tags: [skills-mapping, job-architecture, beamery, forrester-roi, engineering]
company: AtkinsRéalis
industry: [engineering, construction]
region: [global]
employee_class: [기술사무직]
vendor: [Beamery]
vendor_type: [talent-marketplace]
output: "⚠️ 벤더 주장: AtkinsRéalis — Workday 연동 skills-based 채용의 best-fit 후보 식별·개인화 커뮤니케이션; Flex — 1,200+ JD를 필요·희망 skill과 숙련도 포함 40개 역할 세트로 변환 (4주 미만, 핵심 job profile 17일 납품)"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [information-extraction, clustering-classification, recommendation-ranking]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: []
kr_law: skills 기반 채용·후보 식별 → AI 기본법 고영향 AI(채용) 검토
kr_union: 단체교섭/근로자대표 협의 필요 (인사 의사결정 영향)
kr_language: 미확인 (벤더 확인 필요)
kr_vendor: 미확인 (국내 파트너 확인 필요)
first_seen_estimated: true
last_confirmed_estimated: true
frequency: monthly
first_seen: 2025-06-30
last_confirmed: 2025-06-30
confidence: 0.15
evidence_grade: C
corroborated_by: 0
freshness: stale
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/beamery-atkins-realis-case-study-2025.md, sources/beamery-flex-job-architecture-case-study-2025.md, sources/beamery-forrester-tei-467-roi-2023-10.md]
related_usecases:
  - jnj-digital-talent-platform-skills-ai
  - visier-vee-people-analytics
related_vendors: []
---

# AtkinsRéalis + Flex — Beamery Skills Architecture

## Summary

**AtkinsRéalis** ($8.6B 엔지니어링)가 Beamery로 skills-based 채용 전환 (Workday 연동). ⚠️ 벤더 주장: Beamery 경유 신규 채용자가 **25% 빨리 성과 마일스톤** 도달, best-fit 후보 식별 **30% 시간↓**, 후보 engagement 점수 **40%↑**. [[sources/beamery-atkins-realis-case-study-2025.md]] **Flex** (전자 제조)는 ⚠️ 벤더 주장: **1,200+ JD를 40개 역할**로 통합, JD 통합 시간 **89% 단축** (수작업 4~6개월 → 4주 미만), 핵심 job profile 17일 납품, JD 복잡도 97% 감소. [[sources/beamery-flex-job-architecture-case-study-2025.md]] ⚠️ 벤더 의뢰 연구: Forrester Consulting TEI **467% ROI** (고객 1개사 인터뷰 기반, 2023). [[sources/beamery-forrester-tei-467-roi-2023-10.md]] (2026-09-27 grounding 점검: 종전 "스킬 추론 90퍼센트 적합도"는 소스에 없어 제거.)

## Problem / Why (도입 배경)

- **Before**: ⚠️ 벤더 주장 (Flex): 1,200개 이상의 JD가 비일관 — 40개 역할의 skills composition을 수작업으로 정의하면 4~6개월 소요. [[sources/beamery-flex-job-architecture-case-study-2025.md]] AtkinsRéalis baseline ❓ 미공개
- **Pain point**: ⚠️ 벤더 주장 (AtkinsRéalis): 인프라·에너지 시스템 혁신을 이끌 인재 확보 — skills-based 접근으로 채용 품질 개선. [[sources/beamery-atkins-realis-case-study-2025.md]]
- **Trigger**: ❓ 미공개 (도입 결정 계기는 두 사례 모두 소스에 없음)

## Solution Architecture

### A. Process (프로세스)

- **Before**: ⚠️ 벤더 주장 (Flex): 수작업 JD 통합·skills 정의 (4~6개월). [[sources/beamery-flex-job-architecture-case-study-2025.md]]
- **After**:
  1. ⚠️ 벤더 주장 (Flex): Beamery가 1,200+ JD를 필요·희망 skill과 숙련도 수준을 포함한 40개 역할 세트로 변환. [[sources/beamery-flex-job-architecture-case-study-2025.md]]
  2. ⚠️ 벤더 주장 (Flex): 4주 미만에 40개 역할 skills composition 정의; 핵심 job profile은 데이터 수집→납품 17일. [[sources/beamery-flex-job-architecture-case-study-2025.md]]
  3. ⚠️ 벤더 주장 (AtkinsRéalis): Workday 연동 skills-based 채용 — best-fit 후보 식별, 개인화된 커뮤니케이션. [[sources/beamery-atkins-realis-case-study-2025.md]]
  (종전 6단계 "Skills Inference 엔진·Dynamic Job Architecture·SAP 동기화·자동 갱신" 서술은 인용 소스에 없는 제품 페이지 기반이라 제거)
- **HITL**: _미공개 (not disclosed)_
- **Frequency**: _미공개 (not disclosed)_
- **Scope of autonomy**: _미공개 (not disclosed)_

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS / 기반 시스템**: ⚠️ 벤더 주장 (AtkinsRéalis): Workday 연동. [[sources/beamery-atkins-realis-case-study-2025.md]] Flex _미공개_
- **AI 시스템 배치**: ⚠️ 벤더 주장: Beamery 플랫폼 (AI-powered Talent Lifecycle Management). [[sources/beamery-forrester-tei-467-roi-2023-10.md]]
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: ⚠️ 벤더 주장 (AtkinsRéalis): Workday. [[sources/beamery-atkins-realis-case-study-2025.md]] 그 외 _미공개_
- **사용자 접점**: _미공개 (not disclosed)_
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: ⚠️ 벤더 주장 (Flex): 1,200+ 직무 기술서. [[sources/beamery-flex-job-architecture-case-study-2025.md]]
- **데이터 규모**: ⚠️ 벤더 주장 (Flex): 1,200+ JD → 40개 역할. [[sources/beamery-flex-job-architecture-case-study-2025.md]]
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: _미공개 (not disclosed)_
- **데이터 거버넌스**: _미공개 (not disclosed)_
- **민감정보 처리**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **Model 유형**: _미공개 (not disclosed)_ — 소스는 "AI"로만 표현
- **제공 방식**: _미공개 (not disclosed)_
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **평가·가드레일**: _미공개 (not disclosed)_

### E. Organization & Team (조직·팀 구조)

- **오너십**: _미공개 (not disclosed)_ — ⚠️ 벤더 주장 (AtkinsRéalis): Shijo Thomas 인용. [[sources/beamery-atkins-realis-case-study-2025.md]]
- **참여 역할**: _미공개 (not disclosed)_
- **팀 규모·기간**: ⚠️ 벤더 주장 (Flex): 4주 미만 (40개 역할 정의). [[sources/beamery-flex-job-architecture-case-study-2025.md]]
- **거버넌스 체계**: _미공개 (not disclosed)_
- **파트너**: _미공개 (not disclosed)_


## Impact / Metrics (기대효과)

### 기대효과 요약
Skills-based 채용으로 성과 마일스톤 도달 25% 가속, 후보 식별 시간 30% 단축, Flex는 skills mapping 89% 단축 (벤더 주장 기반).

### AtkinsRéalis ($8.6B 엔지니어링)
| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| 성과 마일스톤 도��� 속도 | **25% 빠름** (Beamery 채용자) | Beamery case study | ⚠️ 벤더 주장 |
| Best-fit 후보 식별 시간 | **30%↓** | Beamery case study | ⚠️ 벤더 주장 |
| 후보 engagement | **40%↑** | Beamery case study | ⚠️ 벤더 주장 |

### Flex (전자 제조)
| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| JD 통합 시간 | **89%↓** (수작업 4~6개월 → 4주 미만) | [[sources/beamery-flex-job-architecture-case-study-2025.md]] | ⚠️ 벤더 주장 |
| 핵심 job profile 납품 | **17일** (데이터 수집→납품) | [[sources/beamery-flex-job-architecture-case-study-2025.md]] | ⚠️ 벤더 주장 |
| JD 통합 | **1,200+ JD → 40개 역할** | [[sources/beamery-flex-job-architecture-case-study-2025.md]] | ⚠️ 벤더 주장 |
| JD 복잡도 감소 | **97%** | [[sources/beamery-flex-job-architecture-case-study-2025.md]] | ⚠️ 벤더 주장 |
| 스킬 추론 적합도 | _미공개_ | — | (수치 근거 미확보 — 2026-09-27 grounding 점검) |

### Platform-wide
| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| ROI | **467%** (3년, 고객 1개사 인터뷰 기반 복합 모델) | [[sources/beamery-forrester-tei-467-roi-2023-10.md]] | ⚠️ 벤더 의뢰 연구 (Forrester Consulting TEI — Beamery 보도자료) |
| 채용 시간 절감 | **30,000+ 시간**, 리크루터 생산성 **10%↑** (~$613,000) | [[sources/beamery-forrester-tei-467-roi-2023-10.md]] | ⚠️ 벤더 의뢰 연구 |

## Governance & Risk

- ⚠️ 모든 수치가 벤더 작성 고객 사례·벤더 의뢰 TEI — 측정 방법·기간·표본 _미공개_, Tier 1·2 독립 검증 없음
- skills 기반 후보 식별·랭킹은 채용 의사결정에 관여 → 한국 AI 기본법 고영향 AI(채용) 검토 대상, EU AI Act Annex III
- 편향 감사·설명가능성 장치: _미공개 (not disclosed)_

## Contradictions

> [!note] 2026-09-27 grounding — 종전 본문의 "스킬 추론 90퍼센트 적합도"는 Flex 사례 페이지에 없음(페이지에는 97퍼센트 복잡도 감소·89퍼센트 시간 단축·17일만 존재). "4~6개월→17일" 표기는 소스상 "4~6개월→4주 미만"과 "17일 납품(핵심 profile)"이 별개 수치라 정정. Forrester TEI는 Beamery 의뢰·고객 1개사 기반이므로 "Tier 1 독립 검증"에서 ⚠️ 벤더 의뢰 연구로 하향. Skills Inference 엔진·Dynamic Job Architecture·SAP 동기화 서술은 인용 소스에 없어 제거. 두 사례 페이지 모두 게시일 불명.

## Consulting Angle

- **Job Architecture AI의 대표 사례**: Flex의 "1,200 JD→40역할" 통합은 [[workday-illuminate-job-architecture]]와 같은 도메인이지만 **실제 deployment + metric**이 있음
- **Forrester TEI 467% ROI**: 벤더 의뢰·고객 1개사 기반 복합 모델이므로 제안서에는 "Beamery 의뢰 Forrester TEI"로만 인용 — 타 벤더 TEI와 단순 비교 금지
- **J&J(MIT CISR, 스킬 추론)과의 비교**: J&J는 학술 검증(정확도), Beamery는 벤더 의뢰 TEI(ROI) — 검증 축이 다름
