---
title: "포스코DX — 인사·구매·경영분석 110 AI 에이전트 + 그룹 AI 거버넌스"
slug: posco-dx-110-agents-hr
primary_category: Strategic Workforce & Governance
subcategory: HR Tech Governance
tags: [posco-dx, posco-group, 110-agents, hr-procurement-analytics, ai-robot-fusion, organizational-redesign, korea, manufacturing]
company: 포스코DX (포스코 그룹)
industry: [it-services, manufacturing, steel]
region: [kr]
employee_class: [기술사무직, 전임직]
vendor: [POSCO DX internal]
vendor_type: [internal-build]
output: "인사·구매·경영분석 사무 영역 110개 에이전트의 도메인별 자동화 산출물 (계열사 공통 활용, 2026 launch 예정 — 구체 산출물 형태 미공개)"
ai_tech_type: [generative, automation, predictive]
ai_tech_subtype: [summarization-qa, rpa, clustering-classification]
stage: announced
visibility: public
case_type: adoption
regulatory_exposure: []
kr_law: AI 기본법 고영향 AI 분류 가능 (인사 영역 에이전트, 페이지 명시)
kr_union: 인사 에이전트 산출물 미공개 — 인사 결정 관여 시 근로자대표 협의 필요
kr_language: 한국어 네이티브
kr_vendor: 자체 구축 (포스코DX)
frequency: daily
first_seen: 2026-01-01
last_confirmed: 2026-04-01
confidence: 0.8
evidence_grade: A
corroborated_by: 2
freshness: fresh
depth: stub
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/eroun-posco-group-2026-reorg-2025-12.md, sources/posco-newsroom-aw2026-poscodx-ai-workforce-2026-04.md, sources/snmnews-posco-group-2026-appointments-2025-12.md]
related_usecases:
  - woori-bank-175-ai-agents
  - hyundai-mobis-moai-platform
  - sk-group-aibiz-25-companies
related_vendors: []
---

## Summary

포스코DX가 AW 2026(2026-03-04~06) 'AI 워크포스' 존에서 사무용 AI 임플로이(Employee)·생산용 AI 오퍼레이터(Operator) 에이전트와 에이전트 생성·운영·평가·재배치 관리 플랫폼 **'에이전티'**를 소개하고, **인사·구매·경영분석 등 사무 업무 영역 중심으로 약 110개 AI 에이전트를 개발 중**이라고 밝힘 (⚠️ 자사 보고, 그룹 뉴스룸) [[sources/posco-newsroom-aw2026-poscodx-ai-workforce-2026-04]]. 2026 그룹 조직개편으로 UNIST 임치현 부교수가 그룹DX전략실장에 영입되고 윤일용 포스코DX AI기술센터장이 포스코홀딩스 AI로봇융합연구소장에 임명 [[sources/eroun-posco-group-2026-reorg-2025-12]] [[sources/snmnews-posco-group-2026-appointments-2025-12]] — 그룹 차원 AI 거버넌스 맥락. 우리은행 175 에이전트 [[woori-bank-175-ai-agents]]와 함께 KR 기업 **AI 에이전트 portfolio 규모** 트렌드의 제조업 reference.

## Problem / Why (도입 배경)

- **Before**: ❓ baseline 미공개 — 직원 수·업무량 수치는 인용 소스에 없음 (2026-09-27 grounding 점검)
- **Pain point**: 사무 영역의 반복 업무부터 전문 영역까지 사람이 수행하던 업무를 AI 임플로이가 대신 수행 (포스코DX 개념 설명) [[sources/posco-newsroom-aw2026-poscodx-ai-workforce-2026-04]]
- **Trigger**: 2026 그룹 정기 조직개편 — DX 관련 조직 재정비, 그룹DX전략실장 영입·AI로봇융합연구소장 임명 [[sources/eroun-posco-group-2026-reorg-2025-12]] [[sources/snmnews-posco-group-2026-appointments-2025-12]]; 110개 에이전트 개발의 직접 계기는 ❓ 미공개

## Solution Architecture

### A. Process (프로세스)

- **Before**: _미공개 (not disclosed)_ — 도입 전 프로세스는 인용 소스에 없음
- **After (개발 중 — 배포 시점 미공개)** ⚠️ 자사 보고 [[sources/posco-newsroom-aw2026-poscodx-ai-workforce-2026-04]]:
  1. AI 임플로이(사무용 에이전트)가 업무 목적을 이해하고 스스로 판단하며 직원과 함께 문제 해결 (개념)
  2. 인사·구매·경영분석 등 사무 업무 영역 중심 약 110개 에이전트 개발 중
  3. '에이전티' 플랫폼이 에이전트 생성·운영·평가·재배치 전 과정 관리
  - 계열사 공통 활용·그룹DX전략실 portfolio 거버넌스·2026 launch 서술은 인용 소스에 없어 제거 (2026-09-27)
