---
title: "SK C&C — '에이닷 비즈 HR' 전사 채용 도입"
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
output: "자기소개서별 경력·핵심 역량 키워드 추출 + 직무 적합성·리스크 요인 점수 + AI 면접 (영상 응답 분석) + 후보자 맞춤 면접 질문 자동 생성. ⚠️ 자사 보고: 수천 건 4시간 (90% 단축)"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [information-extraction, summarization-qa, clustering-classification]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: [kr-high-impact, eu-annex-iii]
kr_law: AI 기본법 고영향(채용) 인적감독 + 채용절차법 고지 + 영상면접 PIPA 검증
kr_union: 단체교섭/근로자대표 협의 필요 (채용 의사결정 영향)
kr_language: 한국어 네이티브
kr_vendor: SKT·SK AX 'A.Biz HR' (그룹 자체 구축)
frequency: annual
first_seen: 2025-02-20
last_confirmed: 2026-04-01
confidence: 0.8
evidence_grade: A
corroborated_by: 3
freshness: fresh
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/aitimes-sk-cc-adot-biz-hr-2025-02.md, sources/newsis-sk-cc-adot-biz-hr-2025-02.md, sources/zdnet-korea-sk-cc-adot-biz-hr-2025-02.md]
related_usecases:
  - sk-group-aibiz-25-companies
  - sk-hynix-ask-ai-interview
  - sk-group-aict-ai-recruitment
  - midas-inair-ai-assessment-korea
related_vendors: []
---

## Summary

SK C&C가 SKT와 공동 개발 중인 'A.Biz(에이닷 비즈)'의 HR 특화 제품 **'에이닷 비즈 HR'**을 2025년 신입·주니어 탤런트 채용에 전면 도입 ([[sources/newsis-sk-cc-adot-biz-hr-2025-02]]). 지원서의 문맥 흐름·**핵심 역량 키워드** 분석 → **직무 적합성·리스크 포인트 도출**, AICT(AI 활용도 테스트), AI 1:1 면접(음성·영상 분석), 면접관용 맞춤 질문지 자동 생성 ([[sources/aitimes-sk-cc-adot-biz-hr-2025-02]], [[sources/zdnet-korea-sk-cc-adot-biz-hr-2025-02]]). ⚠️ 자사 보고: 수천 개가 넘는 지원서를 4시간 만에 분석·평가 (기존 약 1주 — [[sources/zdnet-korea-sk-cc-adot-biz-hr-2025-02]]; '약 90% 단축'은 기사에 없는 환산값).

## Problem / Why (도입 배경)

- **Before**: SK C&C 신입·주니어 채용 시 수천 건 지원서 review에 HR + 사업부 SME 다수 인력 1주 투입
- **Pain point**: 한국 대졸 정기공채 (3월·9월) 시즌 압박 + 직무 적합성 판단 표준화 어려움
- **Trigger**: 2025년 SKT-SK AX 'A.Biz' 합작 launch + 신입 공채 시즌 적용

## Solution Architecture

### A. Process (프로세스)

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

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS**: _미공개 (not disclosed)_
- **AI 시스템 배치**: ✅ SKT와 공동 개발 중인 '에이닷 비즈 HR' — '에이닷 비즈 프로페셔널'(법무·세무·PR·HR 특화) 라인 ([[sources/newsis-sk-cc-adot-biz-hr-2025-02]])
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: _미공개 (not disclosed)_
- **사용자 접점**: _미공개 (not disclosed)_ — 면접관용 질문지 자동 생성 기능만 확인 ([[sources/zdnet-korea-sk-cc-adot-biz-hr-2025-02]])
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: ✅ 지원서(자기소개서), AICT 답변, 필기 전형 데이터, AI 1:1 면접 음성·영상 답변 ([[sources/zdnet-korea-sk-cc-adot-biz-hr-2025-02]]); JD 텍스트 사용 여부 _미공개_
- **데이터 규모**: ⚠️ 자사 보고: 수천 개가 넘는 지원서 / 채용 cycle ([[sources/aitimes-sk-cc-adot-biz-hr-2025-02]])
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: _미공개 (not disclosed)_
- **데이터 거버넌스**: _미공개 (not disclosed)_ — 채용절차공정화법·AI 기본법 fit 검증 필요 (컨설팅 관점)
- **민감정보 처리**: ✅ 지원자 답변을 음성과 영상으로 분석 ([[sources/zdnet-korea-sk-cc-adot-biz-hr-2025-02]]); 표정·억양·외모 신호 사용 여부 _미공개_

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **모델 유형**: ⚠️ 자사 보고: 지원서 문맥 흐름·핵심 역량 키워드 분석 → 직무 적합성·리스크 포인트 도출, 음성·영상 분석 기반 AI 1:1 면접 ([[sources/aitimes-sk-cc-adot-biz-hr-2025-02]], [[sources/zdnet-korea-sk-cc-adot-biz-hr-2025-02]]); 모델 구성 _미공개_
- **제공 방식**: ✅ SKT와 공동 개발한 '에이닷 비즈 HR' ([[sources/aitimes-sk-cc-adot-biz-hr-2025-02]])
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: _미공개 (not disclosed)_ — 편향·검증 관련 정보 없음 ([[sources/zdnet-korea-sk-cc-adot-biz-hr-2025-02]] Limitations)

