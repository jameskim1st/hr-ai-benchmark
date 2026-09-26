---
title: "BetterUp — AI Coaching Platform"
slug: betterup-ai-coaching-twilio
primary_category: Performance & Talent Management
subcategory: Coaching
tags: [ai-coaching, leadership, retention, performance, twilio, betterup, roi]
company: Twilio
industry: [tech, saas]
region: [na]
employee_class: [all]
vendor: [BetterUp]
vendor_type: [point-solution]
output: "매니저별 Whole Person Assessment 점수 + 개인화 6개월 learning path + AI coach 대화형 nudge·micro-intervention + behavior change → 비즈니스 KPI(retention·promotion) 매핑 dashboard"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [summarization-qa, recommendation-ranking]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: []
kr_law: 일반 개인정보보호법 수준 (코칭 대화 데이터)
kr_union: 협의 의무 낮음 (개인 코칭·개발 성격)
kr_language: 미확인 — 한국어 대응 검증 안 됨 (페이지 명시)
kr_vendor: 미확인 (국내 파트너 확인 필요)
first_seen_estimated: true
last_confirmed_estimated: true
frequency: monthly
first_seen: 2025-06-30
last_confirmed: 2025-06-30
confidence: 0.35
evidence_grade: B
corroborated_by: 1
freshness: stale
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/betterup-roi-page-2026-09.md, sources/inc-betterup-ai-only-coaching-2025-08.md, sources/betterup-customers-page-2026-09.md, sources/bersin-betterup-manage-ai-coaching-2024-04.md, sources/hrexecutive-bersin-coaching-disruptions-2024.md]
related_usecases:
  - moderna-self-review-gpt
related_vendors: []
---

# BetterUp — AI Coaching Platform

## Summary

BetterUp은 **AI 기반 리더십·매니저 코칭** 플랫폼. 2025-04 **BetterUp Grow** (AI-only 코칭 제품) 출시 — ⚠️ 벤더 주장(Inc. 전달, 원문 미확보): 초기 테스트 고객 만족 95%·성과 16% 향상. [[sources/inc-betterup-ai-only-coaching-2025-08.md]] 가장 강력한 레퍼런스는 **Twilio (8,000+ 직원 전원 롤아웃)**: ⚠️ 벤더 주장: 2년 후 분석에서 코칭 받은 직원은 **고성과 평가 가능성 32% 높고, 이탈 가능성 5배 낮음** — human coaching 결과. [[sources/betterup-roi-page-2026-09.md]] 다수 고객에서 수치가 공개돼 있으나 모두 벤더 페이지 전달. (2026-09-27 grounding 점검: 종전 "비용 70퍼센트 절감", "Leadership ROI 600퍼센트"는 인용 소스에 없어 제거.) **Josh Bersin**(Tier 1, 단 BetterUp advisor)이 BetterUp Manage를 "pioneering AI-powered platform for leaders"로 독립 분석 ([[bersin-betterup-manage-ai-coaching-2024-04]]). **HR Executive**(Tier 2)도 Bersin의 코칭 시장 분석을 보도 ([[hrexecutive-bersin-coaching-disruptions-2024]]).

## Problem / Why (도입 배경)

- 리더십·매니저 코칭은 효과가 있지만 **전통 human coaching은 비용이 높아 소수 임원에게만 제공** 가능
- 중간 관리자·일반 직원까지 코칭을 확장하려면 **비용 절감 + 스케일** 필요
- 코칭 효과의 **ROI 정량 측정**이 어려워 HR budget에서 정당화 곤란

## Solution Architecture

### A. Process (프로세스)

- **Before**: ⚠️ 벤더 주장 (Twilio): "어떤 도전에도 대응할 수 있는 비즈니스"를 목표로 리더 코칭 도입. [[sources/betterup-roi-page-2026-09.md]] 도입 전 매니저 역량 baseline ❓ 미공개
- **After**:
  1. ⚠️ 벤더 주장 (Twilio): 리더 대상 코칭 → 8,000+ 전 직원으로 롤아웃. [[sources/betterup-roi-page-2026-09.md]]
  2. ✅ Bersin (BetterUp advisor — COI): BetterUp Manage = AI 기반 Whole Person assessment + 맞춤 학습 경로(주별) + 전문 코치 + AI-driven narrative support 결합. [[sources/bersin-betterup-manage-ai-coaching-2024-04.md]]
  3. ⚠️ 벤더 주장 (Inc. 전달): BetterUp Grow — AI-only 코칭 (2021 개발 시작, 2025-04 출시), 개발 시간 대부분을 안전 가드레일에 투입. [[sources/inc-betterup-ai-only-coaching-2025-08.md]]
  4. ⚠️ 벤더 주장 (Twilio): 2년 후 코칭 효과 분석 (고성과 평가·이탈). [[sources/betterup-roi-page-2026-09.md]]
  (종전 "6개월 learning path·주별 micro-intervention·scenario 질문·dashboard 매핑" 단계는 인용 소스에 없어 제거)
