---
title: "Siemens My Learning World — AI 기반 리스킬링·내부 이동"
slug: siemens-reskilling-internal-mobility
primary_category: Learning & Development
subcategory: Skills & Capabilities
tags: [reskilling, internal-mobility, skills, manufacturing, my-learning-world, europe]
company: Siemens
industry: [manufacturing, energy, tech]
region: [eu, global]
employee_class: [all]
vendor: [Siemens (internal build), ServiceNow]
vendor_type: [internal-build]
output: "My Learning World 학습자별 적응형 학습 경로 추천 (100,000+ 학습 기회·41 capability) + AI 채용·이동 포탈의 후보자-역할 매칭 점수"
ai_tech_type: [predictive]
ai_tech_subtype: [recommendation-ranking]
stage: production
frequency: daily
first_seen: 2025
last_confirmed: 2025
confidence: 0.45               # Tier 2 AIHR(+0.20) + Tier 2 MISQ(+0.20) + Tier 1 WEF(+0.35, 할인→+0.20, 자사 commitment 전달 성격) + Tier 3 ServiceNow(+0.10) = base 0.70, 할인 후 → 0.45
consulting_angle_status: filled
sources:
  - "AIHR Institute https://www.aihr-institute.com/blog/how-ai-is-transforming-hr-at-siemens"
  - "MISQ Executive https://aisel.aisnet.org/cgi/viewcontent.cgi?article=1637&context=misqe"
  - "HRKatha https://www.hrkatha.com/features/how-siemens-india-is-navigating-workforce-transformation-in-the-age-of-ai/"
  - "ServiceNow case study https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/resource-center/case-study/cs-siemens-ag.pdf"
  - sources/wef-siemens-reskilling-revolution-case.md
related_usecases:
  - schneider-electric-gloat-talent-marketplace
  - accenture-ai-learning-workforce
  - docebo-ai-learning-lazboy
related_vendors: []
---

# Siemens — 300k 리스킬링 + 20% 내부 이동 증가

> **제조업 HR AI 대표 사례**: Siemens(300,000+ 직원, 글로벌 산업 자동화·에너지)가 **Future Skills Initiative**로 전 직원 리스킬링 + AI 기반 내부 이동 플랫폼을 운영. ⚠️ 자사 보고: **내부 이동 20% 증가**, 외부 채용 의존도 감소. **WEF Reskilling Revolution**(Tier 1 국제기구)이 Siemens를 공식 사례 기업으로 선정 ([[wef-siemens-reskilling-revolution-case]]) — blended funding model, 정부 co-financing, 디지털화·지속가능성 교육 프로그램 독립 확인.

## Summary

Siemens는 **Future Skills Initiative**를 통해 300,000 직원 대상으로 데이터 분석·디지털 트윈·자동화 역량 리스킬링을 추진. AI 기반 학습 플랫폼 **My Learning World**는 100,000+ 학습 기회를 제공하며, 개인화된 학습 경로를 적응형으로 제공. ⚠️ 자사 보고: 내부 이동 **20% 증가**, AI 기반 채용·내부 이동 포탈이 후보자 매칭·스킬 추천을 최적화.

## Solution Architecture

### A. Process

- **Before**: Siemens가 디지털 전환을 추진하나 data analytics·digital twin·automation 인력은 외부 채용 의존, 기존 직원 reskilling은 부서별 단발 교육
- **After**:
  1. Siemens가 Future Skills Initiative 발표 (300k 직원 대상, 41개 capability 영역 정의)
  2. Germany Qualification Opportunities Act 활용해 정부 25% 비용 분담, 외부 파트너와 cost-sharing
  3. 직원·파트너에게 vocational training (digitalization·sustainability) 콘텐츠 제공
  4. Reskilled 직원을 internal mobility 플랫폼 통해 신규 디지털 role로 재배치
  5. 결과 KPI(internal mobility +20%) tracking, 외부 채용 의존도 축소
