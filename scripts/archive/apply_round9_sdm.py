#!/usr/bin/env python3
"""R9 — Agent (medium-conf) System/Data/Model 20건 보강.

각 entry: slug → (b_section, c_section, d_section)
모든 page에 ### B/C/D 직전 ## Impact 앞에 신규 삽입.
"""
import re
from pathlib import Path

BASE = Path(__file__).parent.parent
UC = BASE / "wiki" / "usecases"

ENH = {
    "linkedin-learning-ai-coaching": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: _미공개_ (LinkedIn Learning은 stand-alone LXP, SCIM/SSO 가능)
- **AI 시스템 배치**: ⚠️ 벤더 주장: Premium·Enterprise tier 내장 SaaS
- **배포 환경**: _미공개_ (Microsoft Azure 추정, 공식 미확인)
- **연동·통합**: ⚠️ 벤더 주장: M365 Copilot 통합 (2025), LinkedIn Skills Graph
- **사용자 접점**: LinkedIn Learning 웹·모바일 — conversational UI
- **인증·권한**: LinkedIn 계정 + 기업 SSO (SAML)""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: 학습 이력·skill profile·career goal·강의 콘텐츠
- **데이터 규모**: ⚠️ 벤더 주장: 16,000+ skills taxonomy
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_ (강의 콘텐츠 grounding 추정)
- **데이터 거버넌스**: _미공개_ (Microsoft enterprise privacy 정책 추정)
- **민감정보 처리**: _미공개_ — KR PIPA cross-border data transfer 검증 필요""",
        d="""### D. Model (R9 research)

- **Foundation model**: _미공개_ (GPT 계열 추정, 공식 발표 없음)
- **모델 유형**: LLM (생성·대화형 코칭)
- **제공 방식**: _미공개_ (LinkedIn 자체 호스팅 추정)
- **커스터마이징 기법**: _미공개_ (role-play scenario prompt template 추정)
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: _미공개_ — soft skill 코칭 quality control governance 미공개""",
    ),
    "microsoft-viva-glint-copilot-sentiment": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: Microsoft Viva (M365 ecosystem) — Glint이 LinkedIn → MS Viva 통합
- **AI 시스템 배치**: ✅ Viva Glint 내장 Copilot
- **배포 환경**: Microsoft Azure cloud (M365 표준)
- **연동·통합**: M365 (Outlook·Teams·Power BI), Viva Insights, LinkedIn Glint 데이터
- **사용자 접점**: Viva Glint 관리자 web portal — "Copilot Highlights" 섹션
- **인증·권한**: Entra ID (Azure AD) RBAC — HRBP·매니저·executive 역할별""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: engagement survey 응답 (open-end + Likert), 직원 메타 (부서·재임·매니저 hierarchy)
- **데이터 규모**: _미공개_ (Microsoft 자체 twice-yearly Employee Signals — 인원 비공개)
- **전처리·정제**: _미공개_ — anonymization·small-group 임계값 적용 추정
- **학습 vs RAG vs In-context**: In-context summarization (서베이 응답 합성)
- **데이터 거버넌스**: ⚠️ Microsoft 표준 enterprise — Glint 응답은 customer tenant 격리
- **민감정보 처리**: ⚠️ 자사 보고: anonymity threshold 적용 — 속성별 slice 시 small group re-identification 위험 잔존""",
        d="""### D. Model (R9 research)

- **Foundation model**: _미공개_ (Azure OpenAI GPT-4 계열 추정)
- **모델 유형**: LLM (open-end 합성·summarization) + classifier (sentiment·테마)
- **제공 방식**: Azure OpenAI service via Microsoft Copilot
- **커스터마이징 기법**: _미공개_ — survey domain prompt engineering 추정
- **Orchestration 프레임워크**: Microsoft Copilot stack (자체)
- **평가·가드레일**: ⚠️ 자사 보고: Copilot Highlights는 자동 합성·HRBP 검토 — explainable. bias·hallucination 테스트 결과 미공개""",
    ),
    "midas-inair-ai-assessment-korea": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: ✅ 마이다스아이티 자체 채용 platform (JOBFLEX 연동)
