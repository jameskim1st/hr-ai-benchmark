---
title: "HSBC — Eightfold AI + Gloat + SAP SF 멀티벤더 HR AI"
slug: hsbc-eightfold-gloat-multi-vendor
primary_category: Talent Acquisition
subcategory: Screening & Assessment
tags: [multi-vendor, skills-based-hiring, talent-marketplace, banking, eightfold, gloat, sap]
company: HSBC
industry: [finance, banking]
region: [eu, global]
employee_class: [all]
vendor: [Eightfold AI, Gloat, SAP SuccessFactors, Accenture]
vendor_type: [talent-marketplace, hrms]
output: "Eightfold의 1.6B+ profile 기반 skills inference + Gloat marketplace의 직원-기회 매칭 점수 + career path 추천 + 매니저용 internal candidate 리스트 (140K 직원 enrolled)"
ai_tech_type: [predictive, generative]
ai_tech_subtype: [recommendation-ranking, information-extraction, clustering-classification]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: []
kr_law: AI 기본법 고영향 AI 검토 (채용 스크리닝·내부 이동 매칭)
kr_union: 단체교섭/근로자대표 협의 필요 (인사 의사결정 영향)
kr_language: 미확인 (벤더 확인 필요)
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
sources: [sources/eightfold-hsbc-talent-forward-2025-09.md, sources/gloat-hsbc-customer-story-2022-07.md, sources/accenture-hsbc-talent-acquisition-2026-05.md]
related_usecases:
  - jpmorgan-llm-suite-redeployment
  - workday-as-customer-paradox
related_vendors:
  - gloat
  - sap-successfactors
---

# HSBC — Eightfold AI + Gloat + SAP SF 멀티벤더 HR AI

> ★ **"벤더 3개 + 구현파트너 1개"의 복잡한 실제 배포 사례**: HSBC(220,000명+ 직원 [[sources/gloat-hsbc-customer-story-2022-07]])가 **Eightfold**(skills inferencing) + TechWolf·middleware + **SuccessFactors**를 통합해 인사이트를 확보하려 하고(Noel Brown, Global Head of Enterprise Talent) [[sources/eightfold-hsbc-talent-forward-2025-09]], **Gloat** 탤런트 마켓플레이스를 약 140,000명에게 배포(2022-07 기준) [[sources/gloat-hsbc-customer-story-2022-07]], **Accenture**와 TA 전환을 수행 [[sources/accenture-hsbc-talent-acquisition-2026-05]]. [[workday-as-customer-paradox]]의 "multi-vendor stack" 논의의 실제 대기업 사례.

## Summary

HSBC는 분권화된 TA(채용)·TM(인재관리)을 단일 전략으로 통합하고 스킬 데이터를 활용해 숨은 스킬 발굴·승계 계획·경력 경로 파일럿을 진행 중 [[sources/eightfold-hsbc-talent-forward-2025-09]]. ⚠️ 자사 보고(Eightfold 팟캐스트): Eightfold가 skills inferencing, TechWolf·middleware·SuccessFactors와 결합해 인사이트 확보 [[sources/eightfold-hsbc-talent-forward-2025-09]]. ⚠️ 벤더 주장(Gloat, 2022-07): 탤런트 마켓플레이스가 약 140,000명에게 live, Q1 2023 전 직원 220,000명 대상 확대 계획; ~60,000 unlocked hours, 프로젝트 45% cross-functional, 구조조정 대상 직원 25%가 새 기회 확보 [[sources/gloat-hsbc-customer-story-2022-07]]. ⚠️ 벤더 주장(Accenture): TA 운영비 18% 절감, $28.5M 절감, time-to-hire 35% 단축, 45+ learning asset·250명+ 교육, 35+ 워크플로 간소화 [[sources/accenture-hsbc-talent-acquisition-2026-05]]. 기존 직원 규모 수치·"billion 단위 프로필"·"Fortune Europe AI 채용 공고 비중"은 인용 소스에 없어 수정·삭제 (2026-09-27 grounding 점검).

## Problem / Why (도입 배경)

