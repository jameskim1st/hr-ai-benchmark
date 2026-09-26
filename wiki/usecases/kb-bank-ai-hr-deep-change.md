---
title: "KB국민은행 — 'HR Deep Change' AI 영업점 인사이동"
slug: kb-bank-ai-hr-deep-change
primary_category: Strategic Workforce & Governance
subcategory: Workforce Planning
tags: [kb-bank, hr-deep-change, ai-staffing, internal-mobility, machine-learning, korean-bank, 1100-staff, pb-rm, korea, public-best-practice]
company: KB국민은행
industry: [finance, banking]
region: [kr]
employee_class: [전임직, 기술사무직]
vendor: [KB국민은행 internal]
vendor_type: [internal-build]
output: "1,100+ 영업점 직원 인사 배치안 (출퇴근·자격증·업무 경력·육아 고충 등 수십 변수 다변량 최적화). HR 검토·조정 후 매니저·직원 통보. 2025 PB·RM 상담 직원에게는 AI 활용 추천"
ai_tech_type: [decision-optimization, predictive]
ai_tech_subtype: [optimization, clustering-classification]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: [kr-high-impact-review, eu-annex-iii]
kr_law: AI 기본법 고영향 AI (인사이동) — 인적감독·설명가능성 (페이지 명시)
kr_union: 노조 사전 합의 필수 (페이지 명시; 합의 process 세부 미공개)
kr_language: 한국어 네이티브
kr_vendor: KB국민은행 자체 구축 (SI 수행사 미공개)
frequency: monthly
first_seen: 2020-07-15
last_confirmed: 2026-04-01
confidence: 0.8
evidence_grade: A
corroborated_by: 4
freshness: fresh
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/asiatoday-kb-bank-ai-personnel-deep-change-2020-07.md, sources/etnews-kb-ai-hr-system-2022-12.md, sources/etnews-kb-ai-hr-system-2022-12.md, sources/hankyung-kb-bank-pb-rm-ai-57pct-2025-10.md, sources/sedaily-kb-ai-hr-commute-2020-07.md]
related_usecases:
  - shinhan-bank-ai-one-platform
  - shinhan-bank-ai-staffing-algorithm
  - ibm-blue-match-internal-mobility
related_vendors: []
---

## Summary

KB국민은행 **HR Deep Change** — 2020-07-10 단행한 하반기 인사에서 직원 1100여 명의 배치를 AI 알고리즘으로 결정: 업무경력·근무기간·자격증·출퇴근 거리 등을 고려해 최적 근무지 배치, 인사제도 전반의 "총체적 변화(Deep Change)" 첫 단계 [[sources/asiatoday-kb-bank-ai-personnel-deep-change-2020-07]] [[sources/sedaily-kb-ai-hr-commute-2020-07]]. 2022 확장: 출퇴근 이동시간·육아·개인 고충 등 수십 가지 정량·정성 데이터를 머신러닝으로 분석해 최적 근무 영업점을 추천하는 혁신 HR 시스템 + 거주지·자격증·관심 분야 기반 실시간 인재추천 시스템 [[sources/etnews-kb-ai-hr-system-2022-12]]. 2025 상반기 PB·RM 상담 업무 AI 도입 — 두 달 만에 적용 직원 57%가 활용 [[sources/hankyung-kb-bank-pb-rm-ai-57pct-2025-10]] (HR 인사이동과는 별개의 상담 AI). 직원 규모 1만7,000여명 [[sources/sedaily-kb-ai-hr-commute-2020-07]].

## Problem / Why (도입 배경)

- **Before (baseline)**: 직원 1만7,000여명의 인사 배치를 위해 업무경력·근무기간·자격증·출퇴근 거리 등 특성을 파악해야 함 [[sources/asiatoday-kb-bank-ai-personnel-deep-change-2020-07]] [[sources/sedaily-kb-ai-hr-commute-2020-07]]; 정량 baseline ❓ 미공개
- **Pain point**: 직원 개인 사정(출퇴근·육아·고충)과 영업점 수요를 종합하는 어려움 [[sources/etnews-kb-ai-hr-system-2022-12]]
- **Trigger**: 허인 행장의 인사제도 혁신 — Deep Change 의지 [[sources/asiatoday-kb-bank-ai-personnel-deep-change-2020-07]]

## Solution Architecture

### A. Process (프로세스)

