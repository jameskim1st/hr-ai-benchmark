---
title: "Visier — Vee AI Digital Assistant + Org Design"
slug: visier-vee-people-analytics
primary_category: Strategic Workforce & Governance
subcategory: People Analytics
tags: [people-analytics, vee, natural-language, workforce-planning, org-design, providence]
company: Providence (healthcare, 주요 고객)
industry: [healthcare, all]
region: [na, global]
employee_class: [all]
vendor: [Visier]
vendor_type: [point-solution]
output: "자연어 workforce 질의에 대한 narrative 답변 + 자동 생성 chart·요약·대시보드 + Org Design 변경 영향 narrative 설명 (Teams/웹 인터페이스)"
ai_tech_type: [generative]
ai_tech_subtype: [summarization-qa]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: []
kr_law: 이직 예측·조직설계 결과가 인사 결정에 쓰이면 AI 기본법 고영향 AI 분류 가능
kr_union: 단체교섭/근로자대표 협의 필요 (인사 의사결정 영향 — 이직 예측·조직설계)
kr_language: 미확인 (벤더 확인 필요)
kr_vendor: 미확인 (국내 파트너 확인 필요)
first_seen_estimated: true
last_confirmed_estimated: true
frequency: daily
first_seen: 2025-06-30
last_confirmed: 2025-06-30
confidence: 0.35
evidence_grade: B
corroborated_by: 1
freshness: stale
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/visier-vee-people-analytics-ai-agent-2026-09.md, sources/techintelpro-visier-org-design-2025-09.md]
related_usecases:
  - workday-illuminate-job-architecture
related_vendors: []
---

# Visier — Vee AI Digital Assistant + Org Design

## Summary

Visier는 **People Analytics 전문 AI 플랫폼**. 주력 AI 제품 **Vee**는 자연어로 workforce 데이터에 질문하면 인사이트를 제공하는 people analytics AI 에이전트 — ⚠️ 벤더 주장: 2 million+ 사용자, Microsoft 365 Copilot·Teams·Slack 등 업무 도구 내 통합 ([[sources/visier-vee-people-analytics-ai-agent-2026-09]]). 2025년 HR Tech에서 **Visier Org Design** 출시 — 비용·스킬·몰입·성과 데이터를 결합한 AI 기반 조직 설계 ([[sources/techintelpro-visier-org-design-2025-09]]). 고객 사례(Providence 간호사 onboarding 등)는 인용 소스 2건에 없음 — _미공개_ (2026-09-27 grounding 점검).

## Problem / Why (도입 배경)

- 🚫 일반론: 벤더 제품이므로 특정 기업의 도입 배경은 고객별 상이. People analytics 영역의 일반적 pain point는 HRBP·매니저의 workforce 데이터 질문이 데이터 팀 대기열에 묶이는 것.
- **Before (baseline)**: ❓ baseline 미공개 (고객별 상이)
- **Pain point**: ⚠️ 벤더 주장: 리더별 맞춤 분석가 부재 — Vee가 'personalized analyst for every leader' 역할 ([[sources/visier-vee-people-analytics-ai-agent-2026-09]]); 조직 개편은 business-critical 결정 ([[sources/techintelpro-visier-org-design-2025-09]])
- **Trigger**: ❓ 미공개

## Solution Architecture

### A. Process (프로세스)

- **Before**: HRBP·매니저가 People analytics 질문에 데이터 팀 ticket 의존, 답변 수일 소요
- **After**:
  1. 사용자가 Visier People 또는 Microsoft Teams에서 Vee와 자연어로 채팅
  2. Vee가 자연어 질문을 Visier query로 변환
  3. 조직의 people data로 query 실행 (proprietary customer data는 LLM 학습 미사용)
  4. narrative 답변·차트·요약·자동 보고서 생성
  5. 사용자가 chart·data point 기반으로 후속 질문 가능
  6. 응답에 Visier governance·permission 모델 적용
- **HITL**: 사용자가 답변 검토·해석·의사결정
- **Frequency**: daily (ad-hoc 질의)
- **Source**: [[sources/visier-vee-people-analytics-ai-agent-2026-09]] (⚠️ 벤더 주장; 2·3·6단계 세부는 원문 미확인)

### Vee AI Digital Assistant
- **자연어 쿼리** → workforce 데이터 인사이트 (text-to-insight)
- 성과 추적, 이직 예측, workforce gap 분석
- HR 리더·비즈니스 리더 대상

### Org Design (2025 출시)
- AI 기반 조직 설계
- 인력·스킬·비용·engagement·성과 데이터 통합
- GenAI가 변경의 영향을 narrative로 설명

