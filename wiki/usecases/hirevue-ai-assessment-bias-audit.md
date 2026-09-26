---
title: "HireVue — AI 비디오 면접 + 게임 기반 평가"
slug: hirevue-ai-assessment-bias-audit
primary_category: Talent Acquisition
subcategory: Interview & Selection
tags: [video-interview, game-based-assessment, bias-audit, nyc-ll144, compliance]
company: _다수 (major financial institution 등)_
industry: [all]
region: [global]
employee_class: [all]
vendor: [HireVue]
vendor_type: [point-solution]
output: "⚠️ 벤더 주장: 후보자 비디오 면접·게임 기반 평가 결과를 결합한 리크루터용 explainable recommendations (결정 지원, 대체 아님) + DCI Consulting 외부 알고리즘 편향 감사 (역량·게임 기반 알고리즘, 인종·성별·교차 기준, 2023-01 개시·결과 공개 예정)"
ai_tech_type: [predictive]
ai_tech_subtype: [clustering-classification, prediction]
stage: production
visibility: public
case_type: vendor-product
regulatory_exposure: [kr-high-impact, eu-annex-iii]
kr_law: AI 기본법 고영향 AI (채용 평가) + 채용절차법 AI 면접 고지
kr_union: 단체교섭/근로자대표 협의 필요 (인사 의사결정 영향)
kr_language: "미확인 (페이지 명시: 한국어 대응 미확인)"
kr_vendor: 미확인 (국내 파트너 확인 필요)
first_seen_estimated: true
last_confirmed_estimated: true
frequency: daily
first_seen: 2025-06-30
last_confirmed: 2025-06-30
confidence: 0.15
evidence_grade: C
corroborated_by: 0
freshness: stale
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/hirevue-homepage-2026-09.md, sources/hirevue-dci-bias-audit-pr-2023-01.md]
related_usecases:
  - midas-inair-ai-assessment-korea
  - chipotle-paradox-olivia
  - eightfold-ai-talent-intelligence
related_vendors: []
sources_unresolved: [Forrester TEI study (referenced in reviews)]
---

# HireVue — AI 비디오 면접 + 게임 기반 평가

> **이 use case의 핵심 가치**: 제품 기능이 아니라 **bias audit와 compliance 대응**. HireVue는 **NYC Local Law 144 제안 규칙에 따라 DCI Consulting Group 외부 감사**를 의뢰(2023-01)했고, 이전에도 다수의 독립 감사와 업계 최초 AI Explainability Statement를 발간했다고 밝힌다 [[sources/hirevue-dci-bias-audit-pr-2023-01]] — wiki의 Governance 관점에서 가장 가치 있는 Fact.

## Summary

HireVue는 **AI 비디오 면접 + 게임 기반 역량 평가** 플랫폼 (AI Interviewer·Assessments·Video interviewing, 45+ ATS 연동) [[sources/hirevue-homepage-2026-09]]. ⚠️ 벤더 주장: Fortune 100의 40%가 사용, 누적 면접 70M건·평가 200M건 [[sources/hirevue-homepage-2026-09]]. ✅ 2023-01-28 DCI Consulting Group에 알고리즘 외부 편향 감사 의뢰 — 역량 기반·게임 기반 알고리즘을 인종·성별·교차 조합 기준으로 다수 직급·use case에 걸쳐 감사, 결과는 HireVue 웹사이트 공개 예정 [[sources/hirevue-dci-bias-audit-pr-2023-01]]. 기존 페이지의 "time-to-hire 60~89% 단축·만족도 17~25% 향상·Forrester TEI 134% ROI·2020년 facial analysis 제거·ORCAA/Landers 감사·~300건 감사표"는 인용 소스 2건에 없어 _미공개 (not disclosed)_ 처리 (2026-09-27 grounding 점검).

## Problem / Why (도입 배경)

- 🚫 일반론 표기: 벤더 제품이므로 특정 기업의 도입 배경은 고객별 상이. Before baseline·trigger: ❓ 미공개.
- **Pain point (벤더 제시)**: ⚠️ 벤더 주장: 책임 있는 AI 채용에는 투명성·거버넌스·과학적 검증이 필요하며, 조직이 컴플라이언스·규제 요건을 충족하도록 지원 [[sources/hirevue-homepage-2026-09]]
- **규제 Trigger**: NYC Local Law 144 제안 규칙 — HireVue가 외부 감사를 의뢰한 직접 계기 [[sources/hirevue-dci-bias-audit-pr-2023-01]]

## Solution Architecture

### A. Process (프로세스)

- **Before**: _미공개 (not disclosed)_ — 기존 "inference time 학습·bias 점검 없이 운영" 서술은 소스에 없어 삭제
- **After** (bias audit 프로세스, [[sources/hirevue-dci-bias-audit-pr-2023-01]]):
  1. HireVue가 외부 감사기관 DCI Consulting Group(워싱턴 DC 소재 HR 컴플라이언스·데이터 분석 컨설팅)에 감사 의뢰
  2. 역량 기반(competency-based)·게임 기반(game-based) 알고리즘을 인종·성별·인종×성별 교차 기준으로 다수 직급·use case에 걸쳐 감사
  3. 감사는 2023-01 개시, 결과는 완료 후 HireVue 웹사이트에 공개 예정
  4. 알고리즘 lock·재감사 절차·감사표 건수: _미공개 (not disclosed)_
