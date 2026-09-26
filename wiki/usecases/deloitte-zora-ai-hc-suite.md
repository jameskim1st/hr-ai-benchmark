---
title: "Deloitte — Zora AI agentic platform + Human Capital AI Solution Suite"
slug: deloitte-zora-ai-hc-suite
primary_category: Strategic Workforce & Governance
subcategory: Workforce Planning
tags: [deloitte, zora-ai, agentic, human-capital-suite, workforce-analyzer, workforce-planner, 300-workflows, hr-tech-governance, nvidia, llama, big4]
company: Deloitte
industry: [consulting]
region: [global]
employee_class: [all]
vendor: [Deloitte, NVIDIA]
vendor_type: [internal-build, foundation-model]
output: "클라이언트 workforce 세그먼트별 AI 영향평가 리포트 (Workforce Analyzer) + 시나리오 기반 인력 재배치 계획 (Workforce Planner+) + 300+ HR workflow library + HR AI maturity 진단 점수 + ready-to-deploy agents"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [summarization-qa, clustering-classification]
stage: announced
visibility: public
case_type: adoption
regulatory_exposure: [kr-high-impact-review, eu-annex-iii]
kr_law: Analyzer 기반 재배치 → 한국 노동법 리스크 + AI 기본법 고영향 (페이지)
kr_union: 노조 컨텍스트 위험 명시 (페이지) — 재배치 시 협의 필요
kr_language: 미확인 — 한국어 adaptation 필요, 한국 시장 fit 미검증 (페이지)
kr_vendor: Deloitte Anjin(한국 딜로이트) 경유 활용 가능 (페이지 언급)
frequency: daily
first_seen: 2025-06-01
last_confirmed: 2026-04-01
confidence: 0.55
evidence_grade: B
corroborated_by: 1
freshness: fresh
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/deloitte-press-zora-ai-agentic-2025-03.md, sources/deloitte-2026-human-capital-trends.md]
related_usecases:
  - deloitte-2026-human-capital-trends-meta
  - workday-agent-system-of-record-asor
  - accenture-mass-genai-reskilling
related_vendors: []
---

## Summary

Deloitte의 **Zora AI** — agentic AI 플랫폼 (NVIDIA AI · Llama Nemotron reasoning models · AI-Q Blueprint 기반), 2025-03-18 NVIDIA GTC에서 발표 [[sources/deloitte-press-zora-ai-agentic-2025-03]]. 2025-03 시점 finance 에이전트가 먼저 제공되고 **human capital**·supply chain·procurement·sales/marketing·customer service로 **확장 예정**(to be expanded) [[sources/deloitte-press-zora-ai-agentic-2025-03]]. Human Capital AI Solution Suite(Workforce Analyzer·Workforce Planner+·HR workflow library, 2025-06)는 별도 페이지 [[deloitte-workforce-analyzer-salesforce]]에서 다루며, 본 페이지의 인용 소스에는 해당 내용이 없다. HR 기능의 agent governance 맥락은 Deloitte 2026 Human Capital Trends [[sources/deloitte-2026-human-capital-trends]] 참조.

## Problem / Why (도입 배경)

- **Before (baseline)**: ❓ baseline 미공개 — 보도자료는 Deloitte 내부 expense management가 "많은 조직의 공통 과제"라고만 기술 [[sources/deloitte-press-zora-ai-agentic-2025-03]]. HR 영역의 도입 전 상태는 소스에 없음.
- **Pain point**: ⚠️ 벤더 주장: 프로세스 간소화·비효율 제거·직원의 전략 업무 집중 [[sources/deloitte-press-zora-ai-agentic-2025-03]].
- **Trigger**: _미공개 (not disclosed)_ — 소스는 "autonomous enterprise era" 비전(Girzadas CEO)만 언급 [[sources/deloitte-press-zora-ai-agentic-2025-03]]; 경쟁사 동반 발표 등은 소스에 없음.
- 🚫 일반론 표기: 벤더 플랫폼이므로 특정 클라이언트의 도입 배경은 고객별 상이.

## Solution Architecture

### A. Process (프로세스)

- **Before**: _미공개 (not disclosed)_
- **After** (⚠️ 벤더 주장 [[sources/deloitte-press-zora-ai-agentic-2025-03]]):
  1. Zora AI 플랫폼이 ready-to-deploy functional agents 제공 — finance 우선, human capital 등 5개 영역으로 확장 예정
  2. 에이전트가 perceive → reason → act
  3. Deloitte 내부 적용(finance): expense management 에이전트가 payroll·facilities·sales/marketing·employee time and expenses 비용을 모니터링, outlier 식별·업계 비교·예산 drill-down
  4. HR(human capital) 에이전트의 구체 프로세스: _미공개 (not disclosed)_
