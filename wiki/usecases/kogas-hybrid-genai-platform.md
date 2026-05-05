---
title: "한국가스공사 — 하이브리드 GenAI 플랫폼"
slug: kogas-hybrid-genai-platform
primary_category: Employee Experience & HR Ops
subcategory: HR Service Delivery
tags: [kogas, hybrid-llm, energy-public, security-vs-performance, genon, korea, public-energy]
company: 한국가스공사
industry: [public, energy, utility]
region: [kr]
employee_class: [전임직, 기술사무직]
vendor: [GenON]
vendor_type: [point-solution]
output: "직원 query에 대한 보안 민감도 자동 분류 + 사내 LLM 응답 (보안 영역) 또는 상용 LLM 응답 (전문지식) 통합 답변 — 문서 초안·규정 검토·단순 행정"
ai_tech_type: [generative]
ai_tech_subtype: [summarization-qa]
stage: announced
frequency: daily
first_seen: 2025-09-10
last_confirmed: 2026-04-01
confidence: 0.35
consulting_angle_status: filled
sources:
  - sources/kr-conglomerate-2026-q2-research.md
related_usecases:
  - korea-electric-power-hr-bot
  - mirae-asset-ai-assistant-platform
  - hyundai-mobis-moai-platform
related_vendors: []
---

## Summary

한국가스공사가 에너지 공공기관 최초 **하이브리드 생성형 AI 플랫폼** 도입 (2025-09 발주, 2026 구축). **사내 전용 LLM (보안 민감 영역) + 상용 초거대 LLM (전문지식)** 라우팅. 임직원 문서 초안·규정 검토·단순 행정 자동화. **제논(GenON) 구축 사업 수주**. 한국 공공기관 보안 vs 성능 trade-off 해법 표준 패턴.

## Problem / Why

- **Before**: 가스공사 ~3K 직원이 문서 초안·규정 검토를 manual
- **Pain point**: 공공기관 보안 민감 영역 (에너지 인프라) + 성능 우수한 상용 LLM 활용 동시 필요
- **Trigger**: 2025-09 발주 — 제논 우선협상자, 2026 구축

## Solution Architecture

### A. Process

- **Before**: 문서 초안·규정 검토 manual
- **After**:
  1. 직원 query → 보안 민감도 자동 분류
  2. 보안 민감 영역 → 사내 LLM
  3. 일반 영역 (전문지식) → 상용 LLM (외부 API)
  4. 답변 통합 → 직원 활용
- **HITL**: 보안 분류 정책 governance + 직원 자율 사용

### B. System

- 사내 LLM (vendor·모델 _미공개_)
- 상용 LLM (OpenAI·Anthropic 등 추정)
- GenON 구축

### C/D. Data & Model

- 데이터: 가스공사 사내 문서 + 공개 전문지식
- 모델: 자체 LLM + 상용 LLM 라우팅

### E. Organization

- 가스공사 IT + GenON 파트너 (수주)

## Impact / Metrics

### 기대효과 요약
한국 공공기관 보안 + 성능 trade-off 해법 — 사내 + 상용 LLM 라우팅 표준 패턴.

- ✅ 에너지 공공기관 최초 하이브리드 AI 플랫폼
- ✅ GenON 우선협상 (2025-09)
- 2026 구축

## Consulting Angle

- **KR 공공·에너지 reference**:
  - 한국전력 [[korea-electric-power-hr-bot]] (솔트룩스 단일 플랫폼)
  - 가스공사 (GenON 하이브리드)
  - 도로공사·국민연금공단·한국조폐 등 비교
- **하이브리드 패턴**: 보안 민감 KR 그룹사 (반도체·바이오·국방) reference
- **반면교사**: vendor 의존 + 라우팅 정책 quality 검증 필요
