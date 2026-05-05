---
title: "Deloitte — Workforce Analyzer + Planner+ AI Suite (Salesforce 도입, 300+ HR 워크플로)"
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
stage: production
frequency: adhoc
first_seen: 2025-06-24
last_confirmed: 2025-06-24
confidence: 0.35               # Tier 1 Deloitte(+0.35) + named customer Salesforce + recency excellent - 구체 metric 부족 = 0.35
consulting_angle_status: filled
sources:
  - "Deloitte PR 2025-06-24 https://www.deloitte.com/us/en/about/press-room/deloitte-launches-ai-solution-suite-for-human-and-machine-workforce.html"
  - "PR Newswire 2025-06-24 https://www.prnewswire.com/news-releases/deloitte-launches-ai-solution-suite-to-help-organizations-enhance-their-human-and-machine-workforce-302488802.html"
related_usecases:
  - visier-vee-people-analytics
  - amazon-hr-ai-restructuring
related_vendors: []
---

# Deloitte — Workforce Analyzer + Planner+ AI Suite

## Summary

Deloitte가 2025-06-24에 발표한 **Human Capital AI 솔루션 suite**: **Workforce Analyzer** (AI가 직무·역할에 미치는 영향 평가) + **Workforce Planner+** (AI 기반 인력 수급 분석·전략 정렬) + **HR AI Maturity Model**. **Salesforce**가 named customer로 확인됨 (Ruth Hickin, VP Workforce Innovation). ⚠️ 벤더 주장: **300+ HR 워크플로**를 agentic AI로 재설계.

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
- **300+ HR 워크플로**를 agentic AI 기반으로 재설계한 라이브러리
- HR AI 성숙��� 진단 도구 + 가속화 toolkit

## Solution Architecture

### A. Process

- **Before**: 역할별 AI 영향도를 수기 워크숍·인터뷰로 6~12개월에 걸쳐 평가
- **After**:
  1. 조직의 job catalog·task inventory를 Workforce Analyzer에 로드
  2. GenAI 엔진이 role별 task 분해·AI 자동화/증강 가능성 점수화
  3. 시나리오 모델링 — task automation 비율·재배치 영향·skills gap 시뮬레이션
  4. Workforce Planner+ 모듈이 우선순위·도입 로드맵 추천
  5. HR·전략·재무 리더가 시나리오 비교·승인
  6. Salesforce 사례에서는 skills data와 결합해 reskilling 결정에 활용
- **HITL**: 비즈니스 리더가 AI 영향 시나리오를 검토·전략 결정
- **Frequency**: adhoc (전사 AI 전략 수립 시)
- **Source**: Deloitte HC AI Suite press release


## Impact / Metrics (기대효과)

### 기대효과 요약
⚠️ 벤더 주장: 300+ HR 워크플로 라이브러리 구축 — 이는 feature/output 수치이며 outcome(시간 절감·비용 절감·채택률) 아님. Salesforce가 named customer(Fact)이나 해당 고객의 정량 성과 _미공개_.

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| Named customer | **Salesforce** (Ruth Hickin, VP) | Deloitte PR | ✅ Fact |
| HR 워크플로 라이브러리 | **300+** | Deloitte PR | ⚠️ 벤더 주장 |
| 출시일 | 2025-06-24 | PR Newswire | ✅ Fact |

## Consulting Angle

### ★ "Big 4 컨설팅이 HR AI 솔루션을 파는 시대"
- Deloitte가 컨설팅 advice를 넘어 **제품(Workforce Analyzer/Planner+)을 직접 판매** — Bersin이 Galileo Learn을 파는 것과 같은 "analyst → vendor" 전환 패턴
- **300+ HR workflow 라이브러리**는 컨설팅 프로젝트의 "standard playbook"화 — 개별 기업이 0에서 설계할 필요 줄어듬
- **Salesforce가 customer**: Salesforce 자체가 HR tech 플랫폼(MuleSoft, Slack 등)��� 보유하면서도 Deloitte의 HR AI 도구를 쓴다는 것 — [[workday-as-customer-paradox]]와 같은 "벤더가 다른 벤더의 고객" 패턴

### 한국 적용
- 국내 Big 4 (삼일·삼정·안진·한영)가 같은 패턴으로 HR AI 솔루션을 팔 가능성
- Deloitte Korea가 Workforce Analyzer를 국내 고객에 제안 시 이 wiki의 reference
