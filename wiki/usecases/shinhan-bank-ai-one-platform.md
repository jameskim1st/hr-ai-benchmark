---
title: "신한은행 — 'AI ONE' 직원 업무비서 플랫폼"
slug: shinhan-bank-ai-one-platform
primary_category: Employee Experience & HR Ops
subcategory: Employee Self-service
tags: [shinhan-bank, ai-one, employee-assistant, ai-studio, ai-ocr, korean-bank, multi-agent-hub, speech-to-ai, mobile, korea]
company: 신한은행
industry: [finance, banking]
region: [kr]
employee_class: [all]
vendor: [신한은행 internal]
vendor_type: [internal-build]
output: "14,000+ 직원의 단일 AI ONE 인터페이스 출력 — 40+ 업무비서 task 결과 (AI-STUDIO·AI-OCR·R비서) + Speech-to-AI 음성 응답. ⚠️ 자사 보고: 1인당 일 30분+ 절감, 향후 상담→전산처리 80% 자동화 목표"
ai_tech_type: [generative, recognition]
ai_tech_subtype: [summarization-qa, ocr, speech-recognition]
stage: production
frequency: daily
first_seen: 2024-09-24
last_confirmed: 2026-04-01
confidence: 0.50
consulting_angle_status: filled
sources:
  - sources/korea-conglomerate-hr-ai-2025-2026.md
related_usecases:
  - kb-bank-ai-hr-deep-change
  - hana-bank-knowledge-chatbot
  - mirae-asset-ai-assistant-platform
  - jpmorgan-llm-suite-redeployment
related_vendors: []
---

## Summary

신한은행 **AI ONE** — 기존 'A.I 몰리' 시스템을 통합 개편한 직원용 멀티-AI 허브 (2024-09 production). AI-STUDIO·AI-OCR·R비서 등 **40여 개 업무비서** 기능을 단일 인터페이스에 통합. **Speech-to-AI**로 모바일/태블릿 음성 지시 지원. ⚠️ 자사 보고: 직원 1인당 일 30분 이상 절감 기대, 향후 상담→전산처리 종결 업무의 **80%까지 자동화 목표**.

## Problem / Why (도입 배경)

- **Before**: 신한은행 직원이 다수의 산발 AI 도구 (A.I 몰리·OCR·R비서) 별도 사용 — UX 분산
- **Pain point**: 14,000+ 직원 base에서 AI 도구 fragmentation으로 ROI 약화
- **Trigger**: 2024-09 통합 launch — 단일 인터페이스 + 모바일·태블릿 음성 지원

## Solution Architecture

### A. Process (프로세스)

- **Before**: A.I 몰리 + AI-OCR + R비서 등 산발 사용
- **After**:
  1. 직원이 AI ONE 단일 인터페이스 접속
  2. 40+ 업무비서 중 task 선택 (또는 음성 지시)
  3. AI-STUDIO (분석)·AI-OCR (문서 인식)·R비서 (자동화) 통합 호출
  4. 모바일·태블릿 Speech-to-AI 지원
  5. 향후 상담 → 전산처리 종결 80% 자동화 목표
- **HITL**: 직원이 결과 검토·승인. 고객 응대 자동 종결은 단계적 확장
- **Frequency**: daily

### B. System

- 신한은행 자체 구축 (한국 자체 LLM·AI 스택 추정)
- 모바일·태블릿 통합 — Speech-to-AI front-end
- 14,000+ 직원 SSO

### C/D. Data & Model

- **Foundation model**: 자체 + 외부 partner 혼합 (구체 _미공개_)
- **데이터**: 사내 정책·매뉴얼·업무 처리 로그
- **거버넌스**: 금융정보보호 강화

### E. Organization

- 신한은행 디지털혁신단 + IT/AI Plat팀 + 사업부 SME

## Impact / Metrics (기대효과)

### 기대효과 요약
40+ AI 통합 단일 허브로 직원 daily 30분 절감 + 상담→전산처리 80% 자동화 목표.

- ⚠️ 자사 보고:
  - 직원 1인당 일 30분 이상 절감 기대
  - 상담→전산처리 종결 업무 80% 자동화 목표 (향후)
  - 40+ AI 비서 통합

## Governance & Risk

- ✅ 금융권 자체 구축 — 데이터 주권·금융정보보호 강력
- ⚠️ 30분 절감은 ⚠️ 자사 보고 + 기대치 — 실측 _미공개_
- ⚠️ Speech-to-AI 개인정보 처리 PIPA 준수 검증 필요
- ⚠️ 한국 AI 기본법 (2026-01-22) 고영향 AI 분류 가능성 (인사 의사결정 영향 시)

## Consulting Angle

- **KR 금융권 사내 AI 플랫폼 reference (Top 3)**:
  - 신한 AI ONE + KB AI [[kb-bank-ai-hr-deep-change]] + 하나 [[hana-bank-knowledge-chatbot]] — 한국 4대 은행 자체 플랫폼 비교
  - JPMorgan LLM Suite [[jpmorgan-llm-suite-redeployment]] 글로벌 reference와 pair
- **40+ AI 통합 모델**: 한국 대기업 (KB·신한·우리·하나·미래에셋 + 제조 그룹사)이 산발 AI 통합 갈증 큼 — AI ONE 패턴 직접 차용 가능
- **Speech-to-AI 모바일 차별점**: 한국 대기업 외근·영업·매장 직원에게 매력적 차별화 — 데스크 외 작업 환경 fit
- **2026 Q3-Q4 KR 금융 컨설팅 deck**:
  - "단일 통합 vs 산발 AI" 슬라이드에 신한 AI ONE = best practice
  - 30분 절감 × 14,000 직원 × 250일 = 연 ~17,500 인-일 → 표면적 ROI 계산
- **반면교사**:
  - "30분 절감"은 자사 추정 — 외부 reference로 사용 시 "신한 자체 추정" 명시 필수
  - 80% 자동화 목표는 단계적 — 일시적 layoff risk는 한국 노동법 컨텍스트에서 회피 권장
- **국가핵심기술 보유 KR 그룹사**: 자체 LLM 활용 패턴 — SK 그룹 'A.X' [[sk-group-aibiz-25-companies]]와 비교
