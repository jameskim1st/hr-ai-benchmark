---
title: "Goldman Sachs — GS AI Assistant 전사 배포"
slug: goldman-sachs-gs-ai-assistant
page_type: enterprise-ai
moved_from_usecases: 2026-09-27
primary_category: Employee Experience & HR Ops
subcategory: Employee Self-service
tags: [gs-ai-assistant, employee-productivity, knowledge-worker, generative-ai, firmwide-rollout, github-copilot, developer-copilot, banking, workforce-restructuring]
company: Goldman Sachs
industry: [finance, banking]
region: [na, global]
employee_class: [all]
vendor: [OpenAI, Google, Anthropic]
vendor_type: [foundation-model, internal-build]
output: "지식노동자 자연어 요청에 대한 LLM 멀티모델 답변 (GPT-4o/o3-mini, Gemini 2.0, Claude 3.7 라우팅) — 문서 요약·리서치 노트·규제 문서 분석·코드·다국어 번역. 사내 방화벽 격리"
ai_tech_type: [generative]
ai_tech_subtype: [summarization-qa]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: []
frequency: daily
first_seen: 2025-01-21
last_confirmed: 2025-06-24
confidence: 0.50
sources:
  - sources/cnbc-goldman-gs-ai-assistant-2025-01.md
  - sources/fortune-goldman-gs-ai-2025-06.md
  - sources/hrkatha-goldman-ai-assistant-2025.md
  - "CNBC 2025-10-15 https://www.cnbc.com/2025/10/15/jpmorgan-chase-goldman-sachs-ai-hiring.html"
  - "HR Executive https://hrexecutive.com/jpmorgan-ceo-we-have-displaced-people-from-ai-and-we-offer-them-other-jobs/"
  - "HR Dive https://www.hrdive.com/news/banks-ramp-up-ai-hiring-roi-efficiency-gains-evident-insights/746724/"
related_usecases:
  - jpmorgan-llm-suite-employee-productivity
  - jpmorgan-llm-suite-redeployment
  - lloyds-banking-workday-genai-hr
related_vendors:
  - openai
---

## Summary

Goldman Sachs는 2025년 1월 GS AI Assistant를 10,000명 파일럿으로 시작, 2025년 6월 전 지식노동자 대상 전사 배포를 완료했다. ✅ **Fact** 이 도구는 다수의 LLM(OpenAI GPT-4o/o3-mini, Google Gemini 2.0, Anthropic Claude 3.7 포함)을 단일 인터페이스로 접근하는 멀티모델 어시스턴트로, 문서 요약·리서치 노트 초안·규제 문서 분석·코드 생성·다국어 번역 등을 지원한다. [[sources/fortune-goldman-gs-ai-2025-06.md]] 2026-09-27 `jpmorgan-goldman-sachs-hr-ai` 합본 페이지의 Goldman 사실 이관: 12,000 개발자 GitHub Copilot 배포(⚠️ 자사 보고 ~20% 효율 향상), 46.5K knowledge worker firm-wide, 1,000명 감축 보도 (CNBC 2025-10-15).

## Problem / Why (도입 배경)

Goldman Sachs의 지식노동자들은 리서치 노트 작성, 규제 문서 요약, 클라이언트 쿼리 응답 등 정형화된 고숙련 작업에 많은 시간을 소비하고 있었다. 외부 AI 도구 사용 시 민감 금융·고객 데이터가 방화벽 외부로 유출될 위험이 있었다.

## Solution Architecture

> **최우선 원칙**: 이 섹션은 **공개된 사실만** 기록한다.

### A. Process (프로세스)

- **Before (As-is)**: 지식노동자가 직접 문서 작성, 수동 검색, 개별 도구 사용.
- **After (To-be)**: ✅ **Fact** GS AI Assistant를 통해 문서 요약, 리서치 노트·코드·번역 초안 생성. 다양한 부서(채용·운영·리서치 등)에서 사용. [[sources/fortune-goldman-gs-ai-2025-06.md]] (병합 이관, CNBC 2025-10-15) ✅ 사용자가 portal 내에서 모델 선택(GPT/Gemini/Claude/OSS) → 문서 요약·이메일 초안·Excel/data 분석·번역 요청; Developer Copilot·Banker Copilot으로 확장.
- **Human-in-the-loop (HITL) 지점**: AI 생성 콘텐츠는 직원이 검토 후 사용. 완전 자율 의사결정 없음.
- **Trigger & Frequency**: 일상 업무 중 수시(on-demand).
- **Scope of autonomy**: Recommend 수준.

