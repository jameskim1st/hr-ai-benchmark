---
title: "Cisco — AI Assistant for HR (PTO Q&A → 매니저 outbound 메시지 자동 작성, agentic)"
slug: cisco-ai-assistant-hr-agentic
primary_category: Employee Experience & HR Ops
subcategory: Employee Self-service
tags: [cisco, ai-assistant, hr-agentic, pto, time-off, beyond-q-and-a, outbound-message, 35k-upskilled]
company: Cisco
industry: [tech, networking]
region: [global]
employee_class: [all]
vendor: [Cisco internal]
vendor_type: [internal-build]
ai_tech_type: [generative]
ai_tech_subtype: [summarization-qa]
stage: production
frequency: daily
first_seen: 2024-06-01
last_confirmed: 2025-11-01
confidence: 0.65
consulting_angle_status: filled
sources:
  - sources/us-large-enterprise-hr-ai-2025-2026.md
related_usecases:
  - moderna-ask-hr-routing
  - ibm-askhr-watsonx
  - sap-successfactors-1h-2026-joule-agents
related_vendors: []
---

## Summary

Cisco의 사내 AI HR Assistant — HR 정책 Q&A를 넘어 **agentic** 수준으로 진화. 직원 PTO 잔여 조회 + 매니저에게 보낼 **time-off notification 메시지 자동 작성**까지. HR case 열지 않고 처리. broader Cisco "AI agents + nudges" cut-bureaucracy 이니셔티브 일부. 35,000+ Cisco 직원이 2025-06까지 AI-upskilled (+121% YoY).

## Problem / Why

- **Before**: HR Q&A 챗봇은 정보 조회까지만 — "내 매니저에게 휴가 알리는 메시지 어떻게 쓰지" 같은 outbound 작업은 수동
- **Pain point**: HR 챗봇이 Q&A에 머물러 ROI 한계 — agentic 수준 도약 필요
- **Trigger**: Cisco의 "AI agents + nudges" 전사 bureaucracy 감소 이니셔티브 (Jeetu Patel 주도)

## Solution Architecture

### A. Process

- **Before**: 1) 직원이 HR 포털에서 PTO 잔여 조회 / 2) 직원이 직접 매니저에게 메시지 작성 / 3) HR 케이스 필요 시 별도 ticketing
- **After**:
  1. 직원이 AI Assistant에 "다음주 휴가 가능한지 + 매니저에게 알려줘" 한 번에 요청
  2. Assistant가 PTO 잔여 + 부서 calendar 조회
  3. 매니저용 time-off notification 메시지 **자동 작성** (직원 검토·전송)
  4. HR 정책 위배 시 alert + 사람 escalation
- **HITL**: 직원이 outbound 메시지 검토·전송. 정책 위배 케이스만 사람 HR
- **Frequency**: daily
- **Scope**: agentic — Q&A 넘어 "drafting + action"

### B/C/D/E. System

- Cisco 자체 구축 (사내 AI Assistant 일부)
- HRMS 통합 (Workday 추정 — Cisco는 Workday customer)
- 모델: 자체 + 외부 API 혼합 추정
- 오너십: Cisco HR + IT/AI Plat

## Impact / Metrics

### 기대효과 요약
HR Q&A 챗봇의 agentic 진화 — Q&A를 넘어 outbound 메시지 drafting까지 수행하는 KR Ask-HR RFP의 mature reference.

- ⚠️ 자사 보고: 35,000+ Cisco 직원 AI-upskilled by Jun 2025 (+121% YoY) — broader 측정
- HR Assistant standalone case-volume metric _미공개_

## Governance & Risk

- ✅ outbound 메시지는 직원 검토·전송 — 사람 통제 유지
- ⚠️ 매니저 정책 위배 시 alert 정확도 _미공개_
- ⚠️ "정책 위배" 판정의 explainability 부족 가능성

## Consulting Angle

- **KR Ask-HR RFP의 mature reference (1순위)**:
  - 한국 대기업 사내 챗봇은 대부분 Q&A 단계 (LG CNS·삼성SDS·SK C&C·신한 AI ONE·하나 지식챗봇)
  - Cisco의 "Q&A → drafting + action" agentic 진화는 KR 차세대 챗봇 RFP의 standard
- **2026 Q3-Q4 KR 컨설팅 deck**: Moderna Ask HR (routing) + IBM AskHR (80+ 태스크) + Cisco AI Assistant (agentic outbound) — 3-tier maturity ladder
- **반면교사**:
  - 매니저 outbound 메시지 자동 작성이 "manager 우회 자동화"로 인식되지 않도록 직원 검토 단계 명시 필수
  - 한국 위계 문화에서 "매니저에게 보내는 메시지"의 자동 작성은 cultural fit 검증 필요 (존댓말·격식)
- **agentic 진화 차원**: Workday Illuminate Performance Review Agent + SAP Joule HR Service + Cisco AI Assistant — vendor 별 agentic HR 솔루션 비교덱
