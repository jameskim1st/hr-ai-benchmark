---
title: "SK하이닉스 — A!SK (AI Interview with SK Hynix) AI 영상면접 + 미래 동료 평가 hybrid (2025 신규)"
slug: sk-hynix-ask-ai-interview
primary_category: Talent Acquisition
subcategory: Interview & Selection
tags: [sk-hynix, ask-ai-interview, video-interview, hybrid-evaluation, peer-evaluation, semiconductor, korean-recruitment, korea, early-career]
company: SK하이닉스
industry: [semiconductor]
region: [kr]
employee_class: [기술사무직, 신입]
vendor: [SK하이닉스 internal]
vendor_type: [internal-build]
stage: production
frequency: annual
first_seen: 2025-09-16
last_confirmed: 2026-04-01
confidence: 0.45
consulting_angle_status: filled
sources:
  - sources/korea-conglomerate-hr-ai-2025-2026.md
related_usecases:
  - sk-cc-adot-biz-hr-recruitment
  - sk-group-aibiz-25-companies
  - midas-inair-ai-assessment-korea
related_vendors: []
---

## Summary

SK하이닉스가 2025 하반기 신입 채용에 **'A!SK' (AI Interview with SK Hynix)** 전형 신설. AI가 직무별 특화 문제를 출제하면 지원자가 영상 녹화 답변 제출. 자기소개서로 파악 어려운 **커뮤니케이션·팀워크·상황 대처** 능력을 종합 검증. 제출 영상은 **미래 동료 구성원이 직접 평가**하는 **hybrid 모델**. AI single decision 회피 — bias mitigation + 한국 채용절차법 fit.

## Problem / Why

- **Before**: SK하이닉스 신입 채용은 자기소개서 + 인적성 + 면접 — 직무 적합 soft skill (커뮤니케이션·팀워크) 측정 어려움
- **Pain point**: 반도체 기술사무직 신입 채용 volume 크지만 면접관 시간 한정 + soft skill 평가 표준화 어려움
- **Trigger**: 2025 하반기 신입 공채 — A!SK 전형 신설 (마이다스 inAIR 차별 논란 후 자체 hybrid 설계)

## Solution Architecture

### A. Process

- **Before**: 자기소개서 → 인적성 → 면접관 in-person 면접
- **After**:
  1. AI가 직무별 특화 문제 자동 출제
  2. 지원자가 영상 녹화 답변 제출 (시간·장소 자율)
  3. 영상 → AI 1차 분석 (응답 내용 위주, 표정·외모 신호 사용 여부 _미공개_)
  4. **미래 동료 구성원이 영상 직접 평가** (peer review)
  5. AI score + peer evaluation → HR 종합 판단
  6. 다음 단계 (in-person 면접) 진행
- **HITL**: 미래 동료가 영상 평가 + HR 종합 판단 — AI single decision 회피
- **Frequency**: annual (신입 공채)
- **Scope**: AI screening + peer evaluation hybrid

### B/C/D. System

- 영상 면접 platform (자체 또는 vendor _미공개_)
- AI 분석 모델 (구체 _미공개_)
- 미래 동료 peer review interface

### E. Organization

- SK하이닉스 인사 + 미래 동료 (현업) + AI/IT

## Impact / Metrics

### 기대효과 요약
AI single decision 회피 + 미래 동료 평가로 bias mitigation. 한국 채용절차법 + AI 기본법 (2026-01-22) 인적감독 의무 자동 충족 model.

- 2025 하반기 신입 채용 launch
- ⚠️ 자사 보고: standalone metric _미공개_ (launch 직후)

## Governance & Risk

- ✅ **AI single decision 회피** — 미래 동료 peer review + HR 종합 — 한국 AI 기본법 인적감독 의무 best practice
- ✅ peer review로 직무 fit 정량 신호 추가
- ⚠️ AI 영상 분석의 표정·억양·외모 신호 사용 여부 _미공개_ — 마이다스 inAIR 차별 논란 trigger와 같은 카테고리
- ⚠️ 미래 동료 peer review의 본인 편향 (학교·전공·외모) 동반 가능 — 별도 mitigation 필요
- ⚠️ 영상 녹화 시 시간·장소 자율은 socioeconomic gap 가능 (장비·환경)

## Consulting Angle

- **KR 대기업 채용 AI hybrid model reference (1순위)**:
  - 마이다스 inAIR (vendor single AI) vs SK C&C [[sk-cc-adot-biz-hr-recruitment]] (자체 single AI) vs SK하이닉스 (자체 hybrid AI + peer)
  - **hybrid model이 한국 AI 기본법 + 채용절차법 fit 가장 우수**
- **2026 Q3-Q4 KR 채용 컨설팅 deck**:
  - "AI single decision의 위험" → "AI + peer hybrid의 mitigation" 슬라이드 핵심 reference
  - 글로벌 IBM Watson Recruitment [[ibm-watson-recruitment]] (protected attribute suppression) + SK하이닉스 (hybrid) — bias mitigation 2가지 접근법
- **한국 채용 시즌 적용**: 한국 대졸 정기공채 (3월·9월) 시즌 AI 영상면접 + peer review 도입 reference
- **반면교사**:
  - peer review의 본인 편향 — 평가자 bias training + protected attribute 비공개 권장
  - 영상 녹화의 socioeconomic gap (조용한 공간·고품질 카메라 access) — 학교·공공도서관 등 무료 녹화 booth 옵션 권장
  - AI 영상 분석에 표정·외모 신호 사용 여부 transparency — 한국 채용절차법 가이드라인 정합성 검증
- **글로벌 비교**: HireVue·Pymetrics 표정·억양 신호 사용 → US/EU 차별 소송 history → SK하이닉스 hybrid 설계가 risk 회피 우위
