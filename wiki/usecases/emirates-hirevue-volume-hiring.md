---
title: "Emirates — HireVue AI"
slug: emirates-hirevue-volume-hiring
primary_category: Talent Acquisition
subcategory: Interview & Selection
tags: [hirevue, video-interview, airline, middle-east, volume-hiring]
company: Emirates
industry: [airline, aviation]
region: [apac]
employee_class: [all]
vendor: [HireVue]
vendor_type: [point-solution]
output: "영어 평가 점수 (15분 객관식) + situational video 응답 채점 결과 (verbal/written, 벤더 주장 non-verbal cues 포함) + assessment day 진출 후보 shortlist"
ai_tech_type: [predictive, recognition]
ai_tech_subtype: [clustering-classification, speech-recognition]
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
sources: [sources/hirevue-emirates-volume-hiring-2026-09.md]
related_usecases:
  - cathay-pacific-hirevue
  - hirevue-ai-assessment-bias-audit
related_vendors: []
---

# Emirates — HireVue AI 대량 채용

## Summary

Emirates(중동 최대 항공사)가 고객서비스 직군 대량 채용(월 500~1,000명, 수십만 건 지원서)에 HireVue의 **AI-scored Video Interview**와 **Games Based Assessments**를 도입 [[sources/hirevue-emirates-volume-hiring-2026-09]]. ⚠️ 벤더 주장: time-to-hire **60일→7일**, 채용팀 **2/3**를 전략 업무로 재배치, 리크루터·hiring manager **8,000시간** 절감, **$500k** 비용 절감, 후보 CSAT **93%** [[sources/hirevue-emirates-volume-hiring-2026-09]]. 근거는 HireVue 영상 페이지 설명문 1건(Tier 3)뿐이며 측정 기간·기준선·독립 검증 없음.

## Problem / Why (도입 배경)

- **Before (baseline)**: ⚠️ 벤더 주장: time-to-hire 60일 [[sources/hirevue-emirates-volume-hiring-2026-09]]; 그 외 프로세스 baseline ❓ 미공개
- **Pain point**: 규모 — 월 500~1,000명 채용과 수십만 건 지원서를 처리하면서 일관된 글로벌·후보 중심 프로세스 필요 [[sources/hirevue-emirates-volume-hiring-2026-09]]
- **Trigger**: _미공개 (not disclosed)_ — 기존 페이지의 "pandemic 후 cabin crew 재채용" 서술은 인용 소스에 없어 삭제 (2026-09-27 grounding 점검)

## Solution Architecture

### A. Process (프로세스)

- **Before**: _미공개 (not disclosed)_ — 인용 소스는 60일 time-to-hire 외 기존 단계 미기술
- **After** (⚠️ 벤더 주장 [[sources/hirevue-emirates-volume-hiring-2026-09]]):
  1. 대량 지원서 접수 (수십만 건)
  2. HireVue AI-scored Video Interview로 후보 평가 — "job success를 예측하는 skills·motivations" 기준
  3. Games Based Assessments 병행
  4. 일관된 글로벌 프로세스로 funnel 상단 확대
  5. 이후 단계(assessment day·최종 결정): _미공개 (not disclosed)_ — 기존 "15분 객관식 영어 평가·non-verbal cue·assessment day" 서술은 인용 소스 본문에 없어 삭제
- **HITL**: _미공개 (not disclosed)_
- **Trigger & Frequency**: 월 500~1,000명 상시 대량 채용 [[sources/hirevue-emirates-volume-hiring-2026-09]]
- **Scope of autonomy**: _미공개 (not disclosed)_ — AI 채점 결과가 자동 탈락에 쓰이는지 여부 소스에 없음

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS / ATS**: _미공개 (not disclosed)_
- **AI 시스템 배치**: HireVue SaaS (AI-scored Video Interview + Games Based Assessments) [[sources/hirevue-emirates-volume-hiring-2026-09]]
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: _미공개 (not disclosed)_
- **사용자 접점**: _미공개 (not disclosed)_ — 비디오 면접 채널(web·모바일) 미기술
- **인증·권한**: _미공개 (not disclosed)_
- **가용성·SLA**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: ⚠️ 벤더 주장: 후보 비디오 면접 응답, 게임 기반 평가 결과 [[sources/hirevue-emirates-volume-hiring-2026-09]]
- **데이터 규모**: ⚠️ 벤더 주장: 수십만 건 지원서, 월 500~1,000명 채용 [[sources/hirevue-emirates-volume-hiring-2026-09]]
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: _미공개 (not disclosed)_
- **데이터 거버넌스**: _미공개 (not disclosed)_
- **민감정보 처리**: _미공개 (not disclosed)_
- **데이터 출처의 오너십**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **Model 유형**: ⚠️ 벤더 주장: AI 채점(scoring) 모델 — 비디오 면접·게임 평가 [[sources/hirevue-emirates-volume-hiring-2026-09]]; 세부(음성 인식·언어 모델) _미공개_
- **제공 방식**: HireVue 상용 SaaS [[sources/hirevue-emirates-volume-hiring-2026-09]]
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: _미공개 (not disclosed)_ — HireVue 전반의 bias audit은 [[hirevue-ai-assessment-bias-audit]] 참조
- **비용·성능 지표**: _미공개 (not disclosed)_
- **Fallback·degradation 전략**: _미공개 (not disclosed)_

