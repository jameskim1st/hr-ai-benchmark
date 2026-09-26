---
title: "Deloitte — Workforce Analyzer + Planner+ AI Suite"
slug: deloitte-workforce-analyzer-salesforce
primary_category: Strategic Workforce & Governance
subcategory: Workforce Planning
tags: [workforce-planning, ai-impact-assessment, agentic-ai, consulting, deloitte, salesforce]
company: Salesforce (named customer)
industry: [consulting, tech]
region: [global]
employee_class: [all]
vendor: [Deloitte]
vendor_type: [point-solution]
output: "역할별 AI disruption 영향도 점수 + task automation/증강 가능성 시나리오 + 인력 수급 시뮬레이션 + reskilling 우선순위 로드맵 + 300+ agentic HR 워크플로 라이브러리"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [summarization-qa, clustering-classification, prediction]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: [kr-high-impact-review, eu-annex-iii]
kr_law: AI 기본법 고영향 AI(직무 영향평가·인력 계획) — kr-high-impact
kr_union: 단체교섭/근로자대표 협의 필요 (인사 의사결정 영향)
kr_language: 미확인 (벤더 확인 필요)
kr_vendor: Deloitte Korea 지사 경유 언급 (페이지) — 실적 미공개
frequency: adhoc
first_seen: 2025-06-24
last_confirmed: 2025-06-24
confidence: 0.15
evidence_grade: C
corroborated_by: 0
freshness: stale
depth: stub
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/deloitte-pr-human-capital-ai-suite-2025-06.md, sources/prnewswire-deloitte-human-capital-ai-suite-2025-06.md]
related_usecases:
  - visier-vee-people-analytics
  - amazon-hr-ai-restructuring
related_vendors: []
---

# Deloitte — Workforce Analyzer + Planner+ AI Suite

## Summary

Deloitte가 2025-06-24에 발표한 **Human Capital AI 솔루션 suite**: **Workforce Analyzer** (AI가 직무·역할에 미치는 영향 평가) + **Workforce Planner+** (AI 기반 인력 수급 분석·전략 정렬) + **HR AI Maturity Model**. **Salesforce**가 named customer로 확인됨 (Ruth Hickin, VP Workforce Innovation) [[sources/deloitte-pr-human-capital-ai-suite-2025-06]]. ⚠️ 벤더 주장: agentic AI workflow library가 **300+ HR 워크플로**를 제공 [[sources/deloitte-pr-human-capital-ai-suite-2025-06]].

## Problem / Why (도입 배경)

- **Before (baseline)**: ❓ baseline 미공개 — 보도자료는 Salesforce의 도입 전 상태를 기술하지 않음.
- **Pain point**: ⚠️ 벤더 주장: agentic AI가 workforce를 재편하는 상황에서 "AI가 workforce segment별로 미치는 영향 평가·프로세스 자동화"가 필요하다는 것이 Deloitte의 문제 정의 [[sources/deloitte-pr-human-capital-ai-suite-2025-06]].
- **Trigger**: _미공개 (not disclosed)_ — Salesforce가 도입을 결정한 직접적 계기는 소스에 없음. Hickin 인용은 Workforce Analyzer + skills data 조합의 유용성만 언급 [[sources/prnewswire-deloitte-human-capital-ai-suite-2025-06]].
- 🚫 일반론 표기: 벤더 제품(suite)이므로 특정 기업의 도입 배경은 고객별 상이.

## 핵심 구성요소

### Workforce Analyzer
- AI가 직무·역할에 미치는 disruption 잠재력 평가
- 각 역할의 AI 영향도를 시나리오별 분석
- 생산성 향상·비용 관리·혁신 촉진 지원

### Workforce Planner+
- 독점 AI로 노동 공급·수요 분석
- 인력 계획과 전략 정렬
- 비즈니스 리더에게 시나리오 기반 의사결정 지원

### HR AI Maturity Model + Agentic AI Workflow Library
- ⚠️ 벤더 주장: **300+ HR 워크플로**를 최신 reasoning 기반으로 재구성한 라이브러리 [[sources/deloitte-pr-human-capital-ai-suite-2025-06]]
- HR AI 성숙도 모델·진단 도구(전략·데이터·기술·거버넌스·솔루션 딜리버리·인력 enablement 6개 차원) + 가속화 toolkit [[sources/deloitte-pr-human-capital-ai-suite-2025-06]]

## Solution Architecture

### A. Process (프로세스)

- **Before**: ❓ baseline 미공개 — 도입 전 프로세스·소요 기간은 소스에 없음 (수치 근거 미확보 — 2026-09-27 grounding 점검).
- **After** (⚠️ 벤더 주장, 보도자료 기술 범위 [[sources/deloitte-pr-human-capital-ai-suite-2025-06]]):
  1. Workforce Analyzer가 work function을 평가하고 역할별 AI disruption 잠재력을 추산
  2. 효율·성장 시나리오를 생성
  3. Workforce Planner+가 인력 계획·전략적 배치를 지원 [[sources/prnewswire-deloitte-human-capital-ai-suite-2025-06]]
  4. Salesforce는 Workforce Analyzer를 "robust skills data"와 결합해 인재에 대한 AI 영향을 파악 (Hickin 인용) [[sources/prnewswire-deloitte-human-capital-ai-suite-2025-06]]
