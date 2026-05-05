---
title: "Microsoft People Skills + Skills Agent — 직원 활동 기반 16K 스킬 ontology 자동 추론"
slug: microsoft-people-skills-inferred-ontology
primary_category: Learning & Development
subcategory: Skills & Capabilities
tags: [microsoft, people-skills, skills-agent, viva, copilot, skills-inference, linkedin-taxonomy, 16k-skills, m365, workforce-insights]
company: Microsoft
industry: [tech, cloud]
region: [global]
employee_class: [all]
vendor: [Microsoft]
vendor_type: [foundation-model, hrms]
output: "직원별 dynamic 스킬 프로파일 (이메일·문서·미팅 텔레메트리 자동 추론, LinkedIn 16K taxonomy 매핑) + 매니저용 Skills Agent의 internal talent 매칭 + Workforce Insights agent의 workforce planning insight"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [information-extraction, clustering-classification, recommendation-ranking]
stage: production
frequency: daily
first_seen: 2025-04-01
last_confirmed: 2026-04-01
confidence: 0.70
consulting_angle_status: filled
sources:
  - sources/us-large-enterprise-hr-ai-2025-2026.md
  - "Forrester: Microsoft Viva Disrupts EX Operating System https://www.forrester.com/blogs/microsoft-viva-disrupts-todays-ex-operating-system/"
related_usecases:
  - eightfold-talent-intelligence-platform
  - workday-illuminate-job-architecture
related_vendors: []
---

## Summary

Microsoft **People Skills** + **Skills Agent** — M365 Copilot/Viva 데이터 레이어. OpenAI 모델로 직원 이메일·문서·미팅에서 **스킬을 자동 추론**해 dynamic 스킬 프로파일 생성. LinkedIn 공동 개발 16,000-skill taxonomy 기반. Skills Agent는 매니저에게 internal talent 매칭·workforce planning insight 제공. 2025 GA. 2026-03 Skills Agent → Learning + Workforce Insights agents로 분리.

## Problem / Why

- **Before**: 한국·글로벌 대기업 모두 직원 self-update profile에 의존 — outdated·incomplete
- **Pain point**: 스킬 inventory 부정확하면 internal mobility·workforce planning·learning 추천 모두 약화
- **Trigger**: Microsoft가 M365 Copilot 위에 People Skills 출시 (2025-04, Bersin "HR tech market 변경"으로 평가)

## Solution Architecture

### A. Process

- **Before**: 직원이 HR 시스템에 직접 스킬 입력 (drop-out high, drift fast)
- **After**:
  1. M365 Copilot이 일상 활동 (이메일·문서·미팅) 텔레메트리 수집
  2. OpenAI 모델로 LinkedIn 16K taxonomy 매핑 → 추론 스킬 프로파일 자동 생성
  3. 직원 검토·승인 (HITL — 추론 결과 거부·수정 가능)
  4. 매니저 Skills Agent 활용 — "이 프로젝트에 맞는 사내 talent" search
  5. Workforce Insights agent — workforce planning insight
- **HITL**: 직원이 추론 스킬 검토·수정. 매니저가 매칭 결정
- **Scope**: recommend-only

### B/C/D. System

- M365 + Viva ecosystem (이미 도입한 KR 대기업 다수)
- Copilot 데이터 레이어 (Azure)
- LinkedIn 16K taxonomy
- 모델: OpenAI (GPT-4 추정) + Microsoft 자체 fine-tuning

### E. Organization

- Microsoft Viva + LinkedIn 협업 + 고객사 HR

### B. System & Infrastructure (Agent research, 2026-05)

- **Core HRIS / 기반 시스템**: _미공개_ (People Skills는 HRMS overlay — Workday/SAP/SuccessFactors와 통합 가능하나 specific connector 명시 없음)
- **AI 시스템 배치**: ✅ M365 Copilot 데이터 레이어 (Microsoft Graph 기반)
- **배포 환경**: ✅ Microsoft Azure (M365 cloud)
- **연동·통합**: ✅ Microsoft Graph (이메일·문서·미팅·chat), LinkedIn (16K skill taxonomy 매핑), Viva Suite, M365 Copilot Chat
- **사용자 접점**: ✅ Copilot Chat, Microsoft 365 apps, Viva services
- **인증·권한**: ✅ Microsoft 365 IAM (Entra ID/Azure AD); admin이 People Skills setup