### E. Organization & Team (조직·팀 구조)

- **오너십**: _미공개 (not disclosed)_ — 채용팀(recruitment team) 존재만 언급 [[sources/hirevue-emirates-volume-hiring-2026-09]]
- **참여 역할**: recruiter·hiring manager [[sources/hirevue-emirates-volume-hiring-2026-09]]
- **팀 규모·기간**: _미공개 (not disclosed)_ — 채용팀 2/3 재배치 언급만 [[sources/hirevue-emirates-volume-hiring-2026-09]]
- **거버넌스 체계**: _미공개 (not disclosed)_
- **변화관리**: _미공개 (not disclosed)_
- **파트너**: HireVue [[sources/hirevue-emirates-volume-hiring-2026-09]]

## Impact / Metrics (기대효과)

### 기대효과 요약
Before: time-to-hire 60일 → After: 7일 (⚠️ 벤더 주장). 채용팀 2/3 전략 업무 재배치, 8,000시간 절약, $500k 비용 절감, 후보 CSAT 93% [[sources/hirevue-emirates-volume-hiring-2026-09]]. 측정 기간 _미공개_.

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| Time-to-hire | **60일→7일** | HireVue 영상 페이지 | ⚠️ 벤더 주장 |
| 팀 재배치 | **2/3**가 전략적 업무로 | HireVue 영상 페이지 | ⚠️ 벤더 주장 |
| 시간 절약 | **8,000시간** (recruiter·hiring manager) | HireVue 영상 페이지 | ⚠️ 벤더 주장 |
| 비용 절감 | **$500k** | HireVue 영상 페이지 | ⚠️ 벤더 주장 |
| 후보 만족도 | **CSAT 93%** | HireVue 영상 페이지 | ⚠️ 벤더 주장 |

## Governance & Risk

- **편향**: AI 채점 비디오 면접·게임 평가는 채용 선별에 직접 관여 — 편향 감사 결과·adverse impact 분석은 본 사례에서 _미공개_; HireVue 전반의 제3자 감사는 [[hirevue-ai-assessment-bias-audit]] 참조
- **개인정보**: 후보 영상 데이터의 보존·국외 이전(UAE↔벤더 리전) 정책 _미공개_
- **HITL**: _미공개 (not disclosed)_ — AI 점수의 자동 탈락 활용 여부 불명
- **규제 노출**: 한국 적용 시 AI 기본법 고영향 AI(채용)·채용절차법 AI 면접 고지 의무; EU AI Act Annex III 4(a)
- **근거 리스크**: 모든 수치가 벤더 영상 페이지 설명문 1건(게시일 불명)에 의존 — 제안서 인용 시 "벤더 주장" 명시 필수

## Contradictions

> [!note] 2026-09-27 grounding — 기존 페이지의 "단축률(%)"(60→7일 환산값), "15분 객관식 영어 평가", "non-verbal cues", "assessment day", "pandemic 후 1만 명 cabin crew 재채용", "in-person assessor 최종 결정" 서술은 인용 소스 본문에 없어 삭제·_미공개_ 처리. 원 표기(60일→7일)만 유지.

## Consulting Angle

- **참고 가능 산업·규모**: 항공·유통·콜센터 등 월 수백~수천 명 규모의 대량 채용(volume hiring) 조직 — 특히 글로벌 다국적 지원자 풀을 단일 프로세스로 처리해야 하는 경우
- **제안서·워크숍 용도**: "AI 비디오 면접 + 게임 기반 평가"의 time-to-hire 단축 벤치마크(60일→7일, 벤더 주장)로 사용 — 반드시 ⚠️ 벤더 주장 표기와 측정 기간 미공개를 병기. [[cathay-pacific-hirevue]]와 항공업 pair 사례로 제시 가능
- **반면교사·리스크**: 근거가 벤더 자료 1건 — 독립 검증 없음. AI 채점의 편향 논쟁([[hirevue-ai-assessment-bias-audit]])을 함께 제시해 균형 확보
- **파생 질문**: 한국 항공사·대형 유통사의 승무원·매장직 대량 채용에 적용 시 AI 면접 고지·동의 절차와 탈락자 이의 제기 프로세스를 어떻게 설계할 것인가?
- **한국 적용성 4축**: `kr_law` 채용절차법 AI 면접 고지 + AI 기본법 고영향 AI(채용) / `kr_union` 채용 단계이므로 노조 협의 의무는 낮으나 근로자대표 고지 권고 / `kr_language` 한국어 비디오 면접 채점 지원 여부 미확인 / `kr_vendor` HireVue 국내 파트너 미확인 — 국내 대안은 [[midas-inair-ai-assessment-korea]]