- **AI 시스템 배치**: 마이다스 SaaS — 도입 기업 ATS와 별도 운영
- **배포 환경**: _미공개_ (한국 데이터센터 추정)
- **연동·통합**: 도입 기업 ATS와 result feed (구체 _미공개_)
- **사용자 접점**: 지원자용 web/모바일 — 성향파악·전략게임·영상면접
- **인증·권한**: _미공개_""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 지원자 행동 데이터 — 성향 응답·게임 행동 로그·영상 (음성·표정 추정)
- **데이터 규모**: _미공개_ (10+ 대기업·4+ 공공기관, 누적 응시자 미공개)
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: 시뮬레이션 기반 역량 예측 ML (전통 ML 추정)
- **데이터 거버넌스**: ⚠️ 영상면접 데이터 보관·폐기 _미공개_ — KR PIPA 생체정보 처리 검증 필요
- **민감정보 처리**: ⚠️ 채용절차공정화법: AI 평가 사용 시 지원자 고지 의무 — 마이다스 고지 방식 _미공개_""",
        d="""### D. Model (R9 research)

- **Foundation model**: _미공개_ — LLM 기반인지 전통 ML 기반인지 미공개
- **모델 유형**: ✅ predictive (성과역량 예측) + recognition (영상·음성) + simulation (게임 행동)
- **제공 방식**: 자체 모델 (마이다스아이티 R&D)
- **커스터마이징 기법**: _미공개_ — 직무·기업별 norm 조정 가능성 추정
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: ✅ KAIST 연구진 *Nature Scientific Reports* (2025-07) — 채용 1년 후 업무 성과 예측 통계적 유의성 검증. 단 편향 부재 별도 검증 미공개""",
    ),
    "schneider-electric-gloat-talent-marketplace": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: ✅ Oracle Fusion HCM, Taleo (ATS), Cornerstone (LMS) 통합 — Bersin 2019 독립 확인
- **AI 시스템 배치**: Gloat Workforce Agility Platform — SaaS, Schneider 사내 SSO
- **배포 환경**: _미공개_ (Gloat AWS multi-tenant SaaS 추정)
- **연동·통합**: ✅ Oracle Fusion·Taleo·Cornerstone과 데이터 sync (skill·position·learning)
- **사용자 접점**: Gloat web·모바일 — 직원 프로필·기회 매칭 dashboard
- **인증·권한**: 사내 SSO (구체 IdP _미공개_)""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: 직원 프로필 (스킬·관심·포부), 조직 내 기회 (gig·career·mentorship)
- **데이터 규모**: ⚠️ 자사 보고: 135K+ 직원, 등록률 89% (NA 92%), gig 13,400건, mentor 27,500건
- **전처리·정제**: _미공개_ — Gloat skill ontology 기반 inference 추정
- **학습 vs RAG vs In-context**: matching engine = skills graph + ML recommendation
- **데이터 거버넌스**: _미공개_ — 직원 자율 입력 + 매칭 활용 동의
- **민감정보 처리**: _미공개_ — EU GDPR (Schneider HQ 프랑스)""",
        d="""### D. Model (R9 research)

- **Foundation model**: _미공개_ — Gloat 자체 ML/skills inference, LLM 도입 여부 (2024+) 별도 발표 미확인
- **모델 유형**: predictive (recommendation·ranking) + skills inference
- **제공 방식**: Gloat SaaS (자체 호스팅)
- **커스터마이징 기법**: ✅ Schneider 41 capability·career path 자체 정의를 Gloat에 주입
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: _미공개_ — bias audit·explainability 결과 공식 발표 없음""",
    ),
    "sk-cc-adot-biz-hr-recruitment": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: SK C&C 사내 ATS (구체 _미공개_)
- **AI 시스템 배치**: ✅ SKT-SK AX 합작 'A.Biz' B2B AI — 'A.Biz HR'
- **배포 환경**: _미공개_ — SK Cloud 추정
- **연동·통합**: SK C&C 사내 ATS + 신입 공채 시즌 batch
- **사용자 접점**: HR·사업부 SME web UI — 자기소개서 분석·맞춤 면접 질문 review
- **인증·권한**: SK C&C 사내 SSO""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 자기소개서 텍스트, JD 텍스트, AI 면접 영상 응답
- **데이터 규모**: ✅ 수천 건 자기소개서 / 신입 공채 cycle
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: ⚠️ 자사 추정: 자체 LLM + RAG (직무·SK culture 코퍼스) — 공식 architecture 발표 없음
- **데이터 거버넌스**: _미공개_ — 채용절차공정화법 + AI 기본법 (2026-01) fit 검증 필요
- **민감정보 처리**: ⚠️ 영상면접 표정·억양·외모 신호 사용 여부 _미공개_""",
        d="""### D. Model (R9 research)

