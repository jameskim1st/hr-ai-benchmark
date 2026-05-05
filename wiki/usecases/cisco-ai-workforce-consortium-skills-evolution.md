---
title: "Cisco AI Workforce Consortium — ICT 직무 AI 스킬 표준화"
slug: cisco-ai-workforce-consortium-skills-evolution
primary_category: Strategic Workforce & Governance
subcategory: People Analytics
tags: [cisco, workforce-consortium, ict-skills, ai-skills-glossary, multi-vendor-research, microsoft, google, ibm, sap, accenture, skills-evolution, workforce-planning]
company: _Cisco-led consortium (Microsoft·Google·IBM·SAP·Accenture·Eightfold 등)_
industry: [tech, it-services]
region: [global]
employee_class: [all]
vendor: [Cisco, _다수_]
vendor_type: [internal-build]
output: "ICT 직무·AI 스킬 evolution 정량 보고서 (78% AI 포함, top 10 fastest-growing 중 7개 AI) + AI Skills Glossary 표준 + AI Workforce Playbook + 200+ curated learning recommendation 리스트 (PDF 발간물)"
ai_tech_type: [predictive]
ai_tech_subtype: [clustering-classification]
stage: production
frequency: annual
first_seen: 2024-01-01
last_confirmed: 2025-12-01
confidence: 0.75
consulting_angle_status: filled
sources:
  - sources/us-large-enterprise-hr-ai-2025-2026.md
  - "Cisco AI Workforce Consortium Full Report 2025 https://www.cisco.com/content/dam/cisco-cdc/site/m/ai-workforce-consortium/documents/2025-ai-workforce-consortium-full-report.pdf"
related_usecases:
  - cisco-ai-assistant-hr-agentic
  - accenture-mass-genai-reskilling
  - microsoft-people-skills-inferred-ontology
related_vendors: []
---

## Summary

Cisco가 anchor한 다자 컨소시엄 (Microsoft·Google·IBM·SAP·Accenture·Eightfold 등). 2025 보고서: **78% ICT 직무가 AI 기술 스킬 포함**, top 10 fastest-growing ICT 직무 중 7개가 AI 관련. AI Workforce Playbook + 2025 AI Skills Glossary + 200+ curated learning recommendations 발간. multi-vendor 방법론 — Tier 1-equivalent 신뢰도.

## Problem / Why (도입 배경)

- **Before**: ICT 직무·스킬 evolution 정량 데이터는 LinkedIn·Indeed·BLS 산발 — 글로벌 컨소시엄 합의 부재
- **Pain point**: HR·workforce planning 임원이 "AI가 우리 직무에 얼마나 영향을 주나"에 정량 답 부재
- **Trigger**: 2024 multi-vendor 협업 출범 — Cisco가 anchor

## Solution Architecture

### A. Process (프로세스)

- **Before**: 산발 데이터, 컨설팅사·analyst별 다른 framework
- **After**:
  1. 6+ tech 대기업 협업 데이터 pooling
  2. ICT 직무 mapping (BLS·O*NET 기반 + 회사 internal job architecture)
  3. AI 기술 스킬 포함 비율 측정 → 78% 결과
  4. fastest-growing ICT 직무 trend 분석 → top 10 중 7개 AI-related
  5. AI Skills Glossary 표준화 발간
  6. Playbook + 200+ learning recommendation 부속 발간
- **HITL**: 컨소시엄 governance board (참여사 임원 협의)

### B/C/D/E. System

- 컨소시엄 자체가 "system" — vendor-neutral multi-stakeholder
- 데이터: 참여 vendor의 anonymized job posting + skills demand
- 오너십: Cisco anchor + Microsoft/Google/IBM/SAP/Accenture/Eightfold 협업

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS / 기반 시스템**: N/A (consortium 자체가 시스템 — research output 발간)
- **AI 시스템 배치**: ✅ Multi-stakeholder research consortium (Cisco anchor + Microsoft·Google·IBM·SAP·Accenture·Eightfold·Indeed·Intel)
- **배포 환경**: N/A (보고서·playbook·glossary 발간물 형태)
- **연동·통합**: ✅ Indeed (job posting data), 참여사 internal job architecture, BLS/O*NET (역할 mapping baseline)
- **사용자 접점**: ✅ Cisco.com 공개 PDF 보고서 + AI Workforce Playbook + AI Skills Glossary + 200+ curated learning resources
- **인증·권한**: N/A (공개 자료)

### C. Data (데이터)

- **입력 데이터 소스**: ✅ G7 국가 50개 직무 (40 ICT + 10 specialized) job posting volume; 12개월 비교 (Jul 2024–Jun 2025 vs Jul 2023–Jun 2024)
- **데이터 규모**: ✅ 50개 직무 G7 cross-country; 구체 posting count _미공개_
- **전처리·정제**: ✅ "AI Skills Integration" = job posting 중 AI-related skill 포함 비율 측정
- **학습 vs RAG vs In-context**: N/A (research analysis)
- **데이터 거버넌스**: ✅ Multi-stakeholder consortium governance (참여사 협의)
- **민감정보 처리**: N/A (aggregate job market data)

### D. Model (모델)

- **Foundation model**: N/A (research methodology, deployed AI 아님)
- **모델 유형**: ✅ Labor market analysis methodology (job posting NLP 추정 — 명시 없음)
- **제공 방식**: N/A
- **커스터마이징 기법**: N/A
- **Orchestration 프레임워크**: N/A
- **평가·가드레일**: ✅ Multi-vendor 협업 자체가 single-vendor bias 완화


## Impact / Metrics (기대효과)

### 기대효과 요약
ICT 직무 AI 스킬 78% 포함 + AI 직무 top 10 fastest-growing 7개 — KR 대기업 workforce planning deck "burning platform" 데이터 pillar.

- ✅ multi-vendor methodology — Tier 1-equivalent 신뢰도
- 78% ICT 직무 AI 스킬 포함
- Top 10 fastest-growing ICT 직무 중 7개 AI-related
- 200+ curated learning recommendations
- 2025 AI Skills Glossary 표준 (산업 reference)

## Governance & Risk

- ✅ multi-vendor 협업 — single vendor bias 완화
- ⚠️ 데이터 pooling 방법론·표본 _세부 미공개_
- ⚠️ 비ICT 직무(제조·유통·금융 운영) 적용 범위 제한적

## Consulting Angle

- **KR workforce planning deck 핵심 데이터 source**:
  - "78% ICT 직무 AI 스킬" 데이터는 KR 대기업(삼성전자·LG전자·SK하이닉스·LG CNS·삼성SDS) AI 인력 전략 deck 첫 슬라이드
  - "top 10 중 7 AI-related" — KR IT 인재 채용·reskilling 우선순위 재편 명분
- **AI Skills Glossary**: KR HR 직무 dictionary 갱신 시 vendor-neutral reference 활용 가능
- **200+ learning recommendation**: KR 그룹 HRD 센터 curriculum 설계 시 단축 source
- **2026 Q3-Q4 컨설팅 deck 활용**:
  - Accenture 550K reskilling [[accenture-mass-genai-reskilling]] + Cisco Consortium 78% 데이터 + JPMorgan AI Made Easy [[jpmorgan-ai-made-easy-upskilling]] 3-card 합 → "AI 인력 전환 burning platform" 슬라이드 완성
- **반면교사**: 컨소시엄 데이터 = 글로벌 평균 — KR 시장 fit은 추가 local survey 필요 (Cisco·Microsoft Korea 협업 가능성)
