---
title: "Microsoft — Employee Self-Service Agent + Viva Copilot HR"
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
output: "직원 HR/IT 문의에 대한 authoritative 답변 또는 action form (휴가·급여·복리후생·장비) + 배후 시스템 워크플로 트리거 + 미해결 시 자동 ticket 생성·HR 라우팅"
ai_tech_type: [generative, automation]
ai_tech_subtype: [summarization-qa, rpa]
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

### A. Process (프로세스)

- **Before**: 직원이 HR/IT 문의 시 다중 portal·ticket 시스템을 거치며 응답 지연
- **After**:
  1. 직원이 M365 Copilot 비즈니스 채팅에서 "Employee Self-Service" 선택
  2. 자연어로 질문 입력 (휴가 신청·급여·복리후생·장비 요청 등)
  3. Agent가 SharePoint 정책 KB·Workday/SAP/ServiceNow connector 조회
  4. authoritative 응답 또는 action form 제시 (휴가신청·transfer 요청 등)
  5. 직원이 form 제출 → 배후 시스템 워크플로 트리거
  6. 미해결 시 Agent가 자동으로 ticket 생성·HR 담당자에 라우팅
- **HITL**: 복잡 case는 HR agent에게 escalate, manager는 transfer/profile 변경 승인
- **Frequency**: daily (일상 self-service)
- **Source**: Microsoft Adoption — Employee Self-Service Agent product page

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
