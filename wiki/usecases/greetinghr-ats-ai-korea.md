---
title: "그리팅 — 국내 1위 AI ATS (채용 소요시간 65% 단축, 중소기업 도입률 158%↑)"
slug: greetinghr-ats-ai-korea
primary_category: Talent Acquisition
subcategory: Screening & Assessment
tags: [ats, ai-screening, recruitment, korea, sme, saas, candidate-matching]
company: 그리팅 (Greeting HR)
industry: [tech]
region: [kr]
employee_class: [all]
vendor: []
vendor_type: [ats, point-solution]
ai_tech_type: [predictive, automation]
ai_tech_subtype: [recommendation-ranking, clustering-classification]
stage: production
frequency: daily
first_seen: 2025-01-01
last_confirmed: 2025-09-01
confidence: 0.30
sources:
  - sources/greetinghr-ats-guide-2025.md
  - sources/ezyeconomy-greetinghr-2025.md
related_usecases:
  - wantedlab-ai-recruiting-agent
  - chipotle-paradox-olivia
related_vendors: []
---

## Summary

그리팅(GreetingHR)은 국내 1위 채용 관리 솔루션(ATS/TRM)으로, 2025년 고용노동부 "채용관리 솔루션 지원사업" 공급기업으로 선정되어 중소기업 도입률이 전년 대비 158% 급증했다. ⚠️ **자사 보고**: 그리팅 도입 시 채용 소요시간 약 65% 단축, 채용 비용 약 50% 절감을 주장한다. AI를 활용한 정교한 인재풀 구축과 기업 맞춤형 후보자 매칭이 핵심 차별점이다. [[sources/greetinghr-ats-guide-2025.md]] [[sources/ezyeconomy-greetinghr-2025.md]]

## Problem / Why

수시 채용·잦은 이직이 일반화된 한국 노동시장에서 HR 담당자들은 지원자 통합 관리, 면접 일정 조율, 채용 데이터 분석을 수동으로 처리하는 데 과도한 시간을 소비하고 있었다. 특히 중소기업은 전문 HR 인력이 부족하여 채용 효율화 도구에 대한 수요가 높다.

## Solution Architecture

> **최우선 원칙**: 이 섹션은 **공개된 사실만** 기록한다.

### A. Process (프로세스)

- **Before (As-is)**: HR 담당자가 수동으로 이력서 검토, 이메일·전화로 면접 일정 조율, 엑셀로 지원자 관리.
- **After (To-be)**:
  1. ✅ **Fact** 채용 홈페이지 제작, 지원자 통합 관리, 협업 평가, 면접 일정 조율, 채용 데이터 분석 대시보드를 단일 플랫폼에서 제공. [[sources/greetinghr-ats-guide-2025.md]]
  2. ✅ **Fact** AI를 활용한 인재풀 구축·후보자 매칭(키워드 스크리닝을 넘어선 정교한 매칭). [[sources/greetinghr-ats-guide-2025.md]]
  3. ✅ **Fact** 공정 채용·법규 준수 기능(2025 고용노동부 공정 채용 지침 방향 반영). [[sources/greetinghr-ats-guide-2025.md]]
- **Human-in-the-loop**: 최종 채용 결정은 HR 담당자·면접관이 수행.
- **Trigger & Frequency**: 채용 시마다 수시(on-demand).
- **Scope of autonomy**: 스크리닝·일정 조율 자동화(autonomous); 최종 선발 recommend.

### B. System & Infrastructure (시스템·인프라)

- **배포 환경**: ✅ **Fact** 클라우드 SaaS (2025 중소기업 클라우드 서비스 보급·확산 사업 공급기업 선정). [[sources/ezyeconomy-greetinghr-2025.md]]
- **연동·통합**: _미공개 (not disclosed)_
- **사용자 접점**: 웹 포털. _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: 이력서, JD, 지원자 정보, 채용 공고 데이터.
- **데이터 규모**: _미공개 (not disclosed)_ — 국내 중소기업 다수 도입.
- **학습 vs RAG vs In-context**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **AI 기능**: ✅ **Fact** AI 기반 후보자 매칭(키워드 스크리닝 → 정교한 매칭으로 진화). [[sources/greetinghr-ats-guide-2025.md]]

### E. Organization & Team (조직·팀 구조)

- _미공개 (not disclosed)_

## Impact / Metrics (기대효과)

### 기대효과 요약
Before: _미공개 (기존 채용 소요 시간·비용)_ → After: ⚠️ 벤더 주장 채용 소요시간 65% 단축, 채용 비용 50% 절감 (독립 검증 미확인). 중소기업 도입률 전년 동기 대비 158% 증가(Fact).

- ✅ **Fact**: 2025년 상반기 중소기업 도입률 전년 동기 대비 158% 증가. [[sources/ezyeconomy-greetinghr-2025.md]]
- ✅ **Fact**: 고용노동부 "2025 채용관리 솔루션 지원사업" 공급기업 선정. [[sources/ezyeconomy-greetinghr-2025.md]]
- ⚠️ **벤더 주장**: 채용 소요시간 약 65% 단축. [[sources/greetinghr-ats-guide-2025.md]] — Tier 1·2 독립 검증 미확인.
- ⚠️ **벤더 주장**: 채용 비용 약 50% 절감. [[sources/greetinghr-ats-guide-2025.md]] — Tier 1·2 독립 검증 미확인.

## Governance & Risk

- 공정 채용법 준수 기능 내장 주장. 구체 편향 감사 체계 _미공개 (not disclosed)_.
- 개인정보보호법 적용 환경. 세부 DPIA 미공개.

## Contradictions

없음 (현재 기준).

## Consulting Angle

- **국내 ATS 시장 대표 벤더**: 그리팅은 한국 중소·중견기업 ATS 시장에서 가장 높은 인지도를 가진 솔루션. 국내 중소기업 HR AI 도입 제안 시 적합한 솔루션.
- **정부 지원사업 연계**: 고용노동부 채용관리 솔루션 지원사업과 클라우드 보급·확산 사업에 동시 선정되어 보조금 활용 가능성 높음 — 중소기업 클라이언트 비용 절감 방안으로 제시 가능.
- **한계**: 구체 AI 기능 설명과 성과 수치가 벤더 마케팅 주장 수준. Tier 1·2 독립 검증 없음. Confidence가 낮음(0.30) — 추가 독립 검증 소스 필요.
- **원티드랩과 비교**: 원티드랩은 대기업/전문직 수시 채용, 그리팅은 중소기업 ATS — 타겟 세그먼트 차별화 명확. (→ [[wantedlab-ai-recruiting-agent]] 연계)
