---
title: "Anaplan Workforce Analyst — Role-Based AI Agents"
slug: anaplan-workforce-analyst-ai-agents
primary_category: Strategic Workforce & Governance
subcategory: Workforce Planning
tags: [anaplan, workforce-analyst, role-based-ai-agent, scenario-planning, hr-finance-integration, fresenius, canada-goose, natural-language-query, fp-and-a]
company: _다수 (Anaplan 고객 — Fresenius·Canada Goose·Cinemark·healthcare provider 등)_
industry: [all]
region: [global]
employee_class: [all]
vendor: [Anaplan]
vendor_type: [point-solution]
output: "자연어 query에 대한 narrative 답변 (지역별 이직률·보류 채용 등) + 시나리오별 재무 영향 시뮬레이션 결과 (채용 동결·조직 개편·재배치) + position-level 정밀 인건비 계획 + AI 권고안"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [summarization-qa, prediction]
stage: announced
visibility: public
case_type: vendor-product
regulatory_exposure: [kr-high-impact-review, eu-annex-iii]
kr_law: AI 기본법 고영향 AI — autonomous 모드 인적감독 의무 충돌 (페이지)
kr_union: 단체교섭/근로자대표 협의 필요 (인사 의사결정 영향)
kr_language: 미확인 (벤더 확인 필요)
kr_vendor: 미확인 (국내 파트너 확인 필요)
frequency: monthly
first_seen: 2025-12-09
last_confirmed: 2026-04-01
confidence: 0.35
evidence_grade: C
corroborated_by: 0
freshness: fresh
depth: stub
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/verified-pwc-doc-2026-05.md, sources/anaplan-workforce-planning-ai-2025.md]
related_usecases:
  - deloitte-zora-ai-hc-suite
  - deloitte-workforce-analyzer-salesforce
  - workday-agent-system-of-record-asor
related_vendors: []
---

## Summary

Anaplan이 2025-12-09 발표한 **Role-Based AI Agents** 제품군 중 **Workforce Analyst** — ⚠️ 벤더 주장: 인력 리스크 식별, headcount 결정의 영향 산정·전달, 실시간 인력 계획 질의 응답. 2025-11 limited customer availability 시작, GA는 2026 Q1 예정(발표 시점). [[sources/anaplan-workforce-planning-ai-2025.md]] ⚠️ 벤더 주장 고객 사례: healthcare provider(익명) $21M 연 절감 + time-to-market 20% 단축 [[sources/anaplan-workforce-planning-ai-2025.md]]; Fresenius Medical Care planning time **30%+ 단축**, Canada Goose planning cycle **60% 단축** (Anaplan 공식 customer story — PwC fact-check 경유). [[sources/verified-pwc-doc-2026-05.md]] 2026 상반기 첫 autonomous AI 에이전트(이상 감지·다음 단계 권고·워크플로 트리거, "always with human" 감독) 출시 예정. [[sources/anaplan-workforce-planning-ai-2025.md]]

## Problem / Why (도입 배경)

- 벤더 제품이므로 특정 기업의 도입 배경은 고객별 상이. 🚫 일반론 표기: 아래는 인력 계획 영역의 일반적 pain point
- **Before**: ❓ baseline 미공개 — ⚠️ 벤더 주장: 모델 구축에 "days or weeks" 소요 (CoModeler 대비). [[sources/anaplan-workforce-planning-ai-2025.md]] (종전 "90퍼센트+ 기업 Excel 기반·예측 오차" 수치는 소스에 없어 제거 — 2026-09-27 grounding 점검)
- **Pain point**: ⚠️ 벤더 주장: headcount 결정의 영향을 산정·전달하고 인력 리스크를 식별하는 실시간 답변 필요. [[sources/anaplan-workforce-planning-ai-2025.md]] ⚠️ 벤더 주장 (healthcare provider): capacity planning을 단일 시스템으로 통합. [[sources/anaplan-workforce-planning-ai-2025.md]]
- **Trigger**: ✅ 2025-12-09 Anaplan Role-Based AI Agents 발표 — cross-functional planning use case에 AI agent 내장. [[sources/anaplan-workforce-planning-ai-2025.md]]