- **HITL**: 매니저가 reskilling 후보 nominate, HR이 재배치 매칭 승인
- **Frequency**: 교육 등록 = monthly, mobility 매칭 = adhoc/quarterly
- ⚠️ AI 활용 구체 process(어떤 알고리즘이 매칭하는지)는 _미공개_ — reskilling 자체는 fact, AI 의존도는 미명시

### B. System & Infrastructure (R9 research)

- **Core HRIS**: _미공개_ (Workday 사용 여부 미확인) + ✅ ServiceNow (Siemens GBS — ServiceNow case study Tier 3)
- **AI 시스템 배치**: ✅ My Learning World (사내 LXP, 100K+ 학습) + 별도 AI 채용·이동 포탈
- **배포 환경**: _미공개_
- **연동·통합**: ✅ ServiceNow HR Service Delivery (GBS), Siemens HRIS와 mobility 매칭 sync
- **사용자 접점**: My Learning World web·모바일, internal mobility portal
- **인증·권한**: Siemens 사내 SSO

### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 직원 skill profile, 학습 이력, 41 capability, role·position
- **데이터 규모**: ⚠️ 자사 보고: 300K 직원, 100K+ 학습 기회
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_ — 매칭 알고리즘 공식 미명시 (AIHR caveat)
- **데이터 거버넌스**: _미공개_ — EU GDPR (Siemens HQ 독일)
- **민감정보 처리**: _미공개_

### D. Model (R9 research)

- **Foundation model**: _미공개_ — AI 채용·이동 포탈 모델 미공개
- **모델 유형**: predictive (recommendation·ranking)
- **제공 방식**: ✅ 일부 ServiceNow (GBS), 일부 Siemens 자체
- **커스터마이징 기법**: ✅ 41 capability 자체 정의 → matching engine 주입
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: _미공개_


## Impact / Metrics (기대효과)

### 기대효과 요약
300,000 직원 대상 리스킬링, 내부 이동 20% 증가, 100,000+ 학습 기회 제공 (자사 보��� 기반).

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| 리스킬링 대상 | **300,000 직원** | AIHR Institute | ⚠️ 자사 보고 |
| 내부 이동 증가 | **20%** | AIHR Institute | ⚠️ 자사 보고 |
| 학습 기회 | **100,000+** (My Learning World) | HRKatha | ⚠️ 자사 보고 |
| HR 전략적 위치 | "모든 비즈니스 리뷰·전략 논의·인력 계획에 HR 참여" | Shilpa Kabra Maheshwari (EVP, Siemens India) | ⚠️ 자사 보고 |
| WEF Reskilling Revolution 파트너 | 공식 사례 기업 선정 | [[wef-siemens-reskilling-revolution-case]] (WEF Tier 1) | ✅ Fact (Tier 1 국제기구 공식 인정) |
| Blended funding model | 정부 co-financing 최대 **25%** (독일 Qualification Opportunities Act) | [[wef-siemens-reskilling-revolution-case]] | ✅ Fact |
| 교육 범위 | 디지털화·지속가능성 분야 직업교육, 자사 + 외부 파트너 대상 | [[wef-siemens-reskilling-revolution-case]] | ✅ Fact |

## Consulting Angle

- **제조업 L&D AI 최대 규모**: 300k 직원 대상 리스킬링은 wiki의 학습·역량 카테고리에서 가장 큰 scale
- **Schneider Electric과 같은 "European manufacturing + internal mobility" 패턴**: ���사 모두 내부 이동 증가를 핵심 KPI로 측정
- **ServiceNow GBS 통합**: Siemens GBS가 ServiceNow로 employee experience를 통합했다는 별도 case study 존재 — 대기업의 "multi-vendor HR tech stack" 증거
- **한국 제조업 시사점**: 삼성전자·현대자동차·LG 등 국내 제조 대기업의 리스킬링 전략에 Siemens가 직접 reference
