---
title: "Cisco — AI Assistant for HR"
slug: cisco-ai-assistant-hr-agentic
primary_category: Employee Experience & HR Ops
subcategory: Employee Self-service
tags: [cisco, ai-assistant, hr-agentic, pto, time-off, beyond-q-and-a, outbound-message]
company: Cisco
industry: [tech, networking]
region: [global]
employee_class: [all]
vendor: [Cisco internal]
vendor_type: [internal-build]
output: "⚠️ 자사 보고: 직원 HR 질문에 회사 정보·직원 데이터 기반 즉답 (잔여 PTO 등, HR case 없이) + 휴가 요청 기록 + 리더에게 보낼 통지 letter 작성 제안 (drafting + action) + PTO 입력·401k 납입액 조회 등 HR tool 상호작용"
ai_tech_type: [generative]
ai_tech_subtype: [summarization-qa]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: []
kr_law: 일반 개인정보보호법 수준
kr_union: 협의 의무 낮음 (정보 제공 성격)
kr_language: 해당 없음 (자체 구축)
kr_vendor: 해당 없음 (Cisco 자체 구축)
frequency: daily
first_seen: 2024-06-01
last_confirmed: 2025-11-01
confidence: 0.7
evidence_grade: A
corroborated_by: 2
freshness: fresh
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/cisco-blog-internal-ai-assistant-2025-11.md, sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md, sources/hr-brew-cisco-entry-level-ai-2025-11.md]
related_usecases:
  - moderna-ask-hr-routing
  - ibm-askhr-watsonx
  - sap-successfactors-1h-2026-joule-agents
related_vendors: []
---

## Summary

Cisco HR 팀이 회사 정보·직원 데이터로 HR 질문에 직접 답하는 AI 에이전트 구축 — ⚠️ 자사 보고 (Fortune/GPTW 기고, CPO Kelly Jones): 잔여 PTO 조회를 HR case 없이 즉답하고, 휴가 요청을 기록한 뒤 **리더에게 보낼 통지 letter 작성**까지 제안하는 **agentic** 수준. [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]] Cisco 전사 internal AI assistant(IT 주도, 100,000+ 사용자)의 일부 맥락. [[sources/cisco-blog-internal-ai-assistant-2025-11.md]] (2026-09-27 grounding 점검: 종전 "35,000명+ AI-upskilled(+121퍼센트)"는 인용 소스 3건에 없어 제거 — Contradictions 참조.)

## Problem / Why (도입 배경)

- **Before**: ✅ 잔여 PTO 같은 질문도 HR case를 열어야 답을 받는 구조. [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]]
- **Pain point**: ✅ Jones: "86,000명+ 기업에서 5%의 시간을 돌려주면" 고객 성과로 이어진다는 시간 회수 논리 (bureaucracy 감소). [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]]
- **Trigger**: ✅ Cisco의 "AI agents + nudges"로 bureaucracy를 줄이는 People 조직 이니셔티브 (CPO Kelly Jones). [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]]

## Solution Architecture

### A. Process (프로세스)

- **Before**: ✅ 잔여 PTO 같은 HR 질문에 HR case 개설 필요. [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]]
- **After** (⚠️ 자사 보고 — CPO Kelly Jones, Fortune/GPTW 기고):
  1. 직원이 AI 에이전트에 HR 질문 → 회사 정보·직원 데이터로 직접 답변 (예: 잔여 PTO — HR case 없이 즉답). [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]]
  2. 직원이 "9월에 2주 휴가" 요청 → 에이전트가 요청을 기록. [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]]
  3. 에이전트가 다음 단계 제안: "리더에게 보낼 letter를 써 드릴까요?" (drafting + action). [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]]
  4. HR tool 상호작용 — PTO 입력, 401k 납입액 조회 등. [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]]
  (종전 "부서 calendar 조회", "정책 위배 alert + escalation" 단계는 소스에 없어 제거)
- **HITL**: ✅ 에이전트가 letter 작성 여부를 직원에게 묻는 구조 (옵트인). [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]] 검토·전송 세부 _미공개_
- **Frequency**: _미공개 (not disclosed)_
- **Scope**: agentic — Q&A 넘어 "요청 기록 + letter drafting 제안". [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]]

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS / 기반 시스템**: _미공개 (not disclosed)_
- **AI 시스템 배치**: ⚠️ 자사 보고: Cisco IT의 internal AI assistant ("purpose-built with security") — HR 에이전트와의 관계 세부 _미공개_. [[sources/cisco-blog-internal-ai-assistant-2025-11.md]]
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: ✅ HR tools 연동 (PTO 입력·401k 조회). [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]] ⚠️ 자사 보고: enterprise AI agent registry·MCP registry로 사내 원격 에이전트·MCP 서버 연결. [[sources/cisco-blog-internal-ai-assistant-2025-11.md]]
- **사용자 접점**: _미공개 (not disclosed)_
- **인증·권한**: ⚠️ 자사 보고: 표준화된 agent·MCP 보안·entitlements. [[sources/cisco-blog-internal-ai-assistant-2025-11.md]] 세부 _미공개_

### C. Data (데이터)

