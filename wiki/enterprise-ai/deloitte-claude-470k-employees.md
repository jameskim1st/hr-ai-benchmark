---
title: "Deloitte — Anthropic Claude 전직원 배포"
slug: deloitte-claude-470k-employees
page_type: enterprise-ai
moved_from_usecases: 2026-09-27
primary_category: Employee Experience & HR Ops
subcategory: HR Service Delivery
tags: [claude, anthropic, enterprise-ai, consulting, large-scale, productivity]
company: Deloitte
industry: [consulting, professional-services]
region: [global]
employee_class: [all]
vendor: [Anthropic]
vendor_type: [foundation-model]
output: "회계·감사·컨설팅 직무별 문서 합성·코드 생성·클라이언트 자료 분석 결과물 + 회계사·개발자 특화 Claude 응답 (Trustworthy AI framework 검증 통과)"
ai_tech_type: [generative]
ai_tech_subtype: [text-generation, summarization-qa]
stage: announced
visibility: public
case_type: adoption
regulatory_exposure: []
frequency: daily
first_seen: 2025-10-06
last_confirmed: 2025-10-06
confidence: 0.45
evidence_grade: B
corroborated_by: 1
freshness: fresh
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/cnbc-anthropic-deloitte-claude-2025-10.md, sources/anthropic-deloitte-partnership-2025-10.md]
related_usecases:
  - ibm-askhr-watsonx
  - moderna-ask-hr-routing
related_vendors: []
---

# Deloitte — Anthropic Claude 470,000 직원 배포

> ★ **Anthropic 역대 최대 엔터프라이즈 배포**: Deloitte(470,000 직원, 150개국)가 Claude를 전 직원에게 배포 — Anthropic의 가장 큰 엔터프라이즈 고객. ⚠️ 자사 보고: Claude Center of Excellence 설립, 15,000명 전문 인증 계획. 회계사·소프트웨어 개발자용 특화 Claude 버전 개발.

## Problem / Why (도입 배경)

- **Before**: Deloitte 470,000 직원이 150개국에서 회계·감사·컨설팅·세무 업무 수행. 각 직무별 AI 도구가 파편화돼 있거나 부재. 지식 검색·문서 초안·분석에 **사람의 반복 작업 시간이 과도**
- **Pain point**: 경쟁 컨설팅사(Accenture·PwC·McKinsey)가 각각 AI를 전사 배포하는 상황에서 **"consulting firms의 AI 군비 경쟁"**이 Deloitte의 채택 가속화 요인
- **Trigger**: Anthropic Claude가 엔터프라이즈 보안·규정 준수를 충족하면서도 **"회계사·개발자별 특화 버전"**을 제공할 수 있다는 판단 → 역대 최대 엔터프라이즈 배포 결정

## Solution Architecture

### A. Process (프로세스)

- **Before**: Deloitte 470k 직원이 audit·tax·consulting 산출물을 수기·MS Office·기존 internal KM으로 작성. 사내 GenAI 사용은 부서별 파일럿 단위
- **After** (발표 시점 계획 — 소스는 미래형):
  1. ✅ Deloitte가 Claude를 글로벌 네트워크 470,000명에게 제공 예정 (계정 프로비저닝 방식 _미공개_). [[sources/anthropic-deloitte-partnership-2025-10.md]] [[sources/cnbc-anthropic-deloitte-claude-2025-10.md]]
  2. ⚠️ 벤더 주장: Claude Center of Excellence가 implementation framework 개발·leading practice 공유·기술 지원 제공, 15,000명 certification 프로그램 공동 개발. [[sources/anthropic-deloitte-partnership-2025-10.md]]
  3. ✅ 회계사~소프트웨어 개발자 등 직군별 Claude "persona"를 수개월에 걸쳐 구축·배포 예정. [[sources/cnbc-anthropic-deloitte-claude-2025-10.md]]
  4. ⚠️ 벤더 주장: 규제 산업(financial services·healthcare·public services)용 컴플라이언스 솔루션을 Claude + Deloitte Trustworthy AI™ framework 결합으로 공동 개발 (클라이언트 대상). [[sources/anthropic-deloitte-partnership-2025-10.md]]
  5. 사용 로그·prompt 모니터링 체계: _미공개 (not disclosed)_
