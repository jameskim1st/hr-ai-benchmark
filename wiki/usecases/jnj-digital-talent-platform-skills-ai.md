---
title: "Johnson & Johnson — Digital Talent Platform"
slug: jnj-digital-talent-platform-skills-ai
primary_category: Learning & Development
subcategory: Skills & Capabilities
tags: [skills-inference, internal-mobility, learning, academic-validation, mit-cisr, pharma]
company: Johnson & Johnson
industry: [pharma, healthcare, consumer]
region: [global]
employee_class: [기술사무직]
vendor: [J&J (internal build)]
vendor_type: [internal-build]
output: "130K+ 직원별 inferred 스킬 그래프 (HRIS·채용DB·LMS·프로젝트에서 60~70% 자동 추론, 0~5 proficiency) + MySkills 플랫폼의 본인 스킬 갭·추천 학습/이동 + 임원 dashboard region·BU별 capability heatmap"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [information-extraction, clustering-classification, recommendation-ranking]
stage: production
frequency: daily
first_seen: 2020
last_confirmed: 2025
confidence: 0.60               # ★ Tier 1 MIT CISR(+0.35) + Tier 1 학술지 IS Journal(+0.35) - 중복 학술 소스 보정 = 0.60
consulting_angle_status: filled
sources:
  - "MIT CISR Working Paper 2024 https://cisr.mit.edu/publication/MIT_CISRwp461_JohnsonandJohnsonAIDrivenSkills_VanderMeulenTonaSomehWixomLeidner"
  - "Information Systems Journal 2025 https://onlinelibrary.wiley.com/doi/full/10.1111/isj.12594"
related_usecases:
  - midas-inair-ai-assessment-korea
  - eightfold-ai-talent-intelligence
  - siemens-reskilling-internal-mobility
related_vendors: []
---

# Johnson & Johnson — Digital Talent Platform (AI 스킬 추론)

> ★★ **Wiki 최고 수준 학술 검증 사례**: MIT CISR + peer-reviewed *Information Systems Journal* 에 발표된 연구로, AI가 직원 스킬의 60~70%를 자동 추론하고, 내부 배치 8%↑·자발적 이탈 3.2%↓·학습 참여 20%↑를 달성�� 것이 **독립 학술 연구로 확인**됨. 마이다스아이티 Nature 논문(채용 예측)과 함께 wiki의 **양대 ���술 검증 사례**.

## Summary

J&J Technology 부서가 자체 구축한 **Digital Talent Platform**은 HRIS·채용DB·LMS·프로젝트 관리 시스템에서 데이터를 추출해 **각 ��원 스킬의 60~70%를 AI가 자동 추론**. 2020년 4,000명 기술직에서 시작해 2021년 전사 확장. MIT CISR 연구진이 다년간 추적 연구를 수행하고 학술지에 발표.

## Impact / Metrics (기대효과)

### 기대효과 요약
AI가 직원 스킬의 60~70%를 자동 추론(Tier 1 학술 검증), J&J Learn 접근율 90%+, 자발적 학습 참여 20% 증가 (MIT CISR Fact).

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| AI 스킬 추론 비율 | **60~70%** (나머지는 직원 자기보고) | MIT CISR + IS Journal | ✅ **Fact (Tier 1 학술)** ★ |
| J&J Learn 접근율 | **90%+** (Technology 직원, 2024-03 기준) | MIT CISR | ✅ **Fact (Tier 1 학술)** |
| 자발적 학습 참여 | 스킬 추론 도입 후 **20%↑** | IS Journal 2025 | ✅ **Fact (학술)** |
| 내부 배치 | 2023 대비 **8%↑** (2024) | IS Journal 2025 | ✅ **Fact (학술)** |
| 디지털 역할 이탈율 | 전사 대비 **3.2% 낮음** | IS Journal 2025 | ✅ **Fact (학술)** |
| 디지털 역할 충원 시간 | **2.5% 개선** | IS Journal 2025 | ✅ **Fact (학술)** |
| 시작 규모 | 4,000 technologists (2020) → 전사 (2021) | MIT CISR | ✅ **Fact** |

**★ 핵심**: 이 metric들은 모두 **MIT CISR 연구 + IS Journal peer review**를 거쳤으므로 wiki의 다른 어떤 metric보다도 독립 검증 수준이 높음.

## Solution Architecture

### A. Process (프로세스)

- **Before**: 130k+ 직원 스킬 보유 현황은 자가 신고·이력서 기반 단편적이며, 매니저는 후보자 스킬을 일일이 확인해 internal mobility 후보 search. 스킬 갭 진단은 부서별 수기·연 1회 수준
- **After**:
  1. HR이 41개 future-ready skills · 11개 capability를 정의해 taxonomy 등록
  2. LLM(skills inference)이 직원 프로필·learning 이력·과제 이력을 읽어 skill별 0~5 proficiency 자동 산출 (60~70% 추론)
  3. MySkills 플랫폼이 직원에게 본인 스킬 그래프·갭·추천 학습/이동 기회 제시
  4. J&J Learn이 skill gap 기반 과정·growth assignment·멘토링 매칭
  5. 임원은 dashboard에서 region·BU별 capability heatmap 조회 → 채용·재배치·후계 의사결정
  6. 내부 이동 발생 시 last_confirmed 스킬 갱신 → 모델 재추론
- **HITL**: 직원이 inferred score 검토·수정, 매니저가 calibration, HR이 taxonomy·dashboard governance
- **Frequency**: 추론 = 수시(이벤트), dashboard 검토 = monthly, taxonomy review = quarterly

### B. Data Sources (학술 논문에서 명시)
- HRIS (인사 기본 정보)
- Recruiting database (채용 이력)
- LMS (학습 이력)
- Project management tools (프로젝트 참여 이력)

## Consulting Angle

### ★★★★★ Wiki 최고 가치 — 학술 검증 + 구체 outcome metric

1. **"스킬 추론 AI"의 gold standard**: HRIS 데이터에서 60~70% 스킬을 자동 추론한다는 사실이 학���적으로 확인됨 — Eightfold·Gloat 등 벤더의 "skills intelligence" 주장과 달리 **독립 연구로 효과 입증**
2. **내부 이동 + 이탈 감소 + 학습 참여를 모두 측정**: "스킬 AI를 넣으면 무슨 일이 일어나는가?"에 대해 가장 완전한 answer
3. **마이다스아이티(Nature, 채용 예측)와 J&J(MIT CISR, 스킬 추론)**: wiki의 **양대 학술 사례** — 전자는 "AI가 사람을 정확히 평가하��가?"에, 후자는 "AI가 사람의 스킬을 정확히 ��악하는가?"에 답

### 한국 적용
- 국내 대기업 HR이 "스킬 기반 인사관리" 전환을 검토할 때 **J&J가 가장 강력�� reference** (학술 검증)
- 4,000명���전사 확장의 **단계적 전개 패턴**이 한국 대기업 pilot-first 문화와 fit
