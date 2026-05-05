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

### B. System & Infrastructure (R9 research)

- **Core HRIS**: 국민연금공단 자체 (구체 _미공개_)
- **AI 시스템 배치**: ✅ 다중 — AI 사원·AI 규정비서·AI 수어 영상안내
- **배포 환경**: _미공개_ — 망분리상 정부 클라우드 또는 on-prem 추정
- **연동·통합**: _미공개_ — 4개 분과 cross-functional
- **사용자 접점**: ✅ 대고객 web/앱 (AI 사원·수어) + 사내 (AI 규정비서)
- **인증·권한**: ✅ 공공기관 보안 표준 + PIPA strict

### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 연금·복지·규정 문서, 가입자 상담 이력, 수어 영상 콘텐츠
- **데이터 규모**: ✅ 직원 ~7K, 가입자 5,000만+
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_ — AI 규정비서 RAG 추정 (공식 미명시)
- **데이터 거버넌스**: ✅ CAIO 신설 + AI·혁신 추진단 4개 분과
- **민감정보 처리**: ✅ 5,000만+ 국민 — PIPA strict, KR AI 기본법 (2026-01) 고영향 AI 분류 가능

### D. Model (R9 research)

- **Foundation model**: _미공개_ — 다중 vendor 추정 (수어는 별도)
- **모델 유형**: generative (요약·QA) + multimodal (수어 영상 — sign language video synthesis)
- **제공 방식**: _미공개_
- **커스터마이징 기법**: _미공개_
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: ⚠️ KR AI 기본법 인적감독 의무 — 연금 의사결정 영향 시


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
