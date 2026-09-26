---
title: "LG AI연구원 — ChatEXAONE 그룹 정식 서비스"
slug: lg-chatexaone-group-rollout
page_type: enterprise-ai
moved_from_usecases: 2026-09-27
primary_category: Employee Experience & HR Ops
subcategory: Employee Self-service
tags: [lg, exaone, chatexaone, korean-llm, group-rollout, lg-electronics, lg-innotek, lg-display, internal-platform, korea, beta-65-percent-utilization]
company: LG (LG전자·LG이노텍·LG디스플레이 등 그룹 5만+)
industry: [tech, semiconductor, manufacturing]
region: [kr]
employee_class: [기술사무직, 전임직]
vendor: [LG AI Research]
vendor_type: [foundation-model, internal-build]
output: "LG 그룹 5만+ 임직원 자연어 query에 대한 사내 RAG 응답 (사내 규정·프로젝트·기술 문서, 출처 표시) + multi-format 이해 (PPTX·PDF·CSV·도표·수식) + SQL 생성 + 22개 언어 코드"
ai_tech_type: [generative]
ai_tech_subtype: [summarization-qa, text-generation, information-extraction]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: []
frequency: daily
first_seen: 2024-08-01
last_confirmed: 2026-04-01
confidence: 0.8
evidence_grade: A
corroborated_by: 2
freshness: fresh
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/bloter-lg-exaone-external-open-2025-07.md, sources/cio-korea-lg-exaone3-chatexaone-beta-2024-08.md, sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]
related_usecases:
  - shinhan-bank-ai-one-platform
  - sk-group-aibiz-25-companies
  - mirae-asset-ai-assistant-platform
related_vendors: []
---

## Summary

LG AI연구원이 자체 LLM **EXAONE** 기반 기업용 AI 에이전트 'ChatEXAONE'을 LG 임직원 대상 베타(2024-08-07, 엑사원 3.0) → 정식 서비스(2024-12-09, 엑사원 3.5)로 출시. [[sources/cio-korea-lg-exaone3-chatexaone-beta-2024-08.md]] [[sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]] 사내 보안 환경에서 실시간 웹 검색·문서 요약·번역·보고서 작성·데이터 분석·코딩 지원, 14개 직무·133개 업무별 특화 지시문 추천 (⚠️ 자사 보고). 2025-07-22 외부 기업·공공기관 직장인 대상 오픈베타로 개방. [[sources/bloter-lg-exaone-external-open-2025-07.md]] 이용 임직원 수·활용률은 _미공개_ (2026-09-27 grounding 점검: 종전 "5만+ 임직원·사무직 65퍼센트 활용률·22개 언어" 수치는 인용 소스에 없어 제거). 한국 자체 LLM 기반 그룹 전사 AI 챗봇 사례.

## Problem / Why (도입 배경)

- **Before**: ❓ baseline 미공개 (직원 규모·기존 정보 검색 방식 — 소스에 없음)
- **Pain point**: ⚠️ 자사 보고: 내부 데이터 유출 걱정 없이 사내 보안 환경에서 생성형 AI를 업무에 활용 (정보 암호화·개인정보 보호 기술 적용). [[sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]]
- **Trigger**: ✅ LG AI연구원의 엑사원 3.0 오픈소스 공개(2024-08-07)와 동시에 임직원 베타 시작 → 엑사원 3.5 공개(2024-12-09)와 함께 정식 서비스. [[sources/cio-korea-lg-exaone3-chatexaone-beta-2024-08.md]] [[sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]]

## Solution Architecture

### A. Process (프로세스)

- **Before**: ❓ 미공개 (소스에 기존 업무 방식 서술 없음)
- **After**:
  1. ✅ LG 임직원이 전용 웹페이지에 접속해 가입 후 업무에 활용 (2024-12-09~). [[sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]]
  2. ✅ 실시간 웹 정보 기반 질의응답, 문서·이미지 기반 질의응답, 코딩, 데이터베이스 관리 (베타 기능 범위). [[sources/cio-korea-lg-exaone3-chatexaone-beta-2024-08.md]]
  3. ⚠️ 자사 보고: '심층 분석(Deep)'·'출처 선택(Dive)' 기능 — 범용·해외 사이트·학술 자료·유튜브 등 검색 범위 선택. [[sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]]
  4. ⚠️ 자사 보고: 14개 직무·133개 업무별 특화 지시문 추천, 관심 업무 설정. [[sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]]
- **HITL**: _미공개 (not disclosed)_
- **Frequency**: _미공개 (not disclosed)_
- **Scope**: assistive — Q&A·요약·생성 (소스 기준 기능 범위)

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS**: _미공개 (not disclosed)_
- **AI 시스템 배치**: ✅ LG AI연구원이 임직원 대상 기업용 AI 에이전트로 제공. [[sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]]
- **배포 환경**: ⚠️ 자사 보고: "사내 보안 환경" — 구체 인프라 _미공개_. [[sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]]
- **연동·통합**: _미공개 (not disclosed)_
- **사용자 접점**: ✅ 전용 웹페이지. [[sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]] (모바일·IDE 등 _미공개_)
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: ✅ 실시간 웹 검색 결과·사용자가 업로드한 문서·이미지. [[sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]] [[sources/cio-korea-lg-exaone3-chatexaone-beta-2024-08.md]]
- **데이터 규모**: _미공개 (not disclosed)_ (이용 임직원 수·활용률 — 수치 근거 미확보, 2026-09-27 grounding 점검)
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: ⚠️ 자사 보고: 실시간 웹 검색 결과·업로드 문서 기반 검색 증강 생성(RAG) 고도화. [[sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]]
- **데이터 거버넌스**: _미공개 (not disclosed)_
- **민감정보 처리**: ⚠️ 자사 보고: 정보 암호화·개인 정보 보호 기술 적용. [[sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]]