## Solution Architecture

### A. Process (프로세스)

- **Before**: _미공개 (not disclosed)_ — 🚫 일반론: HR·재무 분리 데이터의 수작업 통합·재계산
- **After** (⚠️ 벤더 주장, [[sources/anaplan-workforce-planning-ai-2025.md]]):
  1. Workforce Analyst agent가 인력 리스크 식별
  2. headcount 결정의 영향을 산정·전달
  3. 실시간 인력 계획 질의에 답변
  4. CoModeler: 자연어 요청 → 구조화된 모델·로직·계산 (수분 vs 수일~수주)
  5. Agent suite: 데이터 분석, narrative 리포트 생성, 승인된 액션(예: 리소스 재배치) 권고·실행
  6. 2026 상반기 예정: autonomous agent — 이상 감지·다음 단계 권고·팀·시스템 간 워크플로 트리거 ("always with human" 감독)
  (종전 "HCM(Workday/SAP)+ERP 연동", "position-level 인건비 계획" 단계는 소스에 없어 제거)
- **HITL**: ⚠️ 벤더 주장: "recommend and execute approved actions" — 승인 후 실행; autonomous agent도 human 감독 전제. [[sources/anaplan-workforce-planning-ai-2025.md]]
- **Frequency**: _미공개 (not disclosed)_

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS / 기반 시스템**: _미공개 (not disclosed)_
- **AI 시스템 배치**: ⚠️ 벤더 주장: Anaplan 플랫폼의 cross-functional planning use case·workflow에 AI agent 내장. [[sources/anaplan-workforce-planning-ai-2025.md]]
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: ⚠️ 벤더 주장: autonomous agent가 "across teams and systems" 워크플로 트리거 예정 — 구체 connector _미공개_. [[sources/anaplan-workforce-planning-ai-2025.md]]
- **사용자 접점**: ⚠️ 벤더 주장: 자연어 요청 (CoModeler). [[sources/anaplan-workforce-planning-ai-2025.md]] UI 세부 _미공개_
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: _미공개 (not disclosed)_ — ⚠️ 벤더 주장(healthcare provider): capacity planning 데이터를 단일 Anaplan 시스템으로 이전. [[sources/anaplan-workforce-planning-ai-2025.md]]
- **데이터 규모**: _미공개 (not disclosed)_
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: _미공개 (not disclosed)_
- **데이터 거버넌스**: ⚠️ 벤더 주장: Anaplan Custom Agent(limited availability) — "transparency and governance"로 custom AI analyst 구축·확장. [[sources/anaplan-workforce-planning-ai-2025.md]]
- **민감정보 처리**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **모델 유형**: ⚠️ 벤더 주장: role-based AI agent (자연어 → 모델·계산; 분석·narrative 리포트). [[sources/anaplan-workforce-planning-ai-2025.md]] LLM/ML 구성 세부 _미공개_
- **제공 방식**: _미공개 (not disclosed)_
- **커스터마이징 기법**: ⚠️ 벤더 주장: Anaplan Custom Agent로 고객이 custom AI analyst 구축·확장. [[sources/anaplan-workforce-planning-ai-2025.md]]
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: _미공개 (not disclosed)_ — ⚠️ 벤더 주장: autonomous agent는 "always with human" 감독. [[sources/anaplan-workforce-planning-ai-2025.md]]

### E. Organization & Team (조직·팀 구조)

- **오너십**: Anaplan 벤더 제품 — 고객사 HR·finance 계획 조직이 사용 (구체 _미공개_)
- **참여 역할**: ✅ Adam Thier, Anaplan Chief Product and Technology Officer (제품 발표). [[sources/anaplan-workforce-planning-ai-2025.md]]
- **팀 규모·기간**: _미공개 (not disclosed)_
- **거버넌스 체계**: _미공개 (not disclosed)_
- **파트너**: _미공개 (not disclosed)_


