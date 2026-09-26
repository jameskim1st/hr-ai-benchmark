---
title: "미래에셋증권 — 'AI Assistant 플랫폼'"
slug: mirae-asset-ai-assistant-platform
page_type: enterprise-ai
moved_from_usecases: 2026-09-27
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
visibility: public
case_type: adoption
regulatory_exposure: []
frequency: daily
first_seen: 2024-09-01
last_confirmed: 2026-04-01
confidence: 0.55
evidence_grade: B
corroborated_by: 1
freshness: fresh
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/4th-mirae-asset-ai-assistant-platform-2024-09.md, sources/genon-mirae-asset-genai-platform-case-2025-05.md]
related_usecases:
  - shinhan-bank-ai-one-platform
  - kb-bank-ai-hr-deep-change
  - sk-group-aibiz-25-companies
related_vendors: []
---

## Summary

미래에셋증권이 네이버클라우드 협업 — 전용 LLM **'하이퍼클로바X 대시'** 위에 구축한 **사내 AI 어시스턴트 플랫폼** (2024-09 production). 직원·부서가 본인 업무 매뉴얼·노하우 문서를 업로드해 학습시킨 후 **전용 챗봇을 자체 생성** — AI 비전문가도 활용 가능한 **No-code 빌더**. 한국 자체 LLM (네이버 Hyperclova X) 기반 — 데이터 주권·금융 규제 대응이 driver.

## Problem / Why (도입 배경)

- **Before**: ❓ baseline 미공개 (기존 정보 검색 방식 — 소스에 없음)
- **Pain point**: ✅ 금융사는 망분리·데이터 보안 이슈로 기성 생성형 AI를 사용할 수 없음 → 전용 LLM 필요. [[sources/4th-mirae-asset-ai-assistant-platform-2024-09.md]]
- **Trigger**: ✅ "AI를 통한 전사 업무 효율화와 금융 비즈니스 혁신" (박홍근 IT부문대표). [[sources/4th-mirae-asset-ai-assistant-platform-2024-09.md]]

## Solution Architecture

### A. Process (프로세스)

- **Before**: ❓ 미공개
- **After**:
  1. ✅ 직원·부서가 본인 업무 매뉴얼·노하우 문서 업로드. [[sources/4th-mirae-asset-ai-assistant-platform-2024-09.md]]
  2. ✅ 업로드 문서로 학습시킨 후 전용 챗봇 생성 (AI 비전문가도 가능). [[sources/4th-mirae-asset-ai-assistant-platform-2024-09.md]]
  3. ✅ 직원·부서원이 챗봇 사용. [[sources/4th-mirae-asset-ai-assistant-platform-2024-09.md]] (출처 표시 여부 _미공개_)
- **HITL**: _미공개 (not disclosed)_
- **Frequency**: daily

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS**: 미래에셋증권 사내 시스템 (구체 _미공개_)
- **AI 시스템 배치**: ✅ 자체 AI Assistant 플랫폼 + 네이버클라우드 협업 전용 LLM '하이퍼클로바X 대시'. [[sources/4th-mirae-asset-ai-assistant-platform-2024-09.md]]
- **배포 환경**: ✅ 온프레미스 sLLM (망분리·데이터 보안 이슈 대응). [[sources/4th-mirae-asset-ai-assistant-platform-2024-09.md]] (2026-09-27 grounding 점검: 종전 "NCP 클라우드" 표기는 소스와 상충하여 정정)
- **연동·통합**: ✅ 부서별 매뉴얼·노하우 문서 upload. [[sources/4th-mirae-asset-ai-assistant-platform-2024-09.md]] 시스템 연동 세부 _미공개_
- **사용자 접점**: ✅ 직원·부서가 직접 문서를 올려 전용 챗봇 생성·사용. [[sources/4th-mirae-asset-ai-assistant-platform-2024-09.md]] (web/모바일 등 채널 _미공개_)
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: ✅ 부서별 업무 매뉴얼·노하우 문서 (직원·부서 직접 upload). [[sources/4th-mirae-asset-ai-assistant-platform-2024-09.md]]
- **데이터 규모**: _미공개_ — 챗봇 수·인덱스 크기 비공개
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: ⚠️ 벤더 주장: RAG 서비스 구성 (GenON 고객사례, 원문 미확보). [[sources/genon-mirae-asset-genai-platform-case-2025-05.md]] 소스 기사는 "문서를 업로드해 학습"이라고만 표현. [[sources/4th-mirae-asset-ai-assistant-platform-2024-09.md]]
- **데이터 거버넌스**: _미공개 (not disclosed)_
- **민감정보 처리**: ✅ 망분리·데이터 보안 이슈로 기성 생성형 AI 대신 온프레미스 전용 LLM 구축. [[sources/4th-mirae-asset-ai-assistant-platform-2024-09.md]]

