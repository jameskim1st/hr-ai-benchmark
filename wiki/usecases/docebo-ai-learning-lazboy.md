---
title: "Docebo AI Learning — La-Z-Boy (179% 활성 사용자↑, 85% 과정 완료↑)"
slug: docebo-ai-learning-lazboy
primary_category: Learning & Development
subcategory: Content & Delivery
tags: [lms, ai-native, microlearning, content-generation, lazboy, docebo]
company: La-Z-Boy
industry: [manufacturing, furniture, retail]
region: [na]
employee_class: [all]
vendor: [Docebo]
vendor_type: [lxp]
output: "AI 자동 생성 신규 과정 outline·퀴즈·요약 + 직무·이력 기반 adaptive 다음 과정 추천 + AI virtual coach 대화 답변 + L&D dashboard KPI (active learner·completion)"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [text-generation, summarization-qa, recommendation-ranking]
stage: production
frequency: daily
first_seen: 2025
last_confirmed: 2025
confidence: 0.40               # Tier 3 vendor(+0.10) + Tier 2 G2(+0.20) + Tier 1 Bersin L&D Revolution(+0.35, Docebo 부분은 독립 분석) = base 0.65, 할인 (La-Z-Boy 구체 metric은 벤더 자체 주장, Bersin은 Docebo 플랫폼 분석이지 La-Z-Boy 사례 독립 검증 아님) → 0.40
consulting_angle_status: filled
sources:
  - "Docebo customers https://www.docebo.com/customers/"
  - "Docebo Learning Platform https://www.docebo.com/learning-platform/"
  - sources/bersin-ld-revolution-2025-06.md
related_usecases:
  - bersin-galileo-learn-ai-native-lms
related_vendors: []
---

# Docebo AI Learning — La-Z-Boy + Disguise + Brooks

## Summary

Docebo는 **AI-native LMS/LXP** (3,900+ 고객, 70개국, 30M+ 사용자). **Josh Bersin**(Tier 1)의 2025-06 독립 분석에서 "traditional → AI-native 전환 중"으로 분류된 학습 플랫폼 ([[bersin-ld-revolution-2025-06]]). Bersin이 Project Harmony(neural search), dynamic content generation, virtual coaching 등 AI 기능을 독립적으로 확인. 가장 구체적 고객 사례는 **La-Z-Boy**: ⚠️ 벤더 주장 — **활성 LMS 사용자 179% YoY 증가, 과정 완료율 85% 증가**. Disguise는 활성 learner 4x 증가, 학습 수익 45% 증가. Brooks Automation은 교육 시간·비용 20% 절감.

## Solution Architecture

### A. Process

- **Before**: La-Z-Boy (10k+ 글로벌 직원, 가구 제조·소매)가 15년 된 LMS 사용. 잦은 crash·낮은 engagement, 신상품·VOC 트레이닝 콘텐츠 제작에 instructional designer 수개월 소요
- **After**:
  1. L&D 팀이 Docebo Learning Suite로 마이그레이션, 글로벌 dealer·corporate 대상 통합 카탈로그 구성
  2. Docebo AI가 기존 콘텐츠·정책 문서 학습해 신규 과정 outline·퀴즈·요약 자동 생성
  3. AI virtual coach (beta)가 학습자 질문에 답변, use case template로 instructor 콘텐츠 제작 가속
  4. Adaptive recommendation이 직무·완료 이력 기반 다음 과정 제시
  5. L&D 관리자는 dashboard에서 active learner·completion·engagement KPI 추적
- **HITL**: SME가 AI 생성 콘텐츠 검토·승인, L&D 매니저가 카탈로그 큐레이션
- **Frequency**: 학습 = daily, 콘텐츠 generation = adhoc, KPI 리뷰 = monthly

### B. System & Infrastructure (R9 research)

- **Core HRIS**: La-Z-Boy 측 _미공개_ — Docebo는 stand-alone LMS/LXP
- **AI 시스템 배치**: ✅ Docebo Learning Suite SaaS (AI-native 전환 중)
- **배포 환경**: _미공개_ — Docebo AWS multi-tenant SaaS 일반
- **연동·통합**: SCORM·xAPI 표준, HRIS SSO, 글로벌 dealer·corporate 통합 카탈로그
- **사용자 접점**: ✅ Docebo web·모바일 — 학습자·instructor·L&D 매니저 dashboard
- **인증·권한**: 기업 SSO + RBAC

### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 기존 콘텐츠·정책 문서 (생성 학습용), 직무·완료 이력 (recommendation), VOC·신상품 자료 (La-Z-Boy)
- **데이터 규모**: ✅ Docebo 30M+ 사용자, 3,900+ 고객 / La-Z-Boy 10K+ 글로벌
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: ✅ Project Harmony (neural search — embedding). Dynamic content generation은 LLM (구체 _미공개_)
- **데이터 거버넌스**: _미공개_
- **민감정보 처리**: _미공개_

### D. Model (R9 research)

- **Foundation model**: _미공개_ — Docebo AI 핵심 underlying model 비공개
- **모델 유형**: ✅ generative (content·virtual coach) + embedding (neural search) + recommendation
- **제공 방식**: Docebo 자체 통합 (SaaS)
- **커스터마이징 기법**: ✅ Use-case instructional templates, Collaborative content design (AI 보조)
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: ⚠️ SME가 AI 생성 콘텐츠 검토·승인 (HITL) — 자동 quality scoring 미공개


## Impact / Metrics (기대효과)

### 기대효과 요약
La-Z-Boy 기준 활성 LMS 사용자 179% YoY 증가, 과정 완료율 85% 증가 (벤더 주장). Disguise는 활성 learner 4배 증가.

### La-Z-Boy (가구 제조·리테일) ⭐

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| 활성 LMS 사용자 | **179% YoY 증가** | Docebo customers | ⚠️ 벤더 주장 |
| 과정 완료율 | **85% 증가** | Docebo customers | ⚠️ 벤더 주장 |
| 배경 | 기존 outdated LMS를 Docebo로 교체 → 글로벌 일관 branded training | Docebo | ⚠️ 벤더 주장 |

### Disguise (미디어 테크)

| 지표 | 값 |
|---|---|
| 활성 learner | **4x 증가** |
| 학습 수익 | **45% 증가** |
| 방식 | 8 SCORM courses → **80+ 마이크로러닝 모듈** 전환 |

### Brooks Automation

| 지표 | 값 |
|---|---|
| Training time·cost | **20% 절감** |

## Solution Architecture (요약)

### Docebo AI 핵심 기능 (2025)
- **Dynamic content generation** — AI가 자동 학습 콘텐츠 생성
- **Virtual coaching** (beta) — AI 기반 가상 코칭
- **Project Harmony** — neural search로 콘텐츠 발견 최적화
- **Collaborative content design** — AI 보조 협업 콘텐츠 제작
- **Use-case instructional templates** — 산업·역할별 맞춤 템플릿

### 시장 포지션 (Bersin 2025-06 비교)
- Cornerstone (7,000+) = Traditional + AI
- **Docebo (3,900+)** = **Transitioning to AI-native**
- Sana/Galileo = All-AI native (초기)

→ Docebo는 "전통 LMS의 AI 전환"이라는 **가장 현실적인 migration 경로**를 대표

## Consulting Angle

### 핵심 가치
- **"기존 LMS를 AI-native로 교체"하는 migration 사례의 대표**: La-Z-Boy가 outdated LMS → Docebo로 전환해 179% 사용자 증가를 달성한 것이 **한국 기업의 LMS 교체 프로젝트**에 직접 reference
- **Bersin Galileo Learn과의 대비**: Galileo는 "처음부터 AI-native"이고 고객 극소수, Docebo는 "전통 → AI 전환"이고 3,900+ 고객. **Risk-averse 한국 대기업**에는 Docebo 경로가 더 현실적
- **Disguise 사례의 "SCORM → microlearning" 전환**: 8개 코스 → 80+ 마이크로러닝 = AI가 콘텐츠 granularity를 바꾼 직접적 예시

### 한국 적용
- 국내 대기업 LMS: 삼성 멀티캠퍼스, 휴넷, 더존 러닝 등이 사용 중 — Docebo처럼 AI 전환 중인 곳이 있는지 조사 필요
- 한국어 콘텐츠 품질·법정교육(산업안전·성희롱 예방 등) 자동 생성 대응력이 핵심 fit 판단 기준
