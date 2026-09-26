---
title: "JPMorgan — 'AI Made Easy' 전사 AI 교육"
slug: jpmorgan-ai-made-easy-upskilling
primary_category: Learning & Development
subcategory: Skills & Capabilities
tags: [ai-made-easy, jpmorgan, upskilling, prompt-engineering, mass-training, finance, role-specific-curriculum]
company: JPMorgan Chase
industry: [finance, banking]
region: [na, global]
employee_class: [all]
vendor: [JPMorgan internal]
vendor_type: [internal-build]
output: "직원별 AI fundamentals·prompt engineering·컴플라이언스 모듈 이수 기록 + 직무별 use case 인증서. 신입 분석가는 prompt engineering 필수 수료증"
ai_tech_type: [generative]
ai_tech_subtype: [summarization-qa]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: []
kr_law: 일반 개인정보보호법 수준
kr_union: 협의 의무 낮음 (정보 제공 성격)
kr_language: 해당 없음 (자체 구축)
kr_vendor: 해당 없음 (자체 구축)
frequency: annual
first_seen: 2024-08-01
last_confirmed: 2026-02-12
confidence: 0.7
evidence_grade: A
corroborated_by: 2
freshness: fresh
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/cnbc-jpmorgan-llm-suite-2024-08.md, sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10.md]
related_usecases:
  - jpmorgan-llm-suite-redeployment
  - accenture-mass-genai-reskilling
related_vendors: []
---

## Summary

JPMorgan **AI Made Easy** — Derek Waldron(Chief Analytics Officer, McKinsey 인터뷰)이 밝힌 전사 AI 교육 프로그램: 직원 전체를 대상으로 AI 도구 이해·활용 훈련을 "at scale"로 브랜딩해 운영하며 계속 업데이트 [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]. 세그먼트별 접근 — 기능 익히기 → 프롬프트 구성(프레임워크·예시·제약) → 다중 소스 리서치·데이터 분석 등 심화 모듈 추가; 팀별 프롬프트 라이브러리·"prompt of the week" 이메일·소셜 채널로 동료 학습 [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]. 배경: LLM Suite가 60,000명+ 직원에게 제공(2024-08, 전 직원 약 313,000명) [[sources/cnbc-jpmorgan-llm-suite-2024-08]] → "nearly a quarter-million people"이 플랫폼 접근, 직원의 절반 조금 못 미치는 인원이 매일 gen AI 도구 사용 [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]. CTO Heitsenrether: "도메인에 맞는 prompt engineering을 가르쳐야 한다" [[sources/cnbc-jpmorgan-llm-suite-2024-08]]. 기존 "전 직원 수 대상 표기", "Q1 세션 참석 인원 수", "rollout 인원 수(branch·call center 제외)", "AWM 신입 분석가 prompt engineering 필수", "컴플라이언스 모듈", "3-6h/week 절감", "Anthropic", "8주 통합 주기"는 인용 소스에 없어 _미공개_ 처리 (2026-09-27 grounding 점검).

## Problem / Why (도입 배경)

- **Before (baseline)**: ❓ 정량 baseline 미공개. 직원 대다수가 AI 도구를 이해·활용하는 데 익숙해질 필요 (Waldron) [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]
- **Pain point**: 도구 제공만으로는 부족 — "도메인에 맞는 prompt engineering을 가르쳐야 실제 가능성을 본다"(Heitsenrether) [[sources/cnbc-jpmorgan-llm-suite-2024-08]]; 대규모 long tail 업무는 자기주도(self-service) 도구로 해결해야 함 [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]
- **Trigger**: LLM Suite 출시(2024)와 병행 [[sources/cnbc-jpmorgan-llm-suite-2024-08]] [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]

## Solution Architecture

### A. Process (프로세스)

- **Before**: _미공개 (not disclosed)_
- **After** (⚠️ 자사 보고 [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]):
  1. 직원 전체: AI 도구 이해·활용 기본 훈련 (AI Made Easy, at scale)
  2. 기능 숙지 후 프롬프트 구성법 — 프레임워크·예시·제약 조건
  3. 신규 기능 출시에 맞춘 모듈 추가 — 다중 소스 리서치, 다중 데이터셋 분석
  4. 동료 학습 — 팀별 프롬프트 라이브러리, "prompt of the week" 이메일, 소셜 채널
  5. 세그먼트별 차별화 (직원 전체 외 세그먼트 세부 _미공개_)
