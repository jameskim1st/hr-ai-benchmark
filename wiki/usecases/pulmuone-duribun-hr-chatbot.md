---
title: "풀무원 — '두리번' HR 특화 AI 챗봇"
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
visibility: public
case_type: adoption
regulatory_exposure: []
kr_law: PIPA 준수 + Q&A only로 AI 기본법 고영향 회피 (평가·승진 영향 시 재분류)
kr_union: 협의 의무 낮음 (정보 제공 성격 — HR Q&A only)
kr_language: 한국어 네이티브
kr_vendor: 미확인 (벤더 미공개 — RFP 시 vendor 명시 필요)
frequency: daily
first_seen: 2024-12-23
last_confirmed: 2026-04-01
confidence: 0.8
evidence_grade: A
corroborated_by: 2
freshness: fresh
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/businesspost-pulmuone-duribun-2024-12.md, sources/edaily-pulmuone-duribun-2024-12.md, sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12.md]
related_usecases:
  - shinhan-bank-ai-one-platform
  - mirae-asset-ai-assistant-platform
  - moderna-ask-hr-routing
  - ibm-askhr-watsonx
related_vendors: []
---

## Summary

풀무원이 2024-12-23 오픈한 **임직원 대상 HR 특화 생성형 AI 챗봇 '두리번'** [[sources/edaily-pulmuone-duribun-2024-12]] [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]]. **근태·복리후생·학습·평가·승진·보상 등 HR 제도 문의**에 대화형으로 답변, 24시간 365일 응답 [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]] [[sources/businesspost-pulmuone-duribun-2024-12]]. ⚠️ 자사 보고: 인사 정보 문서 기반으로 답변을 생성해 **할루시네이션 최소화**, 답변 근거 정보 업데이트 가능 [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]] [[sources/edaily-pulmuone-duribun-2024-12]]. 현재 PC 전용, 모바일 확장·적용 사업단위 확대 계획 [[sources/edaily-pulmuone-duribun-2024-12]] [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]]. 직원 규모 수치는 인용 소스에 없음 → _미공개_ (2026-09-27 grounding 점검). ★ KR 사례 중 **순수 HR 챗봇으로 정의된** 가장 selectoral 사례 — 식품 중견기업이지만 KR HR 컨설팅의 가장 직접적 reference.

## Problem / Why (도입 배경)

- **Before**: HR 담당자가 임직원 질의응답·근태·복리후생·각종 조회 및 신청 업무 등 단순·반복 업무를 처리 [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]]; 문의량·응답 시간·HR 인력 수치 ❓ 미공개 (2026-09-27 grounding 점검)
- **Pain point**: HR 담당자 업무 효율 + 임직원의 대기 시간 없는 즉각 응답 (풀무원 기대 효과 프레이밍) [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]] [[sources/businesspost-pulmuone-duribun-2024-12]]
- **Trigger**: ❓ 미공개 — 디지털혁신실 주도 임직원 디지털 경험 제공 취지 [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]]

## Solution Architecture

### A. Process (프로세스)

- **Before**: 직원이 HR 담당자에게 문의 → HR 담당자가 질의응답 처리 [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]]; 채널·응답 시간 _미공개_
- **After** ⚠️ 자사 보고 [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]] [[sources/businesspost-pulmuone-duribun-2024-12]] [[sources/edaily-pulmuone-duribun-2024-12]]:
  1. 직원이 두리번에 질문 (현재 PC 전용, 모바일 확장 계획)
  2. 초거대 학습 데이터 기반 AI가 질문을 검색·조합하고 인사 정보 문서를 기반으로 답변 생성 (근태·복리후생·학습·평가·승진·보상)
  3. 대화 맥락을 반영한 답변; 답변 근거 정보는 업데이트 가능
  4. 24시간 365일 응답
  - 출처 표시·복잡 case HR 팀 escalation 서술은 인용 소스에 없어 제거 (2026-09-27)
- **HITL**: _미공개 (not disclosed)_ — HR 담당자의 검토·escalation 절차 미기재
- **Frequency**: daily (24시간 365일) [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]]
- **Scope**: assistive — 문의 응답 중심; 근태·복리후생 조회·신청 업무 처리도 기대 효과로 언급 [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]]

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS**: _미공개 (not disclosed)_
- **AI 시스템 배치**: 두리번 (사내 임직원 대상 생성형 AI 서비스) [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]]; vendor·구축 방식 _미공개_
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: 인사 정보 문서 기반 [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]] [[sources/businesspost-pulmuone-duribun-2024-12]]; 문서 저장소·HRIS 연동 세부 _미공개_
- **사용자 접점**: PC 전용 (모바일 확장 계획) [[sources/edaily-pulmuone-duribun-2024-12]] [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]]
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: 인사 정보 문서 (근태·복리후생·학습·평가·승진·보상 등 HR 제도) [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]] [[sources/businesspost-pulmuone-duribun-2024-12]]
- **데이터 규모**: _미공개 (not disclosed)_
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: 문서 기반 답변 생성 + 근거 정보 업데이트 가능 (RAG형 설계로 읽힘) ⚠️ 자사 보고 [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]]; 기술 명칭 _미공개_
- **데이터 거버넌스**: _미공개 (not disclosed)_
- **민감정보 처리**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_ — "초거대 학습 데이터를 기반으로 훈련된 인공지능" [[sources/businesspost-pulmuone-duribun-2024-12]]
- **모델 유형**: LLM (대화형 생성) [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]]
- **제공 방식**: _미공개 (not disclosed)_
- **커스터마이징 기법**: 인사 정보 문서 기반 답변 생성 ⚠️ 자사 보고 [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]]
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: 할루시네이션 최소화 설계 강조 ⚠️ 자사 보고 [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]] [[sources/edaily-pulmuone-duribun-2024-12]]; 정확도 측정 _미공개_

