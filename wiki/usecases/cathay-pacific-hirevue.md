---
title: "Cathay Pacific — HireVue AI 면접"
slug: cathay-pacific-hirevue
primary_category: Talent Acquisition
subcategory: Interview & Selection
tags: [hirevue, video-interview, airline, asia-pacific, volume-hiring]
company: Cathay Pacific
industry: [airline, aviation]
region: [apac]
employee_class: [all]
vendor: [HireVue]
vendor_type: [point-solution]
output: "후보자 on-demand video 응답 점수 (언어/콜로키얼 평가 포함) + 채용팀 검토용 shortlist + in-person 최종평가 진출자 결정"
ai_tech_type: [generative, predictive, recognition]
ai_tech_subtype: [summarization-qa, clustering-classification, speech-recognition]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: [kr-high-impact, eu-annex-iii]
kr_law: 채용절차법 AI 면접 고지 + AI 기본법 고영향 AI(채용)
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
sources: [sources/hirevue-cathay-pacific-case-study-2026-09.md]
related_usecases:
  - hirevue-ai-assessment-bias-audit
  - chipotle-paradox-olivia
related_vendors: []
---

# Cathay Pacific — HireVue 비디오 면접

## Summary

Cathay Pacific이 고객서비스·승무원 직군 채용(주 300건+ 지원)에서 전화 스크리닝을 HireVue OnDemand 비디오 면접으로 대체. ⚠️ 벤더 주장: 채용 기간 **3개월 → 2~3주**, 최종 면접 no-show 크게 감소(수치 _미공개_), 졸업생 채용에서 초청 학생의 90%가 비디오 면접 완료. [[sources/hirevue-cathay-pacific-case-study-2026-09.md]] 소스는 AI 채점을 언급하지 않음 — recruiter가 검토하는 비디오 스크리닝 사례. APAC 항공 채용 reference. (2026-09-27 grounding 점검: 종전 "no-show 30퍼센트↓·면접 참석 30퍼센트↑·AI 언어 평가 점수"는 소스 오독·미기재로 정정 — Contradictions 참조.)

## Problem / Why (도입 배경)

- **Before**: ⚠️ 벤더 주장: 주 300건 이상 지원 → CV 스크리닝 → 전화 → 그룹 면접 → 대면 면접의 수작업 프로세스로 수개월 소요; 그룹 면접 no-show 평균 30%. [[sources/hirevue-cathay-pacific-case-study-2026-09.md]]
- **Pain point**: ⚠️ 벤더 주장: 후보자와의 "phone tag"와 그룹 면접 no-show로 충원 지연 (시간·규모 축). [[sources/hirevue-cathay-pacific-case-study-2026-09.md]]
- **Trigger**: ❓ 미공개

## Solution Architecture

### A. Process (프로세스)

- **Before**: ⚠️ 벤더 주장: CV 스크리닝 → 전화 스크리닝 → 그룹 면접 → 대면 면접 (수개월). [[sources/hirevue-cathay-pacific-case-study-2026-09.md]]
- **After**:
  1. ⚠️ 벤더 주장: 전화 스크리닝을 단일 HireVue OnDemand 비디오 면접으로 대체 — 프로세스 단계 축소. [[sources/hirevue-cathay-pacific-case-study-2026-09.md]]
  2. ⚠️ 벤더 주장: 졸업생 채용 — 초청 학생 90%가 비디오 면접 완료. [[sources/hirevue-cathay-pacific-case-study-2026-09.md]]
  3. 비디오 검토·shortlist 방식: _미공개_ (소스는 AI 채점을 언급하지 않음)
  (종전 "HireVue가 콜로키얼/슬랭 포함 언어 사용을 평가해 점수 산출", "ATS 초대", "채용 매니저 인사말 영상" 서술은 소스에 없어 제거)
