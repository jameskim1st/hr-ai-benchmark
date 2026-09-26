---
title: "LinkedIn Learning — AI-Powered Coaching"
slug: linkedin-learning-ai-coaching
primary_category: Learning & Development
subcategory: Skills & Capabilities
tags: [linkedin-learning, ai-coaching, role-play, premium, enterprise, skills-graph, ai-tutor, conversational-learning]
company: _다수 (LinkedIn Learning Premium·Enterprise 고객)_
industry: [all]
region: [global]
employee_class: [all]
vendor: [LinkedIn, Microsoft]
vendor_type: [lxp]
output: "학습자별 AI Coach와의 대화형 Q&A·요약·심화 답변 + role-play scenario (피드백·면접·negotiation 모의) feedback 텍스트 + LinkedIn 16K skills profile 자동 갱신"
ai_tech_type: [generative]
ai_tech_subtype: [summarization-qa]
stage: production
visibility: public
case_type: vendor-product
regulatory_exposure: []
kr_law: 개인정보보호법 국외이전 (LinkedIn/MS 본사 처리) 검증 필요 (페이지)
kr_union: 협의 의무 낮음 (정보 제공 성격; 평가·승진 연계 시 검토)
kr_language: 미확인 (한국어 존댓말 fit 검증 필요 — 페이지 명시)
kr_vendor: 미확인 (국내 파트너 확인 필요)
frequency: daily
first_seen: 2024-04-01
last_confirmed: 2026-04-01
confidence: 0.35
evidence_grade: C
corroborated_by: 0
freshness: fresh
depth: stub
graded_at: 2026-09-27
consulting_angle_status: filled
sources:
  - sources/verified-pwc-doc-2026-05.md
related_usecases:
  - workday-sana-for-workday-lms
  - bersin-galileo-learn-ai-native-lms
  - docebo-ai-learning-lazboy
  - betterup-ai-coaching-twilio
related_vendors: []
---

## Summary

