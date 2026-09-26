---
title: "그리팅 — 국내 1위 AI ATS"
slug: greetinghr-ats-ai-korea
primary_category: Talent Acquisition
subcategory: Screening & Assessment
tags: [ats, recruitment, korea, sme, saas]
company: 그리팅 (Greeting HR)
industry: [tech]
region: [kr]
employee_class: [all]
vendor: [그리팅 (GreetingHR)]
vendor_type: [ats, point-solution]
output: "채용 홈페이지 제작 + 지원자 통합 관리·협업 평가 + 면접 일정 조율 + 채용 데이터 분석 대시보드 (한국 중소기업 ATS; ⚠️ 자사 보고: 채용 소요시간 약 65% 단축·비용 약 50% 절감). AI 후보자 매칭·인재풀 기능은 인용 소스 미확인"
ai_tech_type: [predictive, automation]
ai_tech_subtype: [recommendation-ranking, clustering-classification]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: [kr-high-impact, eu-annex-iii]
kr_law: AI 기본법 고영향 AI (채용 스크리닝) + 공정채용·개인정보보호법 (페이지)
kr_union: 단체교섭/근로자대표 협의 필요 (인사 의사결정 영향)
kr_language: 한국어 네이티브
kr_vendor: 그리팅 (Greeting HR) 자체 SaaS — 고용노동부 지원사업 공급기업
frequency: daily
first_seen: 2025-01-01
last_confirmed: 2025-09-01
confidence: 0.35
evidence_grade: B
corroborated_by: 1
freshness: stale
depth: stub
graded_at: 2026-09-27
sources:
  - sources/greetinghr-ats-guide-2025.md
  - sources/ezyeconomy-greetinghr-2025.md
related_usecases:
  - wantedlab-ai-recruiting-agent
  - chipotle-paradox-olivia
related_vendors: []
---

## Summary

그리팅(GreetingHR, 운영사 두들린)은 "국내 1위 채용관리 솔루션(ATS)"으로, 2025년 고용노동부 "채용관리 솔루션(ATS) 지원사업" 공급기업 2개사 중 하나로 선정됐다 [[sources/greetinghr-ats-guide-2025]] [[sources/ezyeconomy-greetinghr-2025]]. ⚠️ **자사 보고**: 그리팅 도입 시 채용 소요시간 약 65% 단축·채용 비용 약 50% 절감, 현대오토에버·KB증권·삼양식품 등 7,000곳 이상 기업 사용 [[sources/greetinghr-ats-guide-2025]] [[sources/ezyeconomy-greetinghr-2025]]. 기존 페이지의 "중소기업 도입률 전년 대비 158% 급증"과 "AI 인재풀 구축·후보자 매칭" 서술은 인용 소스 2건의 raw 어디에도 없어 _미공개 (not disclosed)_ 처리 (2026-09-27 grounding 점검) — 인용 소스는 AI 기능을 언급하지 않으며, ATS 기능은 채용 홈페이지 제작·지원자 통합 관리·협업 평가·면접 일정 조율·채용 데이터 분석 대시보드로 기술된다 [[sources/greetinghr-ats-guide-2025]].

## Problem / Why (도입 배경)

- **Before (baseline)**: 많은 중소기업이 수기로 지원자를 관리하며 면접 일정 조율·채용 결과 안내에 상당한 시간을 소비 (이태규 대표 인용) [[sources/greetinghr-ats-guide-2025]]; 정량 baseline ❓ 미공개
- **Pain point**: 채용 절차법을 충분히 숙지하지 못해 법 준수 과정에서 어려움 [[sources/greetinghr-ats-guide-2025]]; 중소기업의 인력난 해소·체계적 채용 프로세스 구축 [[sources/ezyeconomy-greetinghr-2025]]
- **Trigger**: 고용노동부 지원사업 — 유료 사용 이력 없는 중소기업에 연간 이용료의 80%(최대 40만원) 지원, 최대 4,000곳 대상 [[sources/greetinghr-ats-guide-2025]] [[sources/ezyeconomy-greetinghr-2025]]
- 🚫 일반론 표기: 벤더 제품이므로 특정 기업의 도입 배경은 고객별 상이

## Solution Architecture

> **최우선 원칙**: 이 섹션은 **공개된 사실만** 기록한다.

### A. Process (프로세스)

- **Before (As-is)**: 수기 지원자 관리, 면접 일정 조율·결과 안내에 수작업 시간 소요 [[sources/greetinghr-ats-guide-2025]]
- **After (To-be)**:
  1. ✅ **Fact** 채용 홈페이지 제작, 지원자 통합 관리, 지원자 협업 평가, 간편 면접 일정 조율, 채용 데이터 분석 대시보드를 단일 플랫폼에서 제공 [[sources/greetinghr-ats-guide-2025]] [[sources/ezyeconomy-greetinghr-2025]]
  2. ✅ **Fact** 국내 채용 절차법에 맞춰 서비스를 지속 업데이트·관리 [[sources/greetinghr-ats-guide-2025]]
  3. AI 기반 인재풀·후보자 매칭: _미공개 (not disclosed)_ — 인용 소스에 AI 기능 언급 없음