- **HITL**: ✅ human feedback loop 포함 [[sources/deloitte-press-zora-ai-agentic-2025-03]] — 개입 지점은 _미공개_
- **Trigger & Frequency**: _미공개 (not disclosed)_
- **Scope of autonomy**: _미공개 (not disclosed)_ — "perceive, reason, and act"로만 기술

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS / 기반 시스템**: _미공개 (not disclosed)_
- **AI 시스템 배치**: ⚠️ 벤더 주장: cloud subscription 모델, pre-built integrations로 "deployed rapidly on existing technologies" [[sources/deloitte-press-zora-ai-agentic-2025-03]]
- **배포 환경**: ⚠️ 벤더 주장: NVIDIA AI Enterprise·accelerated computing 기반 [[sources/deloitte-press-zora-ai-agentic-2025-03]]; hyperscaler·클라이언트 측 배치 옵션 _미공개 (not disclosed)_
- **연동·통합**: ⚠️ 벤더 주장: pre-built integrations [[sources/deloitte-press-zora-ai-agentic-2025-03]]; 구체 connector 목록 _미공개 (not disclosed)_
- **사용자 접점**: _미공개 (not disclosed)_
- **인증·권한**: ⚠️ 벤더 주장: Trustworthy AI 원칙(security·transparency·reliability) [[sources/deloitte-press-zora-ai-agentic-2025-03]] — 권한 모델 자체는 _미공개_

### C. Data (데이터)

- **입력 데이터 소스**: ⚠️ 벤더 주장: (finance 내부 적용) payroll·facilities·sales/marketing·employee time and expenses 비용 데이터 [[sources/deloitte-press-zora-ai-agentic-2025-03]]; HR 에이전트 입력 데이터 _미공개 (not disclosed)_
- **데이터 규모**: ⚠️ 벤더 주장: Deloitte 내부 "thousands of users"(수천 명) 대상 2025년 말까지 배포 계획 [[sources/deloitte-press-zora-ai-agentic-2025-03]]; HR 사용자 수 _미공개_
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: ⚠️ 벤더 주장: NVIDIA AI-Q Blueprint·NeMo 기반 [[sources/deloitte-press-zora-ai-agentic-2025-03]] — RAG/fine-tuning 여부는 _미공개_
- **데이터 거버넌스**: ⚠️ 벤더 주장: human feedback loop [[sources/deloitte-press-zora-ai-agentic-2025-03]]
- **민감정보 처리**: _미공개 (not disclosed)_
- **데이터 출처의 오너십**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: ⚠️ 벤더 주장: NVIDIA Llama Nemotron reasoning models [[sources/deloitte-press-zora-ai-agentic-2025-03]] — 버전 _미공개_
- **모델 유형**: ⚠️ 벤더 주장: agent (perceive·reason·act) — finance·human capital·supply chain·procurement·sales/marketing·customer service [[sources/deloitte-press-zora-ai-agentic-2025-03]]
- **제공 방식**: ⚠️ 벤더 주장: NVIDIA AI Enterprise·NeMo·AI Blueprints·accelerated computing [[sources/deloitte-press-zora-ai-agentic-2025-03]]
- **커스터마이징 기법**: _미공개 (not disclosed)_ — "customized to meet client needs"라는 문구만 존재 [[sources/deloitte-press-zora-ai-agentic-2025-03]]
- **Orchestration 프레임워크**: ⚠️ 벤더 주장: NVIDIA AI-Q Blueprint [[sources/deloitte-press-zora-ai-agentic-2025-03]]
- **평가·가드레일**: ⚠️ 벤더 주장: Trustworthy AI 원칙 + human feedback loop [[sources/deloitte-press-zora-ai-agentic-2025-03]]
- **비용·성능 지표**: _미공개 (not disclosed)_
- **Fallback·degradation 전략**: _미공개 (not disclosed)_

### E. Organization & Team (조직·팀 구조)

