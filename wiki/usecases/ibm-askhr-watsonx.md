---
title: "IBM — AskHR 에이전트"
slug: ibm-askhr-watsonx
primary_category: Employee Experience & HR Ops
subcategory: Employee Self-service
tags: [askhr, chatbot, agent, watsonx, case-deflection, compensation-guidance, recognition, large-scale]
company: IBM
industry: [tech, it-services]
region: [global]
employee_class: [all]
vendor: [IBM]
vendor_type: [internal-build]
output: "직원 자연어 요청에 대한 80+ HR 태스크 처리 — 정책 Q&A 답변 + 매니저용 salary budget 배분 제안 + recognition 메시지 자동 생성·포인트 부여 + expense 자동 처리"
ai_tech_type: [generative, predictive, automation]
ai_tech_subtype: [summarization-qa, text-generation, clustering-classification, rpa]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: []
kr_law: 일반 개인정보보호법 수준 (보상 guidance 기능은 고영향 검토)
kr_union: 협의 의무 낮음 (정보 제공 성격; 보상 배분 제안은 협의 검토)
kr_language: 해당 없음 (자체 구축; 한국어 NLU 선결 — 페이지 명시)
kr_vendor: 해당 없음 (자체 구축)
frequency: daily
first_seen: 2025-06-12
last_confirmed: 2025-10-24
confidence: 0.45
evidence_grade: B
corroborated_by: 1
freshness: fresh
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/hr-brew-ibm-moderna-2025-06.md, sources/hr-brew-hr-adapting-ai-future-2025-10.md, sources/ibm-askhr-case-study-2025.md]
related_usecases:
  - moderna-ask-hr-routing
  - workday-illuminate-employee-sentiment
related_vendors: []
---

# IBM — AskHR 에이전트

> ★ **엔터프라이즈 HR AI 최대 scale 사례**: 270,000명 IBM 직원 대상, 연 210만 대화, 80+ HR 태스크 자동화. Moderna Ask HR의 "routing GPT" 수준을 넘어 **compensation guidance·recognition 생성·expense 처리까지 agentic 수준**으로 진화한 사례.

## Summary

IBM의 내부 HR 가상 에이전트 **AskHR**은 270,000 IBM 직원에게 HR 정책·보상·복리후생 등 전반적 질문에 답하는 AI 서비스. 초기 rule-based 챗봇에서 시작해, 2025년에 **IBM watsonx Orchestrate**를 통합하며 **agentic automation 수준**으로 진화. ⚠️ 자사 보고: 80+ HR 태스크 자동화, 연간 2.1M 대화 처리. IBM CEO Arvind Krishna가 "a couple hundred HR workers의 업무가 AI로 대체됐고 프로그래머·영업 채용이 증가"했다고 공개 발언.

## Problem / Why (도입 배경)

- IBM은 **270,000명** 규모의 글로벌 기업 — HR service center로의 문의 볼륨이 방대
- 기존 AskHR는 FAQ 수준의 단순 응답 → "진짜 업무를 수행하는" agentic 수준으로 진화 필요
- 반복적 행정 업무(expense report, recognition 작성, benefits 안내)에 HR 인력이 과도 투입

## Solution Architecture

### A. Process (프로세스)

- **Before (As-is)**: _미공개_ (IBM 내부 HR service center의 기존 운영)
- **After (To-be)** — ⚠️ 자사 보고 (HR Brew 2025-06, 2025-10):
  1. IBM 직원이 AskHR에 자연어 질문/요청 입력
  2. AskHR이 **80+ 자동화된 HR 태스크** 중 해당 작업 식별
  3. 처리 유형에 따라:
     - **정책 Q&A** → 답변 제공
     - **Compensation guidance** → 매니저에게 "salary budget을 어떻게 배분할지" 제안
     - **Recognition** → watsonx가 "meaningful recognition message" 자동 생성 + 포인트 부여
     - **Expense troubleshooting** → 자동 처리
  4. 해결 안 되면 human HR specialist에 에스컬레이션
