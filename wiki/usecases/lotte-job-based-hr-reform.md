---
title: "롯데그룹 — 직무 기반 HR 인사제도 전면 개편"
slug: lotte-job-based-hr-reform
primary_category: Total Rewards
subcategory: Compensation
tags: [job-based-hr, compensation-reform, skills-based, korea, conglomerate, pay-structure]
company: 롯데그룹
industry: [retail, manufacturing]
region: [kr]
employee_class: [기술사무직, 전임직]
vendor: []
vendor_type: [internal-build]
output: "_N/A_ (전통 HR 개혁, AI 미공개)"
ai_tech_type: []
ai_tech_subtype: []
stage: production
frequency: annual
first_seen: 2025-04-22
last_confirmed: 2025-09-01
confidence: 0.35
sources:
  - sources/newdaily-lotte-hr-2025-04.md
  - sources/etnews-lotte-job-pay-2025-04.md
  - sources/sedaily-lotte-dept-store-2025.md
related_usecases:
  - workday-illuminate-job-architecture
related_vendors: []
---

## Summary

롯데그룹은 2024년부터 일부 계열사를 시작으로 "직무 기반 HR" 인사제도를 순차적으로 도입·확대하고 있다. ✅ **Fact** 직무 전문성과 성과에 따라 보상을 차등 지급하는 직무급제로 전환하며, 연차와 무관하게 직무 전문성에 따른 레벨업 심사를 허용한다. 2025년에는 롯데백화점(직원 95.3% 찬성)·롯데웰푸드 등으로 도입 범위를 확대했다. [[sources/newdaily-lotte-hr-2025-04.md]] [[sources/sedaily-lotte-dept-store-2025.md]]

## Problem / Why (도입 배경)

롯데그룹은 전통적인 연공서열 기반 보상 체계가 직무 전문성 강화와 혁신적 성과 창출을 저해한다고 판단했다. "위기 돌파 카드"로 직무 기반 HR을 채택하여 업무 생산성 강화와 신성장 동력 확보를 추진하고 있다.

## Solution Architecture

> **최우선 원칙**: 이 섹션은 **공개된 사실만** 기록한다.

### A. Process (프로세스)

- **Before (As-is)**: 연공서열 중심 보상 체계. 직급별 일률적 급여.
- **After (To-be)**:
  1. ✅ **Fact** 직무 가치와 성과에 따른 차등 보상(직무급제). [[sources/etnews-lotte-job-pay-2025-04.md]]
  2. ✅ **Fact** 연차 무관 직무 전문성 기반 레벨업 심사 신청 허용. [[sources/sedaily-lotte-dept-store-2025.md]]
  3. ✅ **Fact** 도입 순서: 롯데바이오로직스(2024-05) → 대홍기획·롯데이노베이트(시범) → 롯데백화점·롯데웰푸드(2025). [[sources/newdaily-lotte-hr-2025-04.md]]
- **AI 활용 여부**: _미공개 (not disclosed)_ — 현재 공개된 소스에서 AI 도구 활용 명시 없음. 직무 분류·평가에 AI 활용 여부 불명.
- **Human-in-the-loop**: 직무 평가·레벨업 심사는 HR·관리자가 수행.
- **Trigger & Frequency**: 연간 정기 인사 평가 + 수시 레벨업 신청 가능.
- **Scope of autonomy**: 인간 결정 중심 (AI 자동화 수준 _미공개_).

### B. System & Infrastructure (시스템·인프라)

- _미공개 (not disclosed)_ — 구체 HR 시스템·플랫폼 미공개.

### C. Data (데이터)

- _미공개 (not disclosed)_

### D. Model (모델)

- _미공개 (not disclosed)_ — AI/ML 모델 활용 여부 미확인.

### E. Organization & Team (조직·팀 구조)

- **오너십**: 롯데지주 주도, 계열사별 도입.
- **직원 동의**: ✅ **Fact** 롯데백화점 직원 95.3% 찬성으로 직무기반 보상체계 도입 확정. [[sources/sedaily-lotte-dept-store-2025.md]]

## Impact / Metrics (기대효과)

### 기대효과 요약
정량적 성과(보상 만족도 변화·이직률·생산성) _미공개_ — 도입 초기 단계. 95.3% 직원 찬성(Fact)은 변화관리 수용도 지표이지 outcome metric이 아님에 유의.

- _미공개 (not disclosed)_ — 아직 도입 초기 단계, 정량적 성과 미공개.

## Governance & Risk

- 직무급제 도입 시 기존 연공급 직원의 보상 감소 리스크 → 단계적 전환 및 직원 동의 절차 확보.
- ✅ **Fact**: 롯데백화점은 95.3% 직원 찬성으로 도입 확정 — 법적 취업규칙 변경 동의 요건 충족. [[sources/sedaily-lotte-dept-store-2025.md]]
- AI 활용 여부 미확인 — 현재는 전통적 HR 제도 개혁 수준.

## Contradictions

없음 (현재 기준).

## Consulting Angle

- **한국 대기업 보상 체계 전환의 선도 사례**: 롯데의 직무급제 전환은 삼성·현대·LG 등 대기업들이 연공제에서 직무·성과 기반으로 전환하는 거대한 흐름의 일부. 국내 대기업 보상 체계 개혁 제안 시 레퍼런스.
- **95.3% 직원 찬성의 의미**: 법적으로 취업규칙 변경 시 과반 동의 필요 — 롯데백화점의 95.3% 찬성은 변화관리 성공 사례. 다만 구체 설득 방법론은 미공개.
- **AI 미활용 vs 활용 가능성**: 현재 공개된 정보에는 AI 도구 활용이 없으나, 직무 분류·직무가치 분석에 AI 도구(Workday Illuminate Job Architecture, SAP Joule 등)를 도입하면 효율화 가능 — AI 도입 확대 시 연계 제안 기회.
- **한계**: AI HR 사례라기보다는 전통적 HR 제도 개혁 사례. AI 요소가 확인될 경우 업데이트 필요. 현재 confidence가 낮음(0.35) — 소스가 국내 언론 Tier 4 수준.