- **Before (baseline)**: 220,000명+·60개국+ 직원이 스킬 개발·경력 기회에 대한 가시성 부족, 재배치는 수작업·비체계적 [[sources/gloat-hsbc-customer-story-2022-07]]; TA는 전 세계 다수 외부 리크루터에 의존 → 중복 작업·일관성 없는 후보 경험·높은 비용 [[sources/accenture-hsbc-talent-acquisition-2026-05]]; 분권 모델이 의사결정을 지연 [[sources/eightfold-hsbc-talent-forward-2025-09]]
- **Pain point**: 미래 스킬 확보·사일로 해체·내부 이동 활성화 (3대 프로젝트 목표) [[sources/gloat-hsbc-customer-story-2022-07]]; workforce planning 등 역량 확장 어려움 [[sources/accenture-hsbc-talent-acquisition-2026-05]]
- **Trigger**: 기존 방식을 유지하면 경쟁에서 뒤처진다는 경영진 위기의식(Nisbet) → 스킬 중심 전략으로 전환 결정 [[sources/gloat-hsbc-customer-story-2022-07]]; 2024년 Noel Brown이 채용·인재 팀의 변화 적응 프로젝트 주도 [[sources/eightfold-hsbc-talent-forward-2025-09]]

## Solution Architecture

### A. Process (프로세스)

- **Before**: 수작업·ad-hoc 재배치, 사일로화된 팀·기능별 근무 [[sources/gloat-hsbc-customer-story-2022-07]]; 외부 리크루터 의존 채용 [[sources/accenture-hsbc-talent-acquisition-2026-05]]
- **After**:
  1. ⚠️ 자사 보고: middleware·TechWolf·Eightfold(skills inferencing)·SuccessFactors를 결합해 스킬 데이터·인사이트 확보 [[sources/eightfold-hsbc-talent-forward-2025-09]]
  2. ⚠️ 벤더 주장: Gloat 탤런트 마켓플레이스 — Change Enablement 팀과 단계적 launch, 파일럿 성공 후 확대 배포(약 140,000명) [[sources/gloat-hsbc-customer-story-2022-07]]
  3. 직원이 마켓플레이스에서 프로젝트·경험 학습 기회 참여 (사일로에 막혔던 프로젝트 진전 사례) [[sources/gloat-hsbc-customer-story-2022-07]]
  4. 스킬 인접성 기반 경력 경로 파일럿 — 예: 회계 직무가 사이버보안에 80% fit [[sources/eightfold-hsbc-talent-forward-2025-09]]
  5. Accenture와 4대 전략적 조치로 TA 운영 전환 — 45+ learning asset, 250명+ 교육, 35+ 워크플로 간소화 [[sources/accenture-hsbc-talent-acquisition-2026-05]]
- **HITL**: _미공개 (not disclosed)_ — 매니저 승인 절차는 소스에 없음; 매니저 행동 변화가 과제로 언급 [[sources/eightfold-hsbc-talent-forward-2025-09]]
- **Frequency**: _미공개 (not disclosed)_
- **Scope of autonomy**: _미공개 (not disclosed)_

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS**: ⚠️ 자사 보고: SuccessFactors [[sources/eightfold-hsbc-talent-forward-2025-09]]; Gloat은 HSBC의 주요 HR 플랫폼 3개·mainframe과 연동 [[sources/gloat-hsbc-customer-story-2022-07]]
- **AI 시스템 배치**: Eightfold(skills inferencing) + Gloat(talent marketplace) — 별도 SaaS [[sources/eightfold-hsbc-talent-forward-2025-09]] [[sources/gloat-hsbc-customer-story-2022-07]]
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: ⚠️ 자사 보고: "broader middleware technology and TechWolf" [[sources/eightfold-hsbc-talent-forward-2025-09]]; Gloat–mainframe·job 시스템 통합 [[sources/gloat-hsbc-customer-story-2022-07]]
- **사용자 접점**: _미공개 (not disclosed)_
- **인증·권한**: _미공개 (not disclosed)_
- **가용성·SLA**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: 직원 보유 스킬·학습 희망 스킬(Gloat) [[sources/gloat-hsbc-customer-story-2022-07]]; 스킬 추론 데이터(Eightfold) [[sources/eightfold-hsbc-talent-forward-2025-09]]
- **데이터 규모**: 직원 220,000명+ [[sources/gloat-hsbc-customer-story-2022-07]]; Gloat 배포 약 140,000명 (2022-07) [[sources/gloat-hsbc-customer-story-2022-07]]; Eightfold 프로필 수 _미공개 (not disclosed)_
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: _미공개 (not disclosed)_
- **데이터 거버넌스**: _미공개 (not disclosed)_
- **민감정보 처리**: _미공개 (not disclosed)_
- **데이터 출처의 오너십**: HSBC HR 데이터 + 벤더 플랫폼 (혼합) [[sources/eightfold-hsbc-talent-forward-2025-09]] [[sources/gloat-hsbc-customer-story-2022-07]]

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **Model 유형**: skills inferencing(Eightfold) [[sources/eightfold-hsbc-talent-forward-2025-09]]; 직원–기회 매칭(Gloat marketplace) [[sources/gloat-hsbc-customer-story-2022-07]]
- **제공 방식**: 상용 SaaS (Eightfold·Gloat) [[sources/eightfold-hsbc-talent-forward-2025-09]] [[sources/gloat-hsbc-customer-story-2022-07]]
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: _미공개 (not disclosed)_
- **비용·성능 지표**: _미공개 (not disclosed)_
- **Fallback·degradation 전략**: _미공개 (not disclosed)_

