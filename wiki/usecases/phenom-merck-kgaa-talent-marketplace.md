---
title: "Merck KGaA — Phenom 기반 내부 인재 플랫폼 (36k 직원, 200k 스킬, 1k 멘토십)"
slug: phenom-merck-kgaa-talent-marketplace
primary_category: Onboarding & Transitions
subcategory: Internal Mobility
tags: [talent-marketplace, skills, mentorship, internal-mobility, pharma, phenom]
company: Merck KGaA
industry: [pharma, chemicals]
region: [eu]
employee_class: [all]
vendor: [Phenom]
vendor_type: [talent-marketplace]
ai_tech_type: [predictive, generative]
ai_tech_subtype: [recommendation-ranking, information-extraction]
stage: production
frequency: daily
first_seen: 2025-03
last_confirmed: 2025-03-12
confidence: 0.30               # Tier 3 vendor award(+0.10) + Tier 4 BusinessWire PR(+0.15) + 구체 수치 다수 = 0.30
consulting_angle_status: filled
sources:
  - "BusinessWire/Phenom 2025-03-12 https://www.businesswire.com/news/home/20250312351615/en/Phenom-Announces-2025-Talent-Experience-Award-Winners-Global-Enterprises-Set-New-HR-Benchmarks"
  - "Phenom customers https://www.phenom.com/customers"
related_usecases:
  - unilever-flex-gloat-talent-marketplace
  - schneider-electric-gloat-talent-marketplace
related_vendors: []
---

# Merck KGaA — Phenom 기반 내부 인재 플랫폼

## Summary

Merck KGaA(독일 다름슈타트, 60,000+ 직원, 제약·화학·생명과학)가 Phenom Talent Experience 플랫폼을 도입해 **전 직원 과반(36,000+)이 활발 사용**, **200,000+ 스킬 등록, 29,000+ 학습 콘텐츠 중앙화, 1,000+ 멘토십** 운영. Gloat(Unilever·Schneider) 대비 **Phenom이 talent marketplace + learning + mentoring을 통합한 use case**.

## Impact / Metrics (기대효과)

### 기대효과 요약
⚠️ 벤더 주장: 36,000+/60,000 직원 활발 사용, 200,000+ 스킬 등록, 29,000+ 학습 콘텐츠 중앙화, 1,000+ 멘토십 — 모두 adoption/output 수치이며 outcome(내부 이동률 변화·스킬 갭 감소·시간 절감) 아님. Before 상태 _미공개_.

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| 활성 사용자 | **36,000+ 직원** (과반) | Phenom 2025 Award | ⚠️ 벤더 주장 |
| 개인 프로필 생성 | **14,000+** | Phenom 2025 Award | ⚠️ 벤더 주장 |
| 등록 스킬 | **200,000+** | Phenom 2025 Award | ⚠️ 벤더 주장 |
| 중앙화 학습 콘텐츠 | **29,000+** | Phenom 2025 Award | ⚠️ 벤더 주장 |
| 멘토십 | **1,000+** | Phenom 2025 Award | ⚠️ 벤더 주장 |
| 전체 직원 | ~60,000 | 공개 정보 | ✅ Fact |

## Solution Architecture (요약)

### A. Process

- **Before**: 내부 후보자가 지원해도 결과 통보 없이 발표로 알게 되는 등 candidate experience 미흡
- **After**:
  1. 직원이 MyGrowth 포털에서 profile 생성·skills 입력 (200,000+ skills)
  2. Phenom AI가 inferred skills로 jobs·gigs·learning·mentor 매칭
  3. 개인 dashboard에서 추천 기회·learning(29,000+ 콘텐츠)·mentor 1,000+ 표시
  4. 직원이 gig/job/mentor 신청 → 매니저·HR에 routing
  5. 채용 매니저가 internal candidate 검토·피드백
  6. 결과·진행상황을 candidate에게 자동 통지
- **HITL**: 매니저가 internal candidate 평가·결정
- **Frequency**: continuous
- **Source**: Phenom 2025 Talent Experience Award Winners

### Phenom platform의 통합 범위
- **Internal mobility**: 직원 스킬 → 내부 기회 매칭
- **Skills ontology**: 200,000+ 스킬이 조직 수준에서 관리됨
- **Learning centralization**: 29,000 learning offerings을 단일 플랫폼에 통합
- **Mentorship matching**: 1,000+ 멘토-멘티 매칭

→ Gloat(project-based mobility) 대비 **Phenom은 mobility + learning + mentoring 통합**. 이것이 제품 포지셔닝의 핵심 차이.

## Consulting Angle

### ★ 유럽(EU) region 최초의 fact-rich internal mobility 사례
- Unilever (글로벌/UK), Schneider Electric (글로벌/프랑스)에 이어 **Merck KGaA (독일)**
- **EU 기업 특유의 맥락**: GDPR 규제 하에서 스킬 데이터 200k를 운영한다는 것 자체가 governance 사례

### Dallas College (Phenom) — TA 사례도 함께 기록
| 지표 | 값 |
|---|---|
| Time-to-fill 단축 | **50%** (staff·admin 포지션) |
| Career site 방문 | 업계 벤치마크 **2배 이상** |
| Lead 생성 | 경쟁사 대비 **32% 더 많음** |
| 구현 기간 | **6개월** |

### vs Gloat (Unilever, Schneider) vs Phenom (Merck KGaA)

| | Gloat | Phenom |
|---|---|---|
| 핵심 | Project-based mobility | **Mobility + Learning + Mentoring 통합** |
| 대표 고객 | Unilever (65k), Schneider (135k) | **Merck KGaA (60k)**, Dallas College |
| 수치 유형 | Hours unlocked, $ saved | **스킬 수, 학습 수, 멘토십 수** |
| SAP 연동 | 경쟁 관계 (SF가 대체 시도) | **SAP 파트너** (ISV) |
