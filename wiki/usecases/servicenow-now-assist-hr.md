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
stage: production
frequency: daily
first_seen: 2024
last_confirmed: 2025
confidence: 0.25               # Tier 2·3 혼합 (다수 분석가 언급 + vendor data), 구체 고객 케이스 부재
consulting_angle_status: filled
sources:
  - "ServiceNow 공식 https://www.servicenow.com/products/ai-agents.html"
  - "Klover.ai 분석 https://www.klover.ai/servicenow-ai-strategy-analysis-of-ai-dominance-in-enterprise-software/"
related_usecases:
  - ibm-askhr-watsonx
  - moderna-ask-hr-routing
related_vendors: []
---

# ServiceNow — Now Assist for HR Service Delivery

## Summary

ServiceNow의 **Now Assist**는 HRSD(HR Service Delivery) 모듈에 통합된 GenAI 기능. HR 케이스 요약·해결 노트 생성·직원 셀프서비스 자동 응답을 제공. ⚠️ 벤더 주장: 54% helpfulness rate. Now Assist **ACV $600M** 달성 (2025년 말), QoQ 150%+ 딜 성장. HR 영역에서는 **티켓 분류·라우팅·지식베이스 자동 유지**에 특화 — [[moderna-ask-hr-routing]]의 "routing" 기능과 유사하지만 ITSM DNA를 가진 접근법.

## Solution Architecture (요약)

### Now Assist for HRSD
- **케이스 요약**: HR 티켓의 맥락·이력을 GenAI가 자동 요약 (에이전트 시간 절감)
- **해결 노트 생성**: 케이스 종료 시 resolution note를 AI가 초안 작성
- **직원 셀프서비스**: 직원이 portal에 질문 → AI가 지식베이스에서 답변 (case deflection)
- **라우팅**: 케이스를 적절한 HR 전문가에게 자동 배정

### 사업 규모 (⚠️ 벤더 주장)
- Now Assist ACV: **$600M** (2025년 말)
- QoQ deal 성장: **150%+** (Q4 2024)
- 54% helpfulness rate (내부 benchmark)

## Impact / Metrics (기대효과)

### 기대효과 요약
⚠️ 벤더 주장: Now Assist 전체 ACV $600M(2025년 말), QoQ 딜 성장 150%+, helpfulness rate 54% — 모두 **시장·플랫폼 전체** 수치이며 HR 전용 분리 불가. HR 고객의 시간 절감·티켓 감소·만족도 등 HR-specific outcome _미공개_.

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| ACV (전 제품, HR 한정 아님) | **$600M** (2025년 말) | ServiceNow IR | ⚠️ 벤더 주장 |
| 딜 성장 (QoQ) | **150%+** (Q4 2024) | ServiceNow IR | ⚠️ 벤더 주장 |
| Helpfulness rate | **54%** | ServiceNow 내부 | ⚠️ 벤더 주장 |
| HR 전용 metric | _미공개_ | — | — |

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