- **Foundation model**: SKT 자체 LLM **A.X** 추정 (공식 _미공개_)
- **모델 유형**: ✅ LLM (자기소개서 추출·요약) + classifier (직무 적합성·리스크) + 영상 분석 (멀티모달)
- **제공 방식**: SK 그룹 자체 (A.Biz)
- **커스터마이징 기법**: _미공개_ — 직무·SK culture domain prompt/RAG
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: ⚠️ "리스크 요인" explainability·차별 표현 자동 필터 _미검증·미공개_""",
    ),
    "amazon-hr-ai-restructuring": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: Amazon 자체 (구체 _미공개_) — Workday/SAP 도입 여부 공식 확인 안 됨
- **AI 시스템 배치**: ⚠️ 자사 보고: PXT 조직이 internal AI 시스템(CS·warehouse 자동화에 사용 중)을 talent management·recruiting·employee engagement에 통합
- **배포 환경**: AWS (자사 클라우드)
- **연동·통합**: _미공개_ — 어떤 HR task가 어떤 AI에 연결되는지 공식 발표 없음
- **사용자 접점**: _미공개_ (HRBP·매니저 internal tool 추정)
- **인증·권한**: Amazon 사내 IAM""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: _미공개_ — 채용 지원서·티켓·정책·성과 추정
- **데이터 규모**: ✅ 영향받는 PXT 인력 ~1,500명 (10K+ 중 15%), 250K 계절직 채용
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_
- **데이터 거버넌스**: _미공개_
- **민감정보 처리**: _미공개_""",
        d="""### D. Model (R9 research)

- **Foundation model**: _미공개_ — Amazon Bedrock 또는 자체 추정
- **모델 유형**: ✅ generative + predictive + automation (RPA) — Recruiting screening·티켓·정책 Q&A
- **제공 방식**: ⚠️ 자사 보고: Amazon internal build
- **커스터마이징 기법**: _미공개_
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: _미공개_ — HR 자동화 의사결정 HITL 설계 미공개""",
    ),
    "betterup-ai-coaching-twilio": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: Twilio 측 _미공개_ — BetterUp은 stand-alone SaaS, SSO·SCIM 연동
- **AI 시스템 배치**: ✅ BetterUp Manage (hybrid) + BetterUp Grow (AI-only) SaaS
- **배포 환경**: _미공개_ (BetterUp cloud)
- **연동·통합**: HRIS SSO, calendar (1:1), 학습 dashboard
- **사용자 접점**: BetterUp web·모바일 — assessment·1:1 영상 코칭·micro-intervention·VR (Grow)
- **인증·권한**: 기업 SSO + RBAC (manager·HR dashboard 분리)""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: ✅ Whole Person Assessment (resilience·growth mindset 등), 코칭 세션, behavior change tracker, 비즈니스 KPI
- **데이터 규모**: Twilio 8K+ 직원 cohort
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_ — Grow AI 코치 LLM 기반 추정
- **데이터 거버넌스**: ⚠️ BetterUp 표준: 코칭 세션은 employer에 disaggregated form만 (자사 정책)
- **민감정보 처리**: _미공개_ — 멘탈헬스 인접 — HIPAA·GDPR 별도 명시 없음""",
        d="""### D. Model (R9 research)

- **Foundation model**: _미공개_ — Grow LLM 기반이나 모델·버전 비공개
- **모델 유형**: LLM (conversational coaching) + assessment scoring + recommendation
- **제공 방식**: _미공개_
- **커스터마이징 기법**: ⚠️ 벤더 주장: BetterUp 코칭 IP·과학 자문 (Martin Seligman 등) prompt·rubric
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: ⚠️ 벤더 주장: 95% user satisfaction (Inc.com, BetterUp 자체 측정) — 독립 검증 부재""",
    ),
    "deloitte-claude-470k-employees": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: _미공개_ (Deloitte 사내 — Workday 사용 여부 공식 미확인)
- **AI 시스템 배치**: ✅ Anthropic Claude Enterprise 470K 글로벌 SSO 프로비저닝
- **배포 환경**: _미공개_ — AWS Bedrock 또는 Anthropic 직접 호스팅 추정
- **연동·통합**: ⚠️ 자사 보고: Trustworthy AI framework 산출물 검증, governance dashboard prompt·사용 로그
- **사용자 접점**: ⚠️ 자사 보고: 회계사·개발자용 특화 Claude 버전 + 일반 web/desktop
- **인증·권한**: 글로벌 SSO (구체 IdP _미공개_)""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: ⚠️ 자사 보고: 클라이언트 자료·문서·코드 — use case별 상이
- **데이터 규모**: ✅ 470K 직원, 150개국
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_ — 회계사·개발자 특화 = fine-tuning vs system prompt 미공개
- **데이터 거버넌스**: ⚠️ 자사 보고: Trustworthy AI framework, governance dashboard, Claude CoE
- **민감정보 처리**: _미공개_ — 클라이언트 confidential 처리 정책 미발표""",
        d="""### D. Model (R9 research)

- **Foundation model**: ✅ Anthropic Claude (버전 미명시)
- **모델 유형**: LLM (생성·요약·코드)
- **제공 방식**: ✅ Anthropic Claude Enterprise (commercial API)
- **커스터마이징 기법**: ⚠️ 자사 보고: 회계사·개발자 특화 버전, 규제 산업 industry pack 공동 개발
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: ⚠️ 자사 보고: Trustworthy AI framework + 파트너 검토""",
    ),
    "jobkorea-hiring-center-talent-agent": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: ✅ 잡코리아 ATS '하이어링 센터' (웍스피어 자체)
