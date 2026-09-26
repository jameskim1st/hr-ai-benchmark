---
title: "SK하이닉스 — A!SK AI 영상면접 + 미래 동료 평가 hybrid"
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
output: "직무별 AI 영상면접 질문 출제 + 지원자 영상 답변 평가 + 정량·정성 통합 AI 종합 역량 Report (서류·SKCT·면접·논문·LinkedIn 크롤 통합) — 미래 동료 peer + 면접관용"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [text-generation, clustering-classification]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: [kr-high-impact, eu-annex-iii]
kr_law: 채용절차법·AI 기본법 인적감독을 peer hybrid로 충족, 영상 표정·외모 신호 사용 미공개
kr_union: 단체교섭/근로자대표 협의 필요 (인사 의사결정 영향 — 신입 채용 전형)
kr_language: 한국어 네이티브
kr_vendor: 자체 구축 (SK하이닉스 internal, 영상면접 플랫폼 벤더 미공개)
frequency: annual
first_seen: 2025-09-16
last_confirmed: 2026-04-01
confidence: 0.8
evidence_grade: A
corroborated_by: 2
freshness: fresh
depth: stub
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/ebn-sk-hynix-ask-ai-interview-2025-09.md, sources/nate-ebn-sk-hynix-ask-ai-interview-2025-09.md]
related_usecases:
  - sk-cc-adot-biz-hr-recruitment
  - sk-group-aibiz-25-companies
  - midas-inair-ai-assessment-korea
related_vendors: []
---

## Summary

SK하이닉스가 2025 하반기 신입 채용에 **'A!SK' (AI Interview with SK Hynix)** 전형 신설. AI가 직무별 특화 문제를 출제하면 지원자가 영상 녹화 답변 제출. 자기소개서로 파악 어려운 **커뮤니케이션·팀워크·상황 대처** 능력을 종합 검증. 제출 영상은 **미래 동료 구성원이 직접 평가**하는 **hybrid 모델** ([[sources/ebn-sk-hynix-ask-ai-interview-2025-09]]). AI 단독 결정 회피 설계 — 한국 채용절차법 fit (해석).

## Problem / Why (도입 배경)

- **Before**: SK하이닉스 신입 채용은 자기소개서 + 인적성 + 면접 — 직무 적합 soft skill (커뮤니케이션·팀워크) 측정 어려움
- **Pain point**: 반도체 기술사무직 신입 채용 volume 크지만 면접관 시간 한정 + soft skill 평가 표준화 어려움
- **Trigger**: 2025 하반기 신입 공채 — A!SK 전형 신설 (마이다스 inAIR 차별 논란 후 자체 hybrid 설계)

## Solution Architecture

### A. Process (프로세스)

> ⚠️ 아래 7-Phase 상세는 PwC 내부 자료 기반으로 `sources`에 미등록 — 인용 불가 (2026-09-27 grounding 점검). 인용 소스로 확인되는 범위: 서류전형 → SKCT(인적성) + A!SK(AI 출제·영상 답변 제출·미래 동료 평가) → 11월 말 면접 → 최종 합격 ([[sources/ebn-sk-hynix-ask-ai-interview-2025-09]]).

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

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS**: _미공개 (not disclosed)_
- **AI 시스템 배치**: ✅ 'A! SK' AI 기반 화상 인터뷰 — AI가 직무 특화 문제 출제, 지원자가 온라인 영상 녹화 제출 ([[sources/ebn-sk-hynix-ask-ai-interview-2025-09]]); 플랫폼 자체/벤더 여부 _미공개_
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: ✅ 채용 절차: 서류 → SKCT + A! SK → 면접 ([[sources/ebn-sk-hynix-ask-ai-interview-2025-09]]); 시스템 연동 _미공개_
- **사용자 접점**: ✅ 지원자 온라인 영상 녹화 제출 ([[sources/ebn-sk-hynix-ask-ai-interview-2025-09]]); 평가자 인터페이스 _미공개_
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: ✅ 직무 특화 문제에 대한 지원자 영상 답변 ([[sources/ebn-sk-hynix-ask-ai-interview-2025-09]]); 자기소개서·SKCT 결과 통합 Report·논문·LinkedIn 크롤링은 인용 소스 미확인 — _미공개_
- **데이터 규모**: _미공개 (not disclosed)_
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: _미공개 (not disclosed)_
- **데이터 거버넌스**: ✅ 제출 영상은 미래 동료가 될 구성원들이 직접 평가 ([[sources/ebn-sk-hynix-ask-ai-interview-2025-09]]); 데이터 보존·접근 정책 _미공개_
- **민감정보 처리**: ⚠️ AI 영상 분석의 표정·억양·외모 신호 사용 여부 _미공개_

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **모델 유형**: ✅ AI가 직무별 특화 문제 출제 ([[sources/ebn-sk-hynix-ask-ai-interview-2025-09]]); 자동 채점 여부 _미공개_ (기사상 평가는 구성원)
- **제공 방식**: _미공개 (not disclosed)_
- **커스터마이징 기법**: ✅ 직무별 특화 문제 출제 ([[sources/ebn-sk-hynix-ask-ai-interview-2025-09]]); 문제은행·교차 검증 세부 _미공개_
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: ✅ 미래 동료 구성원 평가로 공정성 보완 ([[sources/ebn-sk-hynix-ask-ai-interview-2025-09]]); 표정·외모 신호 사용 여부 _미공개_

