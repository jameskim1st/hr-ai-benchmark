---
title: "SK C&C — '에이닷 비즈 HR' 전사 채용 도입 (자기소개서 분석 1주→4시간, ⚠️ 자사 보고 90% 단축)"
slug: sk-cc-adot-biz-hr-recruitment
primary_category: Talent Acquisition
subcategory: Screening & Assessment
tags: [sk-cc, adot-biz, sktelecom, sk-ax, recruitment-ai, jd-keyword-extraction, ai-interview-questions, korean-recruitment, korea, hr-screening]
company: SK C&C
industry: [it-services, telecom]
region: [kr]
employee_class: [기술사무직, 신입]
vendor: [SKT, SK AX]
vendor_type: [internal-build]
stage: production
frequency: annual
first_seen: 2025-02-20
last_confirmed: 2026-04-01
confidence: 0.50
consulting_angle_status: filled
sources:
  - sources/korea-conglomerate-hr-ai-2025-2026.md
related_usecases:
  - sk-group-aibiz-25-companies
  - sk-hynix-ask-ai-interview
  - sk-group-aict-ai-recruitment
  - midas-inair-ai-assessment-korea
related_vendors: []
---

## Summary

SK C&C가 SKT·SK AX 합작 'A.Biz' B2B AI 솔루션의 첫 제품 **'에이닷 비즈 HR'**을 2025년 신입·주니어 채용에 전면 적용. 자기소개서에서 **경력·핵심 역량 키워드 추출** + **직무 적합성·리스크 요인 판정**. AI 면접 + 맞춤 면접 질문 자동 생성. ⚠️ 자사 보고: 수천 건 지원서를 4시간 내 분석 (이전 약 1주 소요 → **약 90% 단축**).

## Problem / Why

- **Before**: SK C&C 신입·주니어 채용 시 수천 건 지원서 review에 HR + 사업부 SME 다수 인력 1주 투입
- **Pain point**: 한국 대졸 정기공채 (3월·9월) 시즌 압박 + 직무 적합성 판단 표준화 어려움
- **Trigger**: 2025년 SKT-SK AX 'A.Biz' 합작 launch + 신입 공채 시즌 적용

## Solution Architecture

### A. Process

- **Before**: 1) 수천 건 자기소개서 manual review (1주) / 2) 적합성 판정 reviewer 별 편차 / 3) 면접 질문 면접관 별 ad-hoc
- **After**:
  1. 자기소개서 input → A.Biz HR이 키워드 추출 (경력·핵심 역량)
  2. 직무 적합성 + 리스크 요인 score
  3. 4시간 내 결과 (수천 건)
  4. AI 면접 (영상 응답 분석) + 맞춤 면접 질문 자동 생성
  5. HR + 사업부 SME 검토·면접
- **HITL**: HR + 사업부 SME가 score 검토·면접 진행
- **Frequency**: annual cycle (신입 공채)
- **Scope**: AI score → 사람 결정

### B/C/D. System

- SK AX 산업특화 AI + SKT 자체 LLM 'A.X' 추정 (구체 _미공개_)
- 사내 ATS 통합
- AI 모델: 자체 LLM + RAG (직무·SK culture 코퍼스)

### E. Organization

- SK C&C 인사 + SKT A.Biz 팀 + SK AX

## Impact / Metrics

### 기대효과 요약
자기소개서 분석 1주 → 4시간 (90% 단축, ⚠️ 자사 보고). 한국 대졸 공채 시즌 HR 부담 대폭 경감 reference.

- ⚠️ 자사 보고:
  - 자기소개서 분석: 1주 → 4시간
  - 90% 시간 단축
  - 신입·주니어 채용 전면 적용

## Governance & Risk

- ⚠️ "리스크 요인 판정"의 차별 표현(성별·학력·출신) 자동 필터 _미검증_
- ⚠️ 한국 AI 기본법 (2026-01-22) 고영향 AI 명확 분류 — 인적감독 의무 자동 충족 검증 필요
- ⚠️ 마이다스 inAIR 차별 논란 (2020) trigger와 동일 카테고리 — bias mitigation 설계 reference 필수
- ⚠️ AI 면접 영상 분석의 표정·억양·외모 신호 사용 여부 _미공개_

## Consulting Angle

- **KR 대기업 채용 AI reference (Top 5)**:
  - 마이다스 inAIR [[midas-inair-ai-assessment-korea]] (1,200+ 기업, vendor 모델) vs SK C&C 자체 (그룹 표준화 모델) 비교
  - SK 그룹 25개사 'A.Biz' 확산 [[sk-group-aibiz-25-companies]]과 pair
  - 90% 시간 단축은 강력한 ROI hook
- **2026 Q3-Q4 KR 채용 AI 컨설팅**:
  - 한국 대졸 공채 시즌 (3월·9월) HR 부담 솔루션
  - "vendor 도입 vs 자체 구축" 결정 framework — SK는 그룹 자체 LLM (A.X) 강점
- **AI 면접 분석**: SK하이닉스 A!SK [[sk-hynix-ask-ai-interview]]와 비교 — 동일 SK 그룹 내 vendor (자체) vs hybrid (미래 동료 평가)
- **반면교사**:
  - 마이다스 inAIR 차별 논란 trigger와 같은 카테고리 — bias 사후 검증·명시적 protected attribute 필터·인적감독 설계 필수
  - "리스크 요인" 자동 판정의 explainability — 한국 채용절차법·AI 기본법 정합성 검증
  - AI 면접 영상 분석은 표정·억양 신호 사용 시 차별 risk — text·response 내용 위주 권장
- **글로벌 비교**: IBM Watson Recruitment [[ibm-watson-recruitment]] (protected attribute suppression) vs SK C&C — bias mitigation 명시 vs 미명시 격차