- **HITL**: _미공개 (not disclosed)_
- **Frequency**: daily (개별 사용 — 배포 후 기준); CoE 운영 주기 _미공개_

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS**: _미공개_ (Deloitte 사내 — Workday 사용 여부 공식 미확인)
- **AI 시스템 배치**: ✅ Anthropic Claude를 470,000명 글로벌 네트워크에 제공 (별도 SaaS; 제품 에디션·프로비저닝 방식 _미공개_). [[sources/anthropic-deloitte-partnership-2025-10.md]]
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: ⚠️ 벤더 주장: "technology integration" 포함이라고만 언급 — 세부 _미공개_. [[sources/anthropic-deloitte-partnership-2025-10.md]]
- **사용자 접점**: ✅ 회계사·소프트웨어 개발자 등 직군별 Claude "persona". [[sources/cnbc-anthropic-deloitte-claude-2025-10.md]] (일반 접점 UI _미공개_)
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: ⚠️ 자사 보고: 클라이언트 자료·문서·코드 — use case별 상이
- **데이터 규모**: ✅ 470K 직원, 150개국
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_ — 회계사·개발자 특화 = fine-tuning vs system prompt 미공개
- **데이터 거버넌스**: ⚠️ 벤더 주장: Trustworthy AI™ framework(클라이언트용 솔루션에 결합), Claude CoE. [[sources/anthropic-deloitte-partnership-2025-10.md]] — 사내 데이터 거버넌스 세부 _미공개_
- **민감정보 처리**: _미공개_ — 클라이언트 confidential 처리 정책 미발표

### D. Model (모델)

- **Foundation model**: ✅ Anthropic Claude (버전 미명시)
- **모델 유형**: LLM (생성·요약·코드)
- **제공 방식**: ✅ Anthropic 상용 제공 (Claude) — 에디션·API 경로 _미공개_. [[sources/anthropic-deloitte-partnership-2025-10.md]]
- **커스터마이징 기법**: ⚠️ 자사 보고: 회계사·개발자 특화 버전, 규제 산업 industry pack 공동 개발
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: ⚠️ 자사 보고: Trustworthy AI framework + 파트너 검토


## Impact / Metrics (기대효과)

### 기대효과 요약
Before: 470,000 직원이 파편화된 AI 도구 사용 또는 미사용 → After: 전 직원 Claude 통합 배포(Fact) + 15,000명 인증 계획(⚠️ 자사 보고). 구체 ROI 수치(시간·비용 절감)는 _미공개_ — 2026년 후속 보고 예상.

## Key Facts

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| 배포 규모 | **470,000 직원**, 150개국 | CNBC + Anthropic | ✅ Fact (Tier 1+3 교차) |
| "역대 최대" | Anthropic의 **largest enterprise deployment ever** | Anthropic | ✅ Fact |
| CoE 설립 | Claude Center of Excellence | Anthropic | ⚠️ 자사 보고 |
| 인증 계획 | **15,000명** 전문가 Claude 인증 | CNBC | ⚠️ 자사 보고 |
| 특화 버전 | ��계사용·소프트웨어 개발자용 Claude | CNBC | ⚠️ 자사 보고 |

## Consulting Angle

### 전사 AI 배포�� scale 비교

| | Deloitte Claude | Walmart Ask Sam | IBM AskHR | Moderna GPTs |
|---|---|---|---|---|
| **규모** | **470,000명** | [[usecases/walmart-ask-sam-workforce-ai]] 참조 | [[usecases/ibm-askhr-watsonx]] 참조 | [[usecases/moderna-ask-hr-routing]] 참조 |
| **LLM** | **Anthropic Claude** | 자체 | IBM watsonx | OpenAI GPT |
| **용도** | 범용 생산성 | 매장 운영 | HR 전문 | HR 전문 |
| **특화** | 회��사·개발자 버전 | 매장 특화 | HR 태스크 | HR GPT 라우팅 |

### 핵심 insight
- **"foundation model 선택이 곧 기업 전략"**: Moderna→OpenAI, IBM→watsonx, Deloitte→Anthropic. 각 기업이 다른 foundation model을 선택한 이유가 컨설팅 질문거리
- **15,000명 인증**: "AI를 쓰는 것"을 넘어 **"AI를 잘 쓰는 것을 인증"**하는 단계 — Meta의 "성과 평가에 AI 반영"과 유사한 "AI proficiency institutionalization"
