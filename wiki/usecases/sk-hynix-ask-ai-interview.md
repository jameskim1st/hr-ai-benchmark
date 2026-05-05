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
ai_tech_type: [generative, predictive]
ai_tech_subtype: [text-generation, clustering-classification]
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

### A. Process — 7-Phase 통합 채용 플로우 (PwC 자료 기반)

- **Before**: 자기소개서 → 인적성 → 면접관 in-person 면접 (1시간×2회). 평가 깊이 한계 + 평가자 주관 편차 + 이천 출장 비용
- **After (7 phases)**:
  1. **서류 + AI 종합 역량 Report (Phase 1)**: 학력·전공·직무 연관성 검토 → AI가 정량·정성 역량 점수화 + 직무역량-JD 매칭율 → 면접관 참고 Report 자동 생성
  2. **SKCT (인적성 검사)**: 온라인 역량 검사
  3. **A!SK 전형 (AI 화상 면접)**:
     - AI 인프라 기반 화상 면접 — 문제은행식 직무별 맞춤 출제
     - 지원자가 원하는 시간·장소에서 영상 녹화 제출
     - AI 면접 학습 데이터 수집 → 대면 면접 결과와 교차 검증으로 정합성 향상
     - (향후 고도화) AI 상호작용 적응형 질문 + STT 기반 실시간 평가 요약
  4. **다면 평가 (O/I 고도화)**: 업로드 영상을 **현업 미래 동료 구성원**이 평가 — 평가자 규모 확대 → 다차수 면접 효과 (1시간 → Big Tech 수준 2시간+ 평가 깊이)
  5. **AI 종합 역량 Report 완성 (Phase 2)**: 전 단계 결과 통합 (서류 + SKCT + AI 면접) + 석·박사 대상 Lab·논문 분석 + LinkedIn 코멘트 자동 크롤링 (고도화) → 대면 면접관 종합 Report
  6. **최종 대면 면접**: AI 종합 역량 Report 기반 심층 면접
  7. **최종 합격**
- **HITL**: 미래 동료가 영상 평가 + HR 종합 판단 + 대면 면접관 최종 결정 — AI single decision 회피
- **Frequency**: annual (신입 공채 — 2025 하반기 launch)
- **Scope**: AI screening + peer evaluation + AI Report support → 사람 결정

### B/C/D. System

- 영상 면접 platform (자체 또는 vendor _미공개_)
- AI 분석 모델 (구체 _미공개_)
- 미래 동료 peer review interface

### E. Organization

- SK하이닉스 인사 + 미래 동료 (현업) + AI/IT

### B. System & Infrastructure (R9 research)

- **Core HRIS**: SK하이닉스 사내 채용 (구체 _미공개_)
- **AI 시스템 배치**: ✅ A!SK 영상면접 platform — 자체 또는 vendor 여부 _미공개_
- **배포 환경**: _미공개_ — SK 그룹 클라우드 추정
- **연동·통합**: ✅ 7-phase 채용 플로우 — 서류·SKCT·A!SK·peer review·종합 Report·대면 통합
- **사용자 접점**: 지원자 영상 녹화 web/모바일 + 미래 동료 peer review interface + HR/면접관 종합 Report dashboard
- **인증·권한**: ✅ 사내 SSO (peer·HR·면접관 RBAC) + 지원자 별도 인증

### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 자기소개서, SKCT 결과, AI 면접 영상, JD-역량 매칭, (고도화) 석박사 Lab·논문 + LinkedIn 코멘트 자동 크롤링
- **데이터 규모**: _미공개_ — 2025 하반기 신입 응시자 비공개
- **전처리·정제**: _미공개_ — 영상 STT 기반 실시간 평가 (향후 고도화)
- **학습 vs RAG vs In-context**: _미공개_ — AI 종합 역량 Report 생성은 LLM 기반 추정
- **데이터 거버넌스**: ✅ AI single decision 회피 (peer + HR + 면접관 hybrid) — KR AI 기본법 인적감독 best practice
- **민감정보 처리**: ⚠️ AI 영상 분석의 표정·억양·외모 신호 사용 여부 _미공개_

### D. Model (R9 research)

- **Foundation model**: _미공개_ — 자체 LLM 또는 그룹 표준 (A.X 가능성) 미명시
- **모델 유형**: ✅ generative (Report 자동 생성·맞춤 질문) + classifier (역량-JD 매칭율) + STT (향후)
- **제공 방식**: ✅ SK하이닉스 internal build
- **커스터마이징 기법**: ✅ 직무별 문제은행, JD-역량 매칭 rule, AI 면접 + 대면 면접 결과 교차 검증
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: ✅ peer + HR + 면접관 hybrid (AI single decision 회피). 표정·외모 신호 transparency 부족 risk


## Impact / Metrics

### 기대효과 요약
AI single decision 회피 + 미래 동료 평가 hybrid + 7-phase AI Report 통합으로 평가 깊이는 Big Tech 수준 + 비용은 대폭 절감. 한국 채용절차법 + AI 기본법 (2026-01-22) 인적감독 의무 자동 충족 model.

| 구분 | 기대효과 (PwC 자료) |
|---|---|
| 비용 절감 | ⚠️ 자사 보고: 지원자 인당 **3시간 + 19만원 절감** (이천 왕복·대면 면접 비용 기준) |
| 평가 심층화 | 다차수 면접 효과 — 1시간×2회 → Big Tech 수준 2시간+ 평가 깊이 |
| 평가 공정성 | 정량·정성 통합 AI Report → 평가자 주관 배제 |
| 지원자 편의 | 시공간 제약 없이 원하는 시간·장소 면접 응시 |
| 평가 연속성 | 서류→SKCT→AI 면접 전 단계 통합 Report를 대면 면접관에게 제공 |

- 2025 하반기 신입 채용 launch
- 출처: SK하이닉스 내부 자료, EBN뉴스 2025-09, 세계일보 2025-09, PwC HR AI Use Case 자료 2026-05

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
