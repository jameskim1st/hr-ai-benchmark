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
output: "매장 associate 음성 query에 대한 음성·텍스트 답변 (가격·재고·통로·정책) + 매장 지도 overlay + WFM 시스템 연동 schedule 조회·교대 요청 액션 + GenAI 정책 step-by-step 가이드. 90만 associate, 주 300만+ query"
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

> ★ **리테일 HR AI 최대 규모**: 2.3M 직원, 10,500 매장, **Ask Sam 900k 사용자가 주 3M+ 질문**. IBM AskHR(270k)을 규모에서 3배 이상 초과하는 **세계 최대 HR AI 배포 사례**. **SHRM**(Tier 2)이 "Walmart's AI Revolution: People-Led, Tech-Powered" 독립 기사로 분석 ([[shrm-walmart-ai-revolution-2025]]). **HR Dive**(Tier 2)도 My Assistant GenAI 도구 보도 ([[hrdive-walmart-my-assistant-genai-2024]]).

## Summary

Walmart(2.3M 직원, 10,500 매장)은 세 가지 HR AI 이니셔티브를 병행 운영:

1. **Ask Sam** — 매장 직원용 대화형 음성 AI 어시스턴트. **900,000명 직원**이 사용하며 **주 3,000,000+ 질문** 처리. HR 정책·재고·가격·작업 절차 등 답변.
2. **AI Interview Coach** — 2025-06 파일럿 공개. 직원의 **승진 면접 준비**를 AI가 코칭.
3. **50,000명 리스킬링** — 캐셔·매장 직원 → 드론 기술자·로봇 수퍼바이저로 역할 전환 계획.

전략적 프레이밍: **"People-led, tech-powered"** — AI를 "사람을 대체"가 아니라 "사람을 강화"로 포지셔닝.

## Solution Architecture

### A. Process — Ask Sam

- **Before**: 매장 associate가 가격·재고·통로 위치·근무 schedule을 종이 매뉴얼·Telxon 단말기·매니저 호출로 확인. 신규 정책·프로모션은 매장별 매니저가 구두 전달
- **After**:
  1. associate가 회사 지급 모바일 단말로 Ask Sam 앱을 음성 호출 ("What aisle is hand soap?")
  2. 음성→텍스트 변환 후 Walmart 내부 KB(상품·매장·정책·schedule)에서 답변 검색
  3. 결과를 음성·텍스트로 반환, 위치는 매장 지도 overlay
  4. 본인 schedule 조회·교대 요청은 WFM 시스템 연동, 정책 Q&A는 GenAI 기반 step-by-step 가이드 (2025-Q3 업그레이드)
  5. 모든 query는 store-level operational signal로 수집되어 매장·본사가 friction point 분석
- **HITL**: schedule 변경 승인은 매니저, 정책 답변 부정확 시 associate가 매니저 escalation
- **Frequency**: daily — ⚠️ 자사 보고 주 300만+ query, 90만 associate (Walmart corporate 2025-06-24)

### B. System

- **Core HRIS**: Workday HCM (2017년부터 2.3M 직원 전체 운영)
- ⚠️ 자사 보고: Workday 도입으로 **$35M/년 절약**, 채용 기간 **60일→18일 (70% 단축)**
- Ask Sam: Walmart 자체 구축 음성 AI (별도 벤더 미공개)
- AI Interview Coach: 파일럿 단계 (2025-06)

### C~E. 세부
- **데이터**: 매장 운영·HR 정책·재고 데이터 통합
- **모델**: _미공개_ (자체 구축 추정)
- **조직**: 리더십이 "people-led, tech-powered"를 core principle로 설정

## Impact / Metrics (기대효과)

### 기대효과 요약
Before: _미공개 (Ask Sam 도입 전 HR 문의 처리 방식·소요 시간)_ → After: ⚠️ 자사 보고 900,000명 사용, 주 3,000,000+ 질문 처리. ⚠️ 벤더 주장 Workday 도입 연간 $35M 절감, 채용 기간 60일→18일(70% 단축). 리스킬링 50,000명 대상(⚠️ 자사 보고). 2,300,000 직원, 10,500 매장 규모(Fact).

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| Ask Sam 사용자 | **900,000명** | HR Executive | ⚠️ 자사 보고 |
| 주간 질문 수 | **3,000,000+** | HR Executive | ⚠️ 자사 보고 |
| Workday 연간 절약 | **$35M** | Tipsoi/Workday | ⚠️ 벤더 주장 |
| 채용 기간 단축 | **60일→18일 (70%)** | Tipsoi/Workday | ⚠️ 벤더 주장 |
| 리스킬링 대상 | **50,000명** (캐셔→기술직) | JobsPikr | ⚠️ 자사 보고 |
| AI Interview Coach | 파일럿 (2025-06) | Walmart Corporate | ✅ Fact |
| 전체 직원 규모 | **2,300,000명**, 10,500 매장 | 공개 정보 | ✅ Fact |
| 인력 효율성 | 노동 비용 **15% 절감** | PredictHQ | ⚠️ 업계 분석 |

## Consulting Angle

### 핵심 가치
- **Scale의 증명**: Ask Sam 900k 사용자 × 주 3M 질문 = **HR AI가 "프로토타입이 아닌 operation"**임을 보여줌
- **"People-led, tech-powered"** 프레이밍: AI 도입 시 **직원 저항을 줄이는 narrative 전략**의 모범
- **리��킬링 + AI의 결합**: "AI가 일자리를 없앤다" ���신 "AI가 역할을 전환한다" (50k 캐셔→기술직)

### vs IBM AskHR vs Moderna Ask HR

| | Walmart Ask Sam | IBM AskHR | Moderna Ask HR |
|---|---|---|---|
| 규모 | **900,000명** | 270,000명 | 5,000명 |
| 주요 용도 | 매장 운영 + HR | HR 전문 | HR 전문 |
| 인터페이스 | **음성** | 텍스트 | 텍스트 (ChatGPT) |
| 자동화 수준 | 답변 중심 | **Agentic** (작업 수행) | Routing (분기) |
| 산업 | **리테일** | IT 서비스 | 바이오텍 |
