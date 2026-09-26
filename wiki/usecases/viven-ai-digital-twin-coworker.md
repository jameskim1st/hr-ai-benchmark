---
title: "Viven AI — Digital Twin of Coworkers"
slug: viven-ai-digital-twin-coworker
primary_category: Employee Experience & HR Ops
subcategory: HR Service Delivery
tags: [viven-ai, digital-twin, eightfold-spinoff, coworker-knowledge, seed-funding, knowledge-management, ai-agent, async-collaboration]
company: _N/A (vendor product, stealth exit 직후 customer 0건)_
industry: [tech]
region: [global]
employee_class: [all]
vendor: [Viven AI]
vendor_type: [point-solution]
output: "부재 동료의 Digital Twin이 query에 대해 과거 발언·결정·전문성 기반 답변 + 출처 표시 + 동료 복귀 시 처리 case 요약 보고 (stealth 직후, customer deployment 0건)"
ai_tech_type: [generative]
ai_tech_subtype: [summarization-qa, information-extraction]
stage: announced
visibility: public
case_type: vendor-product
regulatory_exposure: []
kr_law: 개인정보보호법·영업비밀상 직원 메일·문서·미팅 학습은 strict opt-in + 삭제권 필요
kr_union: 노조 사전 합의 필수 (직원 활동 데이터 학습·AI 대리 책임 소재, 페이지 명시)
kr_language: 미확인 (벤더 확인 필요)
kr_vendor: 미확인 (국내 파트너 확인 필요)
frequency: daily
first_seen: 2025-10-15
last_confirmed: 2026-04-01
confidence: 0.35
evidence_grade: C
corroborated_by: 0
freshness: fresh
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources:
  - sources/verified-pwc-doc-2026-05.md
related_usecases:
  - eightfold-ai-talent-intelligence
  - microsoft-people-skills-inferred-ontology
related_vendors: []
---

## Summary

Viven AI — Eightfold 공동창업자 Ashutosh Garg·Varun Kacholia가 분사 창업한 신생 회사. 2025-10-15 stealth 탈출과 함께 Khosla Ventures·Foundation Capital 등으로부터 **$35M seed funding** 확보. 핵심 컨셉: **"Digital Twin of unavailable coworkers"** — 부재중·휴직·시차 동료의 지식·전문성·맥락을 LLM 기반으로 재현해 다른 직원이 query 가능. 비동기 협업의 "동료 부재 시 지식 단절" 문제 해결 시도.

> 📌 **중요**: PwC 자료에서 "Eightfold Digital Twin (2025)"으로 표기된 기능은 실제로는 본 분사 회사 Viven AI 제품. Eightfold 본체와 별개. Mastercard·다른 Eightfold 고객사에 deploy됐다는 증거 없음.

## Problem / Why (도입 배경)

- **Before**: 글로벌 enterprise에서 시차·휴가·휴직·퇴사 동료의 contextual knowledge 단절 — Slack search·Confluence·이메일 검색에 의존
- **Pain point**: 지식 근로자의 정보 검색 시간 부담 (기존 인용 통계는 인용 소스에 없어 삭제 — 수치 근거 미확보, 2026-09-27 grounding 점검). 부재 동료의 "왜 이렇게 결정했나"·"이 고객은 어떻게 대응?" 같은 contextual Q&A 답 부재
- **Trigger**: Eightfold 공동창업자가 Talent Intelligence 영역에서 Knowledge Twin으로 영역 확장 (2025-10 stealth exit + $35M Khosla seed)

## Solution Architecture

### A. Process (프로세스)

- **Before**: 동료 부재 시 다른 동료에게 위임 또는 search → 시차·답변 지연
- **After** (제품 개념 — 실제 deployment 검증 0건):
  1. 직원이 자기 활동 (이메일·문서·미팅·decision log)을 Viven AI에 학습 동의 (opt-in)
  2. AI가 직원별 "Digital Twin" 지식 모델 구축 — RAG + agentic
  3. 다른 동료가 "X에게 물어보고 싶었던 것"을 Twin에게 query
  4. Twin이 X의 과거 발언·결정·전문성 기반 답변 (출처 표시)
  5. X 복귀 시 Twin이 처리한 case 요약 보고
- **HITL**: 직원 본인이 학습 동의 + Twin 답변에 대한 review·수정 권한
- **Frequency**: daily
- **Scope**: assistive — Twin은 답변 제안, 업무 결정은 사람

### B. System & Infrastructure (시스템·인프라)

> stealth exit 직후 신생 제품 — 인용 소스([[sources/verified-pwc-doc-2026-05]])는 회사 존재·펀딩·제품 컨셉만 확인. 아키텍처는 전부 `_미공개_`.