### E. Organization & Team (조직·팀 구조)

- **오너십**: HR — Noel Brown(Global Head of Enterprise Talent, 2022 입사) [[sources/eightfold-hsbc-talent-forward-2025-09]]; Hamish Nisbet(Group Head of Resourcing) [[sources/gloat-hsbc-customer-story-2022-07]]
- **참여 역할**: recruiter·hiring manager 250명+ 교육 [[sources/accenture-hsbc-talent-acquisition-2026-05]]
- **팀 규모·기간**: Gloat 파일럿 → 140,000명 확대, Q1 2023 전사 계획 [[sources/gloat-hsbc-customer-story-2022-07]]; TA 프로젝트 2024 [[sources/eightfold-hsbc-talent-forward-2025-09]]
- **거버넌스 체계**: _미공개 (not disclosed)_
- **변화관리**: Gloat Change Enablement 팀과 단계적 launch [[sources/gloat-hsbc-customer-story-2022-07]]; Accenture 변화 전략·커뮤니케이션, 45+ learning asset [[sources/accenture-hsbc-talent-acquisition-2026-05]]
- **파트너**: Accenture (TA 전환) [[sources/accenture-hsbc-talent-acquisition-2026-05]], Gloat, Eightfold, TechWolf [[sources/eightfold-hsbc-talent-forward-2025-09]]

## Impact / Metrics (기대효과)

### 기대효과 요약
Before: 수작업 재배치·외부 리크루터 의존 → After: ⚠️ 벤더 주장 Gloat ~60,000 unlocked hours·프로젝트 45% cross-functional·구조조정 대상 25% 새 기회 [[sources/gloat-hsbc-customer-story-2022-07]]; Accenture 운영비 18%↓·$28.5M 절감·time-to-hire 35%↓ [[sources/accenture-hsbc-talent-acquisition-2026-05]]. Eightfold 관련 정량 성과 _미공개_.