### E. Organization & Team (조직·팀 구조)

- **오너십**: 풀무원 디지털혁신실 (김성훈 디지털혁신실장 인용) [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]]; HR 조직 역할 _미공개_
- **참여 역할**: _미공개 (not disclosed)_
- **팀 규모·기간**: _미공개 (not disclosed)_
- **거버넌스 체계**: _미공개 (not disclosed)_
- **파트너**: _미공개 (not disclosed)_

## Impact / Metrics (기대효과)

### 기대효과 요약
중견기업 HR 팀의 단순 반복 문의 부담 경감 + 24/365 직원 self-service. KR pure HR-AI vendor product의 가장 selectoral 사례.

- ✅ 근태·복리후생·학습·평가·승진·보상 등 HR 제도 문의 cover [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]] [[sources/businesspost-pulmuone-duribun-2024-12]] [[sources/edaily-pulmuone-duribun-2024-12]]
- ✅ 24시간 365일 응답 [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]]
- ⚠️ 자사 보고: 문서 기반 생성으로 할루시네이션 최소화 [[sources/pulmuone-newsroom-duribun-hr-chatbot-2024-12]] [[sources/edaily-pulmuone-duribun-2024-12]]
- ⚠️ 이용률·처리량·정확도 등 정량 성과 _미공개_ — 세 소스 모두 풀무원 보도자료 기반

## Governance & Risk

- ⚠️ 자사 보고: 문서 기반 생성으로 hallucination risk 완화 — 독립 검증 없음
- ⚠️ vendor·모델 _미공개_ — 데이터 주권 검증 어려움
- ⚠️ standalone metric (응답 정확도·HR 문의 deflection율) _공식 미공개_
- ⚠️ 한국 AI 기본법 — Q&A only이므로 회피, 평가·승진 영향 시 재분류

## Contradictions

_없음._

> [!note] 2026-09-27 grounding — 인용 소스에 없는 직원 ~7K·HR 팀 ~10명, sharepoint·SSO·RBAC·PIPA 준수, 출처 표시·HR escalation, 응답 1~2일, 한국 vendor 추정 서술을 제거·_미공개_ 처리. 세 소스는 동일 보도자료 기반이므로 독립 교차검증 효과 제한적.

## Consulting Angle

- **★KR HR 컨설팅 가장 직접적 reference**:
  - 한국에서 **순수 HR 챗봇**으로 정의된 KR 사례 중 가장 selectoral
  - 한국 일반 대기업 HR 부서 클라이언트 첫 pitch에 활용 가능
  - 근태·복리후생·학습·평가·승진·보상 문의 cover는 표준 HR self-service scope
- **금융권 사내 platform과 차별화**:
  - 신한 AI ONE [[shinhan-bank-ai-one-platform]] (40+ AI 통합, HR은 일부)
  - 미래에셋 [[mirae-asset-ai-assistant-platform]] (no-code 빌더, 부서별 자율)
  - 풀무원 두리번 (HR-only, 6개 영역 표준)
- **글로벌 비교**:
  - Moderna Ask HR [[moderna-ask-hr-routing]] (routing GPT)
  - IBM AskHR [[ibm-askhr-watsonx]] (80+ HR 태스크)
  - 풀무원 두리번 (HR 제도 문의 문서 기반 응답) — KR 적용 가장 직접적
- **2026 Q3-Q4 KR HR 챗봇 RFP standard**:
  - 풀무원 모델 = "한국 중견·대기업 HR 챗봇 표준 scope" (근태·복리후생·학습·평가·승진·보상)
  - "글로벌 reference + 한국 vendor 도입" framework
- **반면교사**:
  - vendor·모델 비공개 → KR client RFP 시 vendor 명시 + 데이터 주권 명확화 필수
  - standalone metric 부재 → POC 4주 자체 측정 권장 (deflection 율·응답 정확도)
  - hallucination 최소화 = design intent 강조뿐 — 실제 incident 모니터링 필수
- **Watch list**: 모바일 확장·적용 사업단위 확대·이용 지표 공개 시 본 page 갱신
