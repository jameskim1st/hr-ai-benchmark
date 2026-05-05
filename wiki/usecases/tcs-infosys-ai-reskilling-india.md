---
title: "TCS·Infosys·Wipro — 인도 IT 서비스 대기업 AI 리스킬링"
slug: tcs-infosys-ai-reskilling-india
primary_category: Learning & Development
subcategory: Skills & Capabilities
tags: [reskilling, upskilling, ai-training, india, it-services, large-scale, genai-academy, generative-ai]
company: TCS
industry: [tech, consulting]
region: [apac]
employee_class: [all]
vendor: [Microsoft]
vendor_type: [foundation-model, internal-build]
output: "직원 AI 역량 인증·proficiency tag (NVIDIA AI Enterprise·Azure OpenAI 커리큘럼 수료) + 인증된 인력 풀의 클라이언트 RFP staffing 매칭"
ai_tech_type: [generative]
ai_tech_subtype: [summarization-qa]
stage: production
frequency: adhoc
first_seen: 2024-01-01
last_confirmed: 2025-12-01
confidence: 0.45
sources:
  - sources/theregister-india-it-2026-01.md
  - sources/aibase-india-it-ai-reskilling-2025.md
  - sources/poniaktimes-india-it-ai-2025.md
related_usecases:
  - walmart-ai-frontline-workforce
related_vendors:
  - microsoft
---

## Summary

인도 3대 IT 서비스 기업 TCS·Infosys·Wipro는 AI 시대 전환에 맞춰 수십만에서 100만 명 이상 규모의 AI 리스킬링을 추진 중이다. ✅ **Fact** TCS는 275,000명이 "Ideate and Build with AI" 이니셔티브에 참여했고, Infosys는 AI 전환 프로그램에서 275,000명을 교육했으며, Wipro는 단 1분기 만에 180,000명에게 GenAI 기초 교육을 완료했다. 3사 합산 FY26 Q1 기준 AI 교육 인원은 약 100만 명에 달한다. [[sources/aibase-india-it-ai-reskilling-2025.md]]

## Problem / Why (도입 배경)

AI가 기존 IT 서비스(코딩·QA·BPO)의 핵심 업무를 자동화하면서, 인도 IT 서비스 대기업들은 인력 구성 재편이라는 구조적 압박에 직면했다. TCS는 12,000명 감원과 동시에 40,000명 신규 채용을 진행하는 역설적 상황이며, Infosys는 역으로 20,000명 신입을 채용하며 AI 역량 기반 전환을 추진하고 있다.

## Solution Architecture

> **최우선 원칙**: 이 섹션은 **공개된 사실만** 기록한다.

### A. Process (프로세스)

- **Before**: TCS·Infosys·Wipro·Tech Mahindra 합산 200만+ IT 인력이 manual testing·infra 운영·기본 코딩 중심. AI 역량은 small subset에 한정, 클라이언트의 GenAI 프로젝트 수요 대응 곤란
- **After**:
  1. NVIDIA와 4사 파트너십 체결 → NVIDIA AI Enterprise·Omniverse 기반 커리큘럼 표준화
  2. 직원이 사내 LMS (Infosys Springboard·TCS iEvolve 등)에서 AI 기초·Agent·Physical AI 단계별 수강
  3. TCS는 25k 엔지니어를 Microsoft Azure OpenAI 별도 트랙, 150k+에 GenAI 기초 완료 후 AI Experience Zone 실습 제공
  4. Cohort별 인증·proficiency tagging → talent supply 시스템 반영
  5. 클라이언트 RFP 수주 시 인증된 인력 풀에서 staffing → 신규 AI 프로젝트 배치
- **HITL**: 인증 시험 채점, staffing 배정은 BU 리더
- **Frequency**: 등록·수강 = daily, 인증 cohort = monthly, NVIDIA 커리큘럼 갱신 = quarterly

**기업별 핵심 fact**:
- **TCS**: 275K "Ideate and Build with AI" 참여, 25K Azure OpenAI 엔지니어, AI CoE 하이데라바드, 620개 AI 고객 engagement (2025-06)
- **Infosys**: GenAI Academy 275K 교육, 460개 GenAI 이니셔티브, 100+ GenAI 에이전트 개발, 2025-26 신입 20K (AI 우선)
- **Wipro**: 1분기 180K GenAI 기초 교육 완료, "AI Practice" 전담 조직