- **HITL**: ✅ Bersin: 전문 코치(human) + AI 결합. [[sources/bersin-betterup-manage-ai-coaching-2024-04.md]] Grow는 AI-only. [[sources/inc-betterup-ai-only-coaching-2025-08.md]]
- **Frequency**: ✅ Bersin: 주별 맞춤 학습 경로. [[sources/bersin-betterup-manage-ai-coaching-2024-04.md]] 그 외 _미공개_

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS**: _미공개 (not disclosed)_
- **AI 시스템 배치**: ✅ BetterUp Manage (AI assessment + human coach) [[sources/bersin-betterup-manage-ai-coaching-2024-04.md]] + ⚠️ 벤더 주장: BetterUp Grow (AI-only). [[sources/inc-betterup-ai-only-coaching-2025-08.md]]
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: _미공개 (not disclosed)_
- **사용자 접점**: _미공개 (not disclosed)_
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: ✅ Bersin: Whole Person assessment (soft-skills 시나리오 매칭). [[sources/bersin-betterup-manage-ai-coaching-2024-04.md]] 그 외 _미공개_
- **데이터 규모**: ⚠️ 벤더 주장: Twilio 8,000+ 직원 전원. [[sources/betterup-roi-page-2026-09.md]]
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: _미공개 (not disclosed)_
- **데이터 거버넌스**: _미공개 (not disclosed)_
- **민감정보 처리**: _미공개_ — 멘탈헬스 인접 — HIPAA·GDPR 별도 명시 없음

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **모델 유형**: _미공개 (not disclosed)_ — ✅ Bersin: "AI-enabled assessment… AI-driven narrative support". [[sources/bersin-betterup-manage-ai-coaching-2024-04.md]]
- **제공 방식**: _미공개 (not disclosed)_
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: ⚠️ 벤더 주장 (Inc. 전달, 원문 미확보): 안전 가드레일에 개발 시간 대부분 투입; 초기 테스트 고객 만족 95% — 독립 검증 부재. [[sources/inc-betterup-ai-only-coaching-2025-08.md]]

### E. Organization & Team (조직·팀 구조)

- **오너십**: BetterUp 벤더 (CEO Alexi Robichaux). [[sources/inc-betterup-ai-only-coaching-2025-08.md]] Twilio 측 담당 조직 _미공개_
- **참여 역할**: _미공개 (not disclosed)_
- **팀 규모·기간**: ⚠️ 벤더 주장: Twilio 2년 운영 후 분석. [[sources/betterup-roi-page-2026-09.md]]
- **거버넌스 체계**: _미공개 (not disclosed)_
- **파트너**: ✅ Josh Bersin — BetterUp 공식 advisor (분석 시 COI). [[sources/bersin-betterup-manage-ai-coaching-2024-04.md]]

## Governance & Risk

- ⚠️ Twilio 수치(32%·5x)는 벤더 페이지가 고객 내부 분석을 전달 — 코칭 참여자 self-selection 편향 가능, 비교군 통제 _미공개_. [[sources/betterup-roi-page-2026-09.md]]
- ⚠️ Bersin 분석은 Tier 1이나 BetterUp advisor로서 이해관계 있음. [[sources/bersin-betterup-manage-ai-coaching-2024-04.md]]
- 코칭 대화 데이터의 보존·접근·employer 공유 정책: _미공개 (not disclosed)_
- 멘탈헬스 인접 영역의 AI-only 코칭 안전성: 벤더 가드레일 주장 외 독립 평가 _미공개_

## Contradictions