### 고객 사례
- _미공개 (not disclosed)_ — 기존 Providence 사례(간호사 proactive onboarding·vacancy forecasting)는 인용 소스 2건에 없어 삭제 (2026-09-27 grounding 점검). Visier 고객 사례는 [[tampa-general-visier-people-analytics]] 참조.

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS / 기반 시스템**: 벤더 제품 — 고객별 상이. _미공개 (not disclosed)_
- **AI 시스템 배치**: ⚠️ 벤더 주장: Visier 플랫폼 내 Vee + Vee Boards ([[sources/visier-vee-people-analytics-ai-agent-2026-09]])
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: ⚠️ 벤더 주장: Microsoft 365 Copilot·Teams·Slack·인트라넷/API ([[sources/visier-vee-people-analytics-ai-agent-2026-09]])
- **사용자 접점 (UX layer)**: ⚠️ 벤더 주장: Visier 내부, Teams·Slack·Copilot 등 업무 도구 ([[sources/visier-vee-people-analytics-ai-agent-2026-09]])
- **인증·권한**: _미공개 (not disclosed)_
- **가용성·SLA**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: ⚠️ 벤더 주장: 고객 조직의 people data (workforce 질문 응답) ([[sources/visier-vee-people-analytics-ai-agent-2026-09]]); Org Design은 비용·스킬·몰입·성과 데이터 결합 ([[sources/techintelpro-visier-org-design-2025-09]])
- **데이터 규모**: ⚠️ 벤더 주장: 2 million+ 사용자 ([[sources/visier-vee-people-analytics-ai-agent-2026-09]]); 데이터 규모 _미공개_
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context 구분**: _미공개 (not disclosed)_
- **데이터 거버넌스**: _미공개 (not disclosed)_
- **민감정보 처리**: _미공개 (not disclosed)_
- **데이터 출처의 오너십**: 고객 HR 데이터 (벤더 플랫폼 처리) — 세부 _미공개_

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **Model 유형**: ⚠️ 벤더 주장: 자연어 질의 응답형 AI 에이전트 (Vee), GenAI 서술 (Vee Boards / Org Design 영향 설명) ([[sources/visier-vee-people-analytics-ai-agent-2026-09]], [[sources/techintelpro-visier-org-design-2025-09]])
- **제공 방식**: _미공개 (not disclosed)_
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: _미공개 (not disclosed)_
- **비용·성능 지표**: _미공개 (not disclosed)_
- **Fallback·degradation 전략**: _미공개 (not disclosed)_

### E. Organization & Team (조직·팀 구조)

- **오너십**: 벤더 제품 — 고객별 상이. _미공개 (not disclosed)_
- **참여 역할·팀 규모·거버넌스·변화관리**: _미공개 (not disclosed)_
- **파트너**: Deloitte 인사(Marc Solow)가 Org Design 출시 기사에 인용 ([[sources/techintelpro-visier-org-design-2025-09]]); 구현 파트너 관계 _미공개_

## Impact / Metrics (기대효과)

### 기대효과 요약
⚠️ 기대효과 수치 미공개 — 고객 outcome metric은 인용 소스에 없음. 확인되는 것: ⚠️ 벤더 주장 2 million+ 사용자 ([[sources/visier-vee-people-analytics-ai-agent-2026-09]]), Org Design HR Tech 2025 출시 ([[sources/techintelpro-visier-org-design-2025-09]]).

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| Vee 사용자 | **2 million+** | [[sources/visier-vee-people-analytics-ai-agent-2026-09]] | ⚠️ 벤더 주장 |
| 고객 outcome (Providence 등) | _미공개_ | 인용 소스에 없음 (2026-09-27 grounding 점검) | ❓ |
| Org Design 출시 | HR Tech 2025 | [[sources/techintelpro-visier-org-design-2025-09]] | ✅ Fact (공개 이벤트) |

## Governance & Risk

- **HITL**: 사용자가 답변 검토·해석·의사결정 (Vee는 분석 제공) — ⚠️ 벤더 주장 ([[sources/visier-vee-people-analytics-ai-agent-2026-09]])
- **데이터 거버넌스**: ⚠️ 벤더 주장: 응답에 Visier governance·permission 모델 적용, 고객 데이터는 LLM 학습 미사용 ([[sources/visier-vee-people-analytics-ai-agent-2026-09]] — 원문 미확인)
- **편향·감사**: _미공개 (not disclosed)_

## Contradictions

> [!note] 2026-09-27 grounding — Providence 사례·2,000+ caregivers 수치는 인용 소스 2건 어디에도 없음([[sources/visier-vee-people-analytics-ai-agent-2026-09]] Limitations) → 삭제·`_미공개_`. Vee 사용자 수는 벤더 제품 페이지 기준 ⚠️ 벤더 주장.

## Consulting Angle

- **7. Strategic Workforce 카테고리 reference**: 제품 존재·Org Design 출시는 Tier 2 매체 확인; 고객 outcome은 [[tampa-general-visier-people-analytics]] 참조 (본 페이지 인용 소스에는 고객 metric 없음)
- **한국 적용**: 국내 대기업의 **인력계획 수립 + 조직설계**에 Visier 같은 People Analytics 도구 평가 시 reference
- **Vee의 자연어 쿼리**: "Text-to-SQL HR"의 실제 구현 사례 — 한국 HR 부서의 "데이터 기반 인사 의사결정" 프로젝트에 직접 연결
- **Limitation**: 본 페이지 인용 소스에 고객 사례 없음, ROI 구체 수치 _미공개_
