---
title: "국민연금공단 — AI·혁신 추진단 + AI사원·AI 규정비서·AI 수어 영상 (CAIO 신설)"
slug: nps-ai-innovation-taskforce
primary_category: Strategic Workforce & Governance
subcategory: HR Tech Governance
tags: [nps, korea-pension, ai-innovation-taskforce, caio, ai-employee, ai-regulation-secretary, korea, public-pension, accessibility]
company: 국민연금공단
industry: [public, pension, finance]
region: [kr]
employee_class: [전임직, 기술사무직]
vendor: [_미공개_]
vendor_type: [point-solution, internal-build]
ai_tech_type: [generative]
ai_tech_subtype: [summarization-qa, multimodal]
stage: production
frequency: daily
first_seen: 2025-09-18
last_confirmed: 2026-04-01
confidence: 0.40
consulting_angle_status: filled
sources:
  - sources/kr-conglomerate-2026-q2-research.md
related_usecases:
  - korea-electric-power-hr-bot
  - korea-gov-ai-hr-public-sector
related_vendors: []
---

## Summary

국민연금공단이 2025-09 **'AI·혁신 추진단'** 출범 — 기획이사 단장, **CAIO(Chief AI Officer) 신설**. 4개 분과 (연금·복지·기금운용·기관운영·시스템). **AI 사원** 활용 상담·홍보, **AI 규정비서**, **AI 수어 영상안내** 운영 중. 한국 공공기관·연기금 CAIO 도입 + AI 거버넌스 추진단 패턴의 표준 사례.

## Problem / Why

- **Before**: 국민연금공단 ~7K 직원, 5,000만+ 국민 가입자 — 상담·규정 응대 부담 거대
- **Pain point**: 공공기관 디지털 전환 + 정부 AI 정책 (한국 AI 기본법 2026-01) 대응
- **Trigger**: 2025-09 AI·혁신 추진단 출범 — 기관 차원 AI 거버넌스 강화

## Solution Architecture

### A. Process — 다중 AI 솔루션

- **AI 사원**: 상담·홍보 자동화 (대고객)
- **AI 규정비서**: 사내 임직원 규정 Q&A
- **AI 수어 영상안내**: 청각장애 가입자 접근성 (multimodal)
- **AI·혁신 추진단**: 4개 분과 cross-functional governance
  - 연금 분과
  - 복지 분과
  - 기금운용 분과
  - 기관운영·시스템 분과

### B/C/D. System

- 다중 vendor 추정 (AI 수어 영상은 별도 vendor 가능성)
- 모델: _미공개_

### E. Organization

- 기획이사 (단장) + CAIO (신설) + 4개 분과장
- 2025-09-18 공식 출범

## Impact / Metrics

### 기대효과 요약
공공기관 CAIO 신설 + AI 거버넌스 추진단 운영 — 한국 공공기관 표준 패턴.

- ✅ AI·혁신 추진단 4개 분과 운영
- ✅ CAIO 신설
- ✅ AI 사원·AI 규정비서·AI 수어 영상 — 3개 솔루션 동시 운영
- ⚠️ standalone metric _미공개_

## Governance & Risk

- ⚠️ 한국 AI 기본법 (2026-01) — 연금 의사결정 영향 시 고영향 AI 분류 가능
- ⚠️ 5,000만+ 국민 데이터 — PIPA strict compliance
- ✅ AI 수어 영상 = 접근성 강화 (best practice)

## Consulting Angle

- **KR 공공기관·연기금 reference**:
  - 한국전력 HR-Bot [[korea-electric-power-hr-bot]] (공공기관 첫 AI 인사추천)
  - 인사혁신처/행정안전부 [[korea-gov-ai-hr-public-sector]] (정부 AI HR)
  - 국민연금공단 (CAIO + 추진단 + 다중 솔루션) — KR 공공섹터 비교표 필수
- **CAIO 도입 트렌드**: KR 대기업도 CAIO 신설 가속 — 국민연금이 공공기관 leading sample
- **AI 수어 영상**: KR 공공기관 접근성 (장애인 포함) reference — 글로벌 best practice
- **반면교사**:
  - vendor·구체 architecture _미공개_ — RFP 정보 공개 후 page 갱신
  - 공공기관 특성상 production 효과 metric publication 지연