> [!note] 2026-09-27 grounding — 종전 본문의 "비용 70퍼센트 절감", "Leadership ROI 600퍼센트 average", "채택 기업 11곳·50+ pipeline", "매니저 effectiveness 70퍼센트", "6개월 learning path·weekly micro-intervention", "SSO·SCIM·VR·RBAC", "Martin Seligman prompt·rubric", "disaggregated form 정책"은 인용 소스 5건의 raw 어디에도 없어 제거·_미공개_ 처리. Inc.·HR Executive 소스는 원문 미확보(403)라 95퍼센트·16퍼센트도 검색 스니펫 기반 벤더 주장으로만 기재.


## Impact / Metrics (기대효과)

### 기대효과 요약
AI 코칭 수혜 직원의 고성과 평가 확률 32% 향상, 이탈률 5배 감소 (벤더 주장 기반, Twilio 사례).

### Twilio (8,000+ 직원, named customer) ★

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| 고성과 평가 확률 | 코칭 받은 직원이 **32% 더 높음** (2년 후 분석) | [[sources/betterup-roi-page-2026-09.md]] | ⚠️ 벤더 주장 (human coaching) |
| 이탈률 | 코칭 받은 직원이 **5x 덜 이탈** | [[sources/betterup-roi-page-2026-09.md]] | ⚠️ 벤더 주장 (human coaching) |

### 기타 고객 사례 (BetterUp ROI 페이지)

| 사례 | 지표 | 값 | 출처 |
|---|---|---|---|
| Chipotle | 승진율 | 본사 **1.2x** / 현장 리더 **1.8x** | [[sources/betterup-roi-page-2026-09.md]] ⚠️ 벤더 주장 |
| Sales 조직 (익명) | Quota hitting | 코칭 매니저 팀 **1.6x** (전년 대비) | [[sources/betterup-roi-page-2026-09.md]] ⚠️ 벤더 주장 |
| 익명 고객 | Attrition | **4.3x** 낮음 / **$14M** 절감 | [[sources/betterup-roi-page-2026-09.md]] ⚠️ 벤더 주장 |
| Moderna | 팀 결속 | **16%** 향상 (사례 카드 제목) | [[sources/betterup-customers-page-2026-09.md]] ⚠️ 벤더 주장 |

### BetterUp Grow AI 제품

| 지표 | 값 | 출처 |
|---|---|---|
| User satisfaction (초기 테스트) | **95%** | [[sources/inc-betterup-ai-only-coaching-2025-08.md]] ⚠️ 벤더 주장 (Inc. 전달, 원문 미확보) |
| 성과 향상 (초기 테스트) | **16%** | [[sources/inc-betterup-ai-only-coaching-2025-08.md]] ⚠️ 벤더 주장 (Inc. 전달, 원문 미확보) |
| 비용 vs human coaching | _미공개_ | (수치 근거 미확보 — 2026-09-27 grounding 점검) |
| 채택 기업 수 | _미공개_ | (수치 근거 미확보) |
| Leadership ROI | _미공개_ | (수치 근거 미확보 — 2026-09-27 grounding 점검) |

**⚠️ 모든 수치가 벤더 자체 주장**. AI-only 제품(Grow)의 outcome 수치는 초기 테스트 만족도·성과 향상만 존재하며, Twilio 등 ROI 수치는 human coaching 결과.

## Consulting Angle

### 핵심 가치
- **코칭 카테고리의 가장 구체적 ROI 사례**: Twilio 이름 + 32%·5x 수치는 CHRO에 직접 제시 가능 — 단 human coaching 결과이며 벤더 페이지 전달임을 명시
- **"AI coaching democratization" 논의의 앵커**: "임원만 받던 코칭을 전 직원에게" = 한국 대기업 HR에서도 관심 높은 주제
- **Human vs AI coaching trade-off 논의**: BetterUp는 두 모델 모두 운영 → "어디까지 AI가, 어디서부터 사람이"를 데이터로 판단 가능

### 한국 적용
- 국내 대기업 리더십 개발(LMD) 프로그램에 AI coaching 도입 시 BetterUp이 reference
- 단, **한국어 대응·한국 리더십 문화 fit**은 검증 안 됨
- 국내 경쟁: 코칭업·마인드풀리 등 한국 코칭 스타트업의 AI 전략과 비교 필요

### 주의
- Twilio 수치(32%·5x)의 **측정 방법론** 미공개 — 선택 편향(자발적 코칭 참여자 = 원래 고성과자) 가능성
- Inc.com이 "95% satisfaction"을 보도했지만 이는 BetterUp 자체 측정 — Tier 2 매체가 **전달**한 것이지 **검증**한 것은 아님
