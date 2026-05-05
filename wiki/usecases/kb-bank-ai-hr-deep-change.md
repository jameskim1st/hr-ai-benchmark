---
title: "KB국민은행 — 'HR Deep Change' AI 영업점 인사이동 (2020 launch, 2025 PB·RM 확장 57% 두 달 사용)"
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
ai_tech_type: [decision-optimization, predictive]
ai_tech_subtype: [optimization, clustering-classification]
stage: production
frequency: monthly
first_seen: 2020-07-15
last_confirmed: 2026-04-01
confidence: 0.55
consulting_angle_status: filled
sources:
  - sources/korea-conglomerate-hr-ai-2025-2026.md
related_usecases:
  - shinhan-bank-ai-one-platform
  - shinhan-bank-ai-staffing-algorithm
  - ibm-blue-match-internal-mobility
related_vendors: []
---

## Summary

KB국민은행 **HR Deep Change** — 2020년 하반기 1,100여 명 영업점 직원 이동 배치를 AI 알고리즘으로 단행. 출퇴근 거리·자격증·업무 경력·**육아 고충** 등 수십 가지 정량/정성 데이터를 머신러닝으로 분석. 한국 KR 대기업 인사이동 AI 도입의 가장 잘 문서화된 reference. 2025 상반기 PB·RM 등 상담 직원 대상 AI 활용 확대 — **적용 직원의 57%가 두 달 만에 실제 사용**.

## Problem / Why

- **Before**: KB국민은행 영업점 직원 인사이동은 매년 manual 조정 — 수천 직원 개인 사정 (출퇴근·육아·자격) 종합 어려움
- **Pain point**: 17,000+ KB 직원 base, 영업점 1,000+ 곳 — manual 인사 운영 한계 + 직원 만족도 격차
- **Trigger**: 2020 'HR Deep Change' 프로젝트 launch — 공공·금융권 최초 large-scale AI 인사 배치

## Solution Architecture

### A. Process

- **Before**: HR이 manual로 직원 개인 사정·점포 수요 매칭 — 수개월 소요
- **After**:
  1. 직원 master data + 영업점 수요 + 정성 데이터 (출퇴근·자격증·육아 고충 등) 입력
  2. ML 알고리즘이 다변량 최적화 — 수십 변수 simultaneous
  3. 후보 배치안 생성 → HR 검토·조정
  4. 매니저·직원 통보
  5. (2025 확장) PB·RM 등 상담 직원 AI 활용으로 확장 — 57% 두 달 만에 사용
- **HITL**: HR이 알고리즘 결과 검토·조정 (인사 결정권 유지)
- **Frequency**: 정기 인사 (반기·연말) + 수시
- **Scope**: recommend → 사람 확정

### B. System

- KB국민은행 자체 구축 (LG CNS 또는 자체 IT 수행 추정)
- HR master + 영업점 master + 직원 사정 input form

### C/D. Data & Model

- **데이터**: HR master + 자격증 DB + 출퇴근 거리 (지오코딩) + 육아 고충 (자가 신고) + 업무 경력 + 평가 이력
- **모델**: 다변량 최적화 ML (LLM 이전 세대, 자체 알고리즘)
- **거버넌스**: 금융정보보호 + 개인정보 (PIPA) 동의 기반

### E. Organization

- KB국민은행 HR + IT/AI 본부

## Impact / Metrics

### 기대효과 요약
1,100여 명 영업점 직원 인사이동 자동화 — 한국 KR 대기업 인사 AI 도입의 canonical case + 2025 상담 직원 확장 정착.

- ⚠️ 자사 보고:
  - 2020 하반기 1,100여 명 일괄 적용
  - 2025 상반기 PB·RM 확장
  - 적용 직원의 **57%가 두 달 만에 실제 사용**
  - 2024 한전과 함께 AI 인사혁신 부문 선두 (공공·금융 비교)

## Governance & Risk

- ✅ "육아 고충" 등 정성 변수 포함 — 직원 친화 design
- ⚠️ ML 알고리즘 black-box risk — 직원·노조에게 explainability 제공 여부 _미공개_
- ⚠️ 한국 AI 기본법 (2026-01-22) 고영향 AI 분류 명확 (인사이동) — 인적감독 의무 자동 충족 검증 필요
- ⚠️ 노조 사전 합의 process _세부 미공개_

## Consulting Angle

- **KR 대기업 인사이동 AI reference (1순위)**:
  - 한국에서 가장 잘 문서화된 large-scale 인사이동 AI 사례
  - 5년+ 운영 (2020~2025) — stability proof
  - 2025 PB·RM 확장 + 57% 두 달 사용은 **adoption 성공 정량 증거**
- **2026 Q3-Q4 KR 금융·서비스 인사이동 컨설팅**:
  - 신한 [[shinhan-bank-ai-staffing-algorithm]] (2,414명 시뮬레이션) + KB (1,100명 + PB·RM) — 양 은행 비교
  - 직원 사정 (육아·출퇴근·자격증) 변수 포함은 한국 직장 컨텍스트 fit
- **공공·서비스업 reference**: 한전 HR-Bot/AI 인사추천 [[korea-electric-power-hr-bot]] + KB HR Deep Change — 한국 large-scale 공공·금융 AI 인사 best practice 묶음
- **반면교사**:
  - 5년+ 운영의 model drift·feature 갱신 process 검증 필요
  - 노조 사전 합의 + explainability 제공 필수 (한국 AI 기본법 고영향 AI 의무)
  - "57% 두 달 사용"은 자체 발표 — 외부 인용 시 출처 명시
- **글로벌 비교**: IBM Blue Match [[ibm-blue-match-internal-mobility]] (opt-in 15%)·Schneider Open Talent Market [[schneider-electric-gloat-talent-marketplace]]·Unilever FLEX [[unilever-flex-gloat-talent-marketplace]] — KR vs 글로벌 internal mobility 모델 비교
