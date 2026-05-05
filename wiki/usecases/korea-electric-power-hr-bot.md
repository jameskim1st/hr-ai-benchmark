---
title: "한국전력 — HR-Bot 채용 챗봇 + AI 인사추천 시스템 (공공기관 최초, 2024 인사혁신 가점)"
slug: korea-electric-power-hr-bot
primary_category: Strategic Workforce & Governance
subcategory: Workforce Planning
tags: [korea-electric-power, kepco, hr-bot, saltlux, public-sector, recruitment-chatbot, ai-staffing-recommendation, korean-public, 2024-evaluation, korea]
company: 한국전력
industry: [public, energy]
region: [kr]
employee_class: [전임직, 기술사무직]
vendor: [솔트룩스]
vendor_type: [point-solution]
stage: production
frequency: monthly
first_seen: 2024-01-01
last_confirmed: 2026-04-01
confidence: 0.45
consulting_angle_status: filled
sources:
  - sources/korea-conglomerate-hr-ai-2025-2026.md
related_usecases:
  - kb-bank-ai-hr-deep-change
  - shinhan-bank-ai-staffing-algorithm
  - korean-public-sector-hr-ai
related_vendors: []
---

## Summary

한국전력의 **HR-Bot** (솔트룩스 기반) — 24/7 채용 상담·단순 반복 채용업무 자동화. 별도 **AI 인사추천 시스템**은 직원 역량·업무 이력 분석으로 적재적소 배치 지원 — **공공기관 최초** 사례. 2024년 한전 경영평가에서 **인사혁신 부문 가점**. 2025년 12월~2026년 3월 사내 규정·법규·문서 작성용 생성형 AI 시스템 전 직원 개방 예정.

## Problem / Why

- **Before**: 한전 23,000+ 직원, 공공기관 특성상 인사이동·채용 manual + 정량 자료 의존
- **Pain point**: 공공기관 인사이동의 표준화 어려움 + 채용 상담 volume 大
- **Trigger**: 2024 공공기관 AI 도입 가속 + 한전 경영평가 인사혁신 부문 (정부 평가 KPI)

## Solution Architecture

### A. Process — HR-Bot

- **Before**: 채용 상담 manual (HR call center) + 단순 반복 업무
- **After**:
  1. 지원자가 HR-Bot 24/7 챗봇 access
  2. 채용 상담·FAQ·일정 안내 자동 응답
  3. 단순 반복 채용업무 자동화 (서류 접수·일정 조율)
  4. 복잡 케이스 사람 HR escalation

### A. Process — AI 인사추천

- **Before**: 인사이동 manual 분석
- **After**:
  1. 직원 역량 (자격증·경력)·업무 이력 (성과·전배 이력) 입력
  2. AI가 적재적소 배치 후보 추천
  3. HR + 부서장 검토·확정
- **HITL**: HR + 부서장 최종 결정

### B/C/D. System

- 솔트룩스 (한국 NLP·AI vendor) 기반
- 한전 자체 HR 시스템 통합
- 2025-12~2026-03: 전 직원 사내 규정·법규·문서 작성용 생성형 AI 추가 개방

### E. Organization

- 한전 HR + 솔트룩스 파트너 + 2025-Q4 디지털혁신 본부

## Impact / Metrics

### 기대효과 요약
공공기관 최초 AI 인사추천 + HR-Bot 채용 자동화 — 2024 경영평가 인사혁신 부문 가점.

- ⚠️ 자사 보고:
  - 공공기관 최초 AI 인사추천 시스템
  - 2024 경영평가 인사혁신 부문 가점
  - 2025-12~2026-03 전 직원 생성형 AI 개방

## Governance & Risk

- ⚠️ 공공기관 인사이동 AI 추천의 explainability — 노조·직원 투명성 필요
- ⚠️ 한국 AI 기본법 (2026-01-22) 고영향 AI 분류 적용 — 인적감독 의무 자동 충족 검증
- ⚠️ 솔트룩스 단일 vendor lock-in
- ⚠️ "공공기관 최초" 주장의 경쟁 사례 추적 필요

## Consulting Angle

- **한국 공공기관 AI 인사 reference (1순위)**:
  - 공공기관 60% AI 도입 통계 (SPRi·NIA) 중 개별 case 식별 — 한전이 가장 잘 문서화
  - 한국전력공사·한국도로공사·국민연금·한국가스공사 등 공공기관 AI 도입 컨설팅의 baseline
- **2026 Q3-Q4 KR 공공·금융 컨설팅 deck**:
  - 한전 (공공) + KB AI HR Deep Change [[kb-bank-ai-hr-deep-change]] (금융) — 한국 large-scale 인사 AI 양대 reference
  - 정부 경영평가 KPI 정합성 — "인사혁신 부문 가점" angle은 공공기관 임원 강력 motivator
- **솔트룩스 한국 vendor 활용**: 글로벌 vendor (Workday·SAP·Eightfold) 비효율 대신 한국 NLP 강점 활용 — 한국 공공기관 보안·언어 fit 우수
- **반면교사**:
  - "최초" 주장의 시점 ambiguity — 외부 인용 시 "솔트룩스 발표 기준" 명시
  - 공공기관 AI 인사 추천 결과의 직원·노조 투명성 process 부재 시 risk
  - 솔트룩스 단일 vendor lock-in — 향후 multi-vendor 전략 권장
- **2025-Q4 생성형 AI 개방**: 전 직원 사내 규정·법규·문서 작성 AI — 신한 AI ONE [[shinhan-bank-ai-one-platform]]·미래에셋 AI Assistant [[mirae-asset-ai-assistant-platform]] 패턴과 유사