- **AI 시스템 배치**: '탤런트 에이전트' — 하이어링 센터 내장 conversational agent
- **배포 환경**: _미공개_ — 한국 데이터센터 추정
- **연동·통합**: 잡코리아 후보자 DB, 공고 데이터, 지원·이력 history
- **사용자 접점**: 채용 담당자 web UI — 자연어 chat
- **인증·권한**: 잡코리아 기업회원 계정""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 잡코리아 후보자 DB, 공고 텍스트, 채용 담당자 의도
- **데이터 규모**: _미공개_ — 잡코리아 누적 회원 비공개
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_ — 매칭 retrieval + LLM ranking 추정
- **데이터 거버넌스**: ⚠️ KR PIPA — 후보자 동의 (잡코리아 약관 의존)
- **민감정보 처리**: ⚠️ 차별 표현 자동 필터 _미검증_ — explainability 미공개""",
        d="""### D. Model (R9 research)

- **Foundation model**: _미공개_ — 자체 LLM 또는 외부 API (OpenAI·Hyperclova X) 추정
- **모델 유형**: LLM (conversational matching) + recommendation
- **제공 방식**: _미공개_
- **커스터마이징 기법**: ⚠️ 자사 보고: 한국어 specialized
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: _미공개_""",
    ),
    "korea-electric-power-hr-bot": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: 한전 자체 HR (구체 _미공개_)
- **AI 시스템 배치**: ✅ HR-Bot (솔트룩스 챗봇) + 별도 AI 인사추천
- **배포 환경**: _미공개_ — 망분리상 정부 클라우드 또는 on-prem 추정
- **연동·통합**: ✅ 한전 사내 HR 통합, 2025-12~2026-03 전 직원 사내 규정·법규·문서 작성용 GenAI 추가 개방
- **사용자 접점**: 채용 챗봇 web/앱 + 사내 인사추천 dashboard
- **인증·권한**: ✅ 한전 SSO + 공공기관 보안 표준""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 채용 FAQ·일정, 직원 역량(자격증·경력), 업무 이력(성과·전배)
- **데이터 규모**: ✅ 한전 23K+ 직원
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_ — 솔트룩스 NLP 표준 RAG·intent classifier 조합 추정
- **데이터 거버넌스**: ⚠️ 공공기관 인사이동 AI 추천의 노조·직원 투명성 process _미공개_
- **민감정보 처리**: ✅ KR PIPA strict — 공공기관 추가 가이드라인""",
        d="""### D. Model (R9 research)

- **Foundation model**: _미공개_ — 솔트룩스 자체 NLP + 2025-Q4 GenAI (모델 미공개)
- **모델 유형**: 챗봇 NLP + recommendation
- **제공 방식**: ✅ 솔트룩스 vendor (한국 NLP) — single vendor lock-in risk
- **커스터마이징 기법**: _미공개_
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: ⚠️ KR AI 기본법 (2026-01) 고영향 AI — 인적감독 의무 자동 충족 검증 _미공개_""",
    ),
    "mirae-asset-ai-assistant-platform": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: 미래에셋증권 사내 시스템 (구체 _미공개_)
- **AI 시스템 배치**: ✅ 자체 AI Assistant 플랫폼 (네이버클라우드 협업)
- **배포 환경**: ✅ 네이버클라우드 (NCP) — 한국 데이터 주권 driver
- **연동·통합**: ✅ 사내 SSO + 부서별 매뉴얼·노하우 문서 upload
- **사용자 접점**: ✅ web 기반 No-code 챗봇 빌더 + 직원 자연어 query
- **인증·권한**: ✅ 사내 SSO + 부서별 RBAC""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 부서별 업무 매뉴얼·노하우 문서 (직원·부서 직접 upload)
- **데이터 규모**: _미공개_ — 챗봇 수·인덱스 크기 비공개
- **전처리·정제**: ✅ RAG indexing (구체 chunking·임베딩 _미공개_)
- **학습 vs RAG vs In-context**: ✅ RAG (No-code 빌더로 부서별 RAG)
- **데이터 거버넌스**: ✅ 부서별 RAG 격리. No-code 빌더 quality governance 세부 _미공개_
- **민감정보 처리**: ✅ 한국 자체 LLM (Hyperclova X) → 데이터 주권. 전자금융감독규정 fit""",
        d="""### D. Model (R9 research)