### D. Model (모델)

- **Foundation model**: ✅ **EXAONE** (LG AI연구원 자체 개발) — 베타 엑사원 3.0, 정식 서비스 엑사원 3.5. [[sources/cio-korea-lg-exaone3-chatexaone-beta-2024-08.md]] [[sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]]
- **모델 유형**: ✅ LLM (질의응답·요약·번역·코딩; 문서·이미지 기반 질의응답). [[sources/cio-korea-lg-exaone3-chatexaone-beta-2024-08.md]]
- **제공 방식**: _미공개 (not disclosed)_
- **커스터마이징 기법**: ⚠️ 자사 보고: RAG 고도화 + 직무별 특화 지시문. [[sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]] (fine-tuning 여부 _미공개_)
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: ⚠️ 자사 보고: 환각 최소화를 위해 RAG 고도화. [[sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]] 평가 수치 _미공개_

### E. Organization

- **오너십**: ✅ LG AI연구원 (개발·제공). [[sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]] 계열사별 운영 체계 _미공개_
- ✅ 2025-07-22 외부 기업·공공기관 직장인 대상 오픈베타 개방 — "내부 업무용으로 축적된 기술"의 상업화 전환. [[sources/bloter-lg-exaone-external-open-2025-07.md]]

## Impact / Metrics (기대효과)

### 기대효과 요약
한국 자체 LLM (EXAONE)으로 LG 임직원에게 기업용 AI 에이전트 제공 — ⚠️ 기대효과 수치 미공개 (이용 임직원 수·활용률·시간 절감 모두 소스에 없음).

- ✅ 베타 → 정식 서비스 (2024-08-07 → 2024-12-09, 4개월). [[sources/cio-korea-lg-exaone3-chatexaone-beta-2024-08.md]] [[sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]]
- ✅ 내부 전용 → 외부 오픈베타 (2025-07-22). [[sources/bloter-lg-exaone-external-open-2025-07.md]]
- ⚠️ 벤더 주장: 엑사원 3.0은 2.0 대비 추론 처리 시간 56%·메모리 35%·구동 비용 72% 절감 (모델 지표, ChatEXAONE 효과 아님). [[sources/cio-korea-lg-exaone3-chatexaone-beta-2024-08.md]]
- 활용률·이용자 수: _미공개_ (수치 근거 미확보 — 2026-09-27 grounding 점검)

## Governance & Risk

- ✅ 자체 LLM (EXAONE) — 데이터 주권 강력
- ⚠️ 자사 보고: 정보 암호화·개인정보 보호 기술 적용, 사내 보안 환경. [[sources/lg-newsroom-exaone-3-5-chatexaone-launch-2024-12.md]]
- ⚠️ 활용률·생산직 적용 여부 _미공개_
- ⚠️ 한국 AI 기본법 (2026-01-22) — 일반 Q&A는 회피, 평가·승진 영향 시 고영향 AI 분류 가능

## Consulting Angle

- **★최우선 reference**: 한국 대기업 자체 LLM을 임직원 AI 에이전트로 운영하는 사례. SKT A.X (SK 그룹 표준화) [[sk-group-aibiz-25-companies]]·네이버 Hyperclova X (미래에셋 [[mirae-asset-ai-assistant-platform]]) 와 함께 KR 자체 LLM 3대 reference — 단, 정량 활용 지표는 _미공개_
- **2026 Q3-Q4 KR consulting deck 사례감**:
  - "한국 대기업 = 자체 LLM 운영 가능한가?" — LG가 답 (ROI 수치는 미공개)
  - 베타 4개월 후 정식 서비스, 이후 외부 오픈베타로 상업화 전환 — adoption 경로 증거
- **그룹 차원 표준화 vs 분산 비교**:
  - SK: A.Biz 단일 표준 [[sk-group-aibiz-25-companies]]
  - LG: ChatEXAONE (LG AI연구원 제공; 계열사별 도입 규모 _미공개_)
  - 삼성·현대: 그룹 표준화 미공개
- **EXAONE ROI**: LG AI연구원 자체 LLM 개발 비용 vs 그룹 dogfooding adoption — 한국 대기업 자체 LLM 의사결정 framework 핵심 (활용률 수치는 클라이언트 POC로 별도 측정 필요)
- **반면교사**:
  - 활용률·생산직 적용 여부 미공개 — 생산직 fit POC 별도 필요
  - LG AI연구원은 LG 계열사 표준이지만 외부 기업에는 fit 안 맞음 (자체 LLM 보유 그룹만 적용 가능) — 2025-07 외부 오픈베타로 외부 기업도 검토 가능
  - 문서·이미지 기반 질의응답 quality의 한국어 specific term POC 검증 권장