- **Before**: _미공개 (not disclosed)_ — 기존 "수개월 소요" 서술은 소스에 없음
- **After** (⚠️ 자사 보고 [[sources/asiatoday-kb-bank-ai-personnel-deep-change-2020-07]] [[sources/etnews-kb-ai-hr-system-2022-12]] [[sources/sedaily-kb-ai-hr-commute-2020-07]]):
  1. 직원 데이터 입력 — 업무경력·근무기간·자격증·출퇴근 거리(2020) [[sources/asiatoday-kb-bank-ai-personnel-deep-change-2020-07]]; 출퇴근 이동시간·육아·개인 고충·직무 등 수십 가지 정량·정성 데이터(2022) [[sources/etnews-kb-ai-hr-system-2022-12]]
  2. 머신러닝이 분석해 최적 근무 영업점 추천 [[sources/etnews-kb-ai-hr-system-2022-12]]; 필수 자격증 보유 직원 자동 배치 [[sources/sedaily-kb-ai-hr-commute-2020-07]]
  3. 인사 배치 확정·통보 — HR 검토·조정 단계는 _미공개 (not disclosed)_
  4. 인재추천 시스템: 거주지·자격증·관심 분야 등 실시간 반영 [[sources/etnews-kb-ai-hr-system-2022-12]]
  5. (계획, 2022) 업무 몰입도·조직 만족도 등 직원 경험·정서 상시 진단 [[sources/etnews-kb-ai-hr-system-2022-12]]
- **HITL**: _미공개 (not disclosed)_ — 소스는 "AI 알고리즘 기반 인사"로만 기술
- **Frequency**: 하반기 정기 인사(2020-07) [[sources/asiatoday-kb-bank-ai-personnel-deep-change-2020-07]]; 이후 주기 _미공개_
- **Scope**: recommend(최적 근무지 추천) [[sources/etnews-kb-ai-hr-system-2022-12]] — 확정 절차 미공개

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS**: _미공개 (not disclosed)_
- **AI 시스템 배치**: KB국민은행 혁신 HR 시스템 (자체) [[sources/etnews-kb-ai-hr-system-2022-12]]; SI 수행사 _미공개 (not disclosed)_
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: 직원 정보 실시간 반영(인재추천) [[sources/etnews-kb-ai-hr-system-2022-12]]; 세부 _미공개_
- **사용자 접점**: _미공개 (not disclosed)_
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: 업무경력·근무기간·자격증·출퇴근 거리 [[sources/asiatoday-kb-bank-ai-personnel-deep-change-2020-07]]; 출퇴근 이동시간·육아·개인 고충·직무 [[sources/etnews-kb-ai-hr-system-2022-12]]; 거주지·관심 분야 [[sources/etnews-kb-ai-hr-system-2022-12]]
- **데이터 규모**: 인사 대상 1100여 명(2020 하반기) [[sources/asiatoday-kb-bank-ai-personnel-deep-change-2020-07]] [[sources/sedaily-kb-ai-hr-commute-2020-07]]; 직원 1만7,000여명 [[sources/sedaily-kb-ai-hr-commute-2020-07]]
- **전처리·정제**: _미공개 (not disclosed)_ — 기존 "지오코딩" 서술은 소스에 없음
- **학습 vs RAG vs In-context**: 머신러닝 분석 [[sources/etnews-kb-ai-hr-system-2022-12]] — 방식 세부 _미공개_
- **데이터 거버넌스**: _미공개 (not disclosed)_
- **민감정보 처리**: 육아·개인 고충 등 정성 데이터 활용 [[sources/etnews-kb-ai-hr-system-2022-12]] — 동의·보호 절차 _미공개_

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_ (LLM 이전 세대 ML)
- **Model 유형**: 다변량 데이터 기반 최적 근무지 추천(ML) [[sources/etnews-kb-ai-hr-system-2022-12]]
- **제공 방식**: 자체 구축 [[sources/etnews-kb-ai-hr-system-2022-12]]
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **평가·가드레일**: _미공개 (not disclosed)_ — 만족도 향상은 정성 진술 [[sources/asiatoday-kb-bank-ai-personnel-deep-change-2020-07]] [[sources/sedaily-kb-ai-hr-commute-2020-07]]

### E. Organization

- **오너십**: KB국민은행 HR — 허인 행장 주도 Deep Change [[sources/asiatoday-kb-bank-ai-personnel-deep-change-2020-07]]
- **참여 역할·팀 규모**: _미공개 (not disclosed)_
- **파트너**: _미공개 (not disclosed)_