- **Human-in-the-loop**: 대부분 자동 처리(agentic), 복잡 케이스만 사람에게 넘김
- **Trigger & Frequency**: **daily** (270k 직원, 연 2.1M 대화 = 일 ~5,700건)
- **Scope of autonomy**: **Agent-level** — Q&A뿐 아니라 "작업 수행"까지

```mermaid
flowchart LR
    Emp[IBM 직원<br/>270,000명] -->|자연어 요청| AskHR[AskHR Agent<br/>watsonx Orchestrate]
    AskHR -->|정책 Q&A| Ans[답변]
    AskHR -->|compensation guidance| Mgr[매니저에게<br/>budget 배분 제안]
    AskHR -->|recognition| Rec[watsonx가 메시지 생성<br/>+ 포인트 부여]
    AskHR -->|expense| Exp[자동 처리]
    AskHR -.->|복잡 케이스| Human[HR Specialist]
    classDef fact fill:#dcfce7
    class Emp,AskHR,Ans,Mgr,Rec,Exp fact
    classDef unknown stroke-dasharray: 5 5
    class Human unknown
```

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS**: _미공개 (not disclosed)_
- **AI 시스템 배치**: ⚠️ 자사 보고: **IBM watsonx Orchestrate** (2025년 통합) [[sources/ibm-askhr-case-study-2025]]
- **배포 환경**: _미공개 (not disclosed)_
- **사용자 접점**: _미공개 (not disclosed)_ (웹/모바일/Slack 등 채널 세부)
- **연동**: ⚠️ 자사 보고: employee letters·vacation requests·payroll access·compensation changes·organizational updates 등 매니저 워크플로 자동화 [[sources/ibm-askhr-case-study-2025]]; expense·recognition 처리 [[sources/hr-brew-ibm-moderna-2025-06]]; 시스템 연동 세부 _미공개_

### C. Data (데이터)

- **입력 데이터 소스**: IBM HR 정책·보상·복리후생 관련 직원 질문 [[sources/hr-brew-ibm-moderna-2025-06]]; 규모 _미공개 (not disclosed)_
- **데이터 규모**: ⚠️ 자사 보고: 연 2.1M+ 직원 대화, 80+ 자동화 태스크 [[sources/ibm-askhr-case-study-2025]]; 270,000명 직원 대상 [[sources/hr-brew-ibm-moderna-2025-06]]
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: ⚠️ 자사 보고: LLM이 직원 프롬프트를 분류·라우팅 [[sources/ibm-askhr-case-study-2025]] — RAG/fine-tuning 여부 _미공개_
- **데이터 거버넌스·민감정보 처리**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: ⚠️ 자사 보고: "highly compliant large language models" (watsonx Orchestrate 기반) [[sources/ibm-askhr-case-study-2025]] — 세부 버전 _미공개_
- **Model 유형**: LLM 분류·라우팅 + 자동화 에이전트 [[sources/ibm-askhr-case-study-2025]]
- **제공 방식**: IBM 자체 (watsonx) [[sources/ibm-askhr-case-study-2025]]
- **커스터마이징 기법**: ⚠️ 자사 보고: 필리핀 기반 전 HR phone agent가 conversational AI specialist로 전환해 prompt engineering 수행 [[sources/hr-brew-ibm-moderna-2025-06]]
- **평가·가드레일**: _미공개 (not disclosed)_

### E. Organization & Team (조직·팀 구조)

- **오너십**: _미공개 (not disclosed)_ — IBM HR 주도로 기술되나 IT/Digital 조직과의 분담은 소스에 없음 [[sources/ibm-askhr-case-study-2025]]
- **참여 역할**: conversational AI specialist (전환 직무) [[sources/hr-brew-ibm-moderna-2025-06]]
- **팀 규모·기간**: 6년간 지속 개선 (case study 기준) [[sources/ibm-askhr-case-study-2025]]; 인력 규모 _미공개_
- **변화관리**: ⚠️ 자사 보고: 직원 대상 watsonx challenge(3년간, 업무 개선 아이디어 피칭) [[sources/hr-brew-hr-adapting-ai-future-2025-10]]
- **파트너**: _미공개 (not disclosed)_ (자체 구축)

