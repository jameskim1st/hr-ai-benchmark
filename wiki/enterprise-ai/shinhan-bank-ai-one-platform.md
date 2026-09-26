---
title: "신한은행 — 'AI ONE' 직원 업무비서 플랫폼"
slug: shinhan-bank-ai-one-platform
page_type: enterprise-ai
moved_from_usecases: 2026-09-27
primary_category: Employee Experience & HR Ops
subcategory: Employee Self-service
tags: [shinhan-bank, ai-one, employee-assistant, ai-studio, ai-ocr, korean-bank, multi-agent-hub, speech-to-ai, mobile, korea]
company: 신한은행
industry: [finance, banking]
region: [kr]
employee_class: [all]
vendor: [신한은행 internal]
vendor_type: [internal-build]
output: "AI ONE 단일 인터페이스의 40여 가지 업무비서 결과 (업무지식 검색·시장지표·마케팅 타겟리스트·대출 서류 발송·일정 대시보드; AI-STUDIO·AI-OCR·R비서 RPA) + Speech to AI 음성 지시 처리. ⚠️ 자사 보고: 1인당 일 30분 이상 절감 기대, 상담→전산처리 80% 자동화 목표"
ai_tech_type: [generative, recognition]
ai_tech_subtype: [summarization-qa, ocr, speech-recognition]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: []
frequency: daily
first_seen: 2024-09-24
last_confirmed: 2026-04-01
confidence: 0.8
evidence_grade: A
corroborated_by: 3
freshness: fresh
depth: stub
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/etnews-shinhan-bank-ai-one-2024-09.md, sources/incheontoday-shinhan-bank-ai-one-2024-09.md, sources/moneys-shinhan-bank-ai-personnel-2021-01.md]
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

- **Before**: ✅ 기존 업무지원시스템 'A.I 몰리' 운영. [[sources/etnews-shinhan-bank-ai-one-2024-09.md]] (직원 규모 수치 _미공개_ — 근거 미확보, 2026-09-27 grounding 점검)
- **Pain point**: ✅ AI-STUDIO·AI-OCR·R비서 등 다양한 AI 서비스를 한 곳에서 이용하도록 '사용 편의성' 개선. [[sources/etnews-shinhan-bank-ai-one-2024-09.md]]
- **Trigger**: ✅ 2024-09 A.I 몰리 개편 → AI ONE 도입 — 단일 인터페이스 + 휴대용 기기 음성 지시. [[sources/incheontoday-shinhan-bank-ai-one-2024-09.md]]

## Solution Architecture

### A. Process (프로세스)

- **Before**: ✅ 기존 업무지원시스템 'A.I 몰리'. [[sources/etnews-shinhan-bank-ai-one-2024-09.md]]
- **After**:
  1. ✅ 직원이 AI ONE에서 AI-STUDIO·AI-OCR·R비서 등 다양한 AI 서비스를 한 곳에서 이용. [[sources/etnews-shinhan-bank-ai-one-2024-09.md]]
  2. ✅ 업무지식 검색·주요 시장지표 확인·마케팅 타겟리스트 작성·대출 사전/사후 서류 발송·일정 및 업무 관리 대시보드 등 40여 가지 업무비서 기능. [[sources/etnews-shinhan-bank-ai-one-2024-09.md]]
  3. ✅ R비서 = RPA 로봇 — 중앙집중형 '알파봇' + 개별 PC '마이봇'. [[sources/incheontoday-shinhan-bank-ai-one-2024-09.md]]
  4. ✅ 스마트폰·태블릿에서 음성인식으로 업무 지시하는 'Speech to AI'. [[sources/incheontoday-shinhan-bank-ai-one-2024-09.md]]
  5. ⚠️ 자사 보고: 향후 '고객 상담부터 전산처리 종결' 업무 전 과정의 80% 수준까지 자동화 지원 확대 계획. [[sources/etnews-shinhan-bank-ai-one-2024-09.md]]
- **HITL**: _미공개 (not disclosed)_
- **Frequency**: _미공개 (not disclosed)_

### B. System

