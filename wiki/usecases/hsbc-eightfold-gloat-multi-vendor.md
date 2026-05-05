---
title: "HSBC — Eightfold AI + Gloat + SAP SF 멀티벤더 HR AI"
slug: hsbc-eightfold-gloat-multi-vendor
primary_category: Talent Acquisition
subcategory: Screening & Assessment
tags: [multi-vendor, skills-based-hiring, talent-marketplace, banking, eightfold, gloat, sap]
company: HSBC
industry: [finance, banking]
region: [eu, global]
employee_class: [all]
vendor: [Eightfold AI, Gloat, SAP SuccessFactors, Accenture]
vendor_type: [talent-marketplace, hrms]
output: "Eightfold의 1.6B+ profile 기반 skills inference + Gloat marketplace의 직원-기회 매칭 점수 + career path 추천 + 매니저용 internal candidate 리스트 (140K 직원 enrolled)"
ai_tech_type: [predictive, generative]
ai_tech_subtype: [recommendation-ranking, information-extraction, clustering-classification]
stage: production
frequency: daily
first_seen: 2025
last_confirmed: 2025
confidence: 0.30               # Tier 3 vendor cases(+0.10×3) + Tier 2 Fortune Europe(+0.20), multi-vendor 교차 = 0.30
consulting_angle_status: filled
sources:
  - "Eightfold case study https://eightfold.ai/learn/how-hsbc-is-staying-talent-forward-in-times-of-change/"
  - "Gloat case study https://resources.gloat.com/resources/hsbc-customer-success-story/"
  - "Accenture case study https://www.accenture.com/us-en/case-studies/talent-organization/hsbc-powers-talent-acquisition-future-ready-workforce"
related_usecases:
  - jpmorgan-goldman-sachs-hr-ai
  - workday-as-customer-paradox
related_vendors:
  - gloat
  - sap-successfactors
---

# HSBC — Eightfold AI + Gloat + SAP SF 멀티벤더 HR AI

> ★ **"벤더 3개 + 구현파트너 1개"의 가장 복잡한 실제 배포 사례**: HSBC(275,000 직원, 글로벌 대형 은행)가 **Eightfold AI**(skills-based 채용) + **Gloat**(내부 talent marketplace, 140k+ 직원) + **SAP SuccessFactors**(core HRIS) + **Accenture**(구현)를 동시 운영. [[workday-as-customer-paradox]]의 "multi-vendor stack" 논의를 **실제 대기업 배포로 입증**.

## Problem / Why (도입 배경)

- **Before**: HSBC(275,000 직원)의 TA(채용)와 TM(인재관리)이 **사일로화**되어 운영. 채용은 전통적 CV 기반, 내부 이동은 **가시성 부족**으로 외부 채용에 과도 의존
- **Pain point**: 글로벌 은행의 **skills transformation 압박** — 디지털·AI 역량 인력 확보가 시급하지만 기존 채용 방식으로는 속도·품질 부족. ⚠️ Fortune Europe 보도: HSBC가 다른 유럽 은행보다 **30% 더 많은 AI 채용 공고**를 게시 (인력 전환 가속화 필요 반증)
- **Trigger**: SAP SuccessFactors(Core HRIS)만으로는 skills-based hiring + internal mobility 모두를 커버하기 어렵다는 판단 → Eightfold(TA) + Gloat(TM) + Accenture(구현) 멀티벤더 결정

## Solution Architecture

### A. Process

- **Before**: 14만 직원 대상 내부공모는 manager 추천·비공식 네트워크 의존, 글로벌 가시성 부재
- **After**:
  1. HSBC middleware가 HRIS·ATS·LMS·skills 데이터를 통합
  2. Eightfold이 1.6B+ profile 기반 skills inferencing 수행 (기반 skill graph)
  3. Gloat marketplace에 inferred skills로 직원·기회 매칭
  4. 직원이 project·gig·job·mentorship 검색·지원 (인도 tech팀 우선 → 14만 확장)
  5. AI가 매칭 점수·career path 추천
  6. 매니저·HR이 매칭 결과 검토·승인
- **HITL**: 매니저가 internal candidate 인터뷰·승인
- **Frequency**: continuous (rolling marketplace)
- **Source**: Gloat HSBC case study


## Impact / Metrics (기대효과)

### 기대효과 요약
Before: 275,000 직원의 TA·TM 사일로 운영, 내부 이동 가시성 부족으로 외부 채용 과도 의존 → After: ⚠️ 벤더 주장 140,000+ 직원 Gloat 등록, 250+ recruiter 교육, 45+ learning asset rollout. 구체적 ROI(채용 비용 절감율·내부 충원률 변화) _미공개_.

## Key Facts

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| Gloat talent marketplace | **140,000+ ��원** enrolled | Gloat case study | ⚠️ 벤더 주장 |
| Eightfold AI | Skills-based 채용, CV ranking, bias 최소화 스크리닝 | Eightfold case study | ⚠️ 벤더 주장 |
| Learning assets | **45+** rolled out | Accenture case study | ⚠️ 벤더 주장 |
| Trained recruiters | **250+** recruiters + hiring managers | Accenture case study | ⚠️ 벤더 주장 |
| Core HRIS | **SAP SuccessFactors** | 공개 정보 | ✅ Fact |
| 구현 파트너 | **Accenture** | 공개 정보 | ✅ Fact |
| AI 채용 비중 | 30% 더 많은 AI job vacancies (vs 다른 유럽 은행) | Fortune Europe 2024-07 | ✅ Fact (Tier 2) |

## Consulting Angle

### ★ Multi-vendor HR AI stack의 실제 작동 증거

HSBC의 배포는 [[workday-as-customer-paradox]]에서 이론적으로 논의한 **"multi-vendor HR AI stack"**의 **가장 복잡한 실제 사례**:

```
SAP SuccessFactors (Core HRIS)
    ├── Eightfold AI (Skills-based 채용)
    ├── Gloat (Internal talent marketplace)
    └── Accenture (구현·통합)
```

이는 **Workday 패턴**(suite + point solutions)과 유사하며, **SAP SF의 consolidation 패턴**(Delta/Pepsi가 3rd party 버림)과는 **정반대**. 즉:
- Delta/Pepsi: SF만으로 충분, Gloat·Eightfold 불필요
- **HSBC: SF + Eightfold + Gloat 모두 사용** — SF만으로 불충분

→ "suite consolidation vs multi-vendor"는 **고객의 선택**이지 벤더의 결정이 아님.

### 한국 금융 시사점
- 한국 대형 은행(KB·신한·하나·우리)이 HR AI 도입 시 HSBC가 reference
- 국내 은행은 SAP SF·Workday 도입률이 높으므로 **HSBC의 "SF + point solutions" 패턴**이 가장 현실적 경로