### E. Organization & Team (조직·팀 구조)

- **오너십**: SK하이닉스 (채용 주체) ([[sources/ebn-sk-hynix-ask-ai-interview-2025-09]]); 담당 조직 _미공개_
- **참여 역할**: ✅ 미래 동료가 될 현업 구성원이 영상 평가 참여 ([[sources/ebn-sk-hynix-ask-ai-interview-2025-09]])
- **팀 규모·기간·거버넌스·변화관리·파트너**: _미공개 (not disclosed)_


## Impact / Metrics (기대효과)

### 기대효과 요약
AI single decision 회피 + 미래 동료 평가 hybrid + 7-phase AI Report 통합으로 평가 깊이는 Big Tech 수준 + 비용은 대폭 절감. 한국 채용절차법 + AI 기본법 (2026-01-22) 인적감독 의무 자동 충족 model.

| 구분 | 기대효과 |
|---|---|
| 비용 절감 | _미공개_ (기존 '지원자 인당 시간·비용 절감' 수치는 PwC 내부 자료 기반 — sources 미등록, 수치 근거 미확보 — 2026-09-27 grounding 점검) |
| 평가 심층화 | ✅ 자기소개서만으로 파악하기 어려운 커뮤니케이션·팀워크·상황 대처 능력을 다각도로 검증 ([[sources/ebn-sk-hynix-ask-ai-interview-2025-09]]) |
| 평가 공정성 | ✅ 미래 동료 구성원이 직접 평가해 공정성 보완 ([[sources/ebn-sk-hynix-ask-ai-interview-2025-09]]) |
| 지원자 편의 | ✅ 온라인 영상 녹화 제출 ([[sources/ebn-sk-hynix-ask-ai-interview-2025-09]]) |
| 평가 연속성 | ⚠️ 출처 미인용 (PwC 자료 — 통합 Report 제공은 인용 소스에 없음) |

- 2025 하반기 신입 채용에서 전형 신설 ([[sources/ebn-sk-hynix-ask-ai-interview-2025-09]])
- 인용 소스: EBN 2025-09-16 ([[sources/ebn-sk-hynix-ask-ai-interview-2025-09]]; 네이트 전재본 [[sources/nate-ebn-sk-hynix-ask-ai-interview-2025-09]]는 동일 기사). 세계일보·SK하이닉스 내부 자료·PwC 자료는 sources 미등록 — 인용 불가

## Governance & Risk

- ✅ **AI single decision 회피** — 미래 동료 peer review + HR 종합 — 한국 AI 기본법 인적감독 의무 best practice
- ✅ peer review로 직무 fit 정량 신호 추가
- ⚠️ AI 영상 분석의 표정·억양·외모 신호 사용 여부 _미공개_ — 마이다스 inAIR 차별 논란 trigger와 같은 카테고리
- ⚠️ 미래 동료 peer review의 본인 편향 (학교·전공·외모) 동반 가능 — 별도 mitigation 필요
- ⚠️ 영상 녹화 시 시간·장소 자율은 socioeconomic gap 가능 (장비·환경)

## Contradictions

_없음._

> [!note] 2026-09-27 grounding — [[sources/nate-ebn-sk-hynix-ask-ai-interview-2025-09]]는 EBN 기사의 포털 전재본으로 독립 소스가 아님(근거 수 중복 계산 금지). 7-Phase 플로우·인당 절감 수치·통합 Report·LinkedIn 크롤링 등은 PwC 내부 자료 기반으로 인용 소스에 없음 — B/C/D는 EBN 확인 범위로 축소, 수치는 `_미공개_`.

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