### B. System & Infrastructure (시스템·인프라)

- **TCS AI 인프라**: ✅ **Fact** Microsoft Azure OpenAI 파트너십. [[sources/poniaktimes-india-it-ai-2025.md]]
- **Infosys 플랫폼**: _미공개 (not disclosed)_ — GenAI Academy 플랫폼 기술 스택 미공개.
- **사용자 접점**: _미공개 (not disclosed)_

### C. Data (데이터)

- **데이터 규모**: ✅ **Fact** TCS 582,163명, Infosys 337,034명, Wipro 233,232명 (2025 기준). [[sources/theregister-india-it-2026-01.md]]
- **학습 콘텐츠**: 내부 개발 AI 교육 커리큘럼. 세부 _미공개 (not disclosed)_.

### D. Model (모델)

- **Foundation model**: ✅ **Fact** TCS — Microsoft Azure OpenAI. [[sources/poniaktimes-india-it-ai-2025.md]]
- **Infosys·Wipro 모델**: _미공개 (not disclosed)_

### E. Organization & Team (조직·팀 구조)

- **TCS 조직**: ✅ **Fact** AI·서비스 전환 전담 사업부 (2024-09-01). [[sources/poniaktimes-india-it-ai-2025.md]]
- **Infosys 접근**: AI 역량 우선 채용 + 기존 직원 전환.
- **Wipro 접근**: AI Practice 전담 조직.

## Impact / Metrics (기대효과)

### 기대효과 요약
Before: _미공개 (AI 교육 전 이직률 기준선 — 5년 최고점 수치 미기재)_ → After: 3사 합산 AI 교육 약 100만 명(TCS 350,000 포함)(Fact), 5년 중 최저 이직률 TCS 13.3%, Infosys 14.3%, Wipro 14.9%, HCL 12.6%(Fact). 단, 이직률 감소가 AI 리스킬링의 직접 결과인지 경기 요인인지 인과관계 _미공개_.

- ✅ **Fact**: 3사 합산 FY26 Q1 기준 AI 교육 인원 약 100만 명 (TCS 350,000 포함). [[sources/aibase-india-it-ai-reskilling-2025.md]]
- ✅ **Fact**: 지난 5년 중 최저 이직률 — TCS 13.3%, Infosys 14.3%, Wipro 14.9%, HCL 12.6%. [[sources/aibase-india-it-ai-reskilling-2025.md]]
- ✅ **Fact**: TCS 12,000명 감원 + 동시에 40,000명 신규 채용. [[sources/theregister-india-it-2026-01.md]]

## Governance & Risk

- AI 도입으로 IT 서비스 채용 자체가 정체/감소: ✅ **Fact** 4대 아웃소서(TCS·Infosys·Wipro·HCL) 의 고용 성장이 멈추었다는 보고 (The Register, 2026-01). [[sources/theregister-india-it-2026-01.md]]
- 리스킬링으로 모든 직원을 구할 수 없는 현실 — "리스킬 or 퇴직" 압박.

## Contradictions

없음 (현재 기준).

## Consulting Angle

- **"AI로 일자리가 감소하는 첫 번째 명시적 사례"**: 인도 IT 서비스 4사의 고용 정체 현상은 AI가 화이트칼라 지식 노동에 미치는 실질적 영향의 가장 구체적인 데이터 포인트. 국내 IT 서비스(삼성SDS·LG CNS·SK C&C) 인력 계획 논의 시 필수 참고.
- **100만 명 규모 리스킬링 설계**: 대규모 L&D 프로그램을 빠르게 롤아웃하는 방법론(Wipro의 1분기 내 18만 명 교육) 은 국내 대기업 AI 리터러시 교육 프로그램 설계 벤치마크.
- **TCS의 "감원 + 신규 채용" 역설**: AI 시대 인력 포트폴리오 재편 패턴 — 기존 역할 축소 + 새로운 AI 역할 창출. 클라이언트의 인력 전략 수립 시 "숫자 관리" 이상의 역할 재설계 필요성 강조에 활용.
- **파생 질문**: "국내 IT 서비스 기업의 AI 리스킬링 투자 수준은 인도 대비 어느 수준인가? (LG CNS·삼성SDS·SK C&C 비교 필요)"