- **HITL**: _미공개 (not disclosed)_ — 리더의 검토·승인 단계는 소스에 명시되지 않음
- **Trigger & Frequency**: _미공개 (not disclosed)_ (frontmatter `adhoc`은 전사 AI 전략 수립 맥락의 분류값)
- **Scope of autonomy**: _미공개 (not disclosed)_

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS / 기반 시스템**: _미공개 (not disclosed)_
- **AI 시스템 배치**: _미공개 (not disclosed)_ — Deloitte 제공 suite라는 점 외 배치 형태 미기술 [[sources/deloitte-pr-human-capital-ai-suite-2025-06]]
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: _미공개 (not disclosed)_ — Salesforce 인용에서 "skills data" 결합만 언급 [[sources/prnewswire-deloitte-human-capital-ai-suite-2025-06]]
- **사용자 접점 (UX layer)**: _미공개 (not disclosed)_
- **인증·권한**: _미공개 (not disclosed)_
- **가용성·SLA**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: ⚠️ 벤더 주장: skills data (Salesforce Hickin 인용) [[sources/prnewswire-deloitte-human-capital-ai-suite-2025-06]]; 그 외 _미공개 (not disclosed)_
- **데이터 규모**: _미공개 (not disclosed)_
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context 구분**: _미공개 (not disclosed)_
- **데이터 거버넌스**: _미공개 (not disclosed)_
- **민감정보 처리**: _미공개 (not disclosed)_
- **데이터 출처의 오너십**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_ — 보도자료는 "GenAI"·"proprietary AI"로만 기술 [[sources/deloitte-pr-human-capital-ai-suite-2025-06]]
- **Model 유형**: _미공개 (not disclosed)_
- **제공 방식**: _미공개 (not disclosed)_
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: _미공개 (not disclosed)_
- **비용·성능 지표**: _미공개 (not disclosed)_
- **Fallback·degradation 전략**: _미공개 (not disclosed)_

### E. Organization & Team (조직·팀 구조)

- **오너십**: _미공개 (not disclosed)_ — Salesforce 측 인용자는 VP, Workforce Innovation and Transformation [[sources/deloitte-pr-human-capital-ai-suite-2025-06]]
- **참여 역할**: _미공개 (not disclosed)_
- **팀 규모·기간**: _미공개 (not disclosed)_
- **거버넌스 체계**: _미공개 (not disclosed)_ (Maturity Model의 6개 차원 중 governance가 포함되나 Salesforce 적용 여부 미공개)
- **변화관리**: _미공개 (not disclosed)_
- **파트너**: Deloitte (솔루션 제공사 자체) [[sources/deloitte-pr-human-capital-ai-suite-2025-06]]


## Impact / Metrics (기대효과)

### 기대효과 요약
⚠️ 벤더 주장: 300+ HR 워크플로 라이브러리 구축 — 이는 feature/output 수치이며 outcome(시간 절감·비용 절감·채택률) 아님. Salesforce가 named customer(Fact)이나 해당 고객의 정량 성과 _미공개_.

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| Named customer | **Salesforce** (Ruth Hickin, VP) | Deloitte PR | ✅ Fact |
| HR 워크플로 라이브러리 | **300+** | Deloitte PR | ⚠️ 벤더 주장 |
| 출시일 | 2025-06-24 | PR Newswire | ✅ Fact |

## Governance & Risk

- **편향·설명가능성**: _미공개 (not disclosed)_ — 역할별 AI disruption 점수의 산출 방식·검증 절차는 소스에 없음.
- **개인정보**: _미공개 (not disclosed)_ — 인력 계획에 쓰이는 skills data의 범주·처리 방식 미공개.
- **HITL**: _미공개 (not disclosed)_.
- **거버넌스 장치**: HR AI Maturity Model이 governance를 6개 차원 중 하나로 포함 [[sources/deloitte-pr-human-capital-ai-suite-2025-06]] — 단, 이는 진단 프레임워크이며 Salesforce 적용 사례의 거버넌스 장치는 아님.
- **리스크**: 역할별 자동화 가능성 점수가 인력 감축·재배치 결정에 쓰이면 한국 AI 기본법 고영향 AI 검토 대상(`kr-high-impact-review`)·EU AI Act Annex III 노무 관리 영역에 해당할 수 있음.

## Contradictions

> [!note] 2026-09-27 grounding — 두 source(deloitte-pr-human-capital-ai-suite-2025-06, prnewswire-deloitte-human-capital-ai-suite-2025-06)는 동일 보도자료의 배포 채널 사본이며 독립 2차 소스로 계산하지 않음. "300+ HR workflows"는 두 raw 스냅샷 모두에 존재함을 확인(source 페이지 Limitations의 "확인되지 않음" 기술은 발췌 누락). A 섹션의 "6~12개월 수기 평가" 등 소스에 없던 baseline 서술은 삭제.

## Consulting Angle

### ★ "Big 4 컨설팅이 HR AI 솔루션을 파는 시대"
- Deloitte가 컨설팅 advice를 넘어 **제품(Workforce Analyzer/Planner+)을 직접 판매** — Bersin이 Galileo Learn을 파는 것과 같은 "analyst → vendor" 전환 패턴
- **300+ HR workflow 라이브러리**는 컨설팅 프로젝트의 "standard playbook"화 — 개별 기업이 0에서 설계할 필요 줄어듬
- **Salesforce가 customer**: Salesforce 자체가 HR tech 플랫폼(MuleSoft, Slack 등)을 보유하면서도 Deloitte의 HR AI 도구를 쓴다는 것 — [[workday-as-customer-paradox]]와 같은 "벤더가 다른 벤더의 고객" 패턴

### 한국 적용
- 국내 Big 4 (삼일·삼정·안진·한영)가 같은 패턴으로 HR AI 솔루션을 팔 가능성
- Deloitte Korea가 Workforce Analyzer를 국내 고객에 제안 시 이 wiki의 reference
