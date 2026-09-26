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
visibility: public
case_type: adoption
regulatory_exposure: [kr-high-impact, eu-annex-iii]
kr_law: AI 기본법 고영향 + 채용절차법 정합성; 후보자 개인정보 동의 (페이지)
kr_union: 단체교섭/근로자대표 협의 필요 (인사 의사결정 영향)
kr_language: "한국어 네이티브 (자사 보고: 한국어 specialized)"
kr_vendor: 잡코리아·웍스피어 자체 구축
frequency: daily
first_seen: 2026-03-31
last_confirmed: 2026-04-01
confidence: 0.8
evidence_grade: A
corroborated_by: 2
freshness: fresh
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/inews24-jobkorea-ai-agent-survey-2026-04.md, sources/zdnet-korea-jobkorea-hiring-center-2026-03.md]
related_usecases:
  - wantedlab-ai-recruiting-agent
  - sk-cc-adot-biz-hr-recruitment
  - midas-inair-ai-assessment-korea
  - ibm-watsonx-orchestrate-ta-agent
related_vendors: []
---

## Summary

잡코리아 운영사 **웍스피어**가 출시한 **통합 채용 솔루션 '하이어링 센터'** (2026-03 일부 기업 오픈). 자연어 대화로 채용 담당자 의도를 이해하고 공고 맥락 분석 후 후보자 제안하는 **'탤런트 에이전트'** 탑재. 잡코리아 자체 설문 — 채용 담당자 1,286명 중 **65%가 AI 채용 에이전트 도입 또는 검토 중** (적극 검토 13.6% + 검토 48.8%).

## Problem / Why (도입 배경)

- **Before (baseline)**: 기업의 채용 기능이 분산돼 있어 공고 등록·지원자 관리·커뮤니케이션·운영 관리를 별도로 처리 [[sources/zdnet-korea-jobkorea-hiring-center-2026-03]]; 정량 baseline ❓ 미공개
- **Pain point**: 채용 운영 효율화·반복 업무 부담 [[sources/zdnet-korea-jobkorea-hiring-center-2026-03]]; 키워드 검색 중심 인재 탐색의 한계 [[sources/zdnet-korea-jobkorea-hiring-center-2026-03]]
- **Trigger**: _미공개 (not disclosed)_ — 기존 "원티드랩 2025-10 launch 대응" 서술은 소스에 없음; 시장 맥락은 자체 설문(65% 도입·검토) [[sources/inews24-jobkorea-ai-agent-survey-2026-04]]

## Solution Architecture

### A. Process (프로세스)

- **Before**: 채용 담당자가 분산된 도구로 공고·지원자·커뮤니케이션 관리 [[sources/zdnet-korea-jobkorea-hiring-center-2026-03]]
- **After** (⚠️ 자사 보고 [[sources/zdnet-korea-jobkorea-hiring-center-2026-03]]):
  1. 하이어링 센터에서 채용 공고 등록 → 지원자 관리 → 커뮤니케이션 → 운영 관리를 단일 인터페이스로 처리; 복수 담당자 협업 워크스페이스
  2. AI 기반 자동 공고 생성
  3. 탤런트 에이전트가 채용 담당자 의도를 자연어 대화로 이해 → 공고의 요구사항·맥락 분석 → 적합 후보자 제안 + 추천 이유 제시
  4. 채용 담당자가 후보자 contact·면접 진행 (세부 _미공개_)
