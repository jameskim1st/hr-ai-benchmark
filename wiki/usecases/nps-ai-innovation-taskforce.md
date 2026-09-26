---
title: "국민연금공단 — AI·혁신 추진단 + AI사원·AI 규정비서·AI 수어 영상"
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
output: "다중 산출물 — AI 사원의 가입자 상담·홍보 자동 응답 + AI 규정비서의 사내 임직원 규정 Q&A + AI 수어 영상 (청각장애 가입자용 multimodal 안내)"
ai_tech_type: [generative]
ai_tech_subtype: [summarization-qa, multimodal]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: []
kr_law: PIPA strict (5,000만 가입자) + AI 기본법 고영향 (연금 의사결정 영향 시)
kr_union: 협의 의무 낮음 (정보 제공 성격 — 규정 Q&A·상담)
kr_language: 한국어 네이티브
kr_vendor: 미확인 (벤더 미공개 — 다중 vendor)
frequency: daily
first_seen: 2025-09-18
last_confirmed: 2026-04-01
confidence: 0.8
evidence_grade: A
corroborated_by: 2
freshness: fresh
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/biztribune-nps-ai-innovation-taskforce-2025-09.md, sources/newspim-nps-ai-innovation-taskforce-2025-09.md]
related_usecases:
  - korea-electric-power-hr-bot
  - korea-gov-ai-hr-public-sector
related_vendors: []
---

## Summary

국민연금공단이 2025-09-18 **'AI·혁신 추진단'** 출범 발표 — 기획이사 단장·디지털혁신본부장 부단장, 연금·복지 / 기금운용 / 기관운영 / 시스템 4개 분과, 최고 의사결정기구 신설과 **CAIO(AI 최고 책임자) 지정 예정** [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]] [[sources/newspim-nps-ai-innovation-taskforce-2025-09]]. 9월 15일 제1차 AI 운영위원회에서 데이터·인프라 현황 점검 [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]] [[sources/newspim-nps-ai-innovation-taskforce-2025-09]]. 기존 도입 서비스: **AI 수어 영상안내**, **AI 사원** 활용 상담·홍보, **AI 규정 비서** [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]]; 2025 정부혁신 우수사례 경진대회 우수상 [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]]. 한국 공공기관·연기금의 AI 거버넌스 추진단 패턴 사례.

## Problem / Why (도입 배경)

- **Before**: ❓ baseline 미공개 — 직원 수·가입자 수·상담 건수는 인용 소스에 없음 (2026-09-27 grounding 점검)
- **Pain point**: 업무 효율화와 대국민 서비스 개선 (공단 발표 프레이밍) [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]]
- **Trigger**: 정부의 'AI 3대 강국 도약' 목표에 발맞춘 AI 중심 혁신 추진 [[sources/newspim-nps-ai-innovation-taskforce-2025-09]] → 2025-09-18 AI·혁신 추진단 출범

## Solution Architecture

### A. Process — 다중 AI 솔루션

- **AI 사원**: 상담·홍보 활용 (대고객) [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]] [[sources/newspim-nps-ai-innovation-taskforce-2025-09]]; 기능 세부 _미공개_
- **AI 규정 비서**: 사내 규정 관련 AI 서비스 [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]]; 기능·이용 규모 _미공개_
- **AI 수어 영상안내**: 수어 영상 안내 서비스 (접근성) [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]] [[sources/newspim-nps-ai-innovation-taskforce-2025-09]]
- **AI·혁신 추진단**: 4개 분과 cross-functional governance [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]] [[sources/newspim-nps-ai-innovation-taskforce-2025-09]]
  - 연금·복지 분과
  - 기금운용 분과
  - 기관운영 분과
  - 시스템 분과
- **HITL·Frequency·Scope**: _미공개 (not disclosed)_ — 각 서비스의 운영 세부는 인용 소스에 없음

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS**: _미공개 (not disclosed)_
- **AI 시스템 배치**: 다중 서비스 — AI 사원·AI 규정 비서·AI 수어 영상안내 [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]]; 벤더·아키텍처 _미공개_
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: _미공개 (not disclosed)_
- **사용자 접점**: _미공개 (not disclosed)_ — 대고객/사내 구분만 서비스명에서 유추 가능
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: _미공개 (not disclosed)_ — 규정 문서·상담 이력 활용 여부 미명시
- **데이터 규모**: _미공개 (not disclosed)_ — 직원·가입자 수치는 인용 소스에 없음
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: _미공개 (not disclosed)_
- **데이터 거버넌스**: 추진단이 제1차 AI 운영위원회에서 데이터·인프라 현황 점검 [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]] [[sources/newspim-nps-ai-innovation-taskforce-2025-09]]; CAIO 지정·최고 의사결정기구 신설 예정 [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]] [[sources/newspim-nps-ai-innovation-taskforce-2025-09]]
- **민감정보 처리**: _미공개 (not disclosed)_ — 공공 연금 데이터 특성상 PIPA·AI 기본법 검토 대상

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **모델 유형**: 수어 영상 안내(multimodal)·상담·규정 비서(대화형) [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]] — 기술 세부 _미공개_
- **제공 방식**: _미공개_
- **커스터마이징 기법**: _미공개_
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: _미공개 (not disclosed)_ — 연금 의사결정 영향 시 AI 기본법 검토 대상

