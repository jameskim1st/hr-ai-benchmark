---
title: "BetterUp — AI Coaching Platform"
slug: betterup-ai-coaching-twilio
primary_category: Performance & Talent Management
subcategory: Coaching
tags: [ai-coaching, leadership, retention, performance, twilio, betterup, roi]
company: Twilio
industry: [tech, saas]
region: [na]
employee_class: [all]
vendor: [BetterUp]
vendor_type: [point-solution]
output: "매니저별 Whole Person Assessment 점수 + 개인화 6개월 learning path + AI coach 대화형 nudge·micro-intervention + behavior change → 비즈니스 KPI(retention·promotion) 매핑 dashboard"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [summarization-qa, recommendation-ranking]
stage: production
frequency: monthly
first_seen: 2025
last_confirmed: 2025
confidence: 0.45               # Tier 3 vendor(+0.10) + Tier 2 Inc.com(+0.20) + Tier 1 Bersin(+0.20, 할인: advisor 이해관계) + Tier 2 HR Executive(+0.20) = base 0.70, 할인 후 0.45 (Bersin COI + Twilio 구체 metric은 벤더 자체 주장)
consulting_angle_status: filled
sources:
  - "BetterUp ROI page https://www.betterup.com/roi-of-betterup"
  - "Inc.com 2025 https://www.inc.com/annabel-burba/how-betterup-built-an-ai-only-coaching-product-95-percent-of-its-customers-love/91221747"
  - "BetterUp customers https://www.betterup.com/customers"
  - sources/bersin-betterup-manage-ai-coaching-2024-04.md
  - sources/hrexecutive-bersin-coaching-disruptions-2024.md
related_usecases:
  - moderna-self-review-gpt
related_vendors: []
---

# BetterUp — AI Coaching Platform

## Summary

BetterUp은 **AI 기반 리더십·매니저 코칭** 플랫폼. 2025년 **BetterUp Grow** (AI-only 코칭 제품) 출시로 전통 human coaching 대비 **비용 70% 절감 + 95% 사용자 만족**을 주장. 가장 강력한 레퍼런스는 **Twilio (8,000+ 직원)**:  코칭 받은 직원은 **고성과 평가 32% 더 높고, 이탈 5배 낮음**. 다수 고객에서 ROI 수치가 구체적으로 공개돼 wiki의 Performance 카테고리 **가장 fact-rich 사례**. **Josh Bersin**(Tier 1, 단 BetterUp advisor)이 BetterUp Manage를 "pioneering AI-powered platform for leaders"로 독립 분석 ([[bersin-betterup-manage-ai-coaching-2024-04]]). **HR Executive**(Tier 2)도 Bersin의 코칭 시장 분석을 보도 ([[hrexecutive-bersin-coaching-disruptions-2024]]).

## Problem / Why

- 리더십·매니저 코칭은 효과가 있지만 **전통 human coaching은 비용이 높아 소수 임원에게만 제공** 가능
- 중간 관리자·일반 직원까지 코칭을 확장하려면 **비용 절감 + 스케일** 필요
- 코칭 효과의 **ROI 정량 측정**이 어려워 HR budget에서 정당화 곤란

## Solution Architecture

### A. Process

- **Before**: Twilio는 double-digit 성장 속에 매니저 effectiveness 70% 수준. Manager 역량개발은 이벤트성 워크숍·LMS 과정 위주로 1:1 코칭은 임원에 한정
- **After**:
  1. 매니저가 BetterUp Manage 플랫폼에서 Whole Person Assessment 수행 (resilience·growth mindset·risk tolerance 등)
  2. 시스템이 strengths·focus area 식별 → AI가 scenario 질문(예: "low-performer 대화") 통해 맥락 수집
  3. 6개월 단위 personalized learning path + 전담 human coach + AI coach 조합 제공
  4. 주별 micro-intervention (영상·assessment·1:1) 자동 발송, AI coach가 in-the-flow nudge
  5. 분석 dashboard가 behavior change → 비즈니스 지표(retention·engagement·promotion) 매핑
- **HITL**: Human coach가 1:1 세션, HR/CHRO가 cohort·ROI 검토
- **Frequency**: weekly micro-intervention, monthly 1:1 coaching, quarterly 리포팅

### B. System & Infrastructure (R9 research)