- **오너십**: _미공개 (not disclosed)_ — Deloitte 내부 적용은 finance 팀 대상 [[sources/deloitte-press-zora-ai-agentic-2025-03]]
- **참여 역할**: _미공개 (not disclosed)_
- **팀 규모·기간**: _미공개 (not disclosed)_
- **거버넌스 체계**: ⚠️ 벤더 주장: Deloitte Trustworthy AI 프레임워크 [[sources/deloitte-press-zora-ai-agentic-2025-03]]
- **변화관리**: _미공개 (not disclosed)_
- **파트너**: NVIDIA (기술 파트너) [[sources/deloitte-press-zora-ai-agentic-2025-03]]


## Impact / Metrics (기대효과)

### 기대효과 요약
⚠️ 벤더 주장(목표치): Deloitte 내부 finance 적용 시 비용 25% 절감·생산성 40% 향상 target — 실적이 아니며 HR 영역 성과는 _미공개_.

- ⚠️ 벤더 주장: 비용 25% 절감·생산성 40% 향상 (Deloitte finance 내부 **target**) [[sources/deloitte-press-zora-ai-agentic-2025-03]]
- ⚠️ 벤더 주장: 2025년 말까지 "thousands of users"(수천 명) 배포 계획 [[sources/deloitte-press-zora-ai-agentic-2025-03]]
- HR(human capital) 에이전트 성과: _미공개 (not disclosed)_
- HR workflow library 규모·리더 서베이 규모: 본 페이지 인용 소스에 없음 (수치 근거 미확보 — 2026-09-27 grounding 점검; 라이브러리는 [[deloitte-workforce-analyzer-salesforce]] 참조)

## Governance & Risk

- ⚠️ 25%·40% 수치는 ⚠️ 벤더 주장 (Deloitte 자체 운영 target — actual 미공개) [[sources/deloitte-press-zora-ai-agentic-2025-03]]
- ⚠️ 인력 영향평가 결과 기반 직원 재배치는 한국 노동법·노조 컨텍스트에서 위험 (컨설턴트 판단)
- ⚠️ 벤더 주장: Trustworthy AI 원칙·human feedback loop [[sources/deloitte-press-zora-ai-agentic-2025-03]] — 편향 감사·DPIA 등 구체 장치 _미공개_
- 거버넌스 격차 맥락: 임원 60%가 AI를 의사결정에 사용하나 5%만 잘 관리 [[sources/deloitte-2026-human-capital-trends]]

## Contradictions

> [!note] 2026-09-27 grounding — (1) 기존 "천 명 단위 사용자 수" 서술은 원문 "thousands of users"(수천 명)로 수정. (2) 기존 "만 명 단위 leader 서베이" 수치는 인용 소스 어디에도 없어 삭제(2026 HC Trends는 9,000명 임원 서베이). (3) Oracle 파트너십·Oracle Fusion 통합은 인용 소스에 없어 삭제. (4) Human Capital AI Suite(300+ workflows)는 2025-06 별도 보도자료 내용으로 본 페이지 소스에 없음 — [[deloitte-workforce-analyzer-salesforce]]로 이관. (5) 2025-03 보도자료는 HC 에이전트를 "to be expanded"(확장 예정)로 기술 → stage를 announced로 조정.

## Consulting Angle

- **KR 컨설팅 산업 직접 영향**:
  - Deloitte Anjin (한국 Deloitte) 통해 KR 대기업 HR transformation 시 동일 자산 활용 가능
  - 본 프로젝트 (HR AI Benchmark wiki) 자체가 Deloitte HC AI Suite의 한국 대안 — competitive positioning 명확화
- **300+ workflow library 벤치마크**: 본 wiki의 81 use case → 200건 → 300건 확장 시 Deloitte 표준 도달 가능
- **KR client positioning**:
  - Big-4 (Deloitte Anjin) vs domestic consulting + 본 wiki — 비용·local fit 차별화
  - Workforce Analyzer 같은 diagnostic tool은 KR client에게 "한국 시장 fit POC 4주" 제안 가능
- **2026 Q3-Q4 KR consulting positioning slide**:
  - Deloitte HC AI Suite (글로벌 표준) + 본 wiki (KR specific) + KR domestic consulting (LG CNS·삼성SDS·SK C&C) — 3-tier 시장 구조
- **반면교사**:
  - 글로벌 Big-4 자산은 한국 시장 fit 미검증 — 한국어·한국 노동법·한국 KPI cultural adaptation 필요
  - 25%·40% target은 Deloitte finance ops 내부 — KR client 적용 시 별도 baseline 측정 필수
- **NVIDIA 파트너십 시사점**: KR 대기업 자체 LLM (네이버 Hyperclova X·KT Mi:dm·SKT A.X) 위에 동일 agentic 패턴 구축 가능