LinkedIn Learning이 **Premium·Enterprise tier**에 통합한 **AI-Powered Coaching** 기능 [[sources/verified-pwc-doc-2026-05]]. 2024 글로벌 출시 후 2025에 **role-play scenario coaching**으로 확장 (Fast Company 보도, fact-check 문서 경유) [[sources/verified-pwc-doc-2026-05]] — 학습자가 AI coach와 가상 대화로 soft skill 학습. Skills taxonomy 규모(16K·39K 등)는 출처 미확인 → _미공개_ (수치 근거 미확보 — 2026-09-27 grounding 점검). ⚠️ 정량 metric은 LinkedIn 공식 KPI로 미공개 — 시장에 자주 인용되는 "90% 만족·160% 학습시간 증가" 수치는 별도의 [MS-LinkedIn 2024 Work Trend Index](https://blogs.microsoft.com/blog/2024/05/08/microsoft-and-linkedin-release-the-2024-work-trend-index-on-the-state-of-ai-at-work/) 일반 통계 — AI Coaching 자체 metric 아니므로 인용 시 주의.

## Problem / Why (도입 배경)

- **Before**: ❓ baseline 미공개 — 벤더 제품이므로 특정 기업의 도입 배경은 고객별 상이. 🚫 일반론: 1:1 human 코칭은 임원 한정·고비용이라는 L&D 영역의 일반적 pain point (비용 수치 근거 미확보 — 2026-09-27 grounding 점검)
- **Pain point**: 중간 관리자·일반 직원 soft skill (어려운 대화·feedback·negotiation) 학습 기회 부족 → role-play 환경 부재
- **Trigger**: 2024 LinkedIn Learning AI Coaching 글로벌 출시 → 2025 role-play scenario 확장 [[sources/verified-pwc-doc-2026-05]]; Microsoft Copilot 통합 여부는 인용 소스에 없음 _미공개_

## Solution Architecture

### A. Process (프로세스)

- **Before**: 직원이 LMS 비디오 강의 시청 → 실제 적용 어려움 (피드백 부재)
- **After**:
  1. 학습자가 LinkedIn Learning Premium·Enterprise tier 구독
  2. 강의 중 AI Coach와 대화형 Q&A·요약·심화 질문 가능
  3. 2025 확장: role-play scenario coaching [[sources/verified-pwc-doc-2026-05]] — 세부 시나리오 종류·평가 방식 _미공개_
  4. skills taxonomy 연계·profile 자동 갱신 여부 _미공개 (not disclosed)_
- **HITL**: 학습자 자율 사용. 매니저 dashboard 존재 여부 _미공개_
- **Frequency**: daily (학습자 상시)
- **Scope**: assistive — AI는 coach·평가자, 결정 권한 없음

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS**: _미공개 (not disclosed)_ — LinkedIn Learning은 stand-alone LXP
- **AI 시스템 배치**: ⚠️ 벤더 주장: Premium·Enterprise tier 내장 기능 [[sources/verified-pwc-doc-2026-05]]
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: _미공개 (not disclosed)_ — Skills Graph 규모(39K skills·22K courses)는 출처 미확인 [[sources/verified-pwc-doc-2026-05]]
- **사용자 접점**: _미공개 (not disclosed)_
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: _미공개 (not disclosed)_
- **데이터 규모**: _미공개 (not disclosed)_ — skills taxonomy 수치 출처 미확인
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: _미공개 (not disclosed)_
- **데이터 거버넌스**: _미공개 (not disclosed)_
- **민감정보 처리**: _미공개 (not disclosed)_ — KR PIPA cross-border data transfer 검증 필요

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **모델 유형**: LLM (생성·대화형 코칭) [[sources/verified-pwc-doc-2026-05]]
- **제공 방식**: _미공개 (not disclosed)_
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: _미공개 (not disclosed)_ — soft skill 코칭 quality control governance 미공개

### E. Organization & Team (조직·팀 구조)

- **오너십**: LinkedIn (Microsoft 자회사) 벤더 제품 — 고객사 HRD/L&D 팀이 활성화 주체 (고객별 상이)
- **참여 역할**: _미공개 (not disclosed)_
- **팀 규모·기간**: _미공개 (not disclosed)_
- **거버넌스 체계**: _미공개 (not disclosed)_
- **파트너**: _미공개 (not disclosed)_


## Impact / Metrics (기대효과)

### 기대효과 요약
대규모 mass coaching의 ROI 입증 어려운 영역에서 LMS 기존 기능 대비 학습자 engagement·soft skill 적용도 향상 기대.

- ✅ 제품 실재: Premium·Enterprise tier 사용 가능 (Tier 3 LinkedIn 공식, fact-check 문서 경유) [[sources/verified-pwc-doc-2026-05]]
- ⚠️ **수치 caveat**: 시장 자주 인용 "90% 만족·160% 학습시간 증가"는 [MS-LinkedIn 2024 Work Trend Index](https://blogs.microsoft.com/blog/2024/05/08/microsoft-and-linkedin-release-the-2024-work-trend-index-on-the-state-of-ai-at-work/) 일반 통계 — AI Coaching 자체 KPI 아님
- LinkedIn AI Coaching standalone metric: _공식 미공개_

## Governance & Risk

- ⚠️ AI coach 응답 quality control governance _미공개_
- ⚠️ role-play scenario에서 protected attribute 차별 표현 발생 가능성 — bias monitoring 필요
- ⚠️ 직원 학습 데이터의 LinkedIn 본사(Microsoft) 처리 — 한국 개인정보보호법 cross-border data transfer 검증 필요
- ⚠️ 한국 AI 기본법: 학습 결과가 평가·승진에 사용되면 고영향 AI 분류 가능성

## Contradictions

> [!note] 2026-09-27 grounding — 인용 소스(PwC fact-check 문서)에 없는 skills taxonomy 규모(16K+), Microsoft Copilot 통합, Azure·GPT 계열·자체 호스팅 등 '추정' 서술과 1:1 코칭 비용 수치를 제거하고 _미공개_ 처리. 소스 자체가 "Skills Graph 39K skills·22K courses 수치는 출처 미확인"이라고 기록 [[sources/verified-pwc-doc-2026-05]].

## Consulting Angle

- **KR L&D 컨설팅 reference**:
  - LinkedIn Premium·Enterprise 기존 도입 KR 대기업 (대부분 매출 1조+) — AI Coaching 추가 활성화 즉시 가능
  - Microsoft 365 도입사와 cross-sell — Microsoft People Skills [[microsoft-people-skills-inferred-ontology]] 통합
- **Soft skill 학습 카테고리 reference**:
  - BetterUp [[betterup-ai-coaching-twilio]] (전담 human coach + AI hybrid) vs LinkedIn Learning (LMS 통합 AI coach only) — 가격·깊이 비교
  - Workday Sana [[workday-sana-for-workday-lms]] (AI-native LMS) vs LinkedIn Learning (전통 LMS + AI 보강)
- **2026 Q3-Q4 KR 컨설팅 deck**:
  - "AI tutor의 진화 단계" 슬라이드: Q&A → adaptive recommendation → role-play scenario → autonomous coaching agent
- **반면교사**:
  - 시장에 자주 인용되는 "90%·160%" 수치는 LinkedIn AI Coaching 자체 KPI가 **아닌** Work Trend Index 일반 통계 — 외부 인용 시 명시 필수
  - LinkedIn AI Coaching 자체 ROI 증거 부족 → POC 4주 자체 측정 권장
  - 한국어 dialect·존댓말 fit 검증 필요 (글로벌 model 한국 시장 fit)