- **Human-in-the-loop**: _미공개 (not disclosed)_ — 협업 평가 기능상 평가자는 사람이나 소스가 HITL을 명시하지 않음
- **Trigger & Frequency**: 채용 시마다 수시(on-demand) [[sources/greetinghr-ats-guide-2025]]
- **Scope of autonomy**: _미공개 (not disclosed)_

### B. System & Infrastructure (시스템·인프라)

- **배포 환경**: _미공개 (not disclosed)_ — 기존 "클라우드 서비스 보급·확산 사업 선정" 서술은 인용 소스에 없음
- **연동·통합**: _미공개 (not disclosed)_
- **사용자 접점**: 채용 홈페이지(지원자)·관리 화면(기업) [[sources/greetinghr-ats-guide-2025]]; 채널 세부 _미공개_

### C. Data (데이터)

- **입력 데이터 소스**: 지원자 정보·평가 데이터·채용 데이터(분석 대시보드) [[sources/greetinghr-ats-guide-2025]]
- **데이터 규모**: 7,000곳 이상 기업 사용 [[sources/greetinghr-ats-guide-2025]] [[sources/ezyeconomy-greetinghr-2025]]; 지원자 수 _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **AI 기능**: _미공개 (not disclosed)_ — 인용 소스는 AI 매칭·스크리닝을 언급하지 않음 (2026-09-27 grounding 점검)

### E. Organization & Team (조직·팀 구조)

- **오너십**: 두들린(대표 이태규) [[sources/greetinghr-ats-guide-2025]]; 고객사 측 조직 _미공개 (not disclosed)_
- **파트너**: 고용노동부(지원사업), 한국능률협회(신청 접수) [[sources/greetinghr-ats-guide-2025]]

## Impact / Metrics (기대효과)

### 기대효과 요약
Before: _미공개 (기존 채용 소요 시간·비용)_ → After: ⚠️ 자사 보고 채용 소요시간 약 65% 단축, 채용 비용 약 50% 절감 (독립 검증 없음 — 언론 기사는 보도자료 전재) [[sources/greetinghr-ats-guide-2025]] [[sources/ezyeconomy-greetinghr-2025]].

- ⚠️ **자사 보고**: 채용 소요시간 약 65% 단축 [[sources/greetinghr-ats-guide-2025]] [[sources/ezyeconomy-greetinghr-2025]] — Tier 1·2 독립 검증 미확인 (ezyeconomy 기사는 보도자료 전재)
- ⚠️ **자사 보고**: 채용 비용 약 50% 절감 [[sources/greetinghr-ats-guide-2025]] [[sources/ezyeconomy-greetinghr-2025]]
- ⚠️ **자사 보고**: 7,000곳 이상 기업 사용 [[sources/greetinghr-ats-guide-2025]] [[sources/ezyeconomy-greetinghr-2025]]
- ✅ **Fact**: 고용노동부 "2025 채용관리 솔루션 지원사업" 공급기업 선정 (2개사 중 1) [[sources/greetinghr-ats-guide-2025]] [[sources/ezyeconomy-greetinghr-2025]]
- 중소기업 도입률 증가율: _미공개_ (기존 "158% 급증" 수치는 인용 소스 어디에도 없음)

## Governance & Risk

- 채용 절차법 준수를 위한 지속 업데이트 주장 [[sources/greetinghr-ats-guide-2025]] — 구체 편향 감사·AI 거버넌스 체계 _미공개 (not disclosed)_ (AI 기능 자체가 인용 소스에서 미확인)
- 개인정보보호법 적용 환경. 세부 DPIA 미공개.
- 규제 노출: AI 스크리닝이 실제 제공된다면 AI 기본법 고영향 AI(채용) 대상 — 현재 소스로는 AI 관여 여부 불명

## Contradictions

> [!note] 2026-09-27 grounding — "중소기업 도입률 전년 대비 158% 급증", "AI 인재풀 구축·후보자 매칭(키워드 스크리닝을 넘어선 정교한 매칭)", "클라우드 서비스 보급·확산 사업 공급기업 선정"은 인용 소스 2건(두들린 보도자료·ezyeconomy 전재 기사)의 raw에 없어 _미공개_ 처리. 두 소스는 동일 보도자료 기반이라 독립 교차 검증이 아님. 그리팅의 AI 기능 근거 소스 확보는 /hr-research 대상 — 확보 전까지 이 페이지의 AI 관여는 미확인.

## Consulting Angle

- **국내 ATS 시장 대표 벤더**: 그리팅은 한국 중소·중견기업 ATS 시장에서 가장 높은 인지도를 가진 솔루션. 국내 중소기업 HR AI 도입 제안 시 적합한 솔루션.
- **정부 지원사업 연계**: 고용노동부 채용관리 솔루션 지원사업과 클라우드 보급·확산 사업에 동시 선정되어 보조금 활용 가능성 높음 — 중소기업 클라이언트 비용 절감 방안으로 제시 가능.
- **한계**: AI 기능은 인용 소스에서 확인되지 않으며 성과 수치는 벤더 보도자료 수준. Tier 1·2 독립 검증 없음 — AI 기능·독립 검증 소스 추가 확보 필요.
- **원티드랩과 비교**: 원티드랩은 대기업/전문직 수시 채용, 그리팅은 중소기업 ATS — 타겟 세그먼트 차별화 명확. (→ [[wantedlab-ai-recruiting-agent]] 연계)
