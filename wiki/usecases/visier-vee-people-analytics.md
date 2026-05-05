---
title: "Visier — Vee AI Digital Assistant + Org Design (People Analytics)"
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
frequency: daily
first_seen: 2025
last_confirmed: 2025
confidence: 0.25               # Tier 2(+0.20) 벤더 + Tier 3 고객 사례, 독립 검증 제한
consulting_angle_status: filled
sources:
  - "Visier 공식 https://www.visier.com/products/people-analytics-ai-agent/"
  - "TechIntelPro 2025 https://techintelpro.com/news/hr/ai/visier-org-design-ai-powered-workforce-planning-at-hr-tech-2025"
related_usecases:
  - workday-illuminate-job-architecture
related_vendors: []
---

# Visier — Vee AI Digital Assistant + Org Design

## Summary

Visier는 **People Analytics 전문 AI 플랫폼**. 주력 AI 제품 **Vee**는 자연어로 workforce 데이터에 질문하면 즉시 인사이트를 제공하는 디지털 어시스턴트. 2025년 HR Tech에서 **Visier Org Design** 출시 — AI 기반 조직 설계 + workforce planning 통합. 고객 **Providence (헬스케어)**는 Visier로 **2,000+ 간호사(caregiver) proactive onboarding + vacancy forecasting** 달성.

## Solution Architecture (요약)

### A. Process

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
- **Source**: Visier Vee product page

### Vee AI Digital Assistant
- **자연어 쿼리** → workforce 데이터 인사이트 (text-to-insight)
- 성과 추적, 이직 예측, workforce gap 분석
- HR 리더·비즈니스 리더 대상

### Org Design (2025 출시)
- AI 기반 조직 설계
- 인력·스킬·비용·engagement·성과 데이터 통합
- GenAI가 변경의 영향을 narrative로 설명

### Providence 고객 사례
- **Providence** (미국 대형 헬스케어 시스템)
- Visier로 workforce의 **완전한 가시성** 확보
- **정확한 vacancy 예측** → **2,000+ caregivers proactive onboarding**
- costly shortage 방지

## Impact / Metrics (기대효과)

### 기대효과 요약
Before: _미공개 (Providence의 기존 vacancy 예측 정확도·인력 부족 빈도)_ → After: ⚠️ 벤더 주장 (고객 전달) 2,000+ caregivers proactive onboarding으로 인력 부족 사전 방지. ROI 구체 수치(비용 절감·충원 기간) _미공개_. Org Design 제품 HR Tech 2025 출시(Fact).

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| Providence proactive onboarding | **2,000+ caregivers** | Visier 공식 | ⚠️ 벤더 주장 (고객 전달) |
| Org Design 출시 | HR Tech 2025 | TechIntelPro | ✅ Fact (공개 이벤트) |

## Consulting Angle

- **7. Strategic Workforce 카테고리의 첫 fact-rich reference**: 기존 [[workday-illuminate-job-architecture]] (stub 수준)와 달리 실제 고객(Providence) + 구체 metric(2,000+ caregivers) 있음
- **한국 적용**: 국내 대기업의 **인력계획 수립 + 조직설계**에 Visier 같은 People Analytics 도구 평가 시 reference
- **Vee의 자연어 쿼리**: "Text-to-SQL HR"의 실제 구현 사례 — 한국 HR 부서의 "데이터 기반 인사 의사결정" 프로젝트에 직접 연결
- **Limitation**: 고객 이름이 1곳(Providence)만 공개, ROI 구체 수치 _미공개_
