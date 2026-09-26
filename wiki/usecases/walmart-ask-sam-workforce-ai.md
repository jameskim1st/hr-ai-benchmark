---
title: "Walmart — Ask Sam AI 어시스턴트 + AI Interview Coach + 50k 리스킬링"
slug: walmart-ask-sam-workforce-ai
primary_category: Employee Experience & HR Ops
subcategory: Employee Self-service
tags: [ask-sam, voice-assistant, retail, workforce-management, reskilling, interview-coach]
company: Walmart
industry: [retail]
region: [na, global]
employee_class: [all]
vendor: [Walmart (internal build)]
vendor_type: [internal-build]
output: "매장 직원용 대화형 AI 어시스턴트 Ask Sam 응답 (사용자·질문 규모 미공개) + ⚠️ 자사 보고: AI Interview Coach 모의 면접 채점(최대 10개 질문·1~10점)·즉시 피드백 (파일럿) + 사무직 50,000명용 My Assistant 초안 작성·문서 요약 + 계산원 50,000+ 리스킬링 계획"
ai_tech_type: [generative, predictive, recognition]
ai_tech_subtype: [summarization-qa, clustering-classification, speech-recognition]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: []
kr_law: 일반 개인정보보호법 수준 (정책 Q&A·스케줄 조회 중심, 결정은 매니저)
kr_union: 협의 의무 낮음 (정보 제공 성격 — 음성 Q&A·스케줄 조회)
kr_language: 해당 없음 (자체 구축)
kr_vendor: 자체 구축 (Walmart internal, 국내 SI 해당 없음)
first_seen_estimated: true
frequency: daily
first_seen: 2025-06-24
last_confirmed: 2025-10-02
confidence: 0.7
evidence_grade: A
corroborated_by: 3
freshness: fresh
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/hr-brew-accenture-walmart-workforce-ai-2025-10.md, sources/walmart-corporate-ai-interview-coach-2025-06.md, sources/hrexecutive-amazon-walmart-workforce-ai-2026-02.md, sources/jobspikr-walmart-reskilling-2025.md, sources/shrm-walmart-ai-revolution-2025.md, sources/hrdive-walmart-my-assistant-genai-2024.md]
related_usecases:
  - ibm-askhr-watsonx
  - moderna-ask-hr-routing
  - amazon-hr-ai-restructuring
related_vendors: []
---

# Walmart — Ask Sam + AI Interview Coach + Workforce Reskilling

> ★ **리테일 HR AI 대규모 사례**: Ask Sam 사용자·주간 질문 수, 직원·매장 수는 인용 소스 원문 미확인([[hrexecutive-amazon-walmart-workforce-ai-2026-02]]·[[hr-brew-accenture-walmart-workforce-ai-2025-10]] 스냅샷 unavailable) — _미공개_ (2026-09-27 grounding 점검). **SHRM**(Tier 2)이 "Walmart's AI Revolution: People-Led, Tech-Powered" 독립 기사로 전략을 분석 ([[shrm-walmart-ai-revolution-2025]]). **HR Dive**(Tier 2)가 My Assistant GenAI 도구(직원 50,000명 대상) 보도 ([[hrdive-walmart-my-assistant-genai-2024]]).

## Summary

Walmart(직원·매장 규모는 본 페이지 인용 소스 미확인 — _미공개_)은 복수의 HR AI 이니셔티브를 병행 운영:

1. **Ask Sam** — 매장 직원용 대화형 AI 어시스턴트. 사용자 수·주간 질문 수는 _미공개_ (인용 소스 원문 미확보 — 2026-09-27 grounding 점검).
2. **AI Interview Coach** — 2025-06 파일럿 공개. 최대 10개 질문 모의 면접, 1~10점 채점, 구조·명료성·자신감 즉시 피드백 ([[sources/walmart-corporate-ai-interview-coach-2025-06]] — ⚠️ 자사 보고).
3. **50,000+ 리스킬링** — 계산원 → 드론 기술자·로봇 수퍼바이저 역할 전환 계획 ([[sources/jobspikr-walmart-reskilling-2025]] — 1차 출처 미표기).
4. **My Assistant** — 사무직 50,000명 대상 GenAI 도구 (초안 작성·문서 요약; CPO Donna Morris 발표) ([[sources/hrdive-walmart-my-assistant-genai-2024]]).

전략적 프레이밍: **"People-led, tech-powered"** — AI를 "사람을 대체"가 아니라 "사람을 강화"로 포지셔닝 ([[sources/shrm-walmart-ai-revolution-2025]]).

## Problem / Why (도입 배경)