- **HITL**: _미공개 (not disclosed)_ — 기존 "HRD·legal·SME 협업" 서술은 소스에 없음
- **Frequency**: 지속 업데이트 [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]; 주기 세부 _미공개_

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS / 기반 시스템**: _미공개 (not disclosed)_
- **AI 시스템 배치**: 교육 대상 플랫폼 = LLM Suite (JPMorgan 자체 플랫폼) [[sources/cnbc-jpmorgan-llm-suite-2024-08]] [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]
- **배포 환경**: _미공개 (not disclosed)_ — 교육 LMS 명시 없음
- **연동·통합**: LLM Suite는 팀 지식 시스템·전사 데이터·앱과 연결되는 "ecosystem"으로 진화 [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]; 교육 프로그램 자체의 연동 _미공개_
- **사용자 접점**: 프롬프트 라이브러리·이메일·소셜 채널 [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]; 교육 세션 형식(live/온라인) _미공개_
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: 교육 콘텐츠 = AI 도구 이해·프롬프트 구성·리서치·데이터 분석 모듈 [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]
- **데이터 규모**: LLM Suite 접근 "nearly a quarter-million people"; 절반 조금 못 미치는 직원이 매일 사용 [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]; 2024-08 기준 60,000명+ [[sources/cnbc-jpmorgan-llm-suite-2024-08]]; 교육 참석 인원 _미공개 (not disclosed)_
- **전처리·정제**: N/A (training program)
- **학습 vs RAG vs In-context**: N/A
- **데이터 거버넌스**: _미공개 (not disclosed)_ — 컴플라이언스 모듈 존재 여부 소스에 없음
- **민감정보 처리**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: N/A (training program) — 학습 대상 LLM Suite는 OpenAI 모델 기반 [[sources/cnbc-jpmorgan-llm-suite-2024-08]]; Anthropic 병용은 인용 소스에 없음
- **모델 유형**: N/A
- **제공 방식**: N/A
- **커스터마이징 기법**: "Learn by doing" — LLM Suite 직접 사용 [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]
- **평가·가드레일**: ⚠️ 자사 보고: 시간 절감을 정밀 정량화하지 않음(Waldron); AI 프로그램 전체의 gross benefit이 연 30~40% 성장 [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]] — 교육 자체 효과 metric _미공개_

### E. Organization & Team (조직·팀 구조)

- **오너십**: Derek Waldron(Chief Analytics Officer) 주도 AI 프로그램 [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]; HR 역할 _미공개 (not disclosed)_
- **참여 역할**: prompt engineer — 새로 등장한 직무 카테고리 [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]
- **팀 규모·기간**: _미공개 (not disclosed)_
- **거버넌스 체계**: _미공개 (not disclosed)_
- **변화관리**: 동료 학습 채널(프롬프트 라이브러리·주간 이메일·소셜) [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]
- **파트너**: _미공개 (not disclosed)_

## Impact / Metrics (기대효과)

### 기대효과 요약
⚠️ 자사 보고: LLM Suite 접근 nearly a quarter-million, 절반 조금 못 미치는 직원이 매일 사용 [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]. 교육 프로그램 자체의 이수율·효과 metric은 _미공개_.

- LLM Suite 접근: nearly a quarter-million people [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]] (2024-08: 60,000명+ [[sources/cnbc-jpmorgan-llm-suite-2024-08]])
- 매일 사용: 직원의 절반 조금 못 미침 [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]
- 시간 절감: 정밀 정량화하지 않음 (Waldron) [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]] — 기존 "3-6h/week"는 인용 소스에 없음
- AI 프로그램 gross benefit 연 30~40% 성장 (교육 단독 효과 아님) [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]

## Governance & Risk

- ⚠️ 교육 프로그램 자체 효과 측정 metric _미공개_
- ⚠️ 생산성 향상이 비용 절감으로 직결되지 않음 — "an hour saved here… shift bottlenecks" (Waldron) [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]
- ⚠️ agentic 도구 확산 시 신뢰·검증 문제 (Waldron) [[sources/mckinsey-jpmorgan-derek-waldron-ai-first-2024-10]]

## Contradictions

> [!note] 2026-09-27 grounding — 인용 소스 2건(CNBC 2024-08, McKinsey Waldron 인터뷰) raw에 "전 직원 수 대상 표기", "Q1 세션 참석 인원 수", "rollout 인원 수·branch/call center 제외", "8개월 onboarding 인원 수", "AWM 신입 분석가 prompt engineering 필수", "컴플라이언스 모듈", "3-6h/week", "OpenAI + Anthropic 양사", "8주마다 통합", "자체 LMS" 서술이 없어 삭제·_미공개_ 처리. 직원 수는 CNBC 기준 약 313,000명(2024-06).

## Consulting Angle

- **KR 그룹 HRD 센터 직접 reference**: 삼성인력개발원·LG Aspire·SK mySUNI·현대인재개발원 모두 AI 교육 curriculum 기획 중. JPMorgan 구조 (기본 → 프롬프트 구성 → 심화 모듈 + 동료 학습 채널) 직접 차용 가능
- **금융권 fit 우수**: KB·신한·우리·하나·미래에셋 모두 자체 LLM 플랫폼 도입 중 → 동반 교육 프로그램 reference (위 [[jpmorgan-llm-suite-redeployment]]와 pair)
- **신입 prompt engineering 의무화**: 인용 소스에서 미확인(_미공개_) — 확인되면 KR 대기업 신입 OJT/연수원 과정 모듈 통합 아이디어로 활용
- **2026 Q3-Q4 KR 컨설팅 deck**: "AI 도입 = 도구 + 교육의 시간차 0" — JPMorgan의 도구·교육 병행 전략이 모범
- **반면교사**: 단일 corp culture라서 통합 가능 — KR 대기업 그룹사 multi-corp 환경에서는 계열사별 미세 customization 필요
