---
title: "미래에셋증권 — 'AI Assistant 플랫폼' (네이버클라우드 하이퍼클로바X 대시, No-code 직원 챗봇 빌더)"
slug: mirae-asset-ai-assistant-platform
primary_category: Employee Experience & HR Ops
subcategory: Employee Self-service
tags: [mirae-asset, securities, naver-cloud, hyperclova-x, no-code, employee-chatbot-builder, korean-llm, korea, financial-securities, dash]
company: 미래에셋증권
industry: [finance, securities]
region: [kr]
employee_class: [전임직, 기술사무직]
vendor: [Naver Cloud]
vendor_type: [foundation-model, hrms]
output: "직원 자연어 query에 대한 부서별 매뉴얼·노하우 RAG 답변 + 출처 + 부서·직원이 No-code로 자체 생성한 전용 챗봇 인스턴스 (HyperCLOVA X Dash 기반)"
ai_tech_type: [generative]
ai_tech_subtype: [summarization-qa]
stage: production
frequency: daily
first_seen: 2024-09-01
last_confirmed: 2026-04-01
confidence: 0.45
consulting_angle_status: filled
sources:
  - sources/korea-conglomerate-hr-ai-2025-2026.md
related_usecases:
  - shinhan-bank-ai-one-platform
  - kb-bank-ai-hr-deep-change
  - sk-group-aibiz-25-companies
related_vendors: []
---

## Summary

미래에셋증권이 네이버클라우드 협업 — 전용 LLM **'하이퍼클로바X 대시'** 위에 구축한 **사내 AI 어시스턴트 플랫폼** (2024-09 production). 직원·부서가 본인 업무 매뉴얼·노하우 문서를 업로드해 학습시킨 후 **전용 챗봇을 자체 생성** — AI 비전문가도 활용 가능한 **No-code 빌더**. 한국 자체 LLM (네이버 Hyperclova X) 기반 — 데이터 주권·금융 규제 대응이 driver.

## Problem / Why

- **Before**: 미래에셋증권 직원이 사내 매뉴얼·노하우 문서 search 시 sharepoint·이메일 산발 — 정보 접근 비효율
- **Pain point**: 부서별 specific knowledge가 사내 walking encyclopedia (시니어)에 의존 — 시니어 퇴직·부재 시 손실
- **Trigger**: 2024 한국 자체 LLM 시장 성숙 + 금융 데이터 주권 압박

## Solution Architecture

### A. Process

- **Before**: 직원이 sharepoint·이메일·시니어 문의로 정보 search
- **After**:
  1. 직원·부서가 본인 업무 매뉴얼·노하우 문서 업로드
  2. AI Assistant 플랫폼이 RAG indexing
  3. **No-code 빌더**로 부서·직원 전용 챗봇 자체 생성
  4. 직원·부서원이 자연어로 챗봇 query
  5. 답변 + 출처 제공
- **HITL**: 부서 owner가 챗봇 콘텐츠·답변 quality 모니터링
- **Frequency**: daily

### B. System & Infrastructure (R9 research)

- **Core HRIS**: 미래에셋증권 사내 시스템 (구체 _미공개_)
- **AI 시스템 배치**: ✅ 자체 AI Assistant 플랫폼 (네이버클라우드 협업)
- **배포 환경**: ✅ 네이버클라우드 (NCP) — 한국 데이터 주권 driver
- **연동·통합**: ✅ 사내 SSO + 부서별 매뉴얼·노하우 문서 upload
- **사용자 접점**: ✅ web 기반 No-code 챗봇 빌더 + 직원 자연어 query
- **인증·권한**: ✅ 사내 SSO + 부서별 RBAC

### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 부서별 업무 매뉴얼·노하우 문서 (직원·부서 직접 upload)
- **데이터 규모**: _미공개_ — 챗봇 수·인덱스 크기 비공개
- **전처리·정제**: ✅ RAG indexing (구체 chunking·임베딩 _미공개_)
- **학습 vs RAG vs In-context**: ✅ RAG (No-code 빌더로 부서별 RAG)
- **데이터 거버넌스**: ✅ 부서별 RAG 격리. No-code 빌더 quality governance 세부 _미공개_
- **민감정보 처리**: ✅ 한국 자체 LLM (Hyperclova X) → 데이터 주권. 전자금융감독규정 fit

### D. Model (R9 research)

- **Foundation model**: ✅ 네이버 **하이퍼클로바X 대시 (HyperCLOVA X Dash)** — 한국어 specialized
- **모델 유형**: LLM (요약·QA)
- **제공 방식**: ✅ Naver Cloud Platform via 협업
- **커스터마이징 기법**: ✅ RAG + No-code 빌더 (부서별)
- **Orchestration 프레임워크**: _미공개_ — 네이버클라우드 stack 추정
- **평가·가드레일**: ⚠️ No-code 빌더 챗봇의 prompt injection·hallucination 통제 부족 가능 — 모니터링 필요. 공식 framework _미공개_


## Impact / Metrics

### 기대효과 요약
한국 자체 LLM 활용으로 데이터 주권 + 금융 규제 fit + No-code로 부서별 자율 챗봇 확산.

- 2024-09 production launch
- 한국 자체 LLM (Hyperclova X) 활용
- No-code 빌더 — 부서·직원 자율 챗봇 생성
- ⚠️ standalone metric (시간 절감 등) _공식 미공개_

## Governance & Risk

- ✅ 한국 자체 LLM — 데이터 주권 강력
- ✅ 부서별 RAG 격리 — 정보 leakage 통제
- ⚠️ 네이버클라우드 단일 vendor 의존 — 협상력·향후 비용 risk
- ⚠️ No-code 빌더의 quality 통제 governance _세부 미공개_
- ⚠️ 한국 AI 기본법 (2026-01-22) 고영향 AI 분류는 일반 Q&A는 회피 — 그러나 평가·승진 영향 시 재분류

## Consulting Angle

- **KR 금융권 자체 LLM 활용 reference (1순위)**:
  - JPMorgan LLM Suite [[jpmorgan-llm-suite-redeployment]] (외부 LLM private gateway) vs 미래에셋 (한국 자체 LLM) — 양 방향 비교
  - KB·신한·하나·미래에셋 모두 자체 LLM 플랫폼 구축 — 미래에셋은 Hyperclova X 선택, 신한 [[shinhan-bank-ai-one-platform]]은 자체 통합, 하나 [[hana-bank-knowledge-chatbot]]은 자체 GenAI
- **No-code 빌더 패턴**: SK 그룹 25개사 'A.Biz' [[sk-group-aibiz-25-companies]]의 agent builder + 미래에셋 — 한국 KR 대기업 No-code 챗봇 빌더 best practice
- **2026 Q3-Q4 KR 컨설팅 deck**:
  - 한국 자체 LLM 시장 (네이버 Hyperclova X·KT Mi:dm·SKT A.X·LG EXAONE) 활용 reference
  - 데이터 주권·금융 규제·언어 fit 차원 글로벌 LLM (OpenAI·Anthropic) 대비 trade-off
- **반면교사**:
  - 한국 자체 LLM의 모델 capability 격차 (글로벌 frontier model 대비) — task별 fit 평가 필요
  - No-code 빌더로 만든 챗봇이 prompt injection·hallucination 통제 부족 가능 — quality 모니터링 plat 동반 필요
  - 부서별 자율 챗봇 확산 시 그룹 표준·governance 부재 risk — Workday ASOR [[workday-agent-system-of-record-asor]] 같은 거버넌스 framework 동반 권장