- **Before (baseline)**: ❓ baseline 미공개 — Ask Sam 도입 전 매장 직원의 정보 조회·HR 문의 처리 방식은 인용 소스에 없음
- **Pain point**: ⚠️ 자사 보고: 급여직 매장·클럽·공급망 관리자 75%가 시간제 직원 출신 — 내부 승진·경력 경로 지원이 과제 ([[sources/walmart-corporate-ai-interview-coach-2025-06]]); 반복 업무에서 직원을 해방시켜 고객 경험에 집중 ([[sources/hrdive-walmart-my-assistant-genai-2024]])
- **Trigger**: ❓ 미공개 — "people-led, tech-powered" 전략 프레이밍만 확인 ([[sources/shrm-walmart-ai-revolution-2025]])

## Solution Architecture

### A. Process — Ask Sam

> ⚠️ 아래 단계 상세(Telxon·WFM 연동·GenAI 업그레이드 등)는 인용 소스에서 확인되지 않음 — 외부 인용 금지 (2026-09-27 grounding 점검).

- **Before**: 매장 associate가 가격·재고·통로 위치·근무 schedule을 종이 매뉴얼·Telxon 단말기·매니저 호출로 확인. 신규 정책·프로모션은 매장별 매니저가 구두 전달
- **After**:
  1. associate가 회사 지급 모바일 단말로 Ask Sam 앱을 음성 호출 ("What aisle is hand soap?")
  2. 음성→텍스트 변환 후 Walmart 내부 KB(상품·매장·정책·schedule)에서 답변 검색
  3. 결과를 음성·텍스트로 반환, 위치는 매장 지도 overlay
  4. 본인 schedule 조회·교대 요청은 WFM 시스템 연동, 정책 Q&A는 GenAI 기반 step-by-step 가이드 (2025-Q3 업그레이드)
  5. 모든 query는 store-level operational signal로 수집되어 매장·본사가 friction point 분석
- **HITL**: schedule 변경 승인은 매니저, 정책 답변 부정확 시 associate가 매니저 escalation
- **Frequency**: daily; 사용 규모 _미공개_ (수치 근거 미확보 — 2026-09-27 grounding 점검)

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS / 기반 시스템**: _미공개 (not disclosed)_ (기존 Workday HCM·절감액·채용 기간 서술은 인용 소스에 없어 삭제 — 2026-09-27 grounding 점검)
- **AI 시스템 배치**: Ask Sam — 자체/벤더 여부 _미공개_; ✅ AI Interview Coach 파일럿 (2025-06) ([[sources/walmart-corporate-ai-interview-coach-2025-06]]); ✅ My Assistant GenAI (데스크톱·모바일) ([[sources/hrdive-walmart-my-assistant-genai-2024]])
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: _미공개 (not disclosed)_
- **사용자 접점 (UX layer)**: ✅ My Assistant — 데스크톱·모바일 인터페이스 ([[sources/hrdive-walmart-my-assistant-genai-2024]]); Ask Sam 접점 _미공개_
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: ✅ My Assistant — 초안 작성·대규모 문서 요약 대상 문서 ([[sources/hrdive-walmart-my-assistant-genai-2024]]); Ask Sam 입력 데이터 _미공개_
- **데이터 규모**: ✅ My Assistant 사용자 50,000명 (2023-08 발표, 이후 확대) ([[sources/hrdive-walmart-my-assistant-genai-2024]]); Ask Sam 규모 _미공개_
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context 구분**: _미공개 (not disclosed)_
- **데이터 거버넌스**: _미공개 (not disclosed)_
- **민감정보 처리**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **Model 유형**: ✅ GenAI (My Assistant — 초안·요약) ([[sources/hrdive-walmart-my-assistant-genai-2024]]); ✅ AI Interview Coach — 모의 면접 채점·피드백 ([[sources/walmart-corporate-ai-interview-coach-2025-06]]); Ask Sam 모델 유형 _미공개_
- **제공 방식**: _미공개 (not disclosed)_
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: _미공개 (not disclosed)_

### E. Organization & Team (조직·팀 구조)

- **오너십**: ✅ CPO Donna Morris (My Assistant 발표) ([[sources/hrdive-walmart-my-assistant-genai-2024]]); Maren Waggoner (SVP & CPO, Global Tech and Corporate Functions) 인터뷰 ([[sources/shrm-walmart-ai-revolution-2025]])
- **참여 역할·팀 규모·거버넌스**: _미공개 (not disclosed)_
- **변화관리**: ✅ Walmart Academy 기반 skills-first 경력 경로, A2T(Associate to Technician) 프로그램 2030년까지 기술자 4,000명 양성 ([[sources/walmart-corporate-ai-interview-coach-2025-06]] — ⚠️ 자사 보고)
- **파트너**: _미공개 (not disclosed)_

## Impact / Metrics (기대효과)