- **입력 데이터 소스**: ✅ 회사 정보 + 직원 데이터 (PTO·401k 등). [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]]
- **데이터 규모**: ⚠️ 자사 보고: internal AI assistant 전체 — 45M+ 상호작용, 100,000+ 사용자, 일 평균 156,000건. [[sources/cisco-blog-internal-ai-assistant-2025-11.md]] HR domain standalone 수치 _미공개_
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: _미공개 (not disclosed)_
- **데이터 거버넌스**: ✅ Jones: 옵트인·데이터 이동 투명성으로 신뢰 확보 강조. [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]] 세부 _미공개_
- **민감정보 처리**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: ⚠️ 자사 보고: internal AI assistant는 멀티모델 라우팅 (Azure OpenAI·Claude·Gemini·자체 LLM). [[sources/cisco-blog-internal-ai-assistant-2025-11.md]] HR 에이전트 적용 모델 _미공개_
- **모델 유형**: ✅ 생성형 AI 에이전트 (Q&A + 요청 기록 + letter 작성). [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]]
- **제공 방식**: _미공개 (not disclosed)_
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **Orchestration 프레임워크**: ⚠️ 자사 보고: AI agent·MCP 플랫폼, agent registry. [[sources/cisco-blog-internal-ai-assistant-2025-11.md]]
- **평가·가드레일**: ⚠️ 자사 보고 (internal AI assistant 전체, 사용자 설문): 73% 생산성 향상, 주당 평균 5시간 절감. [[sources/cisco-blog-internal-ai-assistant-2025-11.md]] HR 에이전트 평가 _미공개_

### E. Organization & Team (조직·팀 구조)

- **오너십**: ✅ HR 팀이 HR 에이전트 구축 (CPO Kelly Jones). [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]] ⚠️ 자사 보고: internal AI assistant는 Cisco IT. [[sources/cisco-blog-internal-ai-assistant-2025-11.md]]
- **참여 역할**: ✅ Fran Katsoudas (Chief People, Policy & Purpose Officer) — AI로 전 직원 스킬·태스크 코드화 추진. [[sources/hr-brew-cisco-entry-level-ai-2025-11.md]]
- **팀 규모·기간**: _미공개 (not disclosed)_
- **거버넌스 체계**: _미공개 (not disclosed)_
- **변화관리**: ✅ Katsoudas: entry-level 기회 창출을 위한 멘토링·신입 커뮤니티·공식 온보딩 강조 (AI 도입으로 level-one 고객지원 직무 소멸 맥락). [[sources/hr-brew-cisco-entry-level-ai-2025-11.md]]
- **파트너**: _미공개 (not disclosed)_

## Impact / Metrics (기대효과)

### 기대효과 요약
HR Q&A 챗봇의 agentic 진화 — Q&A를 넘어 요청 기록·letter drafting 제안까지 수행하는 KR Ask-HR RFP의 mature reference. ⚠️ HR 에이전트 standalone 정량 효과(case 감소·시간 절감) _미공개_.

- ⚠️ 자사 보고 (internal AI assistant 전체): 45M+ 상호작용, 100,000+ 사용자, 73% 생산성 향상, 주 5시간 절감. [[sources/cisco-blog-internal-ai-assistant-2025-11.md]]
- ✅ 계획: EU 근태 추적 개선, engagement 기반 nudge, 연 10,000 채용 포지션 개인화 추천, 보상 조정 nudge. [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]] (미래형 — 미구현)
- HR Assistant standalone case-volume metric _미공개_ (종전 "35,000명+ AI-upskilled" 수치 근거 미확보 — 2026-09-27 grounding 점검)

## Governance & Risk

- ✅ 에이전트가 letter 작성을 제안하고 직원이 선택 — 사람 통제 유지. [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]]
- ✅ 옵트인·데이터 이동 투명성 강조 (Jones). [[sources/fortune-cisco-ai-agents-nudges-hr-2025-10.md]]
- ⚠️ 향후 nudge(보상 조정·내부 이동 추천)는 평가·승진 영향 시 고영향 AI 검토 대상 — 현재는 계획 단계
- ⚠️ Fortune 기사는 GPTW 소속 필자의 기고 — 독립 검증 아님

## Contradictions

> [!note] 2026-09-27 grounding — 종전 본문의 "35,000명+ Cisco 직원 AI-upskilled (+121퍼센트 YoY)", "Jeetu Patel 주도", "부서 calendar 조회", "정책 위배 alert·escalation", "Workday·Webex 추정"은 인용 소스 3건 raw 어디에도 없어 제거·_미공개_ 처리. cisco-blog 소스는 IT 주도 internal AI assistant 전반(PTO 에이전트 언급 없음)이므로 HR 에이전트 수치로 전용하지 않음. frontmatter `tags`의 `35k-upskilled`는 본 점검에서 손대지 않음 (수정 필요).

## Consulting Angle

- **KR Ask-HR RFP의 mature reference (1순위)**:
  - 한국 대기업 사내 챗봇은 대부분 Q&A 단계 (LG CNS·삼성SDS·SK C&C·신한 AI ONE·하나 지식챗봇)
  - Cisco의 "Q&A → drafting + action" agentic 진화는 KR 차세대 챗봇 RFP의 standard
- **2026 Q3-Q4 KR 컨설팅 deck**: Moderna Ask HR (routing) + IBM AskHR (80+ 태스크) + Cisco AI Assistant (agentic outbound) — 3-tier maturity ladder
- **반면교사**:
  - 매니저 outbound 메시지 자동 작성이 "manager 우회 자동화"로 인식되지 않도록 직원 검토 단계 명시 필수
  - 한국 위계 문화에서 "매니저에게 보내는 메시지"의 자동 작성은 cultural fit 검증 필요 (존댓말·격식)
- **agentic 진화 차원**: Workday Illuminate Performance Review Agent + SAP Joule HR Service + Cisco AI Assistant — vendor 별 agentic HR 솔루션 비교덱
