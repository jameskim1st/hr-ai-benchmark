---
title: "풀무원 — '두리번' HR 특화 AI 챗봇 (6개 영역 24/365, RAG hallucination 최소화)"
slug: pulmuone-duribun-hr-chatbot
primary_category: Employee Experience & HR Ops
subcategory: Employee Self-service
tags: [pulmuone, duribun, hr-chatbot, rag, 6-hr-domains, 24-365, korea, food-industry, mid-large-enterprise, pure-hr-ai]
company: 풀무원
industry: [food, manufacturing]
region: [kr]
employee_class: [전임직, 기술사무직]
vendor: [_미공개_]
vendor_type: [point-solution]
output: "7K 직원 HR 6개 영역 (근태·복리후생·학습·평가·승진·보상) 자연어 질문에 대한 24/365 RAG 답변 (출처 표시, hallucination 최소화) + 복잡 case는 HR 팀 escalation"
ai_tech_type: [generative]
ai_tech_subtype: [summarization-qa]
stage: production
frequency: daily
first_seen: 2024-12-23
last_confirmed: 2026-04-01
confidence: 0.50
consulting_angle_status: filled
sources:
  - sources/kr-conglomerate-2026-q2-research.md
related_usecases:
  - shinhan-bank-ai-one-platform
  - mirae-asset-ai-assistant-platform
  - moderna-ask-hr-routing
  - ibm-askhr-watsonx
related_vendors: []
---

## Summary

풀무원이 2024-12-23 출시한 **임직원 인적자원관리 전용 생성형 AI 챗봇 '두리번'**. **근태·복리후생·학습·평가·승진·보상 6개 HR 영역**에 대해 24/365 응답. 인사 정보 문서 기반 RAG로 **hallucination 최소화**. PC → 모바일 확장 계획. ★ KR 사례 중 **순수 HR 챗봇으로 정의된** 가장 selectoral 사례 — 식품 중견기업이지만 KR HR 컨설팅의 가장 직접적 reference.

## Problem / Why (도입 배경)

- **Before**: 풀무원 ~7K 직원이 HR 정책 문의를 HR 팀 전화·이메일로 처리 — HR 팀 단순 반복 응대 부담
- **Pain point**: 한국 중견기업 HR 팀 ~10명 규모 — 직원당 daily 문의 부담, 정책 변경 시 안내 누락
- **Trigger**: 2024 한국 ChatGPT 도입 가속 + 풀무원 디지털 전환 명분

## Solution Architecture

### A. Process

- **Before**: 직원이 HR 정책 문의 → HR 팀 전화·이메일·sharepoint search → 응답 1~2일
- **After**:
  1. 직원이 두리번 chatbot에 자연어 query (PC, 모바일 확장 예정)
  2. 두리번이 인사 정보 문서 RAG 검색 (근태·복리후생·학습·평가·승진·보상)
  3. 출처 표시 + 답변 생성 (hallucination 최소화 design)
  4. 복잡 case는 HR 팀 escalation
  5. 24/365 운영 — 야간·주말 문의 즉시 처리
- **HITL**: HR 팀이 escalation·정책 업데이트
- **Frequency**: daily
- **Scope**: assistive — Q&A only, 결정 없음

### B. System & Infrastructure

- **Core HRIS**: 풀무원 자체 HR 시스템
- **AI 시스템 배치**: 두리번 chatbot (vendor _미공개_, 한국 vendor 추정)
- **배포 환경**: PC web → 모바일 확장 (2025+)
- **연동·통합**: 풀무원 인사 정책 문서 sharepoint
- **사용자 접점**: PC web, 모바일 (확장)
- **인증·권한**: 풀무원 SSO

### C. Data

- **입력 데이터 소스**: 인사 정책 문서 (6개 HR 영역) RAG 코퍼스
- **데이터 규모**: ~7K 직원 cover
- **전처리·정제**: 정책 문서 RAG indexing
- **학습 vs RAG vs In-context**: ✅ RAG 기반 (hallucination 최소화 design)
- **데이터 거버넌스**: PIPA 준수
- **민감정보 처리**: HR 데이터 RBAC

### D. Model

- **Foundation model**: _미공개_ (한국 자체 LLM 또는 외부 LLM)
- **모델 유형**: LLM + RAG
- **제공 방식**: SaaS 또는 자체 호스팅
- **커스터마이징 기법**: RAG (인사 문서 특화)
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: hallucination 최소화 design 강조 (벤더 주장)

### E. Organization

- 풀무원 HR + IT (디지털 전환)

## Impact / Metrics (기대효과)

### 기대효과 요약
중견기업 HR 팀의 단순 반복 문의 부담 경감 + 24/365 직원 self-service. KR pure HR-AI vendor product의 가장 selectoral 사례.

- ✅ 6개 HR 영역 cover (근태·복리후생·학습·평가·승진·보상)
- ✅ 24/365 운영
- ✅ RAG 기반 hallucination 최소화 design
- 출처: 풀무원 뉴스룸·이데일리·비즈니스포스트 (Tier 2~3 cross-reference)

## Governance & Risk

- ✅ RAG 기반 — hallucination risk 완화
- ⚠️ vendor·모델 _미공개_ — 데이터 주권 검증 어려움
- ⚠️ standalone metric (응답 정확도·HR 문의 deflection율) _공식 미공개_
- ⚠️ 한국 AI 기본법 — Q&A only이므로 회피, 평가·승진 영향 시 재분류

## Consulting Angle

- **★KR HR 컨설팅 가장 직접적 reference**:
  - 한국에서 **순수 HR 챗봇**으로 정의된 KR 사례 중 가장 selectoral
  - 한국 일반 대기업 HR 부서 클라이언트 첫 pitch에 활용 가능
  - 6개 HR 영역 cover는 표준 HR self-service scope
- **금융권 사내 platform과 차별화**:
  - 신한 AI ONE [[shinhan-bank-ai-one-platform]] (40+ AI 통합, HR은 일부)
  - 미래에셋 [[mirae-asset-ai-assistant-platform]] (no-code 빌더, 부서별 자율)
  - 풀무원 두리번 (HR-only, 6개 영역 표준)
- **글로벌 비교**:
  - Moderna Ask HR [[moderna-ask-hr-routing]] (routing GPT)
  - IBM AskHR [[ibm-askhr-watsonx]] (80+ HR 태스크)
  - 풀무원 두리번 (6개 HR 영역 RAG) — KR 적용 가장 직접적
- **2026 Q3-Q4 KR HR 챗봇 RFP standard**:
  - 풀무원 모델 = "한국 중견·대기업 HR 챗봇 표준 scope" (6개 영역)
  - "글로벌 reference + 한국 vendor 도입" framework
- **반면교사**:
  - vendor·모델 비공개 → KR client RFP 시 vendor 명시 + 데이터 주권 명확화 필수
  - standalone metric 부재 → POC 4주 자체 측정 권장 (deflection 율·응답 정확도)
  - hallucination 최소화 = design intent 강조뿐 — 실제 incident 모니터링 필수
- **Watch list**: 모바일 확장·6개 영역 외 추가 시 본 page 갱신