- **Foundation model**: ✅ 네이버 **하이퍼클로바X 대시 (HyperCLOVA X Dash)** — 한국어 specialized
- **모델 유형**: LLM (요약·QA)
- **제공 방식**: ✅ Naver Cloud Platform via 협업
- **커스터마이징 기법**: ✅ RAG + No-code 빌더 (부서별)
- **Orchestration 프레임워크**: _미공개_ — 네이버클라우드 stack 추정
- **평가·가드레일**: ⚠️ No-code 빌더 챗봇의 prompt injection·hallucination 통제 부족 가능 — 모니터링 필요. 공식 framework _미공개_""",
    ),
    "siemens-reskilling-internal-mobility": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: _미공개_ (Workday 사용 여부 미확인) + ✅ ServiceNow (Siemens GBS — ServiceNow case study Tier 3)
- **AI 시스템 배치**: ✅ My Learning World (사내 LXP, 100K+ 학습) + 별도 AI 채용·이동 포탈
- **배포 환경**: _미공개_
- **연동·통합**: ✅ ServiceNow HR Service Delivery (GBS), Siemens HRIS와 mobility 매칭 sync
- **사용자 접점**: My Learning World web·모바일, internal mobility portal
- **인증·권한**: Siemens 사내 SSO""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 직원 skill profile, 학습 이력, 41 capability, role·position
- **데이터 규모**: ⚠️ 자사 보고: 300K 직원, 100K+ 학습 기회
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_ — 매칭 알고리즘 공식 미명시 (AIHR caveat)
- **데이터 거버넌스**: _미공개_ — EU GDPR (Siemens HQ 독일)
- **민감정보 처리**: _미공개_""",
        d="""### D. Model (R9 research)

- **Foundation model**: _미공개_ — AI 채용·이동 포탈 모델 미공개
- **모델 유형**: predictive (recommendation·ranking)
- **제공 방식**: ✅ 일부 ServiceNow (GBS), 일부 Siemens 자체
- **커스터마이징 기법**: ✅ 41 capability 자체 정의 → matching engine 주입
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: _미공개_""",
    ),
    "sk-hynix-ask-ai-interview": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: SK하이닉스 사내 채용 (구체 _미공개_)
- **AI 시스템 배치**: ✅ A!SK 영상면접 platform — 자체 또는 vendor 여부 _미공개_
- **배포 환경**: _미공개_ — SK 그룹 클라우드 추정
- **연동·통합**: ✅ 7-phase 채용 플로우 — 서류·SKCT·A!SK·peer review·종합 Report·대면 통합
- **사용자 접점**: 지원자 영상 녹화 web/모바일 + 미래 동료 peer review interface + HR/면접관 종합 Report dashboard
- **인증·권한**: ✅ 사내 SSO (peer·HR·면접관 RBAC) + 지원자 별도 인증""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 자기소개서, SKCT 결과, AI 면접 영상, JD-역량 매칭, (고도화) 석박사 Lab·논문 + LinkedIn 코멘트 자동 크롤링
- **데이터 규모**: _미공개_ — 2025 하반기 신입 응시자 비공개
- **전처리·정제**: _미공개_ — 영상 STT 기반 실시간 평가 (향후 고도화)
- **학습 vs RAG vs In-context**: _미공개_ — AI 종합 역량 Report 생성은 LLM 기반 추정
- **데이터 거버넌스**: ✅ AI single decision 회피 (peer + HR + 면접관 hybrid) — KR AI 기본법 인적감독 best practice
- **민감정보 처리**: ⚠️ AI 영상 분석의 표정·억양·외모 신호 사용 여부 _미공개_""",
        d="""### D. Model (R9 research)