### 기대효과 요약
Before: _미공개_ → After: Ask Sam 사용 규모·Workday 효과·직원/매장 수·노동 비용 절감 수치는 인용 소스에 없어 _미공개_ (2026-09-27 grounding 점검). 확인되는 것: 리스킬링 50,000+ 대상 (⚠️ 1차 출처 미표기), AI Interview Coach 파일럿 (⚠️ 자사 보고), My Assistant 50,000명 (✅ Tier 2), A2T 기술자 4,000명 양성 목표 (⚠️ 자사 보고).

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| Ask Sam 사용자 | _미공개_ | 인용 소스 원문 미확보 ([[sources/hrexecutive-amazon-walmart-workforce-ai-2026-02]] unavailable) | ❓ |
| 주간 질문 수 | _미공개_ | 인용 소스 원문 미확보 | ❓ |
| Workday 연간 절약 | _미공개_ | 인용 소스에 없음 (2026-09-27 grounding 점검) | ❓ |
| 채용 기간 단축 | _미공개_ | 인용 소스에 없음 (2026-09-27 grounding 점검) | ❓ |
| 리스킬링 대상 | **50,000+** (계산원→기술직) | [[sources/jobspikr-walmart-reskilling-2025]] | ⚠️ 자사 보고 (1차 출처 미표기 블로그 전달) |
| AI Interview Coach | 파일럿 (2025-06), 최대 10개 질문·1~10점 채점 | [[sources/walmart-corporate-ai-interview-coach-2025-06]] | ⚠️ 자사 보고 |
| My Assistant 사용자 | **50,000명** (사무직) | [[sources/hrdive-walmart-my-assistant-genai-2024]] | ✅ Fact (Tier 2 전달) |
| A2T 기술자 양성 | **4,000명** (2030년까지) | [[sources/walmart-corporate-ai-interview-coach-2025-06]] | ⚠️ 자사 보고 |
| 급여직 관리자 중 시간제 출신 | **75%** | [[sources/walmart-corporate-ai-interview-coach-2025-06]] | ⚠️ 자사 보고 |
| 전체 직원 규모 | _미공개_ | 본 페이지 인용 소스에 없음 | ❓ |
| 인력 효율성 | _미공개_ | 인용 소스에 없음 (2026-09-27 grounding 점검) | ❓ |

## Governance & Risk

- **HITL**: AI Interview Coach는 연습 도구 — 실제 면접·승진 결정은 사람 ([[sources/walmart-corporate-ai-interview-coach-2025-06]]); Ask Sam 답변 escalation 절차 _미공개_
- **편향·개인정보**: _미공개 (not disclosed)_
- **인력 전략**: "people-led, tech-powered" — AI를 대체가 아닌 강화로 포지셔닝 ([[sources/shrm-walmart-ai-revolution-2025]]); 리스킬링 계획의 1차 출처 미표기 ([[sources/jobspikr-walmart-reskilling-2025]])

## Contradictions

> [!note] 2026-09-27 grounding — Ask Sam 사용자 수·주간 질문 수, 전체 직원·매장 수, Workday 절감액·채용 기간 단축, 노동 비용 절감률은 인용 소스 6건 중 어디에도 없음([[sources/hrexecutive-amazon-walmart-workforce-ai-2026-02]]·[[sources/hr-brew-accenture-walmart-workforce-ai-2025-10]]는 스냅샷 unavailable, SHRM·Interview Coach 소스는 Ask Sam 수치 미포함). 모두 `_미공개_`로 교체. A. Process 상세는 출처 미인용.

## Consulting Angle

### 핵심 가치
- **Scale의 증명**: Ask Sam 사용 규모 수치는 현재 인용 소스로 뒷받침되지 않음 — 외부 인용 전 1차 출처 확보 필요
- **"People-led, tech-powered"** 프레이밍: AI 도입 시 **직원 저항을 줄이는 narrative 전략**의 모범
- **리��킬링 + AI의 결합**: "AI가 일자리를 없앤다" ���신 "AI가 역할을 전환한다" (50k 캐셔→기술직)

### vs IBM AskHR vs Moderna Ask HR

| | Walmart Ask Sam | IBM AskHR | Moderna Ask HR |
|---|---|---|---|
| 규모 | _미공개_ (본 페이지 소스 미확인) | (IBM 페이지 참조) | (Moderna 페이지 참조) |
| 주요 용도 | 매장 운영 + HR | HR 전문 | HR 전문 |
| 인터페이스 | **음성** | 텍스트 | 텍스트 (ChatGPT) |
| 자동화 수준 | 답변 중심 | **Agentic** (작업 수행) | Routing (분기) |
| 산업 | **리테일** | IT 서비스 | 바이오텍 |
