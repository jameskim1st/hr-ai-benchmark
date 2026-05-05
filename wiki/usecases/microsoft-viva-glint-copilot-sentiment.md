---
title: "Microsoft Viva Glint Copilot — engagement 서베이 open-end NLP 자동 합성 (2026-03 default ON)"
slug: microsoft-viva-glint-copilot-sentiment
primary_category: Employee Experience & HR Ops
subcategory: Listening & Engagement
tags: [microsoft, viva, glint, copilot, sentiment-analysis, employee-survey, open-end-nlp, copilot-highlights, engagement]
company: Microsoft
industry: [tech, cloud]
region: [global]
employee_class: [all]
vendor: [Microsoft]
vendor_type: [hrms]
ai_tech_type: [generative, predictive]
ai_tech_subtype: [summarization-qa, clustering-classification]
stage: production
frequency: monthly
first_seen: 2024-09-01
last_confirmed: 2026-04-01
confidence: 0.55
consulting_angle_status: filled
sources:
  - sources/us-large-enterprise-hr-ai-2025-2026.md
related_usecases:
  - amazon-connections-daily-pulse
  - microsoft-people-skills-inferred-ontology
related_vendors: []
---

## Summary

Microsoft Viva Glint에 Copilot 임베드 — engagement 서베이 open-end 코멘트 대량 합성 + 반복 테마 탐지 + 속성별 sentiment slice + benchmark 비교. **2026-03 transition으로 default ON**, 2026-04부터 Team/Executive 요약 리포트에 "Copilot Highlights" 자동 섹션 추가 (강점·기회·점수 변화·benchmark). Microsoft 자체 사용 — 전사 "Employee Signals" twice-yearly.

## Problem / Why

- **Before**: 5만~10만 직원 KR 대기업 annual 서베이 open-end 코멘트 코딩에 HRBP 팀이 수주 투입
- **Pain point**: open-end NLP 분석은 sentiment·테마 추출에 manual 작업 압도적 — insight 도출 지연
- **Trigger**: Glint Copilot 통합 — Microsoft가 LinkedIn(Glint owner)을 M365 ecosystem 통합

## Solution Architecture

### A. Process

- **Before**: 1) 서베이 open-end 코멘트 export / 2) HRBP 팀 manual 코딩·테마 분류 / 3) sentiment 분석 외부 vendor 또는 manual / 4) Team 리포트 작성 (수주~수개월)
- **After**:
  1. 서베이 데이터 → Glint Copilot 자동 처리
  2. 반복 테마 탐지 + sentiment slice (속성별 — 부서·재임기간·매니저 등)
  3. benchmark 비교 (산업·규모)
  4. Team/Executive 요약 리포트에 **"Copilot Highlights"** 자동 생성 — 강점·기회·점수 변화·benchmark 포함
  5. HRBP·매니저는 강조점 검토·action plan 작성
- **HITL**: HRBP·매니저가 highlight 검토·action 결정
- **Frequency**: monthly pulse 또는 annual + 이슈 기반 ad-hoc

### B/C/D. System

- Viva Glint 내장 Copilot (M365 ecosystem)
- 모델: OpenAI GPT-4 추정 (Microsoft 표준)
- 데이터: 서베이 응답 + 직원 메타데이터 (RBAC)

### E. Organization

- Microsoft HR (자체 사용) + 고객사 HRBP·People Science 팀

## Impact / Metrics

### 기대효과 요약
서베이 open-end NLP 분석을 수주 → 즉시. KR 대기업 annual 조직문화 진단의 ROI 격차 해소.

- 2026-03 default ON (platform-wide)
- 2026-04 Copilot Highlights 자동 섹션
- Microsoft 자체: twice-yearly "Employee Signals" 전사 활용
- standalone 시간 단축 metric _공식 미공개_

## Governance & Risk

- ✅ Copilot Highlights는 자동 합성·HRBP 검토 — explainable
- ⚠️ 직원 코멘트의 anonymization·속성별 slice 시 small group re-identification 위험
- ⚠️ benchmark 비교의 한국 시장 fit 미검증

## Consulting Angle

- **KR 대기업 annual 조직문화 진단의 직접 reference**:
  - 삼성·SK·LG·현대 모두 매년 1~2회 engagement survey (5자리 인원) — open-end 코멘트 코딩에 HRBP 팀 수주 투입
  - Glint Copilot은 이 ROI 격차 즉시 해소 — 이미 M365 도입사는 추가 도입 부담 적음
- **한국 기업 sentiment 한국어 NLP 품질 검증 필수**: Korean Glint Copilot의 존댓말·dialect·industry-specific term 처리 POC 4주
- **2026 Q3-Q4 KR consulting deck**: Glint Copilot + Amazon Connections [[amazon-connections-daily-pulse]] + 워크데이 Illuminate Sentiment — 3-vendor sentiment 비교
- **반면교사**:
  - sentiment slice를 부서·재임기간 등 small group으로 자르면 re-identification — 익명성 약화 가능. 한국 노조 sensitivity 큰 영역
  - Glint Copilot 결과를 매니저 평가에 직접 사용 시 한국 AI 기본법 고영향 AI 의무 (인적감독·고지) 트리거 — sentiment 기반 매니저 평가 자동화 회피 권장
