---
title: "LG AI연구원 — ChatEXAONE 그룹 정식 서비스"
slug: lg-chatexaone-group-rollout
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
frequency: daily
first_seen: 2024-08-01
last_confirmed: 2026-04-01
confidence: 0.55
consulting_angle_status: filled
sources:
  - sources/kr-conglomerate-2026-q2-research.md
related_usecases:
  - shinhan-bank-ai-one-platform
  - sk-group-aibiz-25-companies
  - mirae-asset-ai-assistant-platform
related_vendors: []
---

## Summary

LG AI연구원이 자체 LLM **EXAONE** 기반 'ChatEXAONE' 정식 서비스 출시 (2026 Q1, 1년 베타 후). LG전자·LG이노텍·LG디스플레이 등 LG 그룹 **5만+ 임직원** 대상. 사무직 베타 활용률 **65%** 검증. 사내 규정·프로젝트 자료 검색·요약, **PPTX·PDF·CSV·도표·수식 이해**, SQL 생성, **22개 언어 코드 지원**. 한국 자체 LLM 기반 그룹 전사 AI 챗봇 운영의 가장 큰 사례.

## Problem / Why (도입 배경)

- **Before**: LG 그룹 5만+ 임직원이 사내 정책·프로젝트 자료 검색을 sharepoint·이메일·시니어 문의로 처리 — 정보 fragmented
- **Pain point**: 글로벌 commercial LLM (ChatGPT·Claude) 사용은 데이터 주권·보안 이슈로 제약. 한국어·LG 도메인 fit 부족
- **Trigger**: LG AI연구원이 EXAONE 자체 LLM 개발 → 그룹 dogfooding 명분 → 1년 베타(2024-08~2025) 후 production 정식 launch

## Solution Architecture

### A. Process

- **Before**: 직원이 sharepoint/이메일/시니어 문의로 정보 search → 시간 소요·정확도 변동
- **After**:
  1. 직원이 ChatEXAONE web/모바일 access (그룹 SSO)
  2. 자연어로 query — 사내 규정·프로젝트 자료·기술 문서 등
  3. EXAONE이 multi-format 이해 (PPTX·PDF·CSV·도표·수식)
  4. 응답 + 출처 표시; SQL 생성·22개 언어 코드 지원
  5. 직원이 결과 검토·활용
- **HITL**: 직원 자율 사용. quality 모니터링은 LG AI연구원·계열사 IT
- **Frequency**: daily (사무직 65% 활용률)
- **Scope**: assistive — Q&A·요약·생성, 결정 권한 없음

### B. System & Infrastructure

- **Core HRIS**: 각 LG 계열사 HRIS (Workday·SAP 혼재) — 별도, ChatEXAONE은 horizontal 플랫폼
- **AI 시스템 배치**: LG AI연구원이 운영, 계열사에 share
- **배포 환경**: LG cloud / on-prem (보안 민감 영역) — 구체 _미공개_
- **연동·통합**: 그룹 SSO + 사내 문서 RAG 코퍼스
- **사용자 접점**: Web + 모바일 + IDE plugin (코드 지원)
- **인증·권한**: LG 그룹 SSO

### C. Data

- **입력 데이터 소스**: 사내 규정·프로젝트 자료·기술 문서·매뉴얼 (RAG 코퍼스)
- **데이터 규모**: 5만+ 직원 활용, 사무직 65% 재방문률 (베타 검증)
- **전처리·정제**: multi-format 처리 (PPTX·PDF·CSV·도표·수식)
- **학습 vs RAG vs In-context**: EXAONE base + 사내 문서 RAG (구체 architecture _미공개_)
- **데이터 거버넌스**: LG 계열사별 격리 + 그룹 공통 정책
- **민감정보 처리**: 한국 개인정보보호법 + 영업비밀 — 사내 LLM이라 데이터 주권 우위

### D. Model

- **Foundation model**: ✅ **EXAONE** (LG AI연구원 자체 개발 LLM)
- **모델 유형**: LLM (생성·요약·multi-modal·코드)
- **제공 방식**: Self-hosted (LG cloud)
- **커스터마이징 기법**: LG 도메인 fine-tuning + RAG (사내 문서 코퍼스)
- **Orchestration 프레임워크**: 자체 구축 (LG AI연구원)
- **평가·가드레일**: 베타 1년간 quality 검증 (65% 사무직 재방문률)

### E. Organization

- LG AI연구원 (개발·운영) + LG전자·이노텍·디스플레이 IT·HR
- 그룹 차원 dogfooding → 외부 수요 검증 (B2B 진출 가능성)

## Impact / Metrics (기대효과)

### 기대효과 요약
한국 자체 LLM (EXAONE)으로 그룹 5만+ 임직원에게 AI 챗봇 제공 — 한국 대기업 자체 LLM 활용 ROI의 가장 큰 정량 reference.

- ✅ 5만+ 임직원 활용 (LG전자·이노텍·디스플레이)
- ✅ 사무직 65% 재방문률 (베타 1년 검증)
- ✅ multi-format 이해 (PPTX·PDF·CSV·도표·수식)
- ✅ SQL 생성·22개 언어 코드 지원
- 베타 → 정식 launch (2024-08 → 2026 Q1)
- 출처: CIO 한국, LG 보도자료, 블로터 (Tier 2~3 cross-reference)

## Governance & Risk

- ✅ 자체 LLM (EXAONE) — 데이터 주권 강력
- ✅ 베타 1년 검증 후 정식 launch — quality risk 완화
- ⚠️ 65% 재방문률은 사무직 한정 — 생산직 적용 _미공개_
- ⚠️ 한국 AI 기본법 (2026-01-22) — 일반 Q&A는 회피, 평가·승진 영향 시 고영향 AI 분류 가능

## Consulting Angle

- **★최우선 reference**: 한국 대기업 자체 LLM 활용의 가장 큰 정량 사례. SKT A.X (SK 그룹 표준화) [[sk-group-aibiz-25-companies]]·네이버 Hyperclova X (미래에셋 [[mirae-asset-ai-assistant-platform]]) 와 함께 KR 자체 LLM 3대 reference
- **2026 Q3-Q4 KR consulting deck 표지 사례감**:
  - "한국 대기업 = 자체 LLM ROI 가능한가?" — LG가 답
  - 베타 65% 활용률 + 정식 launch는 가장 강력한 adoption 증거
- **그룹 차원 표준화 vs 분산 비교**:
  - SK: A.Biz 단일 표준 (25개사 8만 명)
  - LG: ChatEXAONE 그룹 5만+ (계열사별 도입)
  - 삼성·현대: 그룹 표준화 미공개
- **EXAONE ROI**: LG AI연구원 자체 LLM 개발 비용 vs 그룹 dogfooding adoption — 한국 대기업 자체 LLM 의사결정 framework 핵심
- **반면교사**:
  - 65% 재방문률은 사무직 한정 — 생산직 fit POC 별도 필요
  - LG AI연구원은 LG 계열사 표준이지만 외부 기업에는 fit 안 맞음 (자체 LLM 보유 그룹만 적용 가능)
  - multi-format 이해 quality (PPTX·도표) 한국어 specific term POC 검증 권장
