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
frequency: daily
first_seen: 2025
last_confirmed: 2025
confidence: 0.20
consulting_angle_status: filled
sources:
  - "HireVue case study https://www.hirevue.com/case-studies/cathay-pacific-ondemand-case-study"
related_usecases:
  - hirevue-ai-assessment-bias-audit
  - chipotle-paradox-olivia
related_vendors: []
---

# Cathay Pacific — HireVue AI 면접

⚠️ 벤더 주장: time-to-hire **3개월→2~3주 (90%+↓)**, no-show **30%↓**, 인터뷰 참석 **30%↑**. 아시아 태평양 첫 항공 HR AI 사례. APAC region 첫 use case.

## Solution Architecture

### A. Process (프로세스)

- **Before**: 졸업생 trainee 채용에 3개월 소요, in-person 면접 no-show율 높음
- **After**:
  1. 지원자가 온라인 지원 → ATS에서 HireVue 초대 발송
  2. 후보자가 mobile/web으로 on-demand video 인터뷰 녹화 (graduate 90% 응답률)
  3. HireVue가 응답·언어 사용 (콜로키얼/슬랭 포함) 평가하여 점수 산출
  4. 채용팀이 score·video 검토 후 최종 라운드 후보 shortlist
  5. 통과 후보만 in-person 최종 평가에 초대
  6. Cathay 채용 매니저의 인사말 영상으로 employer branding 강화
- **HITL**: 채용팀이 HireVue score 검토, 최종 면접관이 합격 결정
- **Frequency**: event-driven (graduate/cabin crew intake)
- **Source**: HireVue Cathay Pacific case study


## Impact / Metrics (기대효과)

### 기대효과 요약
Time-to-hire 3개월에서 2~3주로 90%+ 단축, no-show 30% 감소, 면접 참석 30% 증가 (벤더 주장).

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| Time-to-hire | **3개월→2~3주** | HireVue case study | ⚠️ 벤더 주장 |
| No-show 감소 | **30%** | HireVue case study | ⚠️ 벤더 주장 |
| 면접 참석 증가 | **30%** | HireVue case study | ⚠️ 벤더 주장 |

## Consulting Angle
- **APAC region 첫 사례** — 한국·일본·싱가포르 클라이언트에 reference
- HireVue wiki 고객 생태계: Goldman Sachs + **Cathay Pacific** + Emirates + Holcim + Great Southern Bank
