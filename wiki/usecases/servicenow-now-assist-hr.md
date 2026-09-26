---
title: "ServiceNow — Now Assist for HR Service Delivery"
slug: servicenow-now-assist-hr
primary_category: Employee Experience & HR Ops
subcategory: HR Service Delivery
tags: [now-assist, hr-service-delivery, case-management, ticket-routing, genai]
company: _다수 (구체 고객명 미공개)_
industry: [all]
region: [global]
employee_class: [all]
vendor: [ServiceNow]
vendor_type: [hrms]
output: "HR 케이스 맥락 자동 요약 + 직원 셀프서비스 KB 답변 (case deflection) + 케이스 라우팅 결정 + AI 작성 resolution note 초안 + Schedule Interview/Job Requisition 에이전트 conversational 처리"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [summarization-qa, clustering-classification]
stage: production
visibility: public
case_type: vendor-product
regulatory_exposure: []
kr_law: 일반 개인정보보호법 수준 (HR 케이스 데이터 SaaS 처리)
kr_union: 협의 의무 낮음 (정보 제공·케이스 라우팅 성격)
kr_language: 미확인 (벤더 확인 필요)
kr_vendor: 국내 SI 삼성SDS·LG CNS가 ServiceNow 파트너 (페이지 명시)
first_seen_estimated: true
last_confirmed_estimated: true
frequency: daily
first_seen: 2024-06-30
last_confirmed: 2025-06-30
confidence: 0.35
evidence_grade: B
corroborated_by: 1
freshness: stale
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/servicenow-ai-agents-product-2026-09.md, sources/klover-servicenow-ai-strategy-2025-07.md]
related_usecases:
  - ibm-askhr-watsonx
  - moderna-ask-hr-routing
related_vendors: []
---

# ServiceNow — Now Assist for HR Service Delivery

## Summary

ServiceNow의 **Now Assist**는 ITSM·CSM·HRSD(HR Service Delivery)·Creator 워크플로에 내장된 GenAI 기능 ([[sources/klover-servicenow-ai-strategy-2025-07]]). HR 케이스 요약·해결 노트 생성·직원 셀프서비스 자동 응답을 제공 (⚠️ 벤더 주장 — [[sources/servicenow-ai-agents-product-2026-09]], 스냅샷 unavailable·원문 미확인). ⚠️ 벤더 주장: Now Assist 딜 수 QoQ 150%+ 성장(2024 Q4), AI 제품 ACV $10B 목표(2025) ([[sources/klover-servicenow-ai-strategy-2025-07]]). helpfulness rate·ACV 실적 수치는 _미공개_ (수치 근거 미확보 — 2026-09-27 grounding 점검). HR 영역에서는 **티켓 분류·라우팅·지식베이스 자동 유지**에 특화 — [[moderna-ask-hr-routing]]의 "routing" 기능과 유사하지만 ITSM DNA를 가진 접근법.

## Problem / Why (도입 배경)

- 🚫 일반론: 벤더 제품이므로 특정 기업의 도입 배경은 고객별 상이. HR Service Delivery 영역의 일반적 pain point는 케이스 분류·라우팅·해결의 다단계 수작업과 반복 문의 대응 부담.
- **Before (baseline)**: ❓ baseline 미공개 (고객별 상이)
- **Pain point**: ⚠️ 벤더 주장: 케이스 요약·해결 노트 작성 등 반복 작업의 생산성 ([[sources/klover-servicenow-ai-strategy-2025-07]])
- **Trigger**: ❓ 미공개

## Solution Architecture

### A. Process (프로세스)

- **Before**: HR 케이스가 분류·라우팅·해결까지 다단계 manual ticket 처리 (❓ 고객별 baseline 미공개)
- **After** (⚠️ 벤더 주장 — [[sources/servicenow-ai-agents-product-2026-09]], 스냅샷 unavailable·원문 미확인; Now Assist의 HRSD 내장 사실은 [[sources/klover-servicenow-ai-strategy-2025-07]] 확인):
  1. 직원이 ServiceNow employee portal/Teams에서 HR 요청 제출
  2. Now Assist가 case 내용 분석 → criticality 분류 (non-critical/critical)
  3. Non-critical case는 HR knowledge base·catalog 조회하여 자동 해결
  4. Hiring 영역에서는 Schedule Interview agent·Create Job Requisition agent가 conversational 처리
  5. Critical/판단 필요 케이스는 HR agent에 라우팅하며 context summary 제공
  6. HR agent가 검토·해결, 결과로 KB 업데이트
- **HITL**: critical case·judgment-required 단계에서 HR agent 개입
- **Frequency**: daily (case 발생 시 즉시)
- **Source**: ServiceNow AI Agents 제품 페이지 ([[sources/servicenow-ai-agents-product-2026-09]] — 원문 미확인)

### Now Assist for HRSD (⚠️ 벤더 주장 — [[sources/servicenow-ai-agents-product-2026-09]], 원문 미확인)
- **케이스 요약**: HR 티켓의 맥락·이력을 GenAI가 자동 요약 (에이전트 시간 절감)
- **해결 노트 생성**: 케이스 종료 시 resolution note를 AI가 초안 작성
- **직원 셀프서비스**: 직원이 portal에 질문 → AI가 지식베이스에서 답변 (case deflection)
- **라우팅**: 케이스를 적절한 HR 전문가에게 자동 배정