- **HITL**: "직원과 함께 문제를 해결"하는 실행형 AI (개념) [[sources/posco-newsroom-aw2026-poscodx-ai-workforce-2026-04]]; 승인·검토 단계 _미공개_
- **Trigger & Frequency**: _미공개 (not disclosed)_
- **Scope of autonomy**: "스스로 판단"하는 실행형 AI로 설명 [[sources/posco-newsroom-aw2026-poscodx-ai-workforce-2026-04]]; 실제 자율 범위 _미공개_

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS**: _미공개 (not disclosed)_
- **AI 시스템 배치**: 포스코DX 자체 플랫폼 '에이전티' (에이전트 생성·운영·평가·재배치 관리) ⚠️ 자사 보고 [[sources/posco-newsroom-aw2026-poscodx-ai-workforce-2026-04]]
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: _미공개 (not disclosed)_
- **사용자 접점**: _미공개 (not disclosed)_
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: 인사·구매·경영분석 사무 업무 영역 [[sources/posco-newsroom-aw2026-poscodx-ai-workforce-2026-04]]; 구체 데이터 항목 _미공개_
- **데이터 규모**: _미공개 (not disclosed)_ — 직원 수 수치는 인용 소스에 없음
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: _미공개 (not disclosed)_
- **데이터 거버넌스**: 에이전티 플랫폼이 에이전트 평가·재배치 관리 [[sources/posco-newsroom-aw2026-poscodx-ai-workforce-2026-04]]; 그룹DX전략실·AI로봇융합연구소 신설 [[sources/eroun-posco-group-2026-reorg-2025-12]] [[sources/snmnews-posco-group-2026-appointments-2025-12]] — 에이전트 데이터 거버넌스 역할 여부 _미공개_
- **민감정보 처리**: _미공개 (not disclosed)_ — 인사 영역 에이전트는 AI 기본법 고영향 검토 대상

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **모델 유형**: 실행형 에이전트 (AI 임플로이·AI 오퍼레이터) [[sources/posco-newsroom-aw2026-poscodx-ai-workforce-2026-04]]; 기술 구성 _미공개_
- **제공 방식**: 포스코DX 자체 구축 (에이전티) [[sources/posco-newsroom-aw2026-poscodx-ai-workforce-2026-04]]
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **Orchestration 프레임워크**: 에이전티 — 생성·운영·평가·재배치 관리 [[sources/posco-newsroom-aw2026-poscodx-ai-workforce-2026-04]]; 세부 _미공개_
- **평가·가드레일**: 에이전티의 '평가' 기능 언급 [[sources/posco-newsroom-aw2026-poscodx-ai-workforce-2026-04]]; 기준 _미공개_ — "개발 중"(announced)

### E. Organization & Team (조직·팀 구조)

- **오너십**: 포스코DX (에이전트·플랫폼 개발) [[sources/posco-newsroom-aw2026-poscodx-ai-workforce-2026-04]]
- **참여 역할**: 그룹DX전략실장 임치현(UNIST 부교수 영입), 포스코홀딩스 AI로봇융합연구소장 윤일용(전 포스코DX AI기술센터장) [[sources/eroun-posco-group-2026-reorg-2025-12]] [[sources/snmnews-posco-group-2026-appointments-2025-12]] — 110개 에이전트 프로젝트와의 직접 관계는 _미공개_
- **팀 규모·기간**: _미공개 (not disclosed)_
- **거버넌스 체계**: 2026 조직개편으로 DX 관련 조직 재정비 [[sources/eroun-posco-group-2026-reorg-2025-12]]; 에이전트 거버넌스 체계 세부 _미공개_
- **변화관리**: _미공개 (not disclosed)_
- **파트너**: _미공개 (not disclosed)_


## Impact / Metrics (기대효과)

### 기대효과 요약
한국 제조 그룹의 AI 에이전트 portfolio 첫 사례 + 그룹 차원 거버넌스 — 우리은행 금융권 사례와 paired reference.

- ⚠️ 자사 보고: 약 110개 에이전트 개발 중 — 배포 시점·성과 수치 _미공개_ [[sources/posco-newsroom-aw2026-poscodx-ai-workforce-2026-04]]
- ⚠️ 자사 보고: 인사·구매·경영분석 사무 영역 중심 [[sources/posco-newsroom-aw2026-poscodx-ai-workforce-2026-04]]
- ✅ 그룹 AI 거버넌스 조직 신설·인사 (Tier 2 언론 확인) [[sources/eroun-posco-group-2026-reorg-2025-12]] [[sources/snmnews-posco-group-2026-appointments-2025-12]]

## Governance & Risk

- ⚠️ 110개 에이전트 quality·일관성 governance — 우리은행 175와 동일 risk
- ⚠️ 인사 영역은 한국 AI 기본법 고영향 AI 분류 가능
- ⚠️ "개발 중" — 배포 시점 미공개, production 후 효과 검증 필요

## Contradictions

> [!note] 2026-09-27 grounding — 인용 소스에 없는 그룹 직원 수, 계열사 공통 활용, 2026 launch 예정, 자체 클라우드·SSO·모델 혼합 추정 서술을 제거·_미공개_ 처리. 조직개편 기사 2건은 AI 에이전트 내용을 담지 않으므로 거버넌스 맥락 근거로만 인용.

## Consulting Angle

- **KR 제조 그룹 AI 에이전트 portfolio reference**:
  - 우리은행 175 [[woori-bank-175-ai-agents]] (금융, portfolio framework)
  - 포스코DX 110 (제조, 그룹 거버넌스 강화)
  - SK A.Biz 25개사 [[sk-group-aibiz-25-companies]] (단일 표준 platform)
  - 3가지 KR 그룹사 AI 에이전트 운영 모델 비교
- **그룹 거버넌스 reference**: UNIST 교수 영입 + 신규 연구소장 임명 = 외부 인재 + 내부 R&D 통합 패턴
- **반면교사**:
  - "개발 중" → 배포 시점·production 효과 _미공개_
  - 110개 에이전트 동시 운영 governance 복잡도 (우리은행 동일 risk)
- **Watch list**: 110개 에이전트 배포 발표 시 본 page 갱신