- **채용 프로세스 (제품)**: ⚠️ 벤더 주장: 구조화된 면접 데이터 + 검증된 평가 결과를 결합해 "explainable recommendations"로 리크루터의 결정을 지원(대체 아님) [[sources/hirevue-homepage-2026-09]]
- **HITL**: ⚠️ 벤더 주장: "support—not replace—human decision-making" [[sources/hirevue-homepage-2026-09]]; 감사 결과의 활용 결정 주체 _미공개_
- **Frequency**: _미공개 (not disclosed)_ — 감사 주기 미기술
- **Scope of autonomy**: recommend (⚠️ 벤더 주장 [[sources/hirevue-homepage-2026-09]])

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS / ATS**: ⚠️ 벤더 주장: 45+ ATS 연동("Enriches 45+ ATS") [[sources/hirevue-homepage-2026-09]]
- **AI 시스템 배치**: HireVue SaaS (AI Interviewer·Assessments·Video interviewing) [[sources/hirevue-homepage-2026-09]]
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: ATS 연동 외 _미공개 (not disclosed)_
- **사용자 접점**: _미공개 (not disclosed)_
- **인증·권한**: _미공개 (not disclosed)_
- **가용성·SLA**: ⚠️ 벤더 주장: "Audit-ready platform with advanced scheduling and cheating mitigation" [[sources/hirevue-homepage-2026-09]]

### C. Data (데이터)

- **입력 데이터 소스**: ⚠️ 벤더 주장: 구조화된 면접 데이터, 검증된 평가(assessment) 결과 [[sources/hirevue-homepage-2026-09]]; 감사 대상 데이터의 인구통계 범주: 인종·성별 [[sources/hirevue-dci-bias-audit-pr-2023-01]]
- **데이터 규모**: ⚠️ 벤더 주장: 누적 면접 70M건·평가 200M건 [[sources/hirevue-homepage-2026-09]]
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: _미공개 (not disclosed)_
- **데이터 거버넌스**: ⚠️ 벤더 주장: "enterprise-grade governance practices" [[sources/hirevue-homepage-2026-09]]; 개인정보 처리에 대한 투명 정보 제공(explainability statement) [[sources/hirevue-dci-bias-audit-pr-2023-01]]
- **민감정보 처리**: _미공개 (not disclosed)_
- **데이터 출처의 오너십**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **Model 유형**: 역량 기반·게임 기반 알고리즘 (predictive scoring) [[sources/hirevue-dci-bias-audit-pr-2023-01]]; ⚠️ 벤더 주장: predictive insights [[sources/hirevue-homepage-2026-09]]
- **제공 방식**: HireVue 상용 SaaS [[sources/hirevue-homepage-2026-09]]
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: ✅ DCI Consulting 외부 bias audit (인종·성별·교차), 이전 독립 감사 다수, AI Explainability Statement 발간 [[sources/hirevue-dci-bias-audit-pr-2023-01]]; ⚠️ 벤더 주장: 과학적 검증·구조화 평가·설명가능 추천 [[sources/hirevue-homepage-2026-09]]
- **비용·성능 지표**: _미공개 (not disclosed)_
- **Fallback·degradation 전략**: _미공개 (not disclosed)_

### E. Organization & Team (조직·팀 구조)

- **오너십**: HireVue (벤더 주도 감사) [[sources/hirevue-dci-bias-audit-pr-2023-01]]; 고객사 측 조직 _미공개_
- **참여 역할**: 외부 감사기관 DCI Consulting Group [[sources/hirevue-dci-bias-audit-pr-2023-01]]
- **팀 규모·기간**: 감사 개시 2023-01 [[sources/hirevue-dci-bias-audit-pr-2023-01]]; 기간·인력 _미공개_
- **거버넌스 체계**: ⚠️ 벤더 주장: 윤리적 AI 개발·후보 투명성·프라이버시를 핵심 가치로 명시 [[sources/hirevue-dci-bias-audit-pr-2023-01]]
- **변화관리**: _미공개 (not disclosed)_
- **파트너**: DCI Consulting Group (외부 감사) [[sources/hirevue-dci-bias-audit-pr-2023-01]]

## Impact / Metrics (기대효과)

