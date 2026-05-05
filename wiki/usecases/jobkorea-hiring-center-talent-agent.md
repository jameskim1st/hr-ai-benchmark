---
title: "잡코리아 — '하이어링 센터' 통합 채용 솔루션 + 탤런트 에이전트"
slug: jobkorea-hiring-center-talent-agent
primary_category: Talent Acquisition
subcategory: Sourcing & Attraction
tags: [jobkorea, workspher, hiring-center, talent-agent, conversational-ai, ats, korean-vendor, korea, recruiter-agent, market-survey]
company: 잡코리아 (웍스피어)
industry: [it-services, hr-tech]
region: [kr]
employee_class: [all]
vendor: [잡코리아, 웍스피어]
vendor_type: [ats, point-solution]
output: "채용 담당자 자연어 의도 입력에 대한 후보자 매칭 추천 리스트 + 추천 사유 (잡코리아 후보자 DB·공고 맥락 기반)"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [summarization-qa, recommendation-ranking]
stage: production
frequency: daily
first_seen: 2026-03-31
last_confirmed: 2026-04-01
confidence: 0.45
consulting_angle_status: filled
sources:
  - sources/korea-conglomerate-hr-ai-2025-2026.md
related_usecases:
  - wantedlab-ai-recruiting-agent
  - sk-cc-adot-biz-hr-recruitment
  - midas-inair-ai-assessment-korea
  - ibm-watsonx-orchestrate-ta-agent
related_vendors: []
---

## Summary

잡코리아 운영사 **웍스피어**가 출시한 **통합 채용 솔루션 '하이어링 센터'** (2026-03 일부 기업 오픈). 자연어 대화로 채용 담당자 의도를 이해하고 공고 맥락 분석 후 후보자 제안하는 **'탤런트 에이전트'** 탑재. 잡코리아 자체 설문 — 채용 담당자 1,286명 중 **65%가 AI 채용 에이전트 도입 또는 검토 중** (적극 검토 13.6% + 검토 48.8%).

## Problem / Why

- **Before**: 잡코리아 채용 담당자는 공고 작성·후보자 search·매칭을 별도 도구·매뉴얼 process
- **Pain point**: 한국 채용 시장 vendor 경쟁 (사람인·잡코리아·원티드) — 차별화 압박
- **Trigger**: 2025-10 [[wantedlab-ai-recruiting-agent]] launch + 잡코리아 시장 점유 방어

## Solution Architecture

### A. Process

- **Before**: 채용 담당자가 잡코리아에 공고 게시 → 지원자 manual review → 후보자 추천 받음
- **After**:
  1. 채용 담당자가 탤런트 에이전트에 자연어로 의도 입력 ("Python backend 시니어 + 핀테크 경력 + 서울")
  2. 에이전트가 공고 맥락 분석 → 후보자 매칭 + 추천 사유
  3. 채용 담당자가 후보자 contact·면접 진행
  4. 통합 채용 솔루션으로 ATS 기능 흡수
- **HITL**: 채용 담당자 최종 결정
- **Frequency**: daily

### B/C/D/E. System

- 웍스피어 자체 구축
- 잡코리아 데이터베이스 + 자체 LLM 또는 외부 API
- 한국어 specialized

### B. System & Infrastructure (R9 research)

- **Core HRIS**: ✅ 잡코리아 ATS '하이어링 센터' (웍스피어 자체)
- **AI 시스템 배치**: '탤런트 에이전트' — 하이어링 센터 내장 conversational agent
- **배포 환경**: _미공개_ — 한국 데이터센터 추정
- **연동·통합**: 잡코리아 후보자 DB, 공고 데이터, 지원·이력 history
- **사용자 접점**: 채용 담당자 web UI — 자연어 chat
- **인증·권한**: 잡코리아 기업회원 계정

### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 잡코리아 후보자 DB, 공고 텍스트, 채용 담당자 의도
- **데이터 규모**: _미공개_ — 잡코리아 누적 회원 비공개
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_ — 매칭 retrieval + LLM ranking 추정
- **데이터 거버넌스**: ⚠️ KR PIPA — 후보자 동의 (잡코리아 약관 의존)
- **민감정보 처리**: ⚠️ 차별 표현 자동 필터 _미검증_ — explainability 미공개

### D. Model (R9 research)

- **Foundation model**: _미공개_ — 자체 LLM 또는 외부 API (OpenAI·Hyperclova X) 추정
- **모델 유형**: LLM (conversational matching) + recommendation
- **제공 방식**: _미공개_
- **커스터마이징 기법**: ⚠️ 자사 보고: 한국어 specialized
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: _미공개_


## Impact / Metrics

### 기대효과 요약
한국 ATS·채용 vendor 경쟁의 AI agent 차별화 + 시장 데이터 (65% 도입·검토)로 KR 채용 vendor 시장 기회 입증.

- 2026-03 일부 기업 오픈
- 잡코리아 자체 설문: 채용 담당자 1,286명 중 65%가 AI 채용 에이전트 도입·검토
  - 적극 검토 13.6%
  - 검토 48.8%

## Governance & Risk

- ⚠️ 자연어 매칭의 한국어 직무·전문 용어 fit 검증 필요
- ⚠️ "탤런트 에이전트" 후보자 추천의 차별 표현 자동 필터 _미검증_
- ⚠️ 한국 AI 기본법 + 채용절차법 정합성 — 채용 vendor의 의무 명확화 필요

## Consulting Angle

- **KR 채용 시장 vendor 경쟁 reference**:
  - 잡코리아 '하이어링 센터' (2026-03) + 원티드 [[wantedlab-ai-recruiting-agent]] (2025-10) + 사람인 '커리어 매칭 에이전트' (2026 출시 예정) — 한국 ATS·채용 vendor 3사 AI agent 경쟁 본격화
  - 글로벌 Eightfold AI Interviewer + IBM watsonx Orchestrate TA Agent [[ibm-watsonx-orchestrate-ta-agent]]와 비교
- **시장 데이터 인용**: 채용 담당자 65% AI agent 도입·검토 — KR 컨설팅 deck "burning platform" 데이터
- **2026 Q3-Q4 KR 컨설팅 deck — "한국 채용 시장의 AI agent 경쟁"**:
  - vendor 3사 비교 + 글로벌 leader (Eightfold·IBM watsonx) — KR 대기업 RFP 시 vendor selection framework
- **반면교사**:
  - 자체 설문 65% — 마케팅 motivation 강함, 외부 인용 시 "잡코리아 자체 설문" 명시
  - 자연어 매칭의 한국어 직무·specialized term fit POC 4주 권장
  - 탤런트 에이전트 추천 사유의 explainability — 차별 사후 검증 가능 설계 필수
- **잡코리아 vs 사람인 vs 원티드 비교**: 본 wiki의 [[talent-acquisition-6-vendor-comparison]] 한국 채용 vendor 섹션 추가·갱신 권장
