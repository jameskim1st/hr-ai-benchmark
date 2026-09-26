---
title: "한국가스공사 — 하이브리드 GenAI 플랫폼"
slug: kogas-hybrid-genai-platform
page_type: enterprise-ai
moved_from_usecases: 2026-09-27
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
visibility: public
case_type: adoption
regulatory_exposure: []
frequency: daily
first_seen: 2025-09-10
last_confirmed: 2026-04-01
confidence: 0.55
evidence_grade: B
corroborated_by: 1
freshness: fresh
depth: stub
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/energykorea-kogas-hybrid-ai-platform-2025-09.md, sources/genon-kogas-ai-platform-press-2025-09.md]
related_usecases:
  - korea-electric-power-hr-bot
  - mirae-asset-ai-assistant-platform
  - hyundai-mobis-moai-platform
related_vendors: []
---

## Summary

한국가스공사가 국내 에너지 공공기관 최초 **하이브리드 생성형 AI 플랫폼** 구축 발표 (2025-09-10). **내부망 전용 'KOGAS형 LLM' (민감 자료) + 챗GPT 등 민간 상용 LLM (전문지식)** 을 사용자가 직접 선택. 규정 검토·문서 초안 등 단순 반복 업무 자동화 목표. [[sources/energykorea-kogas-hybrid-ai-platform-2025-09.md]] ⚠️ 벤더 주장: 제논(GenON) 구축 사업 수주. [[sources/genon-kogas-ai-platform-press-2025-09.md]] 한국 공공기관 보안 vs 성능 trade-off 해법 패턴.

## Problem / Why (도입 배경)

- **Before**: ✅ 규정 검토·문서 초안 작성 등 단순 반복 업무를 직원이 직접 처리. [[sources/energykorea-kogas-hybrid-ai-platform-2025-09.md]] (직원 규모 수치 _미공개_ — 근거 미확보, 2026-09-27 grounding 점검)
- **Pain point**: ✅ 임직원이 필요한 정보를 더 쉽게 찾고, 반복 업무는 자동화하며, 보안은 강화 — 민감 내부 자료는 사내 전용 AI, 전문 지식은 외부 AI. [[sources/energykorea-kogas-hybrid-ai-platform-2025-09.md]]
- **Trigger**: ✅ 정부 '세계 1위 AI 정부 실현' 국정과제 (최연혜 사장 발언). [[sources/energykorea-kogas-hybrid-ai-platform-2025-09.md]] 발주·수주 일정 세부 _미공개_

## Solution Architecture

### A. Process (프로세스)

- **Before**: ✅ 규정 검토·문서 초안 작성을 직원이 직접 수행. [[sources/energykorea-kogas-hybrid-ai-platform-2025-09.md]]
- **After** (2025-09 시점 "구축한다" 발표 — 계획형):
  1. ✅ 사용자가 필요에 따라 AI 모델을 직접 선택. [[sources/energykorea-kogas-hybrid-ai-platform-2025-09.md]]
  2. ✅ 민감한 내부 자료 → 보안 강화된 사내 전용 AI('KOGAS형 LLM', 내부 업무망 전용). [[sources/energykorea-kogas-hybrid-ai-platform-2025-09.md]]
  3. ✅ 최신 기술 논문·전문 지식 → 외부 AI(챗GPT 같은 민간 상용 LLM). [[sources/energykorea-kogas-hybrid-ai-platform-2025-09.md]]
  4. ✅ 규정 검토·문서 초안 등 단순 반복 업무를 AI가 대신 처리. [[sources/energykorea-kogas-hybrid-ai-platform-2025-09.md]]
- **HITL**: ✅ 사용자가 모델을 직접 선택 (자동 분류 아님). [[sources/energykorea-kogas-hybrid-ai-platform-2025-09.md]] 검토·승인 절차 _미공개_

### B. System

- **사내 LLM**: ✅ 내부 업무망 전용 'KOGAS형 LLM' — 모델·vendor _미공개_. [[sources/energykorea-kogas-hybrid-ai-platform-2025-09.md]]
- **상용 LLM**: ✅ 챗GPT 같은 민간 상용 초거대 LLM 연동 — 구체 벤더 목록 _미공개_. [[sources/energykorea-kogas-hybrid-ai-platform-2025-09.md]]
- **구축사**: ⚠️ 벤더 주장: 제논(GenON) 구축 사업 수주 — 원문 미확보(404), 검색 스니펫 기반. [[sources/genon-kogas-ai-platform-press-2025-09.md]]

### C/D. Data & Model

- **데이터**: ✅ 민감한 내부 자료(사내 AI) + 최신 논문·전문 지식(외부 AI). [[sources/energykorea-kogas-hybrid-ai-platform-2025-09.md]] 규모·전처리 _미공개_
- **모델**: ✅ 사내 LLM + 상용 LLM 하이브리드 (사용자 선택). [[sources/energykorea-kogas-hybrid-ai-platform-2025-09.md]] 모델명·버전 _미공개_

### E. Organization

- **오너십**: _미공개 (not disclosed)_ — ⚠️ 벤더 주장: 구축 파트너 제논(GenON). [[sources/genon-kogas-ai-platform-press-2025-09.md]]

## Impact / Metrics (기대효과)

### 기대효과 요약
한국 공공기관 보안 + 성능 trade-off 해법 — 사내 + 상용 LLM 라우팅 표준 패턴.

- ✅ 국내 에너지 공공기관 최초 하이브리드 AI 플랫폼 (2025-09-10 발표, 구축 예정). [[sources/energykorea-kogas-hybrid-ai-platform-2025-09.md]]
- ⚠️ 벤더 주장: GenON 구축 사업 수주 (2025-09) — 원문 미확보. [[sources/genon-kogas-ai-platform-press-2025-09.md]]
- 구축 완료·오픈 시점: _미공개_ (인용 소스에 없음)
- ⚠️ 기대효과 수치 미공개

## Consulting Angle

- **KR 공공·에너지 reference**:
  - 한국전력 [[korea-electric-power-hr-bot]] (솔트룩스 단일 플랫폼)
  - 가스공사 (GenON 하이브리드)
  - 도로공사·국민연금공단·한국조폐 등 비교
- **하이브리드 패턴**: 보안 민감 KR 그룹사 (반도체·바이오·국방) reference
- **반면교사**: vendor 의존 + 라우팅 정책 quality 검증 필요
