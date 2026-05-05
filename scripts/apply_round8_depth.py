#!/usr/bin/env python3
"""
Round 8 — Agent A (Depth) 결과 적용:
  11건 high-conf use case에 B (System), C (Data), D (Model) 섹션 신규 삽입.

각 entry에 (slug, b_section, c_section, d_section).
이미 ### B./C./D. 섹션이 있는 경우 skip (Deloitte Zora만 해당).
없는 경우 ### A. Process 끝 직후, "## Impact" 직전에 신규 삽입.
"""
import re
from pathlib import Path

BASE = Path(__file__).parent.parent
UC = BASE / "wiki" / "usecases"

# 각 entry: B section markdown + C section + D section
ENHANCEMENTS = {
    "accenture-mass-genai-reskilling": dict(
        b="""### B. System & Infrastructure (Agent research, 2026-05)

- **Core HRIS / 기반 시스템**: _미공개_ (Accenture는 SAP SuccessFactors 사용 알려졌으나 LearnVantage와 직접 통합 명시 없음)
- **AI 시스템 배치**: ✅ **Accenture LearnVantage** 자체 학습 플랫폼 (2024-03 launch, Udacity 인수 통합)
- **배포 환경**: _미공개_ (LearnVantage 호스팅 인프라 비공개. AWS·Google Cloud·Microsoft 파트너십은 콘텐츠 차원)
- **연동·통합**: ✅ Stanford Online (Generative AI Scholars Program), Pluralsight·Coursera·Workera·Skillsoft (콘텐츠), AWS·Google Cloud·Microsoft (인증)
- **사용자 접점**: ✅ LearnVantage web platform (self-paced, 40h+ Stanford courses)
- **인증·권한**: _미공개_

> Source: [Accenture LearnVantage newsroom 2024-03](https://newsroom.accenture.com/news/2024/accenture-launches-accenture-learnvantage-to-help-clients-and-their-people-gain-essential-skills-and-achieve-greater-business-value-in-the-ai-economy)""",
        c="""### C. Data (Agent research)

- **입력 데이터 소스**: ⚠️ 벤더 주장: AI recommendation engine이 직원 role + 회사 business strategy 기반 스킬 surface; 구체 데이터 항목 _미공개_
- **데이터 규모**: ✅ 550,000+ trained 직원 (CEO Sweet 발언, ⚠️ 자사 보고)
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_
- **데이터 거버넌스**: _미공개_
- **민감정보 처리**: _미공개_""",
        d="""### D. Model (Agent research)

- **Foundation model**: _미공개_ (LearnVantage "always-on skills assistant" base model 비공개)
- **모델 유형**: ✅ recommendation engine + skills assistant
- **제공 방식**: _미공개_
- **커스터마이징 기법**: _미공개_
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: _미공개_""",
    ),
    "cisco-ai-workforce-consortium-skills-evolution": dict(
        b="""### B. System & Infrastructure (Agent research)

- **Core HRIS / 기반 시스템**: N/A (consortium 자체가 시스템 — research output 발간)
- **AI 시스템 배치**: ✅ Multi-stakeholder research consortium (Cisco anchor + Microsoft·Google·IBM·SAP·Accenture·Eightfold·Indeed·Intel)
- **배포 환경**: N/A (보고서·playbook·glossary 발간물 형태)
- **연동·통합**: ✅ Indeed (job posting data), 참여사 internal job architecture, BLS/O*NET (역할 mapping baseline)
- **사용자 접점**: ✅ Cisco.com 공개 PDF 보고서 + AI Workforce Playbook + AI Skills Glossary + 200+ curated learning resources
- **인증·권한**: N/A (공개 자료)""",
        c="""### C. Data (Agent research)

- **입력 데이터 소스**: ✅ G7 국가 50개 직무 (40 ICT + 10 specialized) job posting volume; 12개월 비교 (Jul 2024–Jun 2025 vs Jul 2023–Jun 2024)
- **데이터 규모**: ✅ 50개 직무 G7 cross-country; 구체 posting count _미공개_
- **전처리·정제**: ✅ "AI Skills Integration" = job posting 중 AI-related skill 포함 비율 측정
- **학습 vs RAG vs In-context**: N/A (research analysis)
- **데이터 거버넌스**: ✅ Multi-stakeholder consortium governance (참여사 협의)
- **민감정보 처리**: N/A (aggregate job market data)""",
        d="""### D. Model (Agent research)

- **Foundation model**: N/A (research methodology, deployed AI 아님)
- **모델 유형**: ✅ Labor market analysis methodology (job posting NLP 추정 — 명시 없음)
- **제공 방식**: N/A
- **커스터마이징 기법**: N/A
- **Orchestration 프레임워크**: N/A
- **평가·가드레일**: ✅ Multi-vendor 협업 자체가 single-vendor bias 완화""",
    ),
    "anaplan-workforce-analyst-ai-agents": dict(
        b="""### B. System & Infrastructure (Agent research, 2026-05 expanded)

- **Core HRIS / 기반 시스템**: ✅ HCM (Workday/SAP) + ERP + finance system을 Anaplan platform에 connector로 통합
- **AI 시스템 배치**: ✅ Anaplan cloud platform 내장 (Role-Based AI Agents, 2025-12-09 GA)
- **배포 환경**: ✅ Cloud-native (Anaplan SaaS — multi-tenant); 구체 클라우드 provider _미공개_
- **연동·통합**: ✅ HCM·ERP·finance system connectors; ⚠️ 벤더 주장: pre-built integration
- **사용자 접점**: ✅ Anaplan web app + 자연어 query interface (conversational UI)
- **인증·권한**: ✅ Anaplan tenant 격리 (multi-tenant SaaS); 세부 RBAC 모델 _미공개_""",
        c="""### C. Data (Agent research)

- **입력 데이터 소스**: ✅ HCM 마스터 데이터 + ERP 트랜잭션 + finance ledger (실시간 통합)
- **데이터 규모**: _미공개_ (Polaris Calculation Engine은 "massive sparse datasets" 처리 가능 — 벤더 주장)
- **전처리·정제**: ✅ Polaris Calculation Engine (sparse data 최적화)
- **학습 vs RAG vs In-context**: ⚠️ 벤더 주장: "LLM의 conversational + reasoning + deterministic planning engine 결합" — RAG·fine-tuning 구체 구분 _미공개_
- **데이터 거버넌스**: ✅ Agent Studio가 "full governance and control" 제공 (벤더 주장)
- **민감정보 처리**: _미공개_""",
        d="""### D. Model (Agent research)

- **Foundation model**: _미공개_ (구체 base LLM 비공개; "leverages LLMs" 표현만)
- **모델 유형**: ✅ LLM (conversational/reasoning) + ML (predictive) + deterministic planning engine 혼합
- **제공 방식**: _미공개_ (자체·외부 API 혼합 추정, 명시 없음)
- **커스터마이징 기법**: ✅ Agent Studio toolkit으로 customer가 custom AI assistant 배포 가능
- **Orchestration 프레임워크**: ✅ Anaplan Agent Studio (자체 toolkit)
- **평가·가드레일**: ⚠️ 벤더 주장: "accurate, traceable, auditable calculations" — eval set·red-team 구체 _미공개_""",
    ),
    "cisco-ai-assistant-hr-agentic": dict(
        b="""### B. System & Infrastructure (Agent research, 2026-05)

- **Core HRIS / 기반 시스템**: _미공개_ (Cisco는 Workday customer로 알려져 있으나 HR Assistant의 직접 integration target 명시 없음)
- **AI 시스템 배치**: ✅ Cisco IT 자체 구축 "internal AI assistant — purpose-built with security"
- **배포 환경**: _미공개_
- **연동·통합**: ✅ HR tools (PTO 입력, 401k 조회 등) 통합; 구체 시스템명 _미공개_
- **사용자 접점**: _미공개_ (Webex 통합 추정 가능하나 공식 확인 없음)
- **인증·권한**: ✅ "purpose-built with security" (벤더 주장) — 구체 모델 _미공개_

> Source: [Cisco "Transforming work with our internal AI assistant"](https://blogs.cisco.com/cisco-on-cisco/cisco-secure-internal-ai-assistant)""",
        c="""### C. Data (Agent research)

- **입력 데이터 소스**: ✅ HR data (PTO·401k 등 직원 self-service domain); 정책 문서 RAG 추정
- **데이터 규모**: ⚠️ 자사 보고: 100,000+ 직원 사용 (broader internal AI assistant); HR domain standalone 수치 _미공개_
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_
- **데이터 거버넌스**: ✅ "purpose-built with security" 강조; 세부 _미공개_
- **민감정보 처리**: _미공개_""",
        d="""### D. Model (Agent research)

- **Foundation model**: _미공개_ (외부 API + 자체 혼합 가능성)
- **모델 유형**: ✅ Generative AI (LLM-based agentic assistant)
- **제공 방식**: _미공개_
- **커스터마이징 기법**: _미공개_
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: ⚠️ 자사 보고: 73% 사용자 productivity 증가, 주당 5h 절감""",
    ),
    "deloitte-zora-ai-hc-suite": dict(
        b="""### B. System & Infrastructure (Agent research expanded, 2026-05)

- **Core HRIS / 기반 시스템**: _미공개_ (Zora는 클라이언트 HCM 위 overlay agentic 플랫폼)
- **AI 시스템 배치**: ✅ Cloud subscription 모델 (Deloitte SaaS); pre-built integrations로 "deploy rapidly on existing technologies"
- **배포 환경**: ✅ NVIDIA AI Enterprise stack (cloud-agnostic); Oracle 파트너십 (별도 발표) — 구체 hyperscaler 선택은 클라이언트 옵션
- **연동·통합**: ✅ Pre-built integrations; 구체 connector 목록 _미공개_; ✅ Oracle Fusion Cloud Apps 통합 (Deloitte-Oracle 파트너십)
- **사용자 접점**: _미공개_ (web/conversational 추정)
- **인증·권한**: ✅ "Trustworthy AI principles — security, transparency, reliability" (벤더 주장)""",
        c="""### C. Data (Agent research)

- **입력 데이터 소스**: ✅ Workforce 데이터 (Workforce Analyzer); 클라이언트 HR 시스템에서 수집 — 구체 항목 _미공개_; ✅ Deloitte 13,000+ leader survey (HR AI maturity 모델 baseline)
- **데이터 규모**: ✅ 1,000+ 사용자 by end-2025 (finance pilot); HR 사용자 수 _미공개_
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: ✅ NVIDIA AI-Q Blueprint 기반 (RAG·agent orchestration용 reference architecture)
- **데이터 거버넌스**: ✅ Human feedback loop 포함 (HITL)
- **민감정보 처리**: _미공개_""",
        d="""### D. Model (Agent research)

- **Foundation model**: ✅ NVIDIA Llama Nemotron (reasoning models)
- **모델 유형**: ✅ Agentic LLM (reasoning + generative + predictive) — finance·human capital·supply chain·procurement·sales·customer service agents
- **제공 방식**: ✅ NVIDIA AI Enterprise stack (NeMo, AI Blueprints, accelerated computing)
- **커스터마이징 기법**: ✅ NVIDIA NeMo (fine-tuning framework) + AI-Q Blueprint (RAG); Deloitte 도메인 fine-tuning 추정
- **Orchestration 프레임워크**: ✅ NVIDIA AI-Q Blueprint (agentic orchestration reference)
- **평가·가드레일**: ✅ Trustworthy AI 프레임워크 (Deloitte 자체) + human feedback loop""",
    ),
    "ibm-charlie-learning-ops-agent": dict(
        b="""### B. System & Infrastructure (Agent research, 2026-05)

- **Core HRIS / 기반 시스템**: ✅ IBM 내부 Learning Management System (이름 미공개)
- **AI 시스템 배치**: ✅ IBM watsonx Orchestrate 기반 (production)
- **배포 환경**: ✅ watsonx Orchestrate (IBM Cloud + AWS 옵션); cHaRlie 자체 배포 환경 _미공개_
- **연동·통합**: ✅ IBM 내부 LMS (enrollment, attendance, event metadata); virtual class 시스템 (Webex/Zoom 추정)
- **사용자 접점**: _미공개_ (L&D admin facing)
- **인증·권한**: _미공개_ (IBM SSO 추정)""",
        c="""### C. Data (Agent research)

- **입력 데이터 소스**: ✅ Enrollment data, virtual class attendance, event metadata, learner roster
- **데이터 규모**: _미공개_ (IBM 270K 직원 규모이나 cHaRlie 처리량 standalone 수치 미공개)
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_ (watsonx Orchestrate는 일반적으로 agent + tool-call 패턴)
- **데이터 거버넌스**: _미공개_
- **민감정보 처리**: _미공개_ (직원 attendance가 personal data)""",
        d="""### D. Model (Agent research)

- **Foundation model**: ✅ IBM Granite (watsonx Orchestrate 기본 model)
- **모델 유형**: ✅ Agentic LLM (Granite decoder 아키텍처) + automation/RPA 통합
- **제공 방식**: ✅ IBM watsonx Orchestrate (proprietary platform)
- **커스터마이징 기법**: _미공개_
- **Orchestration 프레임워크**: ✅ watsonx Orchestrate (IBM 자체 — 150+ enterprise connectors, observability dashboards)
- **평가·가드레일**: ⚠️ 자사 보고: 출석 캡처 100% 정확도, NPS +15%, turnaround 91% 단축, onboarding -25%""",
    ),
    "ibm-hr-workforce-reduction-agentic": dict(
        b="""### B. System & Infrastructure (Agent research expanded)

- **Core HRIS / 기반 시스템**: ✅ IBM 내부 HR (legacy + Workday 통합 가능성)
- **AI 시스템 배치**: ✅ Stack 누적: AskHR + cHaRlie + Watson Recruitment + Predictive Attrition + watsonx Orchestrate TA Agent 모두 watsonx Orchestrate 기반
- **배포 환경**: ✅ watsonx Orchestrate on IBM Cloud + AWS 옵션
- **연동·통합**: ✅ AskHR → Workday/Salesforce/Coupa 등 통합 (2025 IBM 발표)
- **사용자 접점**: ✅ AskHR은 직원 self-service portal/채팅; cHaRlie는 admin tool
- **인증·권한**: _미공개_""",
        c="""### C. Data (Agent research)

- **입력 데이터 소스**: ✅ HR 정책 docs, employee master data, payroll·benefits·career·skills domain (AskHR이 4개 도메인 routing)
- **데이터 규모**: ✅ AskHR 11.5M+ 인터랙션 in 2024
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: ✅ Domain classifier가 employee prompt → 4개 HR domain routing → AI-generated response 또는 task trigger
- **데이터 거버넌스**: ✅ "highly compliant LLMs" (벤더 주장)
- **민감정보 처리**: _미공개_""",
        d="""### D. Model (Agent research)

- **Foundation model**: ✅ IBM Granite (watsonx Orchestrate 기본) + fine-tuned foundation models (orchestrator agent 기능, 2025)
- **모델 유형**: ✅ Agentic LLM (Granite + fine-tuned variants) + classifier (prompt routing) + RPA/automation
- **제공 방식**: ✅ Self-hosted on watsonx (proprietary)
- **커스터마이징 기법**: ✅ Fine-tuned Granite + agentic architecture for autonomous reasoning (TechXchange 2025)
- **Orchestration 프레임워크**: ✅ watsonx Orchestrate orchestrator agent (2025 신규) — multi-agent coordination
- **평가·가드레일**: ⚠️ 자사 보고: AskHR 94% autonomous resolution, NPS -35 → +74""",
    ),
    "microsoft-people-skills-inferred-ontology": dict(
        b="""### B. System & Infrastructure (Agent research, 2026-05)

- **Core HRIS / 기반 시스템**: _미공개_ (People Skills는 HRMS overlay — Workday/SAP/SuccessFactors와 통합 가능하나 specific connector 명시 없음)
- **AI 시스템 배치**: ✅ M365 Copilot 데이터 레이어 (Microsoft Graph 기반)
- **배포 환경**: ✅ Microsoft Azure (M365 cloud)
- **연동·통합**: ✅ Microsoft Graph (이메일·문서·미팅·chat), LinkedIn (16K skill taxonomy 매핑), Viva Suite, M365 Copilot Chat
- **사용자 접점**: ✅ Copilot Chat, Microsoft 365 apps, Viva services
- **인증·권한**: ✅ Microsoft 365 IAM (Entra ID/Azure AD); admin이 People Skills setup""",
        c="""### C. Data (Agent research)

- **입력 데이터 소스**: ✅ M365 profile + activity signals via Microsoft Graph: 문서·이메일·chat·미팅
- **데이터 규모**: ✅ 16,000+ skills taxonomy (LinkedIn 공동 개발, customizable)
- **전처리·정제**: ✅ Multi-directional inference runs across Microsoft Graph data (proprietary inferencing)
- **학습 vs RAG vs In-context**: ✅ Inference 기반 (RAG·fine-tuning 명시 없음 — Graph data를 LLM에 input으로 inferencing)
- **데이터 거버넌스**: ✅ M365 tenant boundary; admin governance (setup·permissions)
- **민감정보 처리**: ⚠️ 직원 활동 telemetry 기반 — opt-out 옵션 명시 (admin level)""",
        d="""### D. Model (Agent research expanded)

- **Foundation model**: ✅ "Latest OpenAI LLM models"; 구체 GPT 버전 _미공개_
- **모델 유형**: ✅ LLM (inference) + skills classifier; multi-agent inferencing
- **제공 방식**: ✅ Hybrid — Microsoft (Azure OpenAI 추정) + 자체 inferencing layer
- **커스터마이징 기법**: ✅ **"Proprietary inferencing approach based on game theory and multi-agent frameworks"** — multi-directional inference runs (Microsoft 공식 표현, 신규 발견)
- **Orchestration 프레임워크**: ✅ Microsoft 자체 multi-agent framework
- **평가·가드레일**: ⚠️ Everest Group 평가: "step forward but not yet complete" — 독립 검증 일부 존재""",
    ),
    "walmart-openai-certification": dict(
        b="""### B. System & Infrastructure (Agent research expanded)

- **Core HRIS / 기반 시스템**: _미공개_ (Walmart는 Workday customer로 알려져 있으나 본 certification 프로그램과의 직접 통합 명시 없음)
- **AI 시스템 배치**: ✅ Walmart Academy (LMS 자체 운영) + OpenAI Academy 플랫폼 통합
- **배포 환경**: ✅ ChatGPT Enterprise rollout (Walmart 전사) — Walmart-OpenAI 2025-10 partnership
- **연동·통합**: ✅ Me@Walmart 앱 (frontline access 인프라, Walmart Global Tech 자체 빌드, 2021 launch); OpenAI Academy + Walmart Academy 통합
- **사용자 접점**: ✅ Samsung Galaxy XCover Pro (740K frontline 디바이스), Me@Walmart 앱 (geofencing, push-to-talk, ML/AR/camera vision); 사무직은 ChatGPT Enterprise web/desktop
- **인증·권한**: ✅ Me@Walmart 앱은 work features = on-clock 접근 제한; Walmart는 personal data access 없음 (벤더 주장)""",
        c="""### C. Data (Agent research)

- **입력 데이터 소스**: ✅ OpenAI Academy 콘텐츠 (basics → prompt engineering 다층); Walmart Academy 자체 콘텐츠
- **데이터 규모**: ✅ 2.1M 직원 in scope (전사 training 목표); 740K frontline 디바이스; ~50,000 직원 AI/automation roles 재배치
- **전처리·정제**: N/A (training content, 직원 데이터 처리 시스템 아님)
- **학습 vs RAG vs In-context**: N/A
- **데이터 거버넌스**: _미공개_
- **민감정보 처리**: ✅ Me@Walmart는 personal/work 분리 (Walmart corporate)""",
        d="""### D. Model (Agent research expanded)

- **Foundation model**: ✅ OpenAI ChatGPT Enterprise (구체 GPT-4/4o/5 _미공개_); ✅ **Google Gemini도 별도 인증 파트너** (multi-vendor, 신규 발견)
- **모델 유형**: ✅ Generative LLM (ChatGPT Enterprise) — 직원 hands-on 사용
- **제공 방식**: ✅ 상용 API (OpenAI ChatGPT Enterprise, Google Gemini) — multi-vendor
- **커스터마이징 기법**: _미공개_ (Walmart 자체 fine-tuning 명시 없음)
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: ✅ OpenAI Certifications (자체 평가 체계)""",
    ),
    "amazon-connections-daily-pulse": dict(
        b="""### B. System & Infrastructure (Agent research)

- **Core HRIS / 기반 시스템**: _미공개_ (Amazon 내부 HR 시스템 — 자체 구축 추정)
- **AI 시스템 배치**: ✅ Amazon 자체 구축 (proprietary, People Science 팀 운영)
- **배포 환경**: _미공개_ (Amazon 내부 AWS 추정)
- **연동·통합**: ✅ 직원 login 시스템 (Amazon SSO/A-to-Z 포털); 응답 데이터 → Seattle 본사 People Science team 집계
- **사용자 접점**: ✅ 직원 로그인 시 자동 popup (web app — A-to-Z 직원 포털)
- **인증·권한**: ✅ Amazon employee credential SSO""",
        c="""### C. Data (Agent research)

- **입력 데이터 소스**: ✅ Daily 1-question response (1-5 scale 또는 텍스트), non-response signal, 시간 경과 변화
- **데이터 규모**: ✅ 1.5M+ 직원 cover (55 countries), 연 300M+ 응답 (자사 보고)
- **전처리·정제**: ✅ Aggregation by area/manager (Seattle 팀); confidential 응답 처리 (자사 주장)
- **학습 vs RAG vs In-context**: N/A (predictive ML, LLM 이전 세대)
- **데이터 거버넌스**: ⚠️ Fortune Jun 2024 critical: anonymity 회의론 보고; 매니저별 area aggregation 가능
- **민감정보 처리**: ⚠️ "Confidential responses" 자사 주장 — Fortune 비판 보도""",
        d="""### D. Model (Agent research)

- **Foundation model**: N/A (LLM 이전 세대 — 2014 시작)
- **모델 유형**: ✅ ML + NLP (behavior·sentiment prediction, attrition·engagement 예측)
- **제공 방식**: ✅ Self-hosted (Amazon 내부 proprietary)
- **커스터마이징 기법**: _미공개_ (자체 모델 학습 추정)
- **Orchestration 프레임워크**: N/A
- **평가·가드레일**: ⚠️ Fortune 비판: 응답 이후 manager-level 압력 가능성; 익명성 실효성 의문""",
    ),
    "jpmorgan-ai-made-easy-upskilling": dict(
        b="""### B. System & Infrastructure (Agent research expanded)

- **Core HRIS / 기반 시스템**: _미공개_ (JPM HRIS 명시 없음)
- **AI 시스템 배치**: ✅ AI Made Easy 교육 sessions + LLM Suite hands-on 플랫폼 통합
- **배포 환경**: ✅ LLM Suite는 JPMorgan 자체 portal (proprietary); 교육 LMS 명시 없음
- **연동·통합**: ✅ LLM Suite는 8주마다 internal database·software apps 추가 통합
- **사용자 접점**: ✅ AI Made Easy = 인터랙티브 sessions (live + 직무별 모듈); LLM Suite portal 직접 hands-on
- **인증·권한**: _미공개_ (JPM internal SSO 추정)""",
        c="""### C. Data (Agent research)

- **입력 데이터 소스**: ✅ 교육 콘텐츠 = AI fundamentals + prompt engineering + compliance + 직무별 use case curriculum
- **데이터 규모**: ✅ Q1 alone **30,000+ 직원 attended AI Made Easy sessions** (신규 fact); 230K+ in scope; 250K LLM Suite rollout (branch·call center 제외, 약 절반 daily 사용)
- **전처리·정제**: N/A (training program)
- **학습 vs RAG vs In-context**: N/A
- **데이터 거버넌스**: ✅ Compliance 모듈 별도 (금융정보·고객정보 처리 가이드)
- **민감정보 처리**: ✅ Compliance 모듈에서 다룸""",
        d="""### D. Model (Agent research expanded)

- **Foundation model**: N/A (training program 자체)
- **모델 유형**: N/A — 단, hands-on 학습 대상 LLM Suite는 ✅ **OpenAI + Anthropic 양사** (multi-vendor, 신규 발견)
- **제공 방식**: N/A
- **커스터마이징 기법**: ✅ "Learn by doing" — LLM Suite 직접 사용 통합
- **Orchestration 프레임워크**: N/A
- **평가·가드레일**: ⚠️ 자사 보고: 직원당 3-6h/week saved (LLM Suite 결합 효과)""",
    ),
}