### E. Organization & Team (조직·팀 구조)

- **오너십**: AI·혁신 추진단 — 기획이사(단장)·디지털혁신본부장(부단장) [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]] [[sources/newspim-nps-ai-innovation-taskforce-2025-09]]
- **참여 역할**: 4개 분과 (연금·복지/기금운용/기관운영/시스템) [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]]; CAIO 지정 예정 [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]] [[sources/newspim-nps-ai-innovation-taskforce-2025-09]]
- **팀 규모·기간**: 2025-09-18 출범 [[sources/newspim-nps-ai-innovation-taskforce-2025-09]]; 인원 _미공개_
- **거버넌스 체계**: 최고 의사결정기구 신설, 주기적 위원회 개최 계획, 제1차 AI 운영위원회(2025-09-15) [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]] [[sources/newspim-nps-ai-innovation-taskforce-2025-09]]
- **변화관리**: _미공개 (not disclosed)_
- **파트너**: _미공개 (not disclosed)_


## Impact / Metrics (기대효과)

### 기대효과 요약
공공기관 CAIO 신설 + AI 거버넌스 추진단 운영 — 한국 공공기관 표준 패턴.

- ✅ AI·혁신 추진단 4개 분과 출범 [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]] [[sources/newspim-nps-ai-innovation-taskforce-2025-09]]
- ✅ CAIO 지정·최고 의사결정기구 신설 **예정** (2025-09 시점) [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]] [[sources/newspim-nps-ai-innovation-taskforce-2025-09]]
- ✅ AI 사원·AI 규정 비서·AI 수어 영상 — 기존 도입 서비스 [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]]
- ✅ 2025 정부혁신 우수사례 경진대회 우수상 [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]]
- ⚠️ standalone metric _미공개_

## Governance & Risk

- ⚠️ 한국 AI 기본법 (2026-01) — 연금 의사결정 영향 시 고영향 AI 검토 대상
- ⚠️ 공공 연금 가입자 데이터 — PIPA 준수 필요 (공단 대응 세부 _미공개_)
- ✅ AI 수어 영상 = 접근성 강화 [[sources/biztribune-nps-ai-innovation-taskforce-2025-09]] [[sources/newspim-nps-ai-innovation-taskforce-2025-09]]
- ⚠️ 두 소스 모두 공단 보도자료 기반 짧은 기사 — HR 업무 적용은 '기관운영 분과' 포함 수준으로만 명시 [[sources/newspim-nps-ai-innovation-taskforce-2025-09]]

## Contradictions

> [!note] 2026-09-27 grounding — 인용 소스에 없는 직원 ~7K·가입자 5,000만+, 다중 vendor·정부 클라우드·RAG 추정, 보안 표준·PIPA strict 확정 서술을 제거·_미공개_ 처리. 4개 분과 명칭을 raw 기준(연금·복지/기금운용/기관운영/시스템)으로 정정. CAIO는 '지정 예정'(2025-09)으로 hedging.

## Consulting Angle

- **KR 공공기관·연기금 reference**:
  - 한국전력 HR-Bot [[korea-electric-power-hr-bot]] (공공기관 첫 AI 인사추천)
  - 인사혁신처/행정안전부 [[korea-gov-ai-hr-public-sector]] (정부 AI HR)
  - 국민연금공단 (CAIO + 추진단 + 다중 솔루션) — KR 공공섹터 비교표 필수
- **CAIO 도입 트렌드**: 국민연금공단의 CAIO 지정 계획(2025-09) — KR 공공기관 AI 거버넌스 sample (지정 완료 여부 후속 확인 필요)
- **AI 수어 영상**: KR 공공기관 접근성 (장애인 포함) reference — 글로벌 best practice
- **반면교사**:
  - vendor·구체 architecture _미공개_ — RFP 정보 공개 후 page 갱신
  - 공공기관 특성상 production 효과 metric publication 지연