### D. Model (모델)

- **Foundation model**: ✅ 네이버 **하이퍼클로바X 대시 (HyperCLOVA X Dash)** 전용 LLM. [[sources/4th-mirae-asset-ai-assistant-platform-2024-09.md]]
- **모델 유형**: LLM (요약·QA)
- **제공 방식**: ✅ 네이버클라우드 협업, 온프레미스 sLLM. [[sources/4th-mirae-asset-ai-assistant-platform-2024-09.md]]
- **커스터마이즈 기법**: ✅ 부서·직원이 문서를 업로드해 전용 챗봇 생성. [[sources/4th-mirae-asset-ai-assistant-platform-2024-09.md]] ⚠️ 벤더 주장: RAG + AI 에이전트 (GenOS). [[sources/genon-mirae-asset-genai-platform-case-2025-05.md]]
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: ⚠️ No-code 빌더 챗봇의 prompt injection·hallucination 통제 부족 가능 — 모니터링 필요. 공식 framework _미공개_


## Impact / Metrics (기대효과)

### 기대효과 요약
한국 자체 LLM 활용으로 데이터 주권 + 금융 규제 fit + No-code로 부서별 자율 챗봇 확산.

- 2024-09 production launch
- 한국 자체 LLM (Hyperclova X) 활용
- No-code 빌더 — 부서·직원 자율 챗봇 생성
- ⚠️ standalone metric (시간 절감 등) _공식 미공개_

## Governance & Risk

- ✅ 한국 자체 LLM — 데이터 주권 강력
- 부서별 데이터 격리 여부: _미공개_
- ⚠️ 네이버클라우드 단일 vendor 의존 — 협상력·향후 비용 risk (⚠️ 벤더 주장: 구축에 GenON도 참여. [[sources/genon-mirae-asset-genai-platform-case-2025-05.md]])
- ⚠️ No-code 빌더의 quality 통제 governance _세부 미공개_
- ⚠️ 한국 AI 기본법 (2026-01-22) 고영향 AI 분류는 일반 Q&A는 회피 — 그러나 평가·승진 영향 시 재분류

## Consulting Angle

- **KR 금융권 자체 LLM 활용 reference (1순위)**:
  - JPMorgan LLM Suite [[jpmorgan-llm-suite-redeployment]] (외부 LLM private gateway) vs 미래에셋 (한국 자체 LLM) — 양 방향 비교
  - KB·신한·하나·미래에셋 모두 자체 LLM 플랫폼 구축 — 미래에셋은 Hyperclova X 선택, 신한 [[shinhan-bank-ai-one-platform]]은 자체 통합, 하나 하나은행 지식챗봇 (페이지 없음)은 자체 GenAI
- **No-code 빌더 패턴**: SK 그룹 25개사 'A.Biz' [[sk-group-aibiz-25-companies]]의 agent builder + 미래에셋 — 한국 KR 대기업 No-code 챗봇 빌더 best practice
- **2026 Q3-Q4 KR 컨설팅 deck**:
  - 한국 자체 LLM 시장 (네이버 Hyperclova X·KT Mi:dm·SKT A.X·LG EXAONE) 활용 reference
  - 데이터 주권·금융 규제·언어 fit 차원 글로벌 LLM (OpenAI·Anthropic) 대비 trade-off
- **반면교사**:
  - 한국 자체 LLM의 모델 capability 격차 (글로벌 frontier model 대비) — task별 fit 평가 필요
  - No-code 빌더로 만든 챗봇이 prompt injection·hallucination 통제 부족 가능 — quality 모니터링 plat 동반 필요
  - 부서별 자율 챗봇 확산 시 그룹 표준·governance 부재 risk — Workday ASOR [[workday-agent-system-of-record-asor]] 같은 거버넌스 framework 동반 권장