- **Foundation model**: _미공개_ — 자체 LLM 또는 그룹 표준 (A.X 가능성) 미명시
- **모델 유형**: ✅ generative (Report 자동 생성·맞춤 질문) + classifier (역량-JD 매칭율) + STT (향후)
- **제공 방식**: ✅ SK하이닉스 internal build
- **커스터마이징 기법**: ✅ 직무별 문제은행, JD-역량 매칭 rule, AI 면접 + 대면 면접 결과 교차 검증
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: ✅ peer + HR + 면접관 hybrid (AI single decision 회피). 표정·외모 신호 transparency 부족 risk""",
    ),
    "docebo-ai-learning-lazboy": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: La-Z-Boy 측 _미공개_ — Docebo는 stand-alone LMS/LXP
- **AI 시스템 배치**: ✅ Docebo Learning Suite SaaS (AI-native 전환 중)
- **배포 환경**: _미공개_ — Docebo AWS multi-tenant SaaS 일반
- **연동·통합**: SCORM·xAPI 표준, HRIS SSO, 글로벌 dealer·corporate 통합 카탈로그
- **사용자 접점**: ✅ Docebo web·모바일 — 학습자·instructor·L&D 매니저 dashboard
- **인증·권한**: 기업 SSO + RBAC""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 기존 콘텐츠·정책 문서 (생성 학습용), 직무·완료 이력 (recommendation), VOC·신상품 자료 (La-Z-Boy)
- **데이터 규모**: ✅ Docebo 30M+ 사용자, 3,900+ 고객 / La-Z-Boy 10K+ 글로벌
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: ✅ Project Harmony (neural search — embedding). Dynamic content generation은 LLM (구체 _미공개_)
- **데이터 거버넌스**: _미공개_
- **민감정보 처리**: _미공개_""",
        d="""### D. Model (R9 research)

- **Foundation model**: _미공개_ — Docebo AI 핵심 underlying model 비공개
- **모델 유형**: ✅ generative (content·virtual coach) + embedding (neural search) + recommendation
- **제공 방식**: Docebo 자체 통합 (SaaS)
- **커스터마이징 기법**: ✅ Use-case instructional templates, Collaborative content design (AI 보조)
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: ⚠️ SME가 AI 생성 콘텐츠 검토·승인 (HITL) — 자동 quality scoring 미공개""",
    ),
    "ibm-watson-recruitment": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: ✅ IBM Watson Talent suite의 일부 — IBM 자체 HRIS 또는 외부 ATS와 연동
- **AI 시스템 배치**: ✅ IBM 외부 productized SaaS (다수 IBM 고객 도입)
- **배포 환경**: ✅ IBM Cloud (당시 Watson 표준 인프라)
- **연동·통합**: 외부 ATS·HRIS와 API/feed (구체 고객별 상이)
- **사용자 접점**: recruiter web UI — ranked shortlist + supporting factor
- **인증·권한**: 기업 SSO + RBAC""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 정형 (이력서·JD·과거 outcome) + 비정형 (LinkedIn·소셜) + soft trait
- **데이터 규모**: _미공개_ (IBM + 고객사별)
- **전처리·정제**: ✅ gender·race·age·ethnicity 억제 (bias mitigation 내장)
- **학습 vs RAG vs In-context**: ML supervised (과거 채용 outcome 라벨)
- **데이터 거버넌스**: ✅ protected attribute 억제 design — 미국 EEOC·NYC LL144 우선
- **민감정보 처리**: ✅ 디자인 단계부터 보호변수 분리""",
        d="""### D. Model (R9 research)

- **Foundation model**: ✅ IBM Watson NLP + ML classifier (2018 — pre-LLM era)
- **모델 유형**: ✅ predictive (success prediction·ranking) + classifier (적합도)
- **제공 방식**: ✅ IBM 자체 호스팅 (Watson Cloud)
- **커스터마이징 기법**: 과거 채용 데이터 학습, requisition 복잡도 분석
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: ✅ protected attribute 억제. ⚠️ 모델 age (2018) — LLM 시대 후 fit 약화. ⚠️ "soft trait" explainability 부족""",
    ),
    "jpmorgan-goldman-sachs-hr-ai": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: 양사 _미공개_ (JPM·GS 사내 HRIS 비공개)
- **AI 시스템 배치**: ✅ JPM **LLM Suite** (200K+), GS **AI Assistant** (46.5K knowledge worker, 2025-06 firm-wide)
- **배포 환경**: ✅ 양사 firewall 내 사내 portal — 외부 ChatGPT 차단, 사내 audit trail
- **연동·통합**: ⚠️ 자사 보고: 사내 KM·문서·Excel/data 시스템 연결, prompt·response audit trail
- **사용자 접점**: ✅ 양사 web portal — JPM 8회 메이저 업그레이드, GS Developer Copilot·Banker Copilot
- **인증·권한**: 사내 SSO + RBAC + audit log""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 이메일·메모·리서치·피치덱·코드 (knowledge worker 산출물), 사내 정책
- **데이터 규모**: ✅ JPM 200K+, GS 46.5K (10K → 2025-06 전사) + 12K 개발자 GitHub Copilot
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_ — 사내 RAG 추정, architecture 미공개
- **데이터 거버넌스**: ✅ prompt·response audit trail, 컴플라이언스 모니터링, 모델 swap 시 재학습 불필요
- **민감정보 처리**: ✅ firewall 내 — 외부 LLM 차단""",
        d="""### D. Model (R9 research)

- **Foundation model**: ✅ JPM = OpenAI 백엔드 (private gateway). GS = **GPT/Gemini/Claude/OSS 사용자 선택**
- **모델 유형**: LLM (요약·초안·번역·코드)
- **제공 방식**: ✅ 양사 commercial API + private gateway (Azure OpenAI 또는 동등)
- **커스터마이징 기법**: ✅ JPM custom assistant (8회 업그레이드), GS Developer·Banker Copilot domain-specific
- **Orchestration 프레임워크**: _미공개_ — 양사 자체 portal 추상화
- **평가·가드레일**: ✅ 컴플라이언스 audit log + senior reviewer""",
    ),
    "meta-ai-performance-review-mandate": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: Meta 사내 PSC (Performance Summary Cycle) — 자체 (구체 _미공개_)