```mermaid
flowchart LR
    A[직원 입력\n텍스트·문서] --> B[GS AI Assistant\n사내 방화벽 내]
    B --> C{LLM 라우팅\nGPT-4o·Gemini·Claude 등}
    C --> D[AI 응답 생성]
    D --> E[직원 검토]
    E --> F[사용]
```
범례: 실선 = [[sources/fortune-goldman-gs-ai-2025-06.md]] 확인.

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS / 기반 시스템**: _미공개 (not disclosed)_
- **AI 시스템 배치**: ✅ **Fact** 사내 방화벽 내 격리 운영. 외부 LLM들과 연동하되 데이터가 외부로 나가지 않도록 설계. [[sources/cnbc-goldman-gs-ai-assistant-2025-01.md]] (병합 이관) ✅ 46.5K knowledge worker 대상 firm-wide (10K 파일럿 → 2025-06 전사) — CNBC 2025-10-15
- **배포 환경**: _미공개 (not disclosed)_
- **사용자 접점 (UX layer)**: ✅ 사내 web portal — Developer Copilot·Banker Copilot으로 확장 (병합 이관, CNBC 2025-10-15)
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: 직원이 입력하는 텍스트·문서. 내부 지식베이스 연동 여부 _미공개 (not disclosed)_.
- **데이터 거버넌스**: ✅ **Fact** 사내 방화벽 격리로 민감 데이터 유출 차단. [[sources/cnbc-goldman-gs-ai-assistant-2025-01.md]] (병합 이관, CNBC 2025-10-15) prompt·response audit trail, 컴플라이언스 모니터링, 모델 swap 시 재학습 불필요 — 병합 전 페이지에서 ✅와 ⚠️ 자사 보고 표기가 혼재하여 보수적으로 ⚠️ 자사 보고로 기록
- **민감정보 처리**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: ✅ **Fact** OpenAI GPT-4o, GPT-4o-mini, o3-mini; Google Gemini 2.0 Flash, Gemini 2.0 Flash Vision, Gemini 1.5 Flash, Gemini 1.5 Pro; Anthropic Claude 3.7 Sonnet; 오픈소스 모델. [[sources/fortune-goldman-gs-ai-2025-06.md]]
- **Model 유형**: LLM (생성형), 멀티모델.
- **제공 방식**: 다수 외부 벤더 API + 내부 포털 라우팅.
- **커스터마이징 기법**: _미공개 (not disclosed)_

### E. Organization & Team (조직·팀 구조)

- **오너십**: _미공개 (not disclosed)_
- **팀 규모**: ✅ **Fact** 2024년에만 AI 엔지니어 500명 이상 신규 채용. [[sources/hrkatha-goldman-ai-assistant-2025.md]] (병합 이관) ✅ 12,000 개발자에게 GitHub Copilot 배포 — CNBC 2025-10-15
- **거버넌스 체계**: _미공개 (not disclosed)_

## Impact / Metrics (기대효과)

### 기대효과 요약
10,000명 파일럿에서 전사 확대(Fact). 파일럿 참여자가 효율 개선 및 시간 절약 보고하나 구체 수치 미공개 (자사 보고).

- ✅ **Fact**: 10,000명 파일럿 → 전사 지식노동자 전체로 확대 (2025년 6월). [[sources/fortune-goldman-gs-ai-2025-06.md]]
- ⚠️ **자사 보고**: 파일럿 참여자들이 효율 개선 및 정확도 향상, 시간 절약 보고. 독립 검증 미확인. [[sources/fortune-goldman-gs-ai-2025-06.md]]
- ⚠️ **자사 보고 (CNBC 2025-10-15, 병합 이관)**: 12,000 개발자 GitHub Copilot 배포 → **~20% 효율성 향상**
- ✅ **Fact (CNBC 2025-10-15 보도, 병합 이관)**: **1,000명 감축** 보도 — AI가 investment banking 보상·커리어를 reshape

## Governance & Risk

- 사내 방화벽 내 격리 운영으로 금융 민감 데이터 보호.
- 향후 agentic AI(멀티스텝 자율 실행) 도입 계획 공개 — 현재는 생성 보조 수준.
- 세부 AI 윤리·편향 감사 체계: _미공개 (not disclosed)_

## Contradictions

> [!note] 2026-09-27 합본 페이지 병합
> `jpmorgan-goldman-sachs-hr-ai` 합본 페이지의 Goldman 사실을 이관 (JPM 사실 → [[jpmorgan-llm-suite-redeployment]], 금융 산업 인사이트 → [[industry-region-landscape]]). 10,000명 파일럿(이 페이지)과 "10,000 직원에게 GS AI 배포"(합본 페이지)는 동일 사실이며, 합본 페이지의 46.5K firm-wide 수치는 이 페이지의 "전 지식노동자"와 정합. 충돌 없음.

## Consulting Angle

- JPMorgan LLM Suite와 함께 "월가 지식노동자 AI 생산성 플랫폼" 대표 사례로 짝으로 제시. 두 사례 모두 멀티모델·내부 방화벽 격리·전사 배포의 공통 패턴.
- 국내 증권사·보험사 AI 도입 로드맵 제안 시, 파일럿(10,000명) → 전사(전체) 단계적 확대 전략의 실증 레퍼런스.
- **반면교사**: 2024년 AI 엔지니어 500명 신규 채용은 "내재화 전략의 비용 현실"을 보여줌. 외부 벤더 SaaS 대비 내재화 비용 비교 시 활용.
- **"전 직원에게 AI 도구 배포" 전략** (병합 이관): Moderna의 "모든 직원에게 ChatGPT Enterprise"와 유사한 firm-wide 배포 패턴
- **12k 개발자 Copilot 배포** (병합 이관): HR이 아닌 Engineering 주도지만 **"전사 AI 배포가 HR 전략(채용·감축·보상)에 미치는 영향"**의 증거 — 1,000명 감축 보도와 함께 제시
