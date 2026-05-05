---
title: "Amazon Connections — 1.5M 직원 daily 1-question pulse (300M annual responses, 97% adoption)"
slug: amazon-connections-daily-pulse
primary_category: Employee Experience & HR Ops
subcategory: Listening & Engagement
tags: [amazon, connections, daily-pulse, ml-prediction, frontline, 300m-responses, people-science, attrition-prediction]
company: Amazon
industry: [retail, logistics, tech]
region: [global]
employee_class: [all]
vendor: [Amazon internal]
vendor_type: [internal-build]
ai_tech_type: [predictive]
ai_tech_subtype: [prediction, clustering-classification]
stage: production
frequency: daily
first_seen: 2014-01-01
last_confirmed: 2024-06-01
confidence: 0.60
consulting_angle_status: filled
sources:
  - sources/us-large-enterprise-hr-ai-2025-2026.md
related_usecases:
  - microsoft-viva-glint-copilot-sentiment
  - amazon-hr-ai-restructuring
related_vendors: []
---

## Summary

Amazon **Connections** — 1.5M 직원에게 매일 로그인 시 1개 질문 pulse. 연 300M+ 응답이 People Science 팀의 ML 모델 입력 — 행동·태도 변화로 attrition·engagement 예측. ⚠️ 자사 보고: 97% voluntary adoption (산업 평균 ~25%). Andie Baker (전 principal scientist)가 구축. 단 Fortune Jun 2024 critical coverage — anonymity skepticism 보고.

## Problem / Why

- **Before**: annual·biannual 서베이로는 1.5M frontline 직원의 daily 변화 포착 불가
- **Pain point**: high-turnover frontline (creator·warehouse·delivery)의 sentiment·attrition 신호를 연 1~2회로 잡으면 늦음
- **Trigger**: People Science 데이터 사이언스 팀의 high-frequency listening 실험

## Solution Architecture

### A. Process

- **Before**: annual 서베이 + exit interview 사후 분석
- **After**:
  1. 직원 로그인 시 1개 질문 자동 출현 (5초 답변)
  2. 응답 + non-response 모두 데이터로 수집
  3. ML 모델이 행동(non-response trend)·태도(응답 sentiment) 변화 추적
  4. attrition·engagement 이벤트 사전 예측
  5. 매니저·HR에게 risk 신호 전달
- **HITL**: 매니저·HR이 risk 신호 review·action
- **Frequency**: daily (매일 1 질문)
- **Scope**: predict-only — action은 사람

### B/C/D. System

- Amazon 자체 구축 (proprietary)
- 데이터: 연 300M+ 응답
- 모델: 자체 ML (LLM 이전 세대)
- 사용자 접점: 직원 로그인 시 자동 popup

### E. Organization

- Amazon People Science 팀 (Andie Baker former principal)

## Impact / Metrics

### 기대효과 요약
high-frequency listening + ML 예측으로 frontline attrition·engagement 사전 신호 — KR 제조·유통·물류 대기업 적용 reference.

- ⚠️ 자사 보고:
  - 1.5M 직원 cover
  - 연 300M+ 응답
  - 97% voluntary adoption (vs 산업 ~25%)
- ⚠️ Fortune Jun 2024 critical: anonymity 회의론 보고

## Governance & Risk

- ⚠️ "voluntary" claim에 대한 직원 인지 격차 — Fortune이 의문 제기
- ⚠️ daily pulse가 "감시" 인식 시 KR 노조 sensitivity 높음
- ⚠️ 응답 anonymity 실제 보장 수준 _세부 미공개_

## Consulting Angle

- **KR 제조·유통·물류 frontline reference (1순위)**:
  - 삼성전자 사업장·현대차 공장·CJ대한통운 hub·이마트 매장·쿠팡 fulfilment — 모두 1.5M Amazon 같은 large frontline workforce
  - daily pulse 모델의 frontline fit 매우 높음
- **반면교사 활용 (Fortune critical coverage)**:
  - "voluntary"·"anonymity" 의심 사례를 KR 컨설팅 deck 노조 sensitivity 슬라이드에 인용
  - KR 도입 시 익명성 보장 framework + 노조 사전 합의 권장
- **KR 컨설팅 deck**: Glint Copilot [[microsoft-viva-glint-copilot-sentiment]] (annual deep) + Amazon Connections (daily wide) + Workday Illuminate Sentiment — listening cadence 비교
- **2026 Q3-Q4 frontline AI 어젠다**: Walmart Me@Walmart [[walmart-openai-certification]] + Amazon Connections + Cisco AI Assistant — "frontline AI" 카테고리 종합