## Impact / Metrics (기대효과)

### 기대효과 요약
1100여 명 인사이동 AI 배치(2020) + 2022 ML 기반 근무지 추천·인재추천 확장 — 한국 대기업 인사이동 AI의 가장 잘 문서화된 reference. 정량 만족도 수치는 _미공개_.

- ⚠️ 자사 보고:
  - 2020 하반기 인사 대상 1100여 명 AI 배치 [[sources/asiatoday-kb-bank-ai-personnel-deep-change-2020-07]] [[sources/sedaily-kb-ai-hr-commute-2020-07]]
  - 인사 대상 직원 만족도 상승 (정성) [[sources/asiatoday-kb-bank-ai-personnel-deep-change-2020-07]]; 원하는 근무지 배치 사례(직원 인터뷰) [[sources/sedaily-kb-ai-hr-commute-2020-07]]
  - 2022 혁신 HR 시스템·인재추천 시스템 확장 [[sources/etnews-kb-ai-hr-system-2022-12]]
  - (참고, HR 인사이동과 별개) 2025 상반기 PB·RM 상담 AI — 두 달 만에 적용 직원 57% 활용 [[sources/hankyung-kb-bank-pb-rm-ai-57pct-2025-10]]
  - 만족도·이동 인원 등 정량 성과: _미공개 (not disclosed)_

## Governance & Risk

- ✅ "육아·개인 고충" 등 정성 변수 포함 [[sources/etnews-kb-ai-hr-system-2022-12]] — 직원 친화 design
- ⚠️ ML 알고리즘 black-box risk — 직원·노조에게 explainability 제공 여부 _미공개_
- ⚠️ 한국 AI 기본법 고영향 AI 검토 대상(인사이동·배치, `kr-high-impact-review`) — 인적감독 절차가 소스에 없음
- ⚠️ 노조 사전 합의 process _미공개_ (소스 언급 없음)

## Contradictions

> [!note] 2026-09-27 grounding — (1) 기존 영문식 천 단위 직원 수 표기는 서울경제 원문 표기 "1만7,000여명"으로 수정. (2) "LG CNS 또는 자체 IT 수행 추정", "지오코딩", "평가 이력", "HR 검토·조정 후 통보", "수개월 소요", "영업점 1,000+", "2024 한전과 함께 AI 인사혁신 선두", "정기 인사(반기·연말)+수시"는 인용 소스 4건 raw에 없어 삭제·_미공개_. (3) 한국경제 2025-10 기사의 57%는 PB·RM 상담 AI 활용률로, HR Deep Change 인사이동 성과가 아님 — 참고 지표로만 유지.

## Consulting Angle

- **KR 대기업 인사이동 AI reference (1순위)**:
  - 한국에서 가장 잘 문서화된 large-scale 인사이동 AI 사례
  - 5년+ 운영 (2020~2025) — stability proof
  - 2025 PB·RM 상담 AI 57% 두 달 사용은 KB의 AI adoption 역량 증거 (HR 인사이동 AI와는 별개 시스템)
- **2026 Q3-Q4 KR 금융·서비스 인사이동 컨설팅**:
  - 신한 신한은행 AI 인사 알고리즘 (페이지 없음) (2,414명 시뮬레이션) + KB (1,100명 + PB·RM) — 양 은행 비교
  - 직원 사정 (육아·출퇴근·자격증) 변수 포함은 한국 직장 컨텍스트 fit
- **공공·서비스업 reference**: 한전 AI 인재추천 [[korea-electric-power-hr-bot]] + KB HR Deep Change — 한국 large-scale 공공·금융 AI 인사 reference 묶음
- **반면교사**:
  - 5년+ 운영의 model drift·feature 갱신 process 검증 필요
  - 노조 사전 합의 + explainability 제공 필수 (한국 AI 기본법 고영향 AI 의무)
  - "57% 두 달 사용"은 자체 발표 — 외부 인용 시 출처 명시
- **글로벌 비교**: IBM Blue Match [[ibm-blue-match-internal-mobility]] (opt-in 약 50,000명, 2019)·Schneider Open Talent Market [[schneider-electric-gloat-talent-marketplace]]·Unilever FLEX [[unilever-flex-gloat-talent-marketplace]] — KR vs 글로벌 internal mobility 모델 비교