- **Core HRIS / 기반 시스템**: _미공개 (not disclosed)_
- **AI 시스템 배치**: _미공개 (not disclosed)_
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: _미공개 (not disclosed)_
- **사용자 접점 (UX layer)**: _미공개 (not disclosed)_
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: ✅ 부재중 동료의 지식·전문성을 LLM으로 query 가능한 형태로 재현한다는 제품 컨셉 ([[sources/verified-pwc-doc-2026-05]]); 구체 입력 데이터 _미공개_
- **데이터 규모**: _미공개 (not disclosed)_
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context 구분**: _미공개 (not disclosed)_
- **데이터 거버넌스**: _미공개 (not disclosed)_
- **민감정보 처리**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **Model 유형**: ✅ LLM 기반 digital twin (제품 컨셉) ([[sources/verified-pwc-doc-2026-05]]); 세부 _미공개_
- **제공 방식**: _미공개 (not disclosed)_
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: _미공개 (not disclosed)_

### E. Organization & Team (조직·팀 구조)

- **오너십**: ✅ Viven AI — Eightfold 공동창업자 Ashutosh Garg·Varun Kacholia 분사 창업 ([[sources/verified-pwc-doc-2026-05]])
- **투자자**: ✅ Khosla Ventures·Foundation Capital 등, $35M seed (2025-10-15 stealth exit) ([[sources/verified-pwc-doc-2026-05]])
- **팀 규모·거버넌스·변화관리·파트너**: _미공개 (not disclosed)_

## Impact / Metrics (기대효과)

### 기대효과 요약
글로벌 비동기 협업의 "동료 부재 지식 단절" 해소 시도 — stealth 직후로 customer adoption 0건, ROI 검증 불가.

- ✅ Fact 사실: 2025-10-15 stealth exit, $35M seed, Eightfold 공동창업자 분사
- ⚠️ Customer deployment·KPI _공개 미공개_
- 시장 평가: Khosla Ventures 베팅 + 창업자 신뢰도로 우호적 평가

## Governance & Risk

- ⚠️ 직원 활동 (이메일·문서·미팅) 학습의 privacy 동의 governance — opt-in 강조 필요
- ⚠️ Twin 답변의 책임 소재 (실제 동료 vs AI 환각) — 결정에 사용 시 risk
- ⚠️ 부재 동료의 "AI 대리"가 평가·책임 회피 도구로 악용 가능
- ⚠️ 한국 개인정보보호법 + 영업비밀 보호: 직원 활동 학습은 strict opt-in 필요

## Contradictions

_없음._

> [!note] 2026-09-27 grounding — 인용 소스는 PwC 자료 fact-check 결과(TechCrunch 2025-10-15 인용)로 회사 존재·펀딩·제품 컨셉만 확인. 정보 검색 시간 비율(McKinsey)·Eightfold profile DB 규모·"추정" 아키텍처 서술은 소스에 없어 삭제/`_미공개_`. A. Process 1~5단계는 제품 개념 서술로 인용 소스 미확인 — 외부 인용 금지.

## Consulting Angle

- **KR 컨설팅에서의 위치 — "watch list" reference**:
  - 2025-10 stealth exit 직후 — 2026 customer adoption 시작 시점
  - KR 글로벌 자회사 (삼성·LG·SK·현대 글로벌 본사) "비동기 협업 + 시차" 페인 직접 fit
  - 단, 검증 0건이라 KR client 즉시 도입 권고 어려움 — 2026 Q3 이후 reference customer 출시 후 재평가
- **PwC 자료 오귀속 정정**:
  - "Eightfold Digital Twin"은 사실 분사 회사 Viven AI — 클라이언트 발표에 잘못 인용 시 신뢰도 손상
  - Eightfold 본체 (Talent Intelligence Platform) [[eightfold-ai-talent-intelligence]]와 명확히 분리 권장
- **2026 Q3-Q4 KR consulting "Knowledge Management AI" 카테고리**:
  - Viven AI (coworker twin) + Microsoft People Skills [[microsoft-people-skills-inferred-ontology]] (skill inference) + IBM Blue Match [[ibm-blue-match-internal-mobility]] (digital footprint) — 직원 데이터 활용 AI 3-tier
- **반면교사**:
  - 직원 활동 학습은 한국 노조·개인정보보호 관점에서 가장 민감 — KR 도입 시 strict opt-in + 학습 데이터 범위 명시 + 직원 본인이 Twin 출력 review·삭제권 보장 필수
  - "부재 동료 대리 AI"가 책임 소재 모호화 risk — HR·legal·노조 사전 합의 필수
- **Viven 창업자 신뢰도 베팅**: Khosla·Foundation Capital + Eightfold 운영 경험은 강한 신호 (Eightfold profile DB 규모는 인용 소스에 없어 삭제). 단 1차 customer reference 출시 (예상 2026 H2) 까지 watch list 유지