- **AI 시스템 배치**: ✅ **Metamate** (사내 코딩·업무 어시스턴트) — Llama + GPT-4 hybrid (Fortune 2024-12)
- **배포 환경**: _미공개_ — Meta 자체 인프라 (PyTorch·자체 GPU cluster) 추정
- **연동·통합**: ✅ 코드 commit 시스템 (engineering KPI tracking — agent-assisted % 측정), PSC rubric, People Analytics dashboard
- **사용자 접점**: Metamate IDE plugin·web·내부 도구
- **인증·권한**: Meta 사내 SSO""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 코드 commit history (agent-assisted 비율), 자기 평가·peer review 텍스트, AI 사용 로그
- **데이터 규모**: ✅ Meta 전사 ~70K+ 엔지니어·기술사무직 (정확 인원 미공개)
- **전처리·정제**: _미공개_ — agent-assisted commit 라벨링 방식 미공개
- **학습 vs RAG vs In-context**: _미공개_ — Metamate 내부 architecture 비공개
- **데이터 거버넌스**: ⚠️ rubric 세부 측정 _미공개_ — Zuckerberg/Gale 메모만 공개
- **민감정보 처리**: _미공개_""",
        d="""### D. Model (R9 research)

- **Foundation model**: ✅ **Metamate** — Llama (Meta 자체) + GPT-4 (OpenAI) hybrid
- **모델 유형**: LLM (코딩 어시스턴트·업무 자동화)
- **제공 방식**: ✅ 자체 호스팅 (Llama) + 외부 API (GPT-4)
- **커스터마이징 기법**: _미공개_ — Metamate Meta codebase 학습/RAG 사용 여부 미공개
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: ⚠️ Metamate "at least as good as an intern" (Fortune, 자사 보고)""",
    ),
    "nps-ai-innovation-taskforce": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: 국민연금공단 자체 (구체 _미공개_)
- **AI 시스템 배치**: ✅ 다중 — AI 사원·AI 규정비서·AI 수어 영상안내
- **배포 환경**: _미공개_ — 망분리상 정부 클라우드 또는 on-prem 추정
- **연동·통합**: _미공개_ — 4개 분과 cross-functional
- **사용자 접점**: ✅ 대고객 web/앱 (AI 사원·수어) + 사내 (AI 규정비서)
- **인증·권한**: ✅ 공공기관 보안 표준 + PIPA strict""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 연금·복지·규정 문서, 가입자 상담 이력, 수어 영상 콘텐츠
- **데이터 규모**: ✅ 직원 ~7K, 가입자 5,000만+
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_ — AI 규정비서 RAG 추정 (공식 미명시)
- **데이터 거버넌스**: ✅ CAIO 신설 + AI·혁신 추진단 4개 분과
- **민감정보 처리**: ✅ 5,000만+ 국민 — PIPA strict, KR AI 기본법 (2026-01) 고영향 AI 분류 가능""",
        d="""### D. Model (R9 research)

- **Foundation model**: _미공개_ — 다중 vendor 추정 (수어는 별도)
- **모델 유형**: generative (요약·QA) + multimodal (수어 영상 — sign language video synthesis)
- **제공 방식**: _미공개_
- **커스터마이징 기법**: _미공개_
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: ⚠️ KR AI 기본법 인적감독 의무 — 연금 의사결정 영향 시""",
    ),
    "posco-dx-110-agents-hr": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: 포스코 그룹 사내 HRIS (구체 _미공개_)
