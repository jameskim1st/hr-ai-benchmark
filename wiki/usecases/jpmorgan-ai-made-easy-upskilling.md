---
title: "JPMorgan — 'AI Made Easy' 전사 AI 교육 (230K 직원, 신입 분석가 prompt engineering 의무)"
slug: jpmorgan-ai-made-easy-upskilling
primary_category: Learning & Development
subcategory: Skills & Capabilities
tags: [ai-made-easy, jpmorgan, upskilling, prompt-engineering, mass-training, finance, role-specific-curriculum]
company: JPMorgan Chase
industry: [finance, banking]
region: [na, global]
employee_class: [all]
vendor: [JPMorgan internal]
vendor_type: [internal-build]
ai_tech_type: [generative]
ai_tech_subtype: [summarization-qa]
stage: production
frequency: annual
first_seen: 2024-08-01
last_confirmed: 2026-02-12
confidence: 0.70
consulting_angle_status: filled
sources:
  - sources/us-large-enterprise-hr-ai-2025-2026.md
  - "McKinsey: JPM Derek Waldron interview — 'AI Made Easy' program direct mention https://www.mckinsey.com/industries/financial-services/our-insights/jpmorgan-chases-derek-waldron-on-building-an-ai-first-bank-culture"
related_usecases:
  - jpmorgan-llm-suite-redeployment
  - accenture-mass-genai-reskilling
related_vendors: []
---

## Summary

JPMorgan **AI Made Easy** — 230K 직원 대상 전사 AI 교육 프로그램. AI fundamentals + prompt engineering + 컴플라이언스 + 직무별 use case curriculum. Asset & Wealth Management 신입 분석가에게 **prompt engineering 필수**. LLM Suite 200K+ 8개월 onboarding의 교육 backbone.

## Problem / Why

- **Before**: 230K 직원 중 AI literacy 분포 편차 큰 — 데이터 사이언티스트는 풍부, 운영·영업·고객서비스 직원은 baseline
- **Pain point**: 회사 LLM Suite를 도입해도 사용 모르면 ROI 없음
- **Trigger**: LLM Suite launch 동시 추진 (2024-08)

## Solution Architecture

### A. Process

- **Before**: 직원 AI 교육은 자율·신청 기반
- **After**:
  1. 전 직원 baseline AI fundamentals 모듈 의무
  2. Prompt engineering 모듈 (LLM Suite 활용 직군 의무)
  3. 컴플라이언스 모듈 (금융정보·고객정보 처리 가이드)
  4. 직무별 use case curriculum (analyst·trader·banker·HR·legal·ops 별)
  5. 신입 분석가 (Asset & Wealth Management): prompt engineering 의무 수료
- **HITL**: HRD·legal·각 사업부 SME 협업
- **Frequency**: annual cycle + 신입 onboarding 시

### B/C/D/E. System

- 자체 LMS 추정, LLM Suite 자체가 hands-on lab
- 사업부별 curriculum customization
- 오너십: HR + IT/AI Plat팀 + 사업부 SME

### B. System & Infrastructure (Agent research expanded)

- **Core HRIS / 기반 시스템**: _미공개_ (JPM HRIS 명시 없음)
- **AI 시스템 배치**: ✅ AI Made Easy 교육 sessions + LLM Suite hands-on 플랫폼 통합
- **배포 환경**: ✅ LLM Suite는 JPMorgan 자체 portal (proprietary); 교육 LMS 명시 없음
- **연동·통합**: ✅ LLM Suite는 8주마다 internal database·software apps 추가 통합
- **사용자 접점**: ✅ AI Made Easy = 인터랙티브 sessions (live + 직무별 모듈); LLM Suite portal 직접 hands-on
- **인증·권한**: _미공개_ (JPM internal SSO 추정)

### C. Data (Agent research)

- **입력 데이터 소스**: ✅ 교육 콘텐츠 = AI fundamentals + prompt engineering + compliance + 직무별 use case curriculum
- **데이터 규모**: ✅ Q1 alone **30,000+ 직원 attended AI Made Easy sessions** (신규 fact); 230K+ in scope; 250K LLM Suite rollout (branch·call center 제외, 약 절반 daily 사용)
- **전처리·정제**: N/A (training program)
- **학습 vs RAG vs In-context**: N/A
- **데이터 거버넌스**: ✅ Compliance 모듈 별도 (금융정보·고객정보 처리 가이드)
- **민감정보 처리**: ✅ Compliance 모듈에서 다룸

### D. Model (Agent research expanded)

- **Foundation model**: N/A (training program 자체)
- **모델 유형**: N/A — 단, hands-on 학습 대상 LLM Suite는 ✅ **OpenAI + Anthropic 양사** (multi-vendor, 신규 발견)
- **제공 방식**: N/A
- **커스터마이징 기법**: ✅ "Learn by doing" — LLM Suite 직접 사용 통합
- **Orchestration 프레임워크**: N/A
- **평가·가드레일**: ⚠️ 자사 보고: 직원당 3-6h/week saved (LLM Suite 결합 효과)


## Impact / Metrics

### 기대효과 요약
대규모 단일 교육으로 LLM Suite 200K+ 8개월 onboarding 가능 + 신입 prompt engineering baseline 확립.

- 230K+ 직원 in scope
- 200K+ LLM Suite onboarded in 8 months
- ⚠️ 자사 보고: 직원당 3-6h/week saved (LLM Suite 효과와 결합)

## Governance & Risk

- ⚠️ 의무 prompt engineering 교육이 신입 분석가 워크로드 증가 — 효과 측정 _미공개_
- ⚠️ "AI Made Easy" 자체 효과 측정 metric 별도 _미공개_

## Consulting Angle

- **KR 그룹 HRD 센터 직접 reference**: 삼성인력개발원·LG Aspire·SK mySUNI·현대인재개발원 모두 AI 교육 curriculum 기획 중. JPMorgan 구조 (foundational + role-specific + 신입 의무) 직접 차용 가능
- **금융권 fit 우수**: KB·신한·우리·하나·미래에셋 모두 자체 LLM 플랫폼 도입 중 → 동반 교육 프로그램 reference (위 [[jpmorgan-llm-suite-redeployment]]와 pair)
- **신입 prompt engineering 의무**: KR 대기업 신입 공채 후 OJT/연수원 과정에 모듈 통합 — 2026 신입 입사자부터 적용 가능
- **2026 Q3-Q4 KR 컨설팅 deck**: "AI 도입 = 도구 + 교육의 시간차 0" — JPMorgan의 동시 launch 전략이 모범
- **반면교사**: 230K 단일 corp culture라서 통합 가능 — KR 대기업 그룹사 multi-corp 환경에서는 계열사별 미세 customization 필요