### E. Organization & Team (조직·팀 구조)

- **오너십**: ✅ SK C&C 탤런트(채용) 조직 — 김민환 탤런트 담당 인용 ([[sources/aitimes-sk-cc-adot-biz-hr-2025-02]])
- **참여 역할·팀 규모·거버넌스·변화관리**: _미공개 (not disclosed)_
- **파트너**: ✅ SKT (공동 개발) ([[sources/newsis-sk-cc-adot-biz-hr-2025-02]])


## Impact / Metrics (기대효과)

### 기대효과 요약
⚠️ 자사 보고: 수천 개 지원서 분석·평가 약 1주 → 4시간 ([[sources/aitimes-sk-cc-adot-biz-hr-2025-02]]; '90% 단축'은 기사에 없는 환산값). 1월 채용에서 접수 마감 후 이틀 만에 서류 합격자 발표 ([[sources/aitimes-sk-cc-adot-biz-hr-2025-02]]).

- ⚠️ 자사 보고:
  - 지원서 분석·평가: 약 1주 → 4시간 ([[sources/newsis-sk-cc-adot-biz-hr-2025-02]])
  - 접수 마감 후 이틀 만에 서류 합격자 발표 ([[sources/aitimes-sk-cc-adot-biz-hr-2025-02]])
  - 신입·주니어 탤런트 채용 전면 도입 ([[sources/newsis-sk-cc-adot-biz-hr-2025-02]])
  - 정성 평가: 직무 적합도 높은 인재 신속 선별, 입사자 업무 적응도 향상 (HR 담당자 평가) ([[sources/zdnet-korea-sk-cc-adot-biz-hr-2025-02]])
  - 연내 AI 인재 탐색·추천 기능 도입 예정 (2025-02 기준 로드맵) ([[sources/newsis-sk-cc-adot-biz-hr-2025-02]])

## Governance & Risk

- ⚠️ "리스크 요인 판정"의 차별 표현(성별·학력·출신) 자동 필터 _미검증_
- ⚠️ 한국 AI 기본법 (2026-01-22) 고영향 AI 명확 분류 — 인적감독 의무 자동 충족 검증 필요
- ⚠️ 마이다스 inAIR 차별 논란 (2020) trigger와 동일 카테고리 — bias mitigation 설계 reference 필수
- ⚠️ AI 면접 영상 분석의 표정·억양·외모 신호 사용 여부 _미공개_

## Contradictions

_없음._

> [!note] 2026-09-27 grounding — '약 90% 단축'은 3개 기사 어디에도 없는 환산값(약 1주 → 4시간)이라 원 표기를 병기하고 환산임을 명시. Consulting Angle의 마이다스 inAIR 고객 수는 본 페이지 인용 소스에 없어 삭제. "SK AX 산업특화 AI + A.X 추정"·"자체 LLM + RAG" 등 아키텍처 추정 서술은 `_미공개_`로 교체.

## Consulting Angle

- **KR 대기업 채용 AI reference (Top 5)**:
  - 마이다스 inAIR [[midas-inair-ai-assessment-korea]] (vendor 모델) vs SK C&C 자체 (그룹 표준화 모델) 비교
  - SK 그룹 25개사 'A.Biz' 확산 [[sk-group-aibiz-25-companies]]과 pair
  - "약 1주 → 4시간" 단축(⚠️ 자사 보고)은 강력한 ROI hook
- **2026 Q3-Q4 KR 채용 AI 컨설팅**:
  - 한국 대졸 공채 시즌 (3월·9월) HR 부담 솔루션
  - "vendor 도입 vs 자체 구축" 결정 framework — SK는 그룹 자체 LLM (A.X) 강점
- **AI 면접 분석**: SK하이닉스 A!SK [[sk-hynix-ask-ai-interview]]와 비교 — 동일 SK 그룹 내 vendor (자체) vs hybrid (미래 동료 평가)
- **반면교사**:
  - 마이다스 inAIR 차별 논란 trigger와 같은 카테고리 — bias 사후 검증·명시적 protected attribute 필터·인적감독 설계 필수
  - "리스크 요인" 자동 판정의 explainability — 한국 채용절차법·AI 기본법 정합성 검증
  - AI 면접 영상 분석은 표정·억양 신호 사용 시 차별 risk — text·response 내용 위주 권장
- **글로벌 비교**: IBM Watson Recruitment [[ibm-watson-recruitment]] (protected attribute suppression) vs SK C&C — bias mitigation 명시 vs 미명시 격차
