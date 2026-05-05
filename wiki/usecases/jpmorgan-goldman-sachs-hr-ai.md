---
title: "JPMorgan Chase + Goldman Sachs — 금융권 HR AI (ML 채용, GS AI 10k 직원, 인력 재편)"
slug: jpmorgan-goldman-sachs-hr-ai
primary_category: Talent Acquisition
subcategory: Sourcing & Attraction
tags: [banking, finance, ml-recruiting, ai-hiring-freeze, workforce-restructuring]
company: JPMorgan Chase, Goldman Sachs
industry: [finance, banking]
region: [na, global]
employee_class: [기술사무직]
vendor: [internal build]
vendor_type: [internal-build]
stage: production
frequency: daily
first_seen: 2025-10
last_confirmed: 2025-10-15
confidence: 0.40               # Tier 2 CNBC(+0.20) + Tier 2 HR Executive(+0.20) + CEO 직접 발언 = 0.40
consulting_angle_status: filled
sources:
  - "CNBC 2025-10-15 https://www.cnbc.com/2025/10/15/jpmorgan-chase-goldman-sachs-ai-hiring.html"
  - "HR Executive https://hrexecutive.com/jpmorgan-ceo-we-have-displaced-people-from-ai-and-we-offer-them-other-jobs/"
  - "HR Dive https://www.hrdive.com/news/banks-ramp-up-ai-hiring-roi-efficiency-gains-evident-insights/746724/"
related_usecases:
  - amazon-hr-ai-restructuring
  - ibm-askhr-watsonx
related_vendors: []
---

# JPMorgan Chase + Goldman Sachs — 금융권 HR AI

> **금융권 HR AI 최초 수집 사례**: 미국 최대 은행 JPMorgan Chase와 Goldman Sachs의 AI-driven HR 전략을 한 페이지에 기록. 양사 모두 **AI로 채용을 줄이면서 AI 인력을 늘리는** 구조적 전환 중.

## Problem / Why (도입 배경)

### 공통 Pain Point (금융 산업)
- **Before**: 투자은행·자산관리·리테일금융의 **인건비가 총비용의 50%+** — 금융 산업에서 AI 자동화의 ROI가 가장 큰 이유
- **Pain point**: (1) AI 역량 인력 확보 경쟁 치열, (2) 기존 HR 프로세스(채용·온보딩·분석)에 과도한 인력 투입, (3) 데이터 보안·규제 준수 하에서 AI 도입이 다른 산업보다 복잡
- **Trigger**: 2024~2025 금융 산업 전반에서 "**AI 도입을 안 하면 경쟁에서 뒤처진다**"는 공감대 형성. JPMorgan CEO Dimon의 "모든 프로세스에 AI 주입" 방침이 HR에도 적용

## Impact / Metrics (기대효과)

### 기대효과 요약
**채용 비용·시간 절감 + AI 인력 전환 + 반복 업무 자동화**. 양사 모두 "HR 인력 축소 + AI 기술 인력 확대"라는 workforce composition 변화가 핵심 기대효과. Goldman은 Copilot으로 개발자 20% 효율↑을 이미 달성.

## JPMorgan Chase

### 핵심 Fact
- **CEO Jamie Dimon**: "AI가 사람들을 **displaced** 했고, 우리는 그들에게 **다른 일자리를 제공**한다" (Bloomberg)
- **매니저에게 채용 자제 지시**: AI를 every client experience·employee process·backend operation에 주입하면서 신규 채용 회피
- **ML 기반 채용 도구 특허 출원**: employee public data + 네트워크 분석 → **confidence score** 생성 (후보자 적합도·접촉 용이성·적극적 구직 여부 예측)
- **AI 인력 증가**: 은행 업계 전체에서 AI model development·platform engineering·project management 기술자를 **13% 증가** (JPMorgan·Wells Fargo·Citigroup 주도)

### Consulting Angle
- Dimon의 "displaced but offered other jobs"는 IBM Krishna의 "replaced but elevated"와 **같은 패턴이지만 더 솔직한 표현**
- ML 채용 특허는 **"AI가 네트워크 기반으로 후보자를 찾는"** passive recruiting의 진화

## Goldman Sachs

### 핵심 Fact
- **12,000 개발자에게 GitHub Copilot** 배포 → ⚠️ 자사 보고: **~20% 효율성 향상**
- **10,000 직원에게 GS AI** 배포 (ChatGPT 유사 내부 도구) — bankers·traders·asset managers 대상
- **1,000명 감축** 보도 — AI가 investment banking 보상·커리어를 reshape

### Consulting Angle
- Goldman은 **"전 직원에게 AI 도구 배포"** 전략 (Moderna의 "모든 직원에게 ChatGPT Enterprise"와 유사)
- 12k 개발자 Copilot 배포는 HR이 아닌 Engineering이지만 **"전사 AI 배포가 HR 전략에 미치는 영향"**의 증거

## 금융 산업 전체 Insight

| 지표 | 값 | 출처 |
|---|---|---|
| AI 기술자 증가 | **13%** (JPMorgan·Wells Fargo·Citi) | HR Dive |
| Goldman Copilot 효율 | **~20%** | CNBC |
| Goldman GS AI 사용자 | **10,000명** | CNBC |

## Consulting Angle — 금융 산업 특수

### 왜 금융이 HR AI의 "canary in the coal mine"인가
1. **높은 인건비** → AI 대체 ROI가 가장 큰 산업
2. **규제 환경** → compliance·risk management에 AI governance 성숙
3. **데이터 풍부** → 성과·보상·이직 데이터가 가장 구조화됨
4. **경쟁 압력** → "옆 은행이 AI 쓰면 우리도"

### 한국 금융 시사점
- KB증권·신한은행이 이미 마이다스아이티 inAIR 도입 ([[midas-inair-ai-assessment-korea]])
- 국내 금융 HR AI는 **채용 평가**에서 시작 → **JPMorgan 패턴(ML 기반 sourcing, 채용 억제)으로 진화** 가능성
- 금감원·금융위 규제(AI 활용 가이드라인)와의 정합성 확인 필요
