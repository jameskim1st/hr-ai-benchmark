---
title: "adidas — Qualtrics XM AI (수동 분석 95%↓, 매니저 행동 계획 70%↑)"
slug: qualtrics-adidas-employee-experience-ai
primary_category: Employee Experience & HR Ops
subcategory: Listening & Engagement
tags: [employee-listening, engagement, qualtrics, sentiment, ai-insights, retail]
company: adidas
industry: [retail, sports, fashion]
region: [eu]
employee_class: [all]
vendor: [Qualtrics]
vendor_type: [point-solution]
stage: production
frequency: monthly
first_seen: 2025-10
last_confirmed: 2025-10
confidence: 0.30
consulting_angle_status: filled
sources:
  - "Qualtrics press 2025-10 https://www.qualtrics.com/articles/news/qualtrics-accelerates-ai-leadership-and-value-with-experience-agents/"
  - "BenefitNews https://www.benefitnews.com/news/how-adidas-and-allstate-use-ai-to-make-employee-feedback-more-impactful"
related_usecases:
  - workday-illuminate-employee-sentiment
  - moderna-ask-hr-routing
related_vendors: []
---

# adidas — Qualtrics XM Employee Experience AI

## Summary

adidas가 Qualtrics XM AI를 도입해 ⚠️ 벤더 주장: **수동 분석 95%↓**, **매니저의 개인화 행동 계획 작성 70%↑**. Dr. Sebastian Projahn (Sr. Director People Intelligence, adidas): *"We leveraged Qualtrics AI to democratize insights, reduce bias, and save time"* — 특히 매장·물류센터 매니저에게 즉시 인사이트 제공.

## Solution Architecture

### A. Process

- **Before**: 분기/연간 engagement 설문 후 manager가 보고서 수기 분석 (160+ hours/cycle)
- **After**:
  1. 직원이 Continuous Listening 설문 응답 — Qualtrics가 conversational AI로 follow-up 질문
  2. Qualtrics Assist for EX가 sentiment·테마 분석, manager별 personalized insight 생성
  3. 매니저별 dashboard에 팀 specific feedback + action recommendation 제시
  4. xFlow workflow가 HRIS·ticketing 시스템과 연동해 자동 alert·action
  5. Predictive retention 분석으로 at-risk 직원 식별
  6. 매니저가 추천 action 실행, 다음 cycle에서 효과 측정
- **HITL**: 매니저가 AI action recommendation 채택·실행
- **Frequency**: continuous + cycle-based
- **Source**: Adidas/Allstate Qualtrics (Benefit News)


## Impact / Metrics (기대효과)

### 기대효과 요약
수동 분석 95% 이상 감소, 매니저 행동 계획 작성 70% 증가, AI 고객 성장 346% YoY (벤더 주장).

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| 수동 분석 감소 | **95%+** | Qualtrics press | ⚠️ 벤더 주장 |
| 매니저 행동 계획 작성 | **70%↑** | Qualtrics press | ⚠️ 벤더 주장 |
| AI 고객 성장 | **346% YoY** | Qualtrics press | ⚠️ 벤더 주장 |
| Named leader | **Dr. Sebastian Projahn** (Sr. Dir. People Intelligence) | BenefitNews | ✅ Fact |

## Consulting Angle
- **Listening & Engagement 카테고리 첫 named-customer metric** — [[workday-illuminate-employee-sentiment]]가 stub인 것과 대비
- **"매장·물류센터 매니저에게 인사이트 민주화"** — 현장 직원 engagement에 AI 적용의 직접 사례
- **EU 기업 (독일 본사)**: GDPR 하에서 employee sentiment AI 운영 → EU compliance reference
