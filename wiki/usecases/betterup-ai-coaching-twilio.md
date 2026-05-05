---
title: "BetterUp — AI Coaching Platform (Twilio: 32% 성과↑, 5x 이탈↓)"
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

## Solution Architecture (요약)

### BetterUp Grow (AI-only 코칭)
- 실시간, 역할별 맞춤형 AI 코칭 (기존 human coach를 보조 또는 대체)
- ⚠️ 벤더 주장: **95% user satisfaction**
- ⚠️ 벤더 주장: **비용 70% 절감** (traditional coaching 대비)
- 2025년 기준 11개 기업 도입, 50+ pipeline (Inc.com 보도)
- VR 시뮬레이션 + talent intelligence dashboard

### Human + AI Hybrid (기존 모델)
- BetterUp의 원래 모델: 인간 코치 + AI 보조 (데이터 수집·인사이트 제공)
- Twilio 등 초기 고객은 이 hybrid 모델 사용

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