- **AI 시스템 배치**: ✅ 포스코DX 자체 — ~110개 AI 에이전트 portfolio
- **배포 환경**: _미공개_ — 포스코 그룹 자체 클라우드 추정
- **연동·통합**: ✅ 계열사 (포스코·홀딩스·이앤씨 등) 공통 활용 설계, 그룹DX전략실 portfolio 거버넌스
- **사용자 접점**: _미공개_ (계열사 사업부 web/desktop 추정)
- **인증·권한**: 그룹 SSO 추정""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 인사·구매·경영분석 도메인 데이터
- **데이터 규모**: ✅ 포스코 그룹 ~30K 직원 사무 영역
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_
- **데이터 거버넌스**: ✅ 그룹DX전략실 + AI·로봇 융합 연구소 cross-functional (2026 조직개편)
- **민감정보 처리**: ⚠️ 인사 영역 KR AI 기본법 고영향 AI 분류 가능""",
        d="""### D. Model (R9 research)

- **Foundation model**: _미공개_ — 자체·외부 혼합 추정
- **모델 유형**: generative + automation (RPA) + classifier
- **제공 방식**: ✅ 포스코DX internal build
- **커스터마이징 기법**: _미공개_
- **Orchestration 프레임워크**: _미공개_ — 110개 quality·일관성 governance framework 미공개
- **평가·가드레일**: ⚠️ "개발 중" (announced) — production 후 검증 필요""",
    ),
    "hyundai-steel-hip-platform": dict(
        b="""### B. System & Infrastructure (R9 research)

- **Core HRIS**: 현대제철 사내 HR·경영지원 (구체 _미공개_)
- **AI 시스템 배치**: ✅ HIP — 사내문서검색 + 경영지원챗봇 (자체 구축)
- **배포 환경**: _미공개_ — 현대제철 자체 클라우드 또는 on-prem
- **연동·통합**: ✅ 사내 매뉴얼·기술·경영 문서 코퍼스 통합
- **사용자 접점**: 사내 web/앱 챗봇 — 직원 자율
- **인증·권한**: 현대제철 사내 SSO""",
        c="""### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 매뉴얼·기술 문서·HR·재무·총무 정책
- **데이터 규모**: ✅ 현대제철 ~12K 직원 — 인덱스 크기 _미공개_
- **전처리·정제**: ✅ RAG indexing (chunking·임베딩 _미공개_)
- **학습 vs RAG vs In-context**: ✅ RAG (사내문서 검색·경영지원 Q&A)
- **데이터 거버넌스**: ⚠️ vendor·모델 _미공개_ — 데이터 주권 검증 필요
- **민감정보 처리**: _미공개_""",
        d="""### D. Model (R9 research)

- **Foundation model**: _미공개_ — KR 자체 LLM (Hyperclova X·EXAONE·A.X) 또는 외부 API 추정
- **모델 유형**: LLM (요약·QA·정보 추출)
- **제공 방식**: _미공개_
- **커스터마이징 기법**: ✅ 사내문서 RAG (도메인 특화)
- **Orchestration 프레임워크**: _미공개_
- **평가·가드레일**: ⚠️ 1년+ 운영 후 effect metric 부재 — quality 모니터링 framework 미공개""",
    ),
}


def update_page(slug, b, c, d):
    fp = UC / f"{slug}.md"
    if not fp.exists():
        print(f"SKIP {slug}: not found")
        return False
    text = fp.read_text(encoding="utf-8")

    # Already has B section?
    if re.search(r"^### B\.", text, re.MULTILINE):
        # Replace existing B/C/D block until next ## heading
        new_block = f"{b}\n\n{c}\n\n{d}\n\n"
        new_text, n = re.subn(
            r"### B\.[^\n]*\n.*?(?=\n## )",
            new_block,
            text,
            count=1,
            flags=re.DOTALL,
        )
        if n == 0:
            print(f"FAIL {slug}: existing B not matched")
            return False
        fp.write_text(new_text, encoding="utf-8")
        print(f"  REPLACED | {slug}")
        return True

    # Insert before ## Impact
    new_block = f"{b}\n\n{c}\n\n{d}\n\n"
    new_text, n = re.subn(r"(\n## Impact)", f"\n{new_block}\\1", text, count=1)
    if n == 0:
        print(f"FAIL {slug}: no '## Impact' anchor")
        return False
    fp.write_text(new_text, encoding="utf-8")
    print(f"  INSERTED | {slug}")
    return True


def main():
    ok, fail = 0, 0
    for slug, sec in ENH.items():
        if update_page(slug, sec["b"], sec["c"], sec["d"]):
            ok += 1
        else:
            fail += 1
    print(f"\nR9 applied: {ok}/{len(ENH)}")


if __name__ == "__main__":
    main()