### C. Data (Agent research)

- **입력 데이터 소스**: ✅ M365 profile + activity signals via Microsoft Graph: 문서·이메일·chat·미팅
- **데이터 규모**: ✅ 16,000+ skills taxonomy (LinkedIn 공동 개발, customizable)
- **전처리·정제**: ✅ Multi-directional inference runs across Microsoft Graph data (proprietary inferencing)
- **학습 vs RAG vs In-context**: ✅ Inference 기반 (RAG·fine-tuning 명시 없음 — Graph data를 LLM에 input으로 inferencing)
- **데이터 거버넌스**: ✅ M365 tenant boundary; admin governance (setup·permissions)
- **민감정보 처리**: ⚠️ 직원 활동 telemetry 기반 — opt-out 옵션 명시 (admin level)

### D. Model (Agent research expanded)

- **Foundation model**: ✅ "Latest OpenAI LLM models"; 구체 GPT 버전 _미공개_
- **모델 유형**: ✅ LLM (inference) + skills classifier; multi-agent inferencing
- **제공 방식**: ✅ Hybrid — Microsoft (Azure OpenAI 추정) + 자체 inferencing layer
- **커스터마이징 기법**: ✅ **"Proprietary inferencing approach based on game theory and multi-agent frameworks"** — multi-directional inference runs (Microsoft 공식 표현, 신규 발견)
- **Orchestration 프레임워크**: ✅ Microsoft 자체 multi-agent framework
- **평가·가드레일**: ⚠️ Everest Group 평가: "step forward but not yet complete" — 독립 검증 일부 존재


## Impact / Metrics

### 기대효과 요약
직원 self-update 부담 없이 스킬 ontology 자동 갱신 — Eightfold·Gloat 외부 vendor 대비 M365 native option.

- ✅ Tier 1 (Bersin) endorsement: "Microsoft Launches People Skills, Altering the HR Tech Market"
- 16,000 스킬 baseline taxonomy
- GA 2025, Skills Agent 2026-03 Learning + Workforce Insights로 분리

## Governance & Risk

- ⚠️ 직원 활동 (이메일·문서·미팅) 기반 추론의 privacy 인지 — opt-out 필수
- ⚠️ 한국 개인정보보호법 + AI 기본법 (고영향 AI 분류 가능성: 평가·승진 영향 시) 의무 검증
- ⚠️ 16K taxonomy 한국어 fit 부족 — 한국 직무·전문 용어 cover 검증 필요

## Consulting Angle

- **KR HRMS RFP 시장 game-changer**:
  - 기존 Eightfold·Gloat·Beamery 외부 vendor 대비 **M365 native option** 등장
  - 이미 Microsoft 365 도입 KR 대기업 (대부분) → people skills 추가 도입 비용·통합 부담 적음
  - 2026 Q3-Q4 People Skills 도입 vs Eightfold 도입 비교 RFP 필수 슬라이드
- **자동 스킬 추론 = 한국 대기업 핵심 페인 해소**: 직원 self-update 부담 없이 ontology 유지 — 가장 갈증 큰 영역
- **2026 Q3-Q4 KR consulting deck**: Bersin People Skills 분석 + Cisco Workforce Consortium 78% AI 스킬 데이터 + Eightfold 비교 — talent marketplace 카테고리 종합
- **반면교사**:
  - 활동 텔레메트리 기반 추론은 직원 "감시" 인식 위험 — opt-in/transparent governance 설계 필수
  - 16K taxonomy의 한국어·한국 직무 fit은 POC 4주 검증 필수
- **한국 AI 기본법 dual compliance**: 추론 스킬이 인사평가·승진에 사용되면 고영향 AI — 인적감독 의무 자동 충족 설계 필요 (Microsoft 거버넌스 제공 여부 RFP 항목)