## Impact / Metrics (기대효과)

### 기대효과 요약
HR-finance data 단절 해소 + 시나리오 분석 수주 → 즉시 + 인건비 절감 8~9자리 수치 (대형 고객 사례).

- ⚠️ 벤더 주장 고객 metric (Anaplan 공식 customer story — 독립 검증 없음):
  - **Healthcare provider** (익명): $21M 연 절감 + time-to-market 20% 단축 + case resolution time 10~20% 단축. [[sources/anaplan-workforce-planning-ai-2025.md]]
  - **Cinema chain**: AI 최적화 인력 계획으로 eight-figure ROI. [[sources/anaplan-workforce-planning-ai-2025.md]]
  - **Fresenius Medical Care**: planning time 30%+ 단축. [[sources/verified-pwc-doc-2026-05.md]]
  - **Canada Goose**: planning cycle 60% 단축. [[sources/verified-pwc-doc-2026-05.md]]
- ⚠️ "retail bank 12% → 5% forecast 오차"·"ICRC hours → minutes" 수치는 PwC fact-check에서 검색 미확인 — 인용 불가. [[sources/verified-pwc-doc-2026-05.md]]
- 2026 상반기: autonomous agent 출시 예정. [[sources/anaplan-workforce-planning-ai-2025.md]]

## Governance & Risk

- ⚠️ 모든 metric ⚠️ 벤더 + 고객 자기 보고 — 독립 분석가 검증 별도 필요
- ⚠️ 2026 상반기 autonomous agent는 인간 감독 약화 risk — 한국 AI 기본법 인적감독 의무 충돌 가능 (벤더는 "always with human" 주장)
- ⚠️ HR·finance 데이터 통합 cross-system access의 보안·권한 거버넌스 _세부 미공개_

## Contradictions

> [!note] 2026-09-27 grounding — 종전 본문의 "2025-12-09 GA"는 raw 기준 "limited customer availability 2025-11, GA expected Q1 2026"으로 정정(stage: announced). "90퍼센트+ 기업 Excel 기반·예측 오차 10퍼센트+", "HCM(Workday/SAP)·ERP connector", "multi-tenant", "Polaris Calculation Engine", "Agent Studio"(raw 표기는 Custom Agent), "accurate, traceable, auditable"은 인용 소스 raw에 없어 제거·_미공개_ 처리.

## Consulting Angle

- **KR 대기업 인사기획·재무 통합 reference (Top 3)**:
  - Anaplan Workforce Analyst (HR-finance native 통합) + Deloitte Workforce Analyzer [[deloitte-workforce-analyzer-salesforce]] (컨설팅 기반 진단) + Workday ASOR [[workday-agent-system-of-record-asor]] (AI agent 거버넌스)
  - Excel 기반 인력 계획 갭 — KR 대기업도 동일 갭이라는 가설 (정량 근거는 소스 없음 — 클라이언트 진단으로 확인)
- **시나리오 시뮬레이션 슬라이드**: KR 그룹사 임원에게 "M&A·구조조정·정년 연장·지역 분산 시 인건비 영향 즉시 분석" 가치 제안
- **2026 Q3-Q4 KR consulting deck**:
  - "AI 인사기획"의 5단계 maturity (수기 → BI dashboard → AI 분석 → 자연어 query → autonomous agent) — Anaplan이 4~5단계 상용화
  - SAP HCM 도입 KR 대기업: SAP Joule Performance Agent + Anaplan Workforce Analyst 페어
  - Workday HCM 도입 KR: Workday Adaptive Planning vs Anaplan 양자 RFP 비교
- **반면교사**:
  - $21M 등 "숫자 중심" 마케팅이 강함 — KR client 인용 시 baseline 측정 + POC 명시 필요
  - autonomous agent는 한국 AI 기본법 (2026-01-22) 고영향 AI (인사 의사결정) 분류 가능성 — 인적감독 의무 충돌 미리 검토
  - HR-finance 통합 access 시 한국 개인정보보호법 + 금융정보보호 dual compliance 검증