- **Core HRIS**: Twilio 측 _미공개_ — BetterUp은 stand-alone SaaS, SSO·SCIM 연동
- **AI 시스템 배치**: ✅ BetterUp Manage (hybrid) + BetterUp Grow (AI-only) SaaS
- **배포 환경**: _미공개_ (BetterUp cloud)
- **연동·통합**: HRIS SSO, calendar (1:1), 학습 dashboard
- **사용자 접점**: BetterUp web·모바일 — assessment·1:1 영상 코칭·micro-intervention·VR (Grow)
- **인증·권한**: 기업 SSO + RBAC (manager·HR dashboard 분리)

### C. Data (R9 research)

- **입력 데이터 소스**: ✅ Whole Person Assessment (resilience·growth mindset 등), 코칭 세션, behavior change tracker, 비즈니스 KPI
- **데이터 규모**: Twilio 8K+ 직원 cohort
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_ — Grow AI 코치 LLM 기반 추정
- **데이터 거버넌스**: ⚠️ BetterUp 표준: 코칭 세션은 employer에 disaggregated form만 (자사 정책)
- **민감정보 처리**: _미공개_ — 멘탈헬스 인접 — HIPAA·GDPR 별도 명시 없음

### D. Model (R9 research)

- **Foundation model**: _미공개_ — Grow LLM 기반이나 모델·버전 비공개
- **모델 유형**: LLM (conversational coaching) + assessment scoring + recommendation
- **제공 방식**: _미공개_
- **커스터마이징 기법**: ⚠️ 벤더 주장: BetterUp 코칭 IP·과학 자문 (Martin Seligman 등) prompt·rubric
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: ⚠️ 벤더 주장: 95% user satisfaction (Inc.com, BetterUp 자체 측정) — 독립 검증 부재


## Impact / Metrics (기대효과)

### 기대효과 요약
AI 코칭 수혜 직원의 고성과 평가 확률 32% 향상, 이탈률 5배 감소 (벤더 주장 기반, Twilio 사례).

### Twilio (8,000+ 직원, named customer) ⭐

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| 고성과 평가 확률 | 코칭 받은 직원이 **32% 더 높음** | BetterUp ROI page | ⚠️ 벤더 주장 |
| 이탈률 | 코칭 받은 직원이 **5x 덜 이탈** | BetterUp ROI page | ⚠️ 벤더 주장 |

### 익명 고객 사례

| 사례 | 지표 | 값 | 출처 |
|---|---|---|---|
| Sales 조직 | Quota hitting | 코칭 팀 **1.6x** 달성 / **$4.5M** 추가 기회 | BetterUp ROI |
| Software 회사 | Attrition rate | 코칭 받은 직원 **4.3x 낮음** / 연 **$14M** 절약 | BetterUp ROI |
| Tech consulting | NPS | **+15.6pt** YoY / margin **+6%** vs 평균 | BetterUp ROI |

### BetterUp Grow AI 제품

| 지표 | 값 | 출처 |
|---|---|---|
| User satisfaction | **95%** | Inc.com |
| 비용 vs human coaching | **70% 절감** | BetterUp 공식 |
| Confidence increase | **16%** | BetterUp 공식 |
| 채택 기업 | **11곳** (2025), 50+ pipeline | Inc.com |
| Leadership ROI | **600% average** | BetterUp 공식 |

**⚠️ 모든 수치가 벤더 자체 주장**. 단, **다수 고객·다양한 metric**이 공개돼 있어 wiki의 다른 벤더보다 투명도 높음.

## Consulting Angle

### 핵심 가치
- **코칭 카테고리의 가장 구체적 ROI 사례**: Twilio 이름 + 32%·5x 수치는 CHRO에 직접 제시 가능
- **"AI coaching democratization" 논의의 앵커**: "임원만 받던 코칭을 전 직원에게" = 한국 대기업 HR에서도 관심 높은 주제
- **Human vs AI coaching trade-off 논의**: BetterUp는 두 모델 모두 운영 → "어디까지 AI가, 어디서부터 사람이"를 데이터로 판단 가능

### 한국 적용
- 국내 대기업 리더십 개발(LMD) 프로그램에 AI coaching 도입 시 BetterUp이 reference
- 단, **한국어 대응·한국 리더십 문화 fit**은 검증 안 됨
- 국내 경쟁: 코칭업·마인드풀리 등 한국 코칭 스타트업의 AI 전략과 비교 필요

### 주의
- Twilio 수치(32%·5x)의 **측정 방법론** 미공개 — 선택 편향(자발적 코칭 참여자 = 원래 고성과자) 가능성
- Inc.com이 "95% satisfaction"을 보도했지만 이는 BetterUp 자체 측정 — Tier 2 매체가 **전달**한 것이지 **검증**한 것은 아님