- **HITL**: _미공개 (not disclosed)_ — 소스상 AI 자동 채점 언급 없음
- **Frequency**: ⚠️ 벤더 주장: 상시 지원(주 300건+). [[sources/hirevue-cathay-pacific-case-study-2026-09.md]]
- **Scope of autonomy**: _미공개 (not disclosed)_

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS / ATS**: _미공개 (not disclosed)_
- **AI 시스템 배치**: ⚠️ 벤더 주장: HireVue OnDemand 비디오 면접 (별도 SaaS). [[sources/hirevue-cathay-pacific-case-study-2026-09.md]]
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: _미공개 (not disclosed)_
- **사용자 접점**: _미공개 (not disclosed)_
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: ⚠️ 벤더 주장: 후보자 비디오 면접 응답. [[sources/hirevue-cathay-pacific-case-study-2026-09.md]]
- **데이터 규모**: ⚠️ 벤더 주장: 주 300건+ 지원 (고객서비스·승무원). [[sources/hirevue-cathay-pacific-case-study-2026-09.md]]
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: _미공개 (not disclosed)_
- **데이터 거버넌스**: _미공개 (not disclosed)_
- **민감정보 처리**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **Model 유형**: _미공개 (not disclosed)_ — 소스에 AI 채점·언어 평가 언급 없음
- **제공 방식**: _미공개 (not disclosed)_
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **평가·가드레일**: _미공개 (not disclosed)_

### E. Organization & Team (조직·팀 구조)

- **오너십**: _미공개 (not disclosed)_
- **참여 역할**: _미공개 (not disclosed)_
- **팀 규모·기간**: _미공개 (not disclosed)_
- **거버넌스 체계**: _미공개 (not disclosed)_
- **파트너**: _미공개 (not disclosed)_

## Impact / Metrics (기대효과)

### 기대효과 요약
Before: 채용 기간 3개월, 그룹 면접 no-show 평균 30% → After: ⚠️ 벤더 주장 채용 기간 2~3주, 최종 면접 no-show "크게 감소"(수치 미공개).

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| Time-to-hire | **3개월 → 2~3주** | [[sources/hirevue-cathay-pacific-case-study-2026-09.md]] | ⚠️ 벤더 주장 |
| No-show (baseline) | 그룹 면접 평균 **30%** (도입 전) | [[sources/hirevue-cathay-pacific-case-study-2026-09.md]] | ⚠️ 벤더 주장 |
| No-show 감소폭 | _미공개_ ("크게 감소") | [[sources/hirevue-cathay-pacific-case-study-2026-09.md]] | (수치 근거 미확보 — 2026-09-27 grounding 점검) |
| 졸업생 비디오 면접 완료율 | **90%** | [[sources/hirevue-cathay-pacific-case-study-2026-09.md]] | ⚠️ 벤더 주장 |
| 면접 참석 증가 | _미공개_ | — | (종전 "30퍼센트↑"는 소스 오독 — 제거) |

## Governance & Risk

- 비디오 면접 채용은 한국 채용절차법 AI 면접 고지·AI 기본법 고영향 AI(채용) 검토 대상, EU AI Act Annex III — `regulatory_exposure` 참조
- 소스상 AI 자동 채점 언급이 없으므로 "AI 면접"으로 소개할 경우 과장 위험 — "비디오 스크리닝(recruiter 검토)"으로 표현
- 측정 기간·표본·편향 감사: _미공개 (not disclosed)_ ([[hirevue-ai-assessment-bias-audit]] 참조)

## Contradictions

> [!note] 2026-09-27 grounding — 종전 본문의 "no-show 30퍼센트 감소·면접 참석 30퍼센트 증가"는 원문의 "그룹 면접 no-show 평균 30퍼센트"(도입 전 baseline)를 감소 수치로 오독한 것 → baseline으로 정정, 감소폭은 _미공개_. "HireVue가 언어 사용(콜로키얼/슬랭)을 평가해 점수 산출"은 소스에 없음(AI 채점 언급 없음) → 제거. 벤더 사례 페이지 게시일 불명.

## Consulting Angle
- **APAC 항공 채용 reference** — 한국·일본·싱가포르 클라이언트에 대량 채용(승무원·고객서비스) 비디오 스크리닝 사례로 제시. 단, AI 채점이 아닌 비디오 스크리닝 사례임을 명시
- **제안서 활용**: "전화 스크리닝 단계 제거 → 채용 기간 단축" 논리의 정량 예시 (3개월 → 2~3주, ⚠️ 벤더 주장). no-show 30퍼센트는 도입 전 baseline이므로 감소 효과 수치로 인용 금지
- **한국 적용성**: 채용절차법상 AI 면접 고지 의무·AI 기본법 고영향 AI(채용) 검토 필요; 한국어 비디오 면접 지원 여부 미확인 — POC 검증
- **파생 질문**: "국내 항공사·서비스업 대량 채용에서 그룹 면접 no-show 비율은 얼마이며, 비디오 스크리닝으로 어느 정도 개선 가능한가?"
- HireVue wiki 고객 생태계: Goldman Sachs + **Cathay Pacific** + Emirates + Holcim + Great Southern Bank