## Impact / Metrics (기대효과)

### 기대효과 요약
270,000명 대상, 연간 2.1M 대화, 80+ 태스크 자동화. 필리핀 HR phone agent가 AI specialist로 역할 전환 (자사 보고 기반).

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| 대상 직원 수 | **270,000명** | HR Brew 2025-06 | ⚠️ 자사 보고 |
| 연간 대화 수 | **2.1M** | IBM 공식 case study | ⚠️ 자사 보고 |
| 자동화 태스크 수 | **80+** | IBM 공식 case study | ⚠️ 자사 보고 |
| HR 인력 영향 | "couple hundred HR workers" 업무 대체 | IBM CEO Arvind Krishna (WSJ) | ⚠️ 자사 보고 |
| 직무 전환 사례 | 필리핀 phone agent → conversational AI specialist | HR Brew 2025-06 | ⚠️ 자사 보고 |
| HR 채용 변화 | 프로그래머·영업 채용 증가 (HR 인력 감소 대신) | Krishna (WSJ) | ⚠️ 자사 보고 |

**주의**: IBM은 **벤더이자 고객** (watsonx를 자사에 적용). 모든 수치가 자사 보고이며 독립 검증 없음. 그러나 **270k 규모의 self-dogfooding**이라는 점 자체가 가장 강력한 "실전 검증"이기도 함.

## Governance & Risk

- **HR 인력 대체 narrative의 정치적 위험**: Krishna의 "couple hundred workers replaced" 발언은 클라이언트 CHRO에게 **민감한 메시지** — 인용 시 반드시 "elevated" 프레이밍(역할 전환) 함께 제시
- **HITL 수준**: 80+ 태스크가 얼마나 자율인지 스펙트럼 _미공개_
- **Bias 감사**: compensation guidance agent가 성별·인종별 bias를 갖는지 감사 결과 _미공개_

## Contradictions

> [!note] 2026-09-27 grounding — B~E 섹션의 "IBM Cloud (추정)", "자체 구축 추정", "IBM HR + IBM Digital 공동 운영 추정"을 _미공개_로 정리하고 C·D·E를 분리. Consulting Angle의 Moderna GPT 수는 본 페이지 인용 소스에 없어 삭제([[moderna-ask-hr-routing]] 참조). hr-brew-ibm-moderna-2025-06은 raw 미확보(403)로 270,000명·Krishna 발언·필리핀 직무 전환은 source 페이지 요약(2차 전달)에만 근거.

## Consulting Angle

### 가장 큰 가치 — "HR AI scale의 proof point"
- **Moderna Ask HR ([[moderna-ask-hr-routing]])과의 대비**: Moderna = GPT interface (답변), IBM = **agentic (작업 수행)**. HR Brew 2025-06이 이 대비를 명시적으로 기술 [[sources/hr-brew-ibm-moderna-2025-06]].
- **HR AI maturity의 시각화**: `FAQ 챗봇 → routing GPT → agentic 자동화`라는 3단계 maturity를 IBM·Moderna 대비로 설명 가능
- **"HR 인력 대체 vs 전환" 논의의 앵커**: 필리핀 직원의 "conversational AI specialist" 전환 사례가 **생산적 논의의 출발점**
- **국내 대기업 적용 가능성**: 수만 명 규모의 국내 대기업이 IBM AskHR 수준을 목표로 할 때 필요한 전제조건(자체 AI 플랫폼, 대규모 HR 데이터, 직무 재설계 의지) 정리 가능

### 파생 질문
1. IBM의 270k → 국내 대기업(5만~30만명)에 scale하려면 한국어 NLU + 국내 HR 정책 지식베이스 구축이 선결 — 어떤 벤더가 이걸 할 수 있는가?
2. Compensation guidance agent의 한국 적용: 한국의 연봉 협상 문화·호봉제와 fit 하는가?
3. "couple hundred replaced"가 한국 노사관계에서 어떻게 인식될까?