- **HITL**: 채용 담당자가 추천 이유를 보고 의사결정 [[sources/zdnet-korea-jobkorea-hiring-center-2026-03]] — 최종 결정 주체 명시는 _미공개_
- **Frequency**: _미공개 (not disclosed)_
- **Scope of autonomy**: recommend (후보자 제안) [[sources/zdnet-korea-jobkorea-hiring-center-2026-03]]

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS**: ✅ 잡코리아 통합 채용 솔루션 '하이어링 센터' (웍스피어 운영) [[sources/zdnet-korea-jobkorea-hiring-center-2026-03]]
- **AI 시스템 배치**: '탤런트 에이전트' — 잡코리아 자체 개발, 하이어링 센터에 일부 반영 [[sources/zdnet-korea-jobkorea-hiring-center-2026-03]]
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: _미공개 (not disclosed)_ — 잡코리아 서비스 간 연계 확장 계획만 언급 [[sources/zdnet-korea-jobkorea-hiring-center-2026-03]]
- **사용자 접점**: 채용 담당자용 단일 인터페이스·자연어 대화 [[sources/zdnet-korea-jobkorea-hiring-center-2026-03]]
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: ✅ 채용 공고(요구사항·맥락), 채용 담당자 의도(자연어) [[sources/zdnet-korea-jobkorea-hiring-center-2026-03]]; 후보자 DB 범위 _미공개_
- **데이터 규모**: _미공개 (not disclosed)_
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: _미공개 (not disclosed)_
- **데이터 거버넌스**: _미공개 (not disclosed)_ — 후보자 동의 절차 소스에 없음
- **민감정보 처리**: _미공개 (not disclosed)_ — 차별 표현 필터·explainability 미공개

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **모델 유형**: 대화형 의도 이해 + 후보자 추천(추천 이유 생성) [[sources/zdnet-korea-jobkorea-hiring-center-2026-03]]
- **제공 방식**: _미공개 (not disclosed)_
- **커스터마이징 기법**: _미공개 (not disclosed)_ — 기존 "한국어 specialized" 서술은 소스에 없음
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: _미공개 (not disclosed)_

### E. Organization & Team (조직·팀 구조)

- **오너십**: 잡코리아(운영 법인 웍스피어, 대표 윤현준) — CPO 정승호 [[sources/zdnet-korea-jobkorea-hiring-center-2026-03]]
- **참여 역할**: _미공개 (not disclosed)_
- **팀 규모·기간**: _미공개 (not disclosed)_
- **거버넌스 체계**: _미공개 (not disclosed)_
- **변화관리**: 일부 기업 대상 제한 오픈(2026-03-31) 후 고도화·확장 계획 [[sources/zdnet-korea-jobkorea-hiring-center-2026-03]]
- **파트너**: _미공개 (not disclosed)_ (자체 개발)

## Impact / Metrics (기대효과)

### 기대효과 요약
한국 ATS·채용 vendor 경쟁의 AI agent 차별화 + 시장 데이터 (65% 도입·검토)로 KR 채용 vendor 시장 기회 입증.

- 2026-03-31 일부 기업 대상 오픈 [[sources/zdnet-korea-jobkorea-hiring-center-2026-03]]
- ⚠️ 자사 설문(약 3주, 채용 담당자 1286명): 65%가 AI 채용 에이전트 도입·검토 — 검토 중 48.8%, 적극 검토 중 13.6% [[sources/inews24-jobkorea-ai-agent-survey-2026-04]]
- 도입 기업 수·효과 수치: _미공개 (not disclosed)_

## Governance & Risk

- ⚠️ 자연어 매칭의 한국어 직무·전문 용어 fit 검증 필요 (한국어 특화 여부는 소스에 없음)
- ⚠️ "탤런트 에이전트" 후보자 추천의 차별 표현 자동 필터 _미검증_
- ⚠️ 한국 AI 기본법 + 채용절차법 정합성 — 채용 vendor의 의무 명확화 필요

## Contradictions

> [!note] 2026-09-27 grounding — B~D의 "한국 데이터센터 추정", "매칭 retrieval + LLM ranking 추정", "자체 LLM 또는 외부 API(OpenAI·Hyperclova X) 추정", "한국어 specialized", "잡코리아 기업회원 계정", "후보자 DB·지원 이력 연동"과 Problem의 "원티드랩 launch 대응 trigger"는 인용 소스 2건에 없어 삭제·_미공개_ 처리. 설문 인원 표기는 원문 "1286명" 그대로 사용.

## Consulting Angle

- **KR 채용 시장 vendor 경쟁 reference** (경쟁 구도는 컨설턴트 관점 — 인용 소스에 없음):
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