### 사업 규모 (⚠️ 벤더 주장)
- Now Assist 딜 수 QoQ 성장: **150%+** (2024 Q4) ([[sources/klover-servicenow-ai-strategy-2025-07]])
- AI 제품 ACV **$10B 목표** (2025) ([[sources/klover-servicenow-ai-strategy-2025-07]])
- Now Assist ACV 실적·helpfulness rate: _미공개_ (수치 근거 미확보 — 2026-09-27 grounding 점검)

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS / 기반 시스템**: ✅ ServiceNow Now Platform — Now Assist는 ITSM·CSM·HRSD·Creator 워크플로에 내장 ([[sources/klover-servicenow-ai-strategy-2025-07]])
- **AI 시스템 배치**: ✅ 플랫폼 내장 GenAI (standalone 도구 아님) ([[sources/klover-servicenow-ai-strategy-2025-07]])
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: _미공개 (not disclosed)_
- **사용자 접점 (UX layer)**: ⚠️ 벤더 주장: employee portal·Teams ([[sources/servicenow-ai-agents-product-2026-09]] — 원문 미확인)
- **인증·권한**: _미공개 (not disclosed)_
- **가용성·SLA**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: ⚠️ 벤더 주장: HR 케이스 내용·이력, HR knowledge base·catalog ([[sources/servicenow-ai-agents-product-2026-09]] — 원문 미확인)
- **데이터 규모**: _미공개 (not disclosed)_
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context 구분**: _미공개 (not disclosed)_
- **데이터 거버넌스**: _미공개 (not disclosed)_
- **민감정보 처리**: _미공개 (not disclosed)_
- **데이터 출처의 오너십**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **Model 유형**: ✅ LLM (생성 — 케이스 요약·text-to-code 등) ([[sources/klover-servicenow-ai-strategy-2025-07]])
- **제공 방식**: _미공개 (not disclosed)_
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: _미공개 (not disclosed)_
- **비용·성능 지표**: _미공개 (not disclosed)_ — 'Pro Plus' 프리미엄 SKU로 판매된다는 점만 확인 ([[sources/klover-servicenow-ai-strategy-2025-07]])
- **Fallback·degradation 전략**: _미공개 (not disclosed)_

### E. Organization & Team (조직·팀 구조)

- **오너십**: 벤더 제품 — 고객별 상이. _미공개 (not disclosed)_
- **참여 역할**: _미공개 (not disclosed)_
- **팀 규모·기간**: _미공개 (not disclosed)_
- **거버넌스 체계**: _미공개 (not disclosed)_
- **변화관리**: _미공개 (not disclosed)_
- **파트너**: 국내 SI 파트너는 Consulting Angle 참조 (소스 미인용 — 미확인)

## Impact / Metrics (기대효과)

### 기대효과 요약
⚠️ 벤더 주장: Now Assist 딜 수 QoQ 150%+ 성장(2024 Q4), AI 제품 ACV $10B 목표(2025) ([[sources/klover-servicenow-ai-strategy-2025-07]]) — 모두 **시장·플랫폼 전체** 수치이며 HR 전용 분리 불가. HR 고객의 시간 절감·티켓 감소·만족도 등 HR-specific outcome _미공개_.

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| Now Assist ACV 실적 (전 제품) | _미공개_ | 인용 소스에 없음 (2026-09-27 grounding 점검 — 기존 ACV 실적 수치 삭제) | ❓ |
| AI 제품 ACV 목표 (전 제품) | **$10B** (2025 목표) | [[sources/klover-servicenow-ai-strategy-2025-07]] (ServiceNow 발표 전달) | ⚠️ 벤더 주장 |
| 딜 수 성장 (QoQ) | **150%+** (2024 Q4) | [[sources/klover-servicenow-ai-strategy-2025-07]] | ⚠️ 벤더 주장 |
| Helpfulness rate | _미공개_ | 인용 소스에 없음 (2026-09-27 grounding 점검 — 기존 helpfulness 수치 삭제) | ❓ |
| HR 전용 metric | _미공개_ | — | — |

## Governance & Risk

- **HITL**: ⚠️ 벤더 주장: critical·judgment-required 케이스는 HR agent에 라우팅 ([[sources/servicenow-ai-agents-product-2026-09]] — 원문 미확인)
- **편향·개인정보**: HR 케이스 데이터의 SaaS 처리 — 세부 거버넌스 _미공개 (not disclosed)_
- **가드레일·감사**: _미공개 (not disclosed)_

## Contradictions

> [!note] 2026-09-27 grounding — 기존 본문의 Now Assist ACV 실적(2025년 말)·helpfulness rate 수치는 인용 소스([[sources/klover-servicenow-ai-strategy-2025-07]])에 없음(글은 AI 제품 ACV 목표·딜 QoQ 성장률을 인용). 두 수치를 `_미공개_`로 교체. 제품 페이지([[sources/servicenow-ai-agents-product-2026-09]])는 스냅샷 unavailable — 기능 설명은 벤더 주장·원문 미확인으로 표기.

## Consulting Angle

### 핵심 위치
- ServiceNow는 **ITSM(IT 서비스 관리) 기반의 HR Service Delivery** 벤더 — Workday·SAP가 "HR suite에서 서비스 관리까지 확장"한다면, ServiceNow는 "서비스 관리에서 HR까지 확장"
- 이 **방향의 차이**가 클라이언트 선택에서 중요한 판단 기준

### vs Moderna Ask HR / IBM AskHR
- Moderna: **ChatGPT Enterprise Custom GPT** 기반 (foundation model 래핑)
- IBM: **watsonx 자체** 기반 (internal build)
- ServiceNow: **Now Platform + Now Assist** 기반 (ITSM+HRSD 통합) — **이미 ServiceNow HRSD를 쓰는 기업**에 가장 마찰 낮은 HR AI 경로

### 한국 적용
- 국내 대기업 중 ServiceNow ITSM 도입 기업이 상당수 → HRSD 확장 시 Now Assist가 자연스러운 선택
- 국내 SI (삼성SDS·LG CNS 등)가 ServiceNow 파트너 → implementation 경로 확보
