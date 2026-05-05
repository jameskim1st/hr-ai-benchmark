---
title: "Microsoft — Employee Self-Service Agent + Viva Copilot HR (내부 배포)"
slug: microsoft-employee-self-service-agent
primary_category: Employee Experience & HR Ops
subcategory: Employee Self-service
tags: [employee-self-service, viva, copilot, viva-glint, engagement, self-dogfooding]
company: Microsoft
industry: [tech]
region: [global]
employee_class: [all]
vendor: [Microsoft]
vendor_type: [hrms]
stage: production
frequency: daily
first_seen: 2025
last_confirmed: 2025
confidence: 0.35               # Tier 3 (Microsoft insidetrack = 자사 보고), recency <12m, no independent coverage
consulting_angle_status: filled
sources:
  - "Microsoft InsideTrack 2025 https://www.microsoft.com/insidetrack/blog/accelerating-employee-services-at-microsoft-with-the-employee-self-service-agent/"
  - "Microsoft InsideTrack https://www.microsoft.com/insidetrack/blog/how-microsoft-hr-is-using-viva-and-copilot-for-microsoft-365-to-empower-our-employees/"
related_usecases:
  - ibm-askhr-watsonx
  - moderna-ask-hr-routing
related_vendors: []
---

# Microsoft — Employee Self-Service Agent + Viva Copilot HR

## Summary

Microsoft HR이 **자사 제품 Viva + Microsoft 365 Copilot**을 자체 HR 운영에 적용한 내부 배포 사례. 핵심은 **Employee Self-Service Agent**의 글로벌 phased rollout (UK→Canada→India→US→전 세계). Viva Glint 설문으로 Copilot 도입의 "employee thriving" 영향을 상관 측정. IBM AskHR과 마찬가지로 **벤더 = 고객**인 self-dogfooding 패턴.

## Solution Architecture

### A. Process

- **Employee Self-Service Agent**: 직원 HR 질문에 자동 응답하는 AI 에이전트
  - **글로벌 phased rollout**: UK → Canada → India → US → rest of world
  - 전사 deployment 완료 (세부 timeline _미공개_)
- **Viva Glint 연동**: 반기별(biannual) 조직 설문으로 Copilot 도입 후 AI 사용과 "employee thriving" 상관 측정
- **변화관리**: Viva를 promotion·awareness·skilling·reinforcement 채널로 활용
  - Senior BPM 인용: "Using Viva for our... process is tremendously useful... it captures many more people than instructor-led trainings"

### B. System
- **Core**: Microsoft 365 + Viva suite + Copilot
- **AI 플랫폼**: Azure OpenAI Service (Copilot 백엔드)
- **사용자 접점**: Teams embedded (Viva 통합)

### C~E. 세부
- **데이터**: Microsoft HR 정책·FAQ·지식베이스 (규모 _미공개_)
- **모델**: GPT-4/4o 계열 (Copilot = Azure OpenAI Service)
- **조직**: Microsoft Digital + HR 공동 운영

## Impact / Metrics (기대효과)

### 기대효과 요약
단계적 배포(phased rollout) 진행 중이며 정량 ROI _미공개_. 현재까지 공개된 것은 측정 프레임워크(Viva Glint + Copilot 상관 분석)뿐이고 실제 결과 수치는 0건 (⚠️ 자사 보고 기반).

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| 배포 범위 | 글로벌 전 직원 (phased) | Microsoft InsideTrack | ⚠️ 자사 보고 |
| 측정 방식 | Viva Glint에 Copilot 질문 추가 → "employee thriving" 상관 분석 | Microsoft InsideTrack | ⚠️ 자사 보고 |
| 정량 ROI | _미공개_ | — | — |

## Consulting Angle

- **"product vs deployment 구분"의 교과서**: Microsoft Viva는 **제품**이지만, 이 use case는 Microsoft **자사 HR팀이 실제로 배포·측정·개선한 과정**을 기록
- **Viva Glint + Copilot 상관 측정 방식**은 다른 기업이 "HR AI 효과를 어떻게 측정할 것인가?"의 참고 모델
- **IBM AskHR vs Microsoft Self-Service Agent**: 양사 모두 자사 AI를 자사 HR에 적용한 self-dogfooding — 각각 watsonx vs Azure OpenAI 기반
- **한국 적용**: Microsoft 365를 이미 쓰는 국내 기업은 Viva + Copilot 경로가 가장 마찰 낮은 HR AI 진입점

### 한계
- 모든 정보가 **Microsoft InsideTrack** (자사 블로그) 출처 — 독립 검증 없음
- 정량 ROI 미공개 (employee thriving 상관만, 비용·시간 절감 수치 없음)