- **AI 시스템 배치**: ✅ 기존 'A.I 몰리' 개편 — AI-STUDIO·AI-OCR·R비서(RPA) 통합. [[sources/etnews-shinhan-bank-ai-one-2024-09.md]] 자체 구축 여부·LLM 스택 _미공개_
- **사용자 접점**: ✅ 스마트폰·태블릿 등 휴대용 기기 음성 지시(Speech to AI). [[sources/incheontoday-shinhan-bank-ai-one-2024-09.md]]
- **인증·권한·이용자 규모**: _미공개 (not disclosed)_ (직원 수 근거 미확보 — 2026-09-27 grounding 점검)

### C/D. Data & Model

- **Foundation model**: _미공개 (not disclosed)_
- **데이터**: ✅ 업무지식·시장지표·마케팅 타겟리스트·대출 서류 등 업무 데이터. [[sources/etnews-shinhan-bank-ai-one-2024-09.md]] 세부 _미공개_
- **거버넌스**: _미공개 (not disclosed)_

### E. Organization

- **오너십**: _미공개 (not disclosed)_
- ✅ 별건: 2021 상반기 인사에 'AI 최적해 알고리즘' 적용 (직원 업무 숙련도·영업점 직무 데이터), 과장급 승진자 여성 비중 42% — AI ONE과는 별개 사례. [[sources/moneys-shinhan-bank-ai-personnel-2021-01.md]]

## Impact / Metrics (기대효과)

### 기대효과 요약
40+ AI 통합 단일 허브로 직원 daily 30분 절감 + 상담→전산처리 80% 자동화 목표.

- ⚠️ 자사 보고: [[sources/etnews-shinhan-bank-ai-one-2024-09.md]] [[sources/incheontoday-shinhan-bank-ai-one-2024-09.md]]
  - 직원 1인당 일 30분 이상 절감 기대 (기대치)
  - 상담→전산처리 종결 업무 80% 자동화 목표 (향후 계획)
  - 40여 가지 업무비서 기능 통합

## Governance & Risk

- ✅ 금융권 자체 구축 — 데이터 주권·금융정보보호 강력
- ⚠️ 30분 절감은 ⚠️ 자사 보고 + 기대치 — 실측 _미공개_
- ⚠️ Speech-to-AI 개인정보 처리 PIPA 준수 검증 필요
- ⚠️ 한국 AI 기본법 (2026-01-22) 고영향 AI 분류 가능성 (인사 의사결정 영향 시)

## Consulting Angle

- **KR 금융권 사내 AI 플랫폼 reference (Top 3)**:
  - 신한 AI ONE + KB AI [[kb-bank-ai-hr-deep-change]] + 하나 하나은행 지식챗봇 (페이지 없음) — 한국 4대 은행 자체 플랫폼 비교
  - JPMorgan LLM Suite [[jpmorgan-llm-suite-redeployment]] 글로벌 reference와 pair
- **40+ AI 통합 모델**: 한국 대기업 (KB·신한·우리·하나·미래에셋 + 제조 그룹사)이 산발 AI 통합 갈증 큼 — AI ONE 패턴 직접 차용 가능
- **Speech-to-AI 모바일 차별점**: 한국 대기업 외근·영업·매장 직원에게 매력적 차별화 — 데스크 외 작업 환경 fit
- **2026 Q3-Q4 KR 금융 컨설팅 deck**:
  - "단일 통합 vs 산발 AI" 슬라이드에 신한 AI ONE = best practice
  - 30분 절감 × 직원 수 × 근무일로 표면적 ROI 계산 가능 — 단, 신한은행 직원 수는 인용 소스에 없으므로 클라이언트 제안 시 공시 자료로 별도 확인 (2026-09-27 grounding 점검: 종전 계산식의 직원 수·인-일 수치 제거)
- **반면교사**:
  - "30분 절감"은 자사 기대치 — 외부 reference로 사용 시 "신한 자체 기대치" 명시 필수
  - 80% 자동화 목표는 단계적 — 일시적 layoff risk는 한국 노동법 컨텍스트에서 회피 권장
- **국가핵심기술 보유 KR 그룹사**: 자체 LLM 활용 패턴 — SK 그룹 'A.X' [[sk-group-aibiz-25-companies]]와 비교