## Key Facts

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| 직원 규모 | **220,000명+** (60개국+) | Gloat case study [[sources/gloat-hsbc-customer-story-2022-07]] | ⚠️ 벤더 게시 (자사 발언 인용) |
| Gloat talent marketplace 배포 | **약 140,000명** live (2022-07), Q1 2023 전사 계획 | Gloat case study [[sources/gloat-hsbc-customer-story-2022-07]] | ⚠️ 벤더 주장 |
| Gloat 성과 | **~60,000** unlocked hours / 프로젝트 **45%** cross-functional / 구조조정 대상 **25%** 새 기회 | Gloat case study [[sources/gloat-hsbc-customer-story-2022-07]] | ⚠️ 벤더 주장 |
| Eightfold | skills inferencing (TechWolf·middleware·SuccessFactors 연계) | Eightfold 팟캐스트 [[sources/eightfold-hsbc-talent-forward-2025-09]] | ⚠️ 자사 보고 (벤더 매개) |
| Accenture TA 전환 | 운영비 **18%**↓ / **$28.5M** 절감 / time-to-hire **35%**↓ | Accenture case study [[sources/accenture-hsbc-talent-acquisition-2026-05]] | ⚠️ 벤더 주장 |
| 교육·자산 | **45+** learning assets / **250명+** 교육 / **35+** 워크플로 간소화 | Accenture case study [[sources/accenture-hsbc-talent-acquisition-2026-05]] | ⚠️ 벤더 주장 |
| Core HRIS | SuccessFactors | Eightfold 팟캐스트 (HSBC 발언) [[sources/eightfold-hsbc-talent-forward-2025-09]] | ⚠️ 자사 보고 |
| AI 채용 공고 비중 (Fortune Europe) | _미공개_ (인용 소스에 없음) | — | ❓ |

## Governance & Risk

- **편향**: 스킬 추론·내부 매칭의 편향 감사 결과 _미공개 (not disclosed)_
- **개인정보**: 스킬 데이터의 벤더 간 이동(Eightfold·TechWolf·Gloat·SuccessFactors) 거버넌스 _미공개_
- **HITL**: _미공개 (not disclosed)_ — 매니저 행동 변화가 파일럿 수용의 과제로 언급 [[sources/eightfold-hsbc-talent-forward-2025-09]]
- **근거 리스크**: 인용 소스 3건 모두 Tier 3 벤더 자료(Eightfold 팟캐스트·Gloat 2022 사례·Accenture 사례) — Gloat 수치는 2022-07 기준으로 stale, Accenture 사례는 사용 AI 벤더를 명시하지 않음
- **규제 노출**: 채용 스크리닝·내부 이동 매칭 → AI 기본법 고영향 AI 검토 대상, EU AI Act Annex III 4(a)(b)

## Contradictions

> [!note] 2026-09-27 grounding — (1) 기존 직원 규모 수치(Gloat 자료보다 큰 값)는 인용 소스에 없음 — Gloat 자료의 "over 220,000 employees"로 수정. (2) "1.6B+ profile 기반 skills inferencing"·"Fortune Europe 30% AI 채용 공고"는 인용 소스에 없어 삭제. (3) "140K 직원 enrolled"는 Gloat raw("live to about 140,000 employees")에 있음 — source 페이지 Limitations의 "본 문서에 없음" 기술은 오류. (4) "인도 tech팀 우선" 서술은 소스에 없어 삭제. (5) 시점 불일치: Gloat 사례 2022-07, Eightfold 팟캐스트 2025-09, Accenture 사례 2026-05 — 세 벤더가 동시 운영 중인지는 소스가 직접 확인하지 않음(Eightfold 팟캐스트에서 SuccessFactors·Eightfold·TechWolf만 언급, Gloat 미언급).

## Consulting Angle

### ★ Multi-vendor HR AI stack의 실제 작동 증거

HSBC의 배포는 [[workday-as-customer-paradox]]에서 이론적으로 논의한 **"multi-vendor HR AI stack"**의 **가장 복잡한 실제 사례**:

```
SAP SuccessFactors (Core HRIS)
    ├── Eightfold AI (Skills-based 채용)
    ├── Gloat (Internal talent marketplace)
    └── Accenture (구현·통합)
```

이는 **Workday 패턴**(suite + point solutions)과 유사하며, **SAP SF의 consolidation 패턴**(Delta/Pepsi가 3rd party 버림)과는 **정반대**. 즉:
- Delta/Pepsi: SF만으로 충분, Gloat·Eightfold 불필요
- **HSBC: SF + Eightfold + Gloat 모두 사용** — SF만으로 불충분

→ "suite consolidation vs multi-vendor"는 **고객의 선택**이지 벤더의 결정이 아님.

### 한국 금융 시사점
- 한국 대형 은행(KB·신한·하나·우리)이 HR AI 도입 시 HSBC가 reference
- 국내 은행은 SAP SF·Workday 도입률이 높으므로 **HSBC의 "SF + point solutions" 패턴**이 가장 현실적 경로