### 기대효과 요약
⚠️ 벤더 주장만 존재: 홈페이지 규모 수치(Fortune 100의 40%, 면접 70M·평가 200M) [[sources/hirevue-homepage-2026-09]]. 채용 효율 수치·ROI는 인용 소스에 없어 _미공개_.

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| ROI (Forrester TEI) | _미공개_ (인용 소스에 없음; 1차 연구 미확보 — `sources_unresolved` 참조) | — | ❓ |
| Time-to-hire 단축 | _미공개_ (인용 소스에 없음) | — | ❓ |
| 후보자 만족도 향상 | _미공개_ (인용 소스에 없음) | — | ❓ |
| 고객 기반 | **Fortune 100의 40%** | HireVue 홈페이지 | ⚠️ 벤더 주장 |
| 누적 면접 / 평가 | **70M** / **200M** | HireVue 홈페이지 | ⚠️ 벤더 주장 |
| 외부 bias audit | DCI Consulting, 2023-01 개시 | HireVue 보도자료 | ✅ Fact (자사 발표) |

## Governance & Risk

### NYC Local Law 144 bias audit [[sources/hirevue-dci-bias-audit-pr-2023-01]]
- **DCI Consulting Group** (워싱턴 DC 소재 HR 컴플라이언스·데이터 분석 컨설팅)에 의뢰
- NYC LL144 제안 규칙에 따라 algorithm bias audit 실시
- 감사 대상: **역량 기반(competency-based) + 게임 기반(game-based)** 알고리즘
- 감사 축: **인종(race), 성별(gender), 인종×성별 교차** — 복수 직급·use case별로 실시
- 감사 결과 공개: HireVue 웹사이트에 완료 후 게시 예정 — 결과 자체는 인용 소스에 없음
- 이전 이력: 다수의 독립 감사 자발적 수행 + 업계 최초 AI Explainability Statement 발간 (⚠️ 자사 주장)

### 인용 소스에서 확인되지 않은 기존 서술 (2026-09-27 grounding 점검)
- "2020년 facial analysis(표정 분석) 기능 자발적 제거": _미공개 (not disclosed)_ — 별도 소스 필요
- "ORCAA, Landers Workforce Science LLC 별도 감사": _미공개 (not disclosed)_
- "감사표 ~300건", "알고리즘 lab 학습 후 lock": _미공개 (not disclosed)_

### 리스크
- AI 채점 기반 채용 선별 = AI 기본법 고영향 AI(채용)·채용절차법 AI 면접 고지, EU AI Act Annex III 4(a) 해당
- 감사 결과 미확보 상태에서 "편향 없음"으로 인용하면 안 됨 — 감사 의뢰 사실만 Fact

## Contradictions

> [!note] 2026-09-27 grounding — 인용 소스 2건(HireVue 홈페이지 2026-09, DCI 감사 의뢰 보도자료 2023-01)에 "time-to-hire 60~89% 단축", "만족도 17~25% 향상", "Forrester TEI 134% ROI(major financial institution)", "2020 facial analysis 제거", "ORCAA·Landers 감사", "~300건 감사표", "알고리즘 lock" 서술이 없어 모두 _미공개_ 처리. Forrester TEI는 hirevue.com·forrester.com에서 1차 자료를 찾지 못했고 제3자 리뷰 사이트만 인용하므로 1차 연구 확보 전까지 인용 금지(별도 Nucleus Research ROI 사례 존재 여부도 /hr-research 확인 대상).

## Consulting Angle

### ★ Governance 관점에서 wiki 최고 가치 사례

1. **"AI 채용의 편향 감사를 어떻게 하나?"에 대한 가장 구체적 reference**: DCI Consulting + NYC LL144 기반
2. **"facial analysis 제거" 결정**: 인용 소스에서 미확인(_미공개_) — 확인되면 벤더의 자발적 AI 윤리 결정 선례로 "벤더에게 요구해야 할 것" 체크리스트에 활용
3. **Forrester TEI ROI**: 1차 연구 미확보(_미공개_) — 확보 시 Tier 1 독립 분석으로 인용 가능

### vs 마이다스아이티 inAIR

| | HireVue | 마이다스아이티 inAIR |
|---|---|---|
| **검증 유형** | **Bias audit** (편향 감사) | **성과 예측 ���확도** (Nature 논문) |
| **핵심 질문** | "AI가 공정한가?" | "AI가 정확한가?" |
| **감사 기관** | DCI Consulting (외부 독립) | KAIST (학술 독립) |
| **제거한 기능** | facial analysis 제거 주장 — 인용 소스 미확인 | 없음 |
| **NYC LL144 대응** | ✅ 명시적 | ❓ 미공개 |
| **한국 적용** | 한국어 대응 미확인 | ✅ 한국 특화 |

**두 벤더를 함께 제시하면**: "정확도(마이다스아이티) + 공정성(HireVue)"이라는 **채용 AI의 두 축**을 클라이언트에게 설명할 수 있음.

### EU AI Act 관점
- HireVue의 bias audit approach는 **EU AI Act의 high-risk 시스템 요구사항** (Article 9: Risk Management, Article 10: Data Governance, Article 14: Human Oversight)에 가장 가까운 현존 실무
- Annex III 고용 영역 의무 적용(2027-12-02로 연기) 전에 "이미 이렇게 하는 벤더가 있다"는 증거
