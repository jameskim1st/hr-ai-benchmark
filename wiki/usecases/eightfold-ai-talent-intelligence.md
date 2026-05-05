---
title: "Eightfold AI — Talent Intelligence Platform + AI Interviewer"
slug: eightfold-ai-talent-intelligence
primary_category: Talent Acquisition
subcategory: Screening & Assessment
tags: [talent-intelligence, skills-based-hiring, ai-interviewer, digital-twin, deloitte-alliance]
company: _다수 (specific names in vendor page)_
industry: [all]
region: [global]
employee_class: [all]
vendor: [Eightfold AI]
vendor_type: [talent-marketplace]
stage: production
frequency: daily
first_seen: 2025
last_confirmed: 2025
confidence: 0.20               # Tier 3 벤더 주장 위주, limited independent verification
consulting_angle_status: filled
sources:
  - "Eightfold AI 공식 https://eightfold.ai/customers/customer-stories/"
  - "PR Newswire 2025 https://www.prnewswire.com/news-releases/talent-intelligence-to-talent-advantage-eightfold-ai-revolutionizes-hr-through-agentic-ai-302449233.html"
related_usecases:
  - unilever-flex-gloat-talent-marketplace
  - midas-inair-ai-assessment-korea
related_vendors: []
---

# Eightfold AI — Talent Intelligence Platform

## Summary

Eightfold AI는 **skills-based talent intelligence** 플랫폼으로, 채용·내부 이동·스킬 관리를 AI로 통합. 2025년 **AI Interviewer** (자동 1차 면접)과 **Digital Twin** (직원의 지식·스킬·경험을 캡처하는 개인화 LLM) 발표. ⚠️ 벤더 주장: AI Interviewer로 **time to first interview 90% 감소**, 3,000명 이상 후보자를 AI로 면접 처리. **Deloitte 전략적 제휴** 확인.

## Problem / Why (도입 배경)

벤더 제품이므로 특정 기업의 도입 배경은 고객별 상이. 일반적 pain point: skills-based hiring 전환 필요성, 기존 keyword 매칭의 한계, time-to-hire 병목.

## Solution Architecture (요약)

### A. Process

- **Before**: 채용·내부이동·후계 별도 시스템, 정적 직무 기술서·resume keyword 매칭
- **After**:
  1. 회사 HRIS·ATS·LMS 데이터를 Eightfold에 연결
  2. Capabilities Matrix가 직원 skill·capability·aspiration·work pattern 모델링 (1.6B+ profile 기반)
  3. Job Intelligence Engine이 role 정의·job architecture 자동 생성·refresh
  4. 채용·internal mobility·succession·career에 unified 매칭 점수 제공
  5. Agentic AI가 sourcing·screening·interview scheduling 등 워크플로 자율 실행
  6. 결과/feedback이 self-learning engine에 반영되어 매칭 정확도 개선
- **HITL**: 리크루터·매니저가 매칭 후보 검토·결정, 단계별 checkpoint
- **Frequency**: continuous
- **Source**: Eightfold Talent Intelligence Platform product page

### AI Interviewer
- 자동 1차 면접 진행 (비동기)
- ⚠️ 벤더 주장: time to first interview 90% 감소
- Eightfold 자체가 3,000+ 후보자를 자사 채용에 사용

### Digital Twin
- 각 직원의 지식·스킬·경험을 캡처하는 **개인화 LLM**
- Teams, Slack, CRM, 프로젝트 도구, 코드 저장소 등 통합
- "Talent Intelligence → Talent Advantage" 전환의 핵심 제품

### Deloitte Alliance
- **Deloitte US**와 전략적 제휴 ([[bersin-successfactors-leapfrog-2024-10]]에서도 Eightfold 언급)
- 엔터프라이즈 talent transformation 공동 제공

## Impact / Metrics (기대효과)

### 기대효과 요약
Before: _미공개 (기존 first interview 소요 시간)_ → After: ⚠️ 벤더 주장 time to first interview 90% 감소, 3,000+ 후보자 AI 면접 처리 (자사 채용). Gartner Peer Insights 4.6/5 평점(Fact).

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| Time to first interview 감소 | **90%** | Eightfold 공식 | ⚠️ 벤더 주장 |
| AI Interviewer 처리 후보자 | **3,000+** (자사 채용) | Eightfold 공식 | ⚠️ 자사 보고 |
| 독립 검증 | Gartner Peer Insights에 리뷰 존재 (4.6/5) | Gartner | ✅ Fact |

## Consulting Angle

- **vs SAP SuccessFactors Talent Intelligence Hub**: SAP는 Eightfold을 "대체 대상"으로 지목 (Delta/Pepsi 사례, [[bersin-successfactors-leapfrog-2024-10]]). 이 경쟁 구도가 컨설팅 vendor selection에서 핵심 질문
- **Deloitte 제휴**는 대형 컨설팅 프로젝트에서 implementation partner가 확보됐다는 의미
- **Digital Twin concept**은 아직 초기 — "모든 직원의 LLM"이라는 비전은 데이터 프라이버시·거버넌스 측면에서 매우 도전적
- **한국 진출**: 현재 한국 reference _미공개_. 국내 도입 시 한국어 skills ontology·직무 체계 fit이 과제