def update_page(slug, b, c, d):
    fp = UC / f"{slug}.md"
    if not fp.exists():
        print(f"SKIP {slug}: not found")
        return False
    text = fp.read_text(encoding="utf-8")

    # Skip if B section already exists
    if re.search(r"^### B\.", text, re.MULTILINE):
        # Existing B exists — append A_research separately at end of SA section
        # Anaplan & Deloitte have B already; replace with expanded content
        # Find the section block from "### B." until "## " (next top-level heading)
        if slug in ("deloitte-zora-ai-hc-suite", "anaplan-workforce-analyst-ai-agents"):
            # Replace existing B/C/D with new
            new_block = f"{b}\n\n{c}\n\n{d}\n\n"
            new_text, n = re.subn(
                r"### B\.[^\n]*\n.*?(?=\n## )",
                new_block,
                text,
                count=1,
                flags=re.DOTALL,
            )
            if n == 0:
                print(f"FAIL {slug}: existing B block not matched")
                return False
            fp.write_text(new_text, encoding="utf-8")
            print(f"  REPLACED B/C/D | {slug}")
            return True
        print(f"SKIP {slug}: B already exists, no replacement rule")
        return False

    # Insert before ## Impact
    new_block = f"{b}\n\n{c}\n\n{d}\n\n"
    new_text, n = re.subn(
        r"(\n## Impact)",
        f"\n{new_block}\\1",
        text,
        count=1,
    )
    if n == 0:
        print(f"FAIL {slug}: no '## Impact' anchor")
        return False
    fp.write_text(new_text, encoding="utf-8")
    print(f"  INSERTED B/C/D | {slug}")
    return True


def main():
    ok, fail = 0, 0
    for slug, sections in ENHANCEMENTS.items():
        if update_page(slug, sections["b"], sections["c"], sections["d"]):
            ok += 1
        else:
            fail += 1
    print(f"\nR8-A applied: {ok}/{len(ENHANCEMENTS)} pages")


if __name__ == "__main__":
    main()
