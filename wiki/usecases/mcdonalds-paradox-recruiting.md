---
title: "McDonald's — Paradox AI 채용"
slug: mcdonalds-paradox-recruiting
primary_category: Talent Acquisition
subcategory: Screening & Assessment
tags: [paradox, conversational-ai, high-volume, restaurant, fast-food]
company: McDonald's
industry: [restaurant, fast-food]
region: [global]
employee_class: [계약직]
vendor: [Paradox]
vendor_type: [point-solution]
output: "Olivia의 후보자 conversational 스크리닝 (work history·shift) 결과 + 매장 매니저 캘린더 기반 면접 slot 자동 제시 + McHire ATS 통합 hiring funnel 기록"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [summarization-qa, clustering-classification]
stage: production
frequency: daily
first_seen: 2021
last_confirmed: 2025
confidence: 0.20
consulting_angle_status: filled
sources:
  - "Paradox clients + NBC News https://www.nbcnews.com/tech/innovation/ai-job-recruiters-used-top-companies-glitches-rcna215128"
related_usecases:
  - chipotle-paradox-olivia
  - nestle-paradox-recruiting
related_vendors:
  - paradox
---

# McDonald's — Paradox AI 채용

⚠️ 벤더 주장: time-to-hire **21일→3일 미만** (86%↓). Paradox ecosystem에서 Chipotle·Nestlé·7-Eleven에 이은 4번째 글로벌 식음료 거대 고객. NBC News(Tier 1)가 AI recruiter 사용을 확인.

## Solution Architecture

### A. Process

- **Before**: 매장 매니저가 종이/이메일로 지원 처리, 지원 시간 10분, 시간 부족으로 채용 누수
- **After**:
  1. 후보자가 매장 sign·광고·Alexa/Google Assistant (Apply Thru)로 시작
  2. 텍스트 번호 발송 → Olivia가 즉시 conversational 스크리닝 시작
  3. 기본 work history·available shift 질문 (지원 시간 10분→2분)
  4. 통과 후보에게 매장 매니저 캘린더 기반 interview slot 제시
  5. COVID 기간엔 video로 추가 질문 응답
  6. 매장 매니저가 in-person 인터뷰에서 hire 결정 (McHire 플랫폼 통합)
- **HITL**: 매장 매니저가 in-person interview·hire 결정
- **Frequency**: continuous (대량 시간제 채용)
- **Source**: Paradox McHire launch press release


## Impact / Metrics (기대효과)

### 기대효과 요약
Time-to-hire 21일에서 3일 미만으로 86% 단축 (벤더 주장). NBC News가 AI recruiter 사용을 독립 확인(Fact).

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| Time-to-hire | **21일→3일 미만** | Paradox case study (2021) | ⚠️ 벤더 주장 |
| NBC News 확인 | AI recruiter 사용 confirmed | NBC News | ✅ Fact (Tier 1) |

## Consulting Angle
- **Paradox wiki 고객 생태계 6번째**: Chipotle(75%↓) · Nestlé(600%↑) · 7-Eleven(40k hrs/wk) · GM($2M) · Workday(23k hrs) · **McDonald's(21→3일)**
- 식음료·리테일 고볼륨 채용에서 Paradox의 **market dominance**가 데이터로 확실
