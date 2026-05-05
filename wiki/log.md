# HR AI Benchmark — Operation Log

Append-only. 모든 ingest/query/lint/digest 오퍼레이션이 여기에 기록됩니다.
기존 엔트리는 절대 수정·삭제하지 않습니다. grep 가능한 고정 포맷을 유지합니다.

Format: `## [YYYY-MM-DD] <operation> | <one-line description>`

---

## [2026-05-05] depth-expansion | 라운드 6 — 기업별 use case depth 보강 (사용자 피드백: "IBM 1건만 있는데 실제 많음") | new: 24 usecases + 3 sources + 6 companies

### 컨텍스트
사용자 피드백: "전체적으로 use case들에 대한 정보 depth가 너무 얕은거같아. 예를 들어 IBM의 경우 리서치 간단히만 해도 AI 적용 use case가 엄청 많거든."

### Audit 결과 (라운드 시작 시)
- 81 → 86 use cases (라운드 5 직후)
- IBM 1건, Microsoft 1건, JPMorgan 1건, Walmart 1건, Cisco 0건, Accenture 1건, Deloitte 1건 (모두 depth 부족)

### 작업 범위
1. **3개 background research agent 병렬 실행** (IBM 심화 / US large 7개사 / Korean conglomerate)
2. 결과 종합:
   - IBM 10건 신규 발굴
   - US large 25건 신규 (Microsoft 4·JPMorgan 4·Cisco 4·Accenture 3·Walmart 3·Deloitte 3·Amazon 4)
   - Korea 17건 신규 발굴
3. **Tier A 우선순위 24건 ingest** (KR 컨설팅 가치 높은 것 위주)

### 신규 use case (24건)

#### IBM (6건, 기존 1 → 7)
| Use case | Category | Confidence |
|---|---|---|
| [[ibm-blue-match-internal-mobility]] | Onboarding/Internal Mobility | 0.55 |
| [[ibm-predictive-attrition-comp-ai]] | Strategic Workforce/People Analytics | 0.50 |
| [[ibm-watsonx-orchestrate-ta-agent]] | Talent Acquisition/Sourcing | 0.45 |
| [[ibm-charlie-learning-ops-agent]] | L&D/Content & Delivery | **0.65** |
| [[ibm-watson-recruitment]] | Talent Acquisition/Screening | 0.40 |
| [[ibm-hr-workforce-reduction-agentic]] | Strategic Workforce/Workforce Planning | **0.65** |

#### US large (10건)
| Use case | Company | Confidence |
|---|---|---|
| [[jpmorgan-llm-suite-redeployment]] | JPMorgan | **0.70** |
| [[jpmorgan-ai-made-easy-upskilling]] | JPMorgan | 0.60 |
| [[accenture-mass-genai-reskilling]] | Accenture | **0.75 (최고)** |
| [[cisco-ai-workforce-consortium-skills-evolution]] | Cisco-led consortium | **0.70** |
| [[cisco-ai-assistant-hr-agentic]] | Cisco | 0.65 |
| [[microsoft-people-skills-inferred-ontology]] | Microsoft | 0.65 |
| [[microsoft-viva-glint-copilot-sentiment]] | Microsoft | 0.55 |
| [[amazon-connections-daily-pulse]] | Amazon | 0.60 |
| [[walmart-openai-certification]] | Walmart | 0.65 |
| [[deloitte-zora-ai-hc-suite]] | Deloitte | 0.65 |

#### Korean conglomerate (8건)
| Use case | 기업 | Confidence |
|---|---|---|
| [[shinhan-bank-ai-one-platform]] | 신한은행 | 0.50 |
| [[kb-bank-ai-hr-deep-change]] | KB국민은행 | **0.55** |
| [[sk-cc-adot-biz-hr-recruitment]] | SK C&C | 0.50 |
| [[sk-group-aibiz-25-companies]] | SK 그룹 25개사 | 0.50 |
| [[sk-hynix-ask-ai-interview]] | SK하이닉스 | 0.45 |
| [[korea-electric-power-hr-bot]] | 한국전력 | 0.45 |
| [[mirae-asset-ai-assistant-platform]] | 미래에셋증권 | 0.45 |
| [[jobkorea-hiring-center-talent-agent]] | 잡코리아 | 0.45 |

### 신규 sources (3건, multi-source compilation)
- [[ibm-hr-ai-portfolio-2025-2026]] — IBM 10건 portfolio (Tier 2+3 통합)
- [[us-large-enterprise-hr-ai-2025-2026]] — Microsoft·JPMorgan·Cisco·Accenture·Walmart·Deloitte·Amazon
- [[korea-conglomerate-hr-ai-2025-2026]] — 신한·KB·SK·한전·미래에셋·잡코리아 등

### 신규 companies (6건)
- [[microsoft]], [[cisco]], [[accenture]] (US large)
- [[shinhan-bank]], [[kb-bank]], [[sk-hynix]] (Korean)

### 라운드 종료 상태
- Use cases: 86 → **110** (+24, +28%)
- Sources: 56 → **59** (+3, multi-source compilation)
- Companies: 14 → **20** (+6)
- Vendors: 13 (변경 없음)
- Syntheses: 10 (변경 없음)

### 카테고리 depth 강화
- IBM: 1 → 7건 (Talent Acquisition·Onboarding·L&D·Performance·Total Rewards·Strategic Workforce 6 카테고리 cover)
- JPMorgan: 1 → 3건
- Cisco: 0 → 2건
- Microsoft: 1 → 3건
- Accenture: 1 → 2건
- 신한: 1 → 2건 (AI ONE + AI 인사 algorithm 기존)
- SK 그룹: 1 → 4건 (AICT 기존 + SK C&C + SK 그룹 25 + SK하이닉스)

### 미ingest items (Tier B, 후속 라운드 후보 — 23건)
- IBM Watson Career Coach, AI JD generation 단독 페이지 (이번 라운드는 watsonx Orchestrate TA에 통합)
- Microsoft Connects+AI fluency criterion (Tier 4 sourcing 약함)
- Microsoft Copilot Impact Survey
- Amazon AI candidate matching·AWR·GenAI resume builder (3건)
- JPMorgan ML candidate sourcing patent
- Walmart Me@Walmart device·Skills-First hiring
- Cisco Entry-level redesign·Redeployment pilot
- Accenture myConcerto·myWizard
- Deloitte job-title modernization
- 신한카드 AINa, 하나은행 지식챗봇, 신한 AI 정기인사, 마이다스 inAIR 신규 4 customer (기아·GS리테일·LIG넥스원·CJ Fits), 사람인 커리어 매칭 에이전트, 삼성SDS Brity Copilot HCM 통합 계획

### Hallucination self-check
- 모든 신규 use case: source citation 필수 frontmatter
- ⚠️ 자사 보고 / ⚠️ 벤더 주장 접두사 metric에 일관 적용
- 미공개 항목은 `_미공개_` 명시 — 추측·일반론 금지

### 신규 ingest 후 HTML 산출물
- `python scripts/extract_v3.py && python scripts/build_html_v6.py` 재실행 → wiki/exports/hr-ai-usecase-collection.html 갱신 (~110 use case 반영)

---

## [2026-05-05] refresh | 라운드 5 — 신규 리서치 + 5건 ingest + infrastructure 동기화 + HTML 재빌드 | new: 5 usecases + 5 sources

### 컨텍스트
4월 12~13일 빅뱅 라운드 후 약 3주 경과. 그동안 발표된 신규 HR AI 사례를 리서치하여 wiki에 통합하는 정기 refresh.

### 작업 범위
1. **현재 상태 점검** (라운드 시작 시): 81 use cases · 51 sources · 14 companies · 13 vendors · 10 syntheses
2. **신규 리서치** (background agent, 2026-Q1~Q2): WebSearch로 12건 신규 발견 — 5건 ingest, 7건 secondary log entry
3. **Infrastructure 동기화**: guide.md §12 스냅샷 + 4-2 카운트 갱신, MEMORY.md 갱신, HTML export pipeline memory 추가
4. **HTML 산출물 재빌드**: `python scripts/extract_v3.py && python scripts/build_html_v6.py`

### 신규 ingest (5 use cases + 5 sources)

| Use case | Category | Source(s) | Confidence | KR consulting 가치 |
|---|---|---|---|---|
| [[workday-agent-system-of-record-asor]] | Strategic Workforce & Gov / HR Tech Gov | Workday blog (T3) + Deloitte 2026 (T1 보강) | 0.50 | AI 거버넌스 첫 상용 reference architecture, EU·KR dual compliance |
| [[workday-sana-for-workday-lms]] | L&D / Content & Delivery | HR Brew (T2) + Workday blog | 0.45 | 한국 LMS 교체 사이클(7~10년) 직격, 삼성멀티캠퍼스 등 비교 |
| [[sap-successfactors-1h-2026-joule-agents]] | EX & HR Ops / Self-service (multi) | SAP News (T3) + Bersin (T1) | 0.50 | SAP HCM 점유 KR 제조 대기업(현대·포스코·한화) 직격 |
| [[korea-ai-basic-act-hr-compliance]] | Strategic Workforce & Gov / Compliance | 법령(T1) + 김앤장 분석(T2) | 0.65 | 모든 KR HR AI 프로젝트 legal foundation |
| [[deloitte-2026-human-capital-trends-meta]] | Strategic Workforce & Gov / HR Tech Gov | Deloitte Insights (T1) | 0.55 | 모든 제안서 1page 공통 reference, "60% vs 5%" 갭 |

### Secondary signals (벤더 페이지 update 또는 후속 라운드 ingest 후보 — 7건)

1. **Oracle Fusion Workforce Operations Agentic App** (2026-03-24, Oracle AI World London): Workforce Ops Agent · Team Sync Advisor · Talent Advisor. Oracle HCM 도입 KR 기업(LG에너지솔루션·CJ제일제당) 대상.
2. **Eightfold AI Interviewer + Interview Companion** (2026-04-08): technical/coding interview 자동화 + human-led 면접 실시간 보조. 1.6B career trajectory 학습 주장. KR 대졸 정기공채(3월·9월) 시즌 후보.
3. **Salesforce Agentforce for HR Service** (2026-Q1 rollout): Salesforce 자체 96% deflection ⚠️ 자사 보고. Slack/Employee Portal 임베드. 네이버·카카오·쿠팡 fit.
4. **ServiceNow HR Business Partner Hub** (2026): turnover spike 자동 감지·action plan 자동 작성. 11M autonomous resolution/년 익명 OTA 고객 인용. SK하이닉스 등 ServiceNow ITSM 도입사 확장 어젠다.
5. **Visier Workforce AI 차세대 + Glean MCP Connection** (2026-05): 2M+ user 위 next-action 추천. MCP 채택은 agentic interop 화두.
6. **Anthropic Claude Enterprise — HR plugin marketplace** (2026-02): Rakuten 1주 내 부서별 agent 배포. KT/SKT/네이버 자체 LLM 전략과 비교 분석 자료.
7. **Bersin Galileo Mars Release + "Superagents will radically change HR"** (Jan/Mar 2026): "HR 30% staff 감축 가능" 예측, Galileo가 Workday 등과 fully programmable agent화.

### 보너스 신호 (log-only)
- Lattice Spring/Summer 2026 (May): AI Agent 사이드바 임베드, evidence-based AI Reviews
- EU AI Act high-risk 의무 2026-08-02 발효 예정 (Omnibus 연기안 진행 중)
- Meta Zuckerberg AI avatar for employee comms (Apr 21) — HR risk 사례 caution slide
- Gartner Oct 2025 — Top 4 TA Trends for 2026 ("AI Revolution and Cost Pressures")

### 라운드 종료 상태
- Use cases: 81 → **86** (+5)
- Sources: 51 → **56** (+5)
- Companies/Vendors: 변경 없음 (신규 use case는 multi-customer 또는 정부 규제 카테고리)
- Syntheses: 10 (변경 없음)
- 평균 confidence: 0.36 → **0.37** (5건 평균 0.53으로 상향 보정)
- Strategic Workforce & Gov 카테고리: +3건 강화 (HR Tech Gov 어젠다 보강)
- 한국 region: 11건 → 11건 (KR-specific use case 1건 추가 — Korea AI Basic Act는 region:[kr])

### 파일 수 변경 후 검증
- `ls wiki/usecases/ | wc -l` → 86 (예상값)
- `ls wiki/sources/ | wc -l` → 56 (예상값)

### 산출물 파이프라인 (이번 라운드 재실행)
- `scripts/extract_v3.py` — wiki markdown → JSON
- `scripts/build_html_v6.py` — JSON → `wiki/exports/hr-ai-usecase-collection.html` (~250KB)
- 가이드: `wiki/guide-html-export.md`

---

## [2026-04-12] gap-research | 3개 갭 카테고리 web search 리서치 (Performance·Total Rewards·Korea) | new: 10 usecases + 9 sources | touched: index + log

### 갭 리서치 목표 vs 결과

| 갭 | 목표 | 확보 케이스 | 신규 wiki 페이지 |
|---|---|---|---|
| GAP1 Performance & Talent Mgmt (4→10건) | +4~6건 | 15Five/Kona(ReUp), Culture Amp AI Coach(Asana), SAP Joule P&G Agent, Betterworks NextGen(Colgate), Lattice AI Summarization(Ruggable), Workday Illuminate Perf Agent | 6 usecases |
| GAP2 Total Rewards (5→8건) | +3~5건 | Spring Health/General Mills(EAP 1%→26%), UKG AI Scheduling(KC CARE 92%, Jetro $2.2M), Paychex/Paycor Agentic WFM(800K) | 3 usecases |
| GAP3 한국 L&D·EX 사례 | +2건 | 삼성 멀티캠퍼스 CIC(AI 추천), 플렉스 flex(6만 기업, AI 에이전트 계획) | 2 usecases |

### 신규 생성 파일

**use cases (10건)**:
- [[15five-kona-reup-ai-manager-coaching]] (0.25, Perf/Coaching)
- [[cultureamp-ai-coach-asana]] (0.30, Perf/Coaching)
- [[sap-joule-performance-goals-agent]] (0.45, Perf/Goal & Performance)
- [[betterworks-nextgen-ai-performance]] (0.25, Perf/Goal & Performance)
- [[lattice-ai-performance-summarization]] (0.25, Perf/Goal & Performance)
- [[workday-illuminate-performance-review-agent]] (0.40, Perf/Goal & Performance)
- [[spring-health-general-mills-ai-eap]] (0.30, Total Rewards/Benefits & Wellbeing)
- [[ukg-ai-workforce-scheduling-healthcare]] (0.30, Total Rewards/Benefits & Wellbeing)
- [[paychex-flex-agentic-workforce]] (0.20, Total Rewards/Payroll Operations)
- [[flex-korea-hr-ai-saas]] (0.25, EX & HR Ops/Core HR)

**sources (9건)**:
- sources/15five-kona-launch-2025-05.md (Tier 3)
- sources/cultureamp-ai-coach-expansion-2025-10.md (Tier 3)
- sources/sap-joule-performance-agent-bersin-2025-10.md (Tier 1, Josh Bersin)
- sources/spring-health-general-mills-case.md (Tier 3)
- sources/ukg-healthcare-scheduling-2026-02.md (Tier 3)
- sources/paychex-agentic-workforce-2026-02.md (Tier 3)
- sources/flex-korea-hr-saas-2025.md (Tier 4)
- sources/betterworks-nextgen-2026-01.md (Tier 3)
- sources/lattice-ai-performance-features-2025.md (Tier 3)

### Solution Architecture 품질 리포트
- SAP Joule: Fact 3/5 (Tier 1 Bersin 소스), 미공개 2/5
- Spring Health/General Mills: Fact 3/5, metric-rich (Before/After 정량)
- UKG Scheduling: Fact 3/5, 다수 고객 수치
- 나머지 7건: Fact 1~2/5, 미공개 3~4/5 (stub~draft)

---

## [2026-04-12] ingest | Confidence boost: 7개 use case 대상 Tier 1·2 독립 소스 탐색·추가 | new: 10 sources | touched: 7 usecases

### 목표
기존 use case의 confidence를 독립 Tier 1·2 소스 추가로 향상 (평균 0.35 → 0.45+ 목표)

### 결과

| Use Case | Before | After | 추가 소스 | 핵심 발견 |
|---|---|---|---|---|
| Chipotle Paradox Olivia | 0.35 | **0.55** | HR Dive (T2), CNBC (T2) | CNBC에서 12일→3.5일, completion 50%→85% 신규 metric 확인 |
| SK Group AICT | 0.25 | **0.40** | 서울경제 등 7개+ 한국 경제지 (T2) | '에이닷 비즈 HR' 명칭, 4시간 분석, 이틀 결과발표 |
| BetterUp Twilio | 0.35 | **0.45** | Bersin (T1, COI 할인), HR Executive (T2) | Bersin이 BetterUp advisor — COI 있으나 독립 분석 가치 |
| Schneider Electric Gloat | 0.35 | **0.50** | Bersin (T1, 2019 stale 할인), SHRM (T2) | 47% 퇴직 사유, 75%→89% 등록률, Charise Le CHRO |
| Docebo La-Z-Boy | 0.30 | **0.40** | Bersin L&D Revolution (T1, 기존 source 연결) | Docebo 플랫폼 AI 기능 독립 확인, La-Z-Boy 구체 metric은 여전히 벤더 주장 |
| Walmart Ask Sam | 0.45 | **0.55** | SHRM (T2), HR Dive (T2) | SHRM AI+HI 시리즈 독립 분석, Maren Waggoner CPO 인터뷰 |
| Siemens Reskilling | 0.35 | **0.45** | WEF Reskilling Revolution (T1) | WEF 공식 사례 기업 선정, blended funding model, 정부 co-financing 25% |

**평균 confidence 변화**: 0.34 → **0.47** (목표 0.45 달성)

### 신규 소스 파일 (10건)
- `sources/hrdive-chipotle-paradox-2024-10.md` (T2)
- `sources/cnbc-chipotle-ava-cado-2025-07.md` (T2)
- `sources/sedaily-sk-cc-adot-biz-hr-2025-02.md` (T2)
- `sources/shrm-schneider-electric-chro-nontraditional-2025.md` (T2)
- `sources/bersin-schneider-unilever-talent-marketplace-2019-07.md` (T1)
- `sources/shrm-walmart-ai-revolution-2025.md` (T2)
- `sources/hrdive-walmart-my-assistant-genai-2024.md` (T2)
- `sources/wef-siemens-reskilling-revolution-case.md` (T1)
- `sources/bersin-betterup-manage-ai-coaching-2024-04.md` (T1, COI)
- `sources/hrexecutive-bersin-coaching-disruptions-2024.md` (T2)

### 주의사항
- Bersin은 BetterUp advisor + Gloat 협업 이력 — COI 명시하고 confidence 기여도 할인 적용
- 한국 경제지 보도(SK)는 보도자료 전달 성격 강하나 Tier 2 매체의 독립 채널 확인 가치
- CNBC Chipotle 기사에서 기존 PR에 없던 신규 metric(12일→3.5일, 50%→85%) 발견 — 가장 높은 부가가치

---

## [2026-04-12] gap-research | 7개 갭 카테고리 web search 리서치 (30+ 케이스 탐지) | new: 8 usecases + 11 sources | touched: 20 pages

### 갭 리서치 목표 vs 결과

| 갭 | 목표 | 확보 케이스 | 신규 wiki 페이지 |
|---|---|---|---|
| GAP1 온보딩 | 2건 → 확대 | Hitachi/Ema (+4일 단축), Zapier/Enboarder (206k분), Enboarder 집계 | 2 usecases |
| GAP2 L&D | 2건 → 확대 | Ericsson/Degreed (3만명), Toshiba/Copilot (10k명·5.6h), Mitsubishi/360L, Bayer·Ericsson/Maestro | 2 usecases (+ 2 sources) |
| GAP3 Total Rewards | 3건 → 확대 | ADP Assist (이상탐지·30분/사이클), UKG WIH, Dayforce AI WFM | 1 usecase + 2 sources |
| GAP4 EX/Listening | 얇음 → 보강 | Coca-Cola SW/Perceptyx (+24pp), adidas/Qualtrics (-160h), Iowa/Qualtrics (+20%), Emerson/Perceptyx (+12pp), BDR Thermea/Workday Peakon | 1 usecase + 2 sources |
| GAP5 Strategic WF | 2건 → 확대 | Tampa General/Visier (-70% 에이전시), Salesforce/Orgvue (6개월→6일), Docusign/Visier (+75%), Anaplan 헬스케어 $21M | 2 usecases + 2 sources |
| GAP6 DEI AI | 없음 → 신규 | T-Mobile/Textio (+17% 여성), Duolingo/Textio (Score 54→90), Hired/Holistic AI LL144 | 1 usecase + 1 source |
| GAP7 AI 거버넌스/컴플라이언스 | 없음 → 신규 | Allegis/Holistic AI (500~600 AI 발견, 고위험 -50%), NYC LL144 집행 감사(2025-12), EU AI Act HR 타임라인 | 1 usecase (포함 source) |

### 신규 생성 파일

**use cases (8건)**:
- [[hitachi-ema-agentic-hr-onboarding]] (0.35, Onboarding)
- [[zapier-enboarder-ai-onboarding]] (0.30, Onboarding)
- [[ericsson-degreed-ai-skills-upskilling]] (0.25, L&D)
- [[toshiba-microsoft-copilot-viva]] (0.35, L&D/EX)
- [[adp-assist-payroll-ai]] (0.30, Total Rewards)
- [[coca-cola-southwest-perceptyx-activate]] (0.35, EX/Listening)
- [[tampa-general-visier-people-analytics]] (0.40, Strategic WF/Analytics)
- [[salesforce-orgvue-org-design-ai]] (0.25, Strategic WF/Org Design)
- [[allegis-group-holistic-ai-governance]] (0.25, Governance)
- [[t-mobile-textio-dei-hiring]] (0.35, DEI)

**sources (11건)**:
- [[ema-hitachi-agentic-hr-2025]] (Tier 2/3)
- [[enboarder-zapier-onboarding-2022]] (Tier 4)
- [[perceptyx-ex-impact-awards-2025]] (Tier 2)
- [[qualtrics-ai-enterprise-adoption-2025]] (Tier 2)
- [[visier-outsmart-2025-customers]] (Tier 2)
- [[holistic-ai-allegis-bias-audit-2025]] (Tier 3)
- [[orgvue-salesforce-henshaw-ai-2025]] (Tier 3)
- [[degreed-ericsson-lens-2025]] (Tier 3)
- [[360learning-mitsubishi-electric-case-2024]] (Tier 3)
- [[toshiba-microsoft-viva-copilot-2025]] (Tier 3)
- [[textio-tmobile-duolingo-dei-2025]] (Tier 3)
- [[adp-assist-innovation-day-2025]] (Tier 2)
- [[ukg-workforce-intelligence-hub-2025]] (Tier 3)
- [[anaplan-workforce-planning-ai-2025]] (Tier 3)

### Solution Architecture 품질 리포트

| use case | Fact 채움 | 미공개 | 상태 |
|---|---|---|---|
| hitachi-ema-agentic-hr-onboarding | A·B·E (3/5) | C·D | near-stub |
| zapier-enboarder-ai-onboarding | A·B·E (3/5) | C·D | near-stub |
| ericsson-degreed-ai-skills-upskilling | A·E (2/5) | B·C·D | stub |
| toshiba-microsoft-copilot-viva | A·B·D·E (4/5) | C 일부 | fact-rich |
| adp-assist-payroll-ai | A·B·E (3/5) | C·D 일부 | near-stub |
| coca-cola-southwest-perceptyx-activate | A·B·E (3/5) | C·D | near-stub |
| tampa-general-visier-people-analytics | A·B·E (3/5) | C·D | near-stub |
| salesforce-orgvue-org-design-ai | A·C (2/5) | B·D·E | stub |
| allegis-group-holistic-ai-governance | A·B·C·E (4/5) | D | fact-rich |
| t-mobile-textio-dei-hiring | A·B·C·E (4/5) | D | fact-rich |

### 리서치 중 발견된 추가 조사 대상 (미wiki화)

- **아직 페이지 없는 고품질 케이스**: Mitsubishi Electric/360Learning, Docusign/Visier, adidas/Qualtrics, Emerson/Perceptyx, BDR Thermea/Workday Peakon, Coca-Cola Southwest 2026 Candler Cup
- **Anaplan 헬스케어 $21M**: 기업명 미공개 → 소스만 저장
- **NYC LL144 집행 감사**: 규제 컨텍스트 페이지화 권고 (Allegis use case에 포함)
- **Culture Amp**: AI Coach 출시 (2025) — stub 페이지 생성 권고
- **Cornerstone Galaxy**: 7,000 고객·140M 사용자 — stub 권고
- **Degreed Maestro**: HR Executive 2025 Top Product 수상 — Ericsson 소스에 포함

## [2026-04-12] ingest | 업종별·지역별 HR AI 리서치 Batch A-D | touched: 21 pages | new: 12 usecases | contradictions: 1 (resolved)
- **신규 use case (12건)**:
  - **금융**: [[jpmorgan-llm-suite-employee-productivity]] (0.55, na), [[goldman-sachs-gs-ai-assistant]] (0.50, na), [[lloyds-banking-workday-genai-hr]] (0.55, eu)
  - **제조/독일**: [[bosch-rob-hr-ai-assistant]] (0.50, global), [[siemens-servicenow-hr-gbs]] (0.55, eu)
  - **일본/APAC**: [[hitachi-skye-hr-ai-assistant]] (0.40, apac), [[fujitsu-hr-ai-skills-career]] (0.40, apac)
  - **싱가포르**: [[dbs-bank-hr-ai-talent-analytics]] (0.50, apac)
  - **호주**: [[commonwealth-bank-ai-workforce]] (0.55, apac) — ⚠️ contradiction resolved: AI 챗봇 45명 대체 결정 후 번복
  - **의료**: [[mercy-health-ai-nursing-workforce]] (0.55, na) — 계약직 25%→8%, $30M 절감
  - **리테일**: [[walmart-ai-frontline-workforce]] (0.55, na) — OpenAI 파트너십, 1.5M 직원 AI 도구
  - **글로벌 L&D**: [[tcs-infosys-ai-reskilling-india]] (0.45, apac) — 100만명+ 리스킬링
  - **Novartis**: [[novartis-gloat-skills-marketplace]] (0.45, eu) — Gloat, 이동성 132%↑
  - **🇰🇷 국내**: [[korea-gov-ai-hr-public-sector]] (0.35, kr), [[greetinghr-ats-ai-korea]] (0.30, kr), [[clap-ai-performance-korea]] (0.30, kr), [[lotte-job-based-hr-reform]] (0.35, kr)
- **소스 방법**: Web search 20회+ (배치 A~D 병렬 검색)
- **이번 세션 이후 누적 use case 수**: ~35건 (이전 23건 + 신규 12건)
- **solution architecture 품질**: fact 충실 9건 / stub 수준 3건 (Hitachi·한국공공·CLAP — 소스 수 제한)
- **contradiction**: CBA AI 챗봇 45명 대체 발표→번복 사건 resolved로 기록

## [2026-04-12] massive-ingest | 대대적 리서치 wave 2+3 | new: 23 usecases → total 58
- J&J MIT CISR (conf 0.60, wiki 최고 학술), Meta AI 성과평가 의무화, HSBC multi-vendor, Deloitte Claude 470k, Beamery 467% ROI, Textio DEI, McDonald's/Paradox, Cathay Pacific/HireVue, Emirates/HireVue, Qualtrics/adidas, Fuel50/Lennox, PwC 65k upskilling, Walmart 900k Ask Sam, Amazon PXT 15%↓, Phenom/Merck 36k, HireVue bias audit 134% ROI, JPMorgan/Goldman, Accenture L&D, Siemens 300k, Nestlé/Paradox, Deloitte WF Analyzer/Salesforce + others

## [2026-04-12] bootstrap | HR AI Benchmark wiki 초기 스캐폴딩 (CLAUDE.md, index, log, slash commands)
- Taxonomy: 7 대그룹 / 26 중그룹 / 80+ 소그룹 확정
- Source tiers: 4-tier whitelist (Gartner·McKinsey·Deloitte·Bersin + AIHR·HR Brew + 주요 HR tech vendors + 실사례 신호)
- Consumption: Obsidian + Dataview (주), MkDocs Material (부, 클라이언트 공유용)
- Next: 첫 소스 ingest + scripts/fetch_sources.ps1 작성

## [2026-04-12] schema-update | Solution Architecture 섹션 대폭 확장 + 3중 hallucination 가드레일
- Use case 템플릿 §3: Solution Architecture를 A~F 6개 하위 섹션(Process/System/Data/Model/Org/Diagrams)으로 확장
- Ingest protocol §6: "Solution Architecture 작성 — Fact-only 모드" 단계 신설 (금지어·self-check·stub 처리 규칙)
- Lint protocol §7: 점검 항목 9번 신설 (금지어 탐지·벤더 주장 접두사·citation 커버리지·Mermaid 누락)
- 가드레일: 4단계 표기(✅ Fact / ⚠️ 벤더 주장 / ❓ 미공개 / 🚫 금지), 일반론 빈칸 채우기 전면 금지

## [2026-04-12] ingest | Bersin "What Is Workday Illuminate" (2024-09-17) + Workday Illuminate expansion PR (2025-09-16) | touched: 5 pages | new: 2 sources, 1 vendor, 2 usecases | contradictions: 1 (unresolved)
- Source A: [[bersin-workday-illuminate-2024-09]] — Tier 1, Josh Bersin 분석
- Source B: [[workday-illuminate-pr-2025-09]] — Tier 3, Workday 공식 PR
- Vendor: [[workday]] — 신규 생성
- Use case 1: [[workday-illuminate-job-architecture]] — 양 소스 교차, confidence 0.25, LLM 파라미터 수 800B/70B 모순 발견 → contradiction 콜아웃
- Use case 2: [[workday-illuminate-employee-sentiment]] — Tier 3 단독, confidence 0.10, **STUB** 상태
- Quality report: fact-rich usecase 1건 + stub usecase 1건, Mermaid 도식 1개 (job architecture process)

## [2026-04-12] obsidian-setup | .obsidian/ config 준비 + wiki/dashboard.md (Dataview 10개 쿼리)
- Obsidian 설치 후 vault 오픈 확인 (config가 Obsidian에 의해 덮어씀)
- Dashboard 쿼리: low-confidence · stub · stale · 카테고리별 · 벤더별 · 산업별 · stage별 · 최근 ingest · 제안서 quick-pick · 국내 필터 · unresolved contradictions
- Next: fact-rich use case 확보 (Moderna)

## [2026-04-12] lint-fix | C-1 broken wikilinks 4건 수정 + W-1 금지어 5곳 리라이트 + W-4 스키마 업데이트
- C-1: `[[../../CLAUDE...]]` → `[[CLAUDE|CLAUDE.md]]` (moderna-ask-hr-routing, workday-illuminate-employee-sentiment×2, workday-illuminate-job-architecture)
- W-1: 금지어 "추정"(3곳)·"일반적"(1곳)·"통상"(1곳) 모두 "미공개"·"소스 미확인"·"공개되지 않음"으로 리라이트
- W-4: CLAUDE.md §3 Fact/주장 표에 **⚠️ 자사 보고 (customer self-report)** 마커 신규 행 추가, 벤더 주장과의 구분 예시 4개 제공
- W-4: CLAUDE.md §7.9 lint 규칙에도 자사 보고 마커 검사 로직 추가
- 잔여 Critical: 1건 (C-2 Workday LLM 800B/70B contradiction)
- 잔여 Warning: 6건 (W-2 low confidence·W-3 tier imbalance·W-5/6 stale sources — 모두 추가 ingest로 해소)

## [2026-04-12] lint | 2차 전수 점검 (D+E1+E2 이후) | critical: 1, warning: 7, info: 3
- Report: [[lint-2026-04-12-round2]]
- Round 1 대비: critical 5→1, warning 9→7, category coverage 2/7→7/7, KR 0→2, avg confidence 0.33→0.28 (breadth trade-off), stub ratio 33%→10%
- Critical 잔존: C-2 Workday LLM 파라미터 contradiction (해결 우선순위 낮게 유지)
- W-1 금지어 16건 (대부분 disclaimer 병기된 "추정") → 패턴 A/B/C로 분류, 처리 전략 제시
- W-2 평균 confidence 0.28 — 다음 라운드는 depth 보강 목표

## [2026-04-12] lint + synthesis | 3차 lint + 2개 synthesis 생성
- [[lint-2026-04-12-round3]] — 22건 전수 점검. critical 1 (동일), warning 5, info 2. 금지어 21건·날짜형식 8건·avg conf 0.29
- ⭐ [[korean-3-si-hr-ai-comparison]] — 한국 3대 SI + HR tech 벤더 비교. "그룹 SI가 만든다" 패턴, 마이다스아이티 Nature 논문이 유일 학술 검증, 클라이언트별 추천 경로
- ⭐ [[talent-acquisition-6-vendor-comparison]] — 채용 AI 6개 솔루션 비교. 4축(커버리지·autonomy·검증·fit) 분석, 한국 대기업·중견·글로벌 시나리오별 추천
- Syntheses 총계: 3 → **6** (lint 3 + insight 3)

## [2026-04-12] ingest | 부족 카테고리 보강 (I 시리즈) | new: 4 usecases, 1 vendor
- **목표**: Onboarding(1→2), L&D(1→2), Performance(1→2) 보강 + 한국 TA 추가
- **신규 Use Cases** (4건):
  1. [[schneider-electric-gloat-talent-marketplace]] — **2. Onboarding** 보강. $15M+, 360k hours, 50% 퇴직 사유 해소 (0.35)
  2. [[docebo-ai-learning-lazboy]] — **3. L&D** 보강. La-Z-Boy 179% 사용자↑, Disguise 4x learner, 3,900+ 고객 (0.30)
  3. [[betterup-ai-coaching-twilio]] — **4. Performance** 보강. Twilio 32% 성과↑·5x 이탈↓, $4.5M quota 달성 (0.35)
  4. 🇰🇷 [[lgcns-agentic-ai-hr]] — **1. TA (KR)** 추가. LG CNS 에이전틱 AI HR, 26% 생산성↑, **아키텍처 4컴포넌트 공개** (0.25)
- **신규 Vendor**: [[flex-korea]] stub (추가 확인됨: 삼성SDS Brity Copilot 18만+사용자도 발견)
- **Use case 총계**: 18 → **22**
- **카테고리 분포 변화**: Onboarding 1→2, L&D 1→2, Performance 1→2, TA 5→6 (KR)
- **핵심 발견**:
  - Schneider Electric의 **"50% 퇴직 사유"** before data = wiki 전체에서 가장 강력한 before metric
  - BetterUp의 **Twilio 5x 이탈 감소** = coaching 카테고리 최강 ROI 사례
  - LG CNS의 **Knowledge Lake → Hub → Refiner → Router** 아키텍처 = 국내 유일 아키텍처 공개 사례
  - **한국 3대 SI (삼성SDS·LG CNS·SK AX) 모두 HR AI 진출 확인**

## [2026-04-12] ingest | 대대적 리서치 라운드 (H 시리즈) | touched: ~20 pages | new: 8 usecases, 2 vendors
- **목표**: 7개 카테고리 전면 보강, 글로벌+한국 벤더 landscape 확충
- **신규 Use Cases** (8건):
  1. 🇰🇷 [[midas-inair-ai-assessment-korea]] — ⭐ **confidence 0.50 (wiki 2위)**, Nature Scientific Reports 논문 검증, 10+ 한국 대기업·공공기관, 마이다스아이티 inAIR
  2. [[ibm-askhr-watsonx]] — IBM AskHR, 270k 직원·2.1M 대화/년·80+ 태스크, watsonx Orchestrate, confidence 0.45
  3. [[microsoft-employee-self-service-agent]] — Microsoft Viva+Copilot HR, Employee Self-Service Agent 글로벌 rollout, confidence 0.35
  4. [[eightfold-ai-talent-intelligence]] — Eightfold AI Interviewer+Digital Twin, Deloitte 제휴, confidence 0.20
  5. [[syndio-pay-equity-ai]] — Syndio Syndi pay equity, 300+ 고객, EU AI Act 대응, confidence 0.20
  6. [[servicenow-now-assist-hr]] — ServiceNow Now Assist HRSD, ACV $600M, confidence 0.25
  7. [[visier-vee-people-analytics]] — Visier Vee AI + Org Design, Providence 2,000+ caregivers, confidence 0.25
  8. (Flex Korea vendor page stub — use case는 AI 기능 상세 공개 후 생성)
- **신규 Vendors**: [[midas-it]], [[flex-korea]]
- **카테고리 분포**: TA +2건 (Eightfold, Midas), EX +3건 (IBM, MS, ServiceNow), TR +1건 (Syndio), SW +1건 (Visier)
- **핵심 발견**: 마이다스아이티 inAIR의 **Nature 학술 검증**은 wiki 전체에서 가장 높은 독립 검증 수준. IBM AskHR 270k scale은 엔터프라이즈 HR AI 최대 deployment.
- **Use case 총계**: 11 → **19**
- **Vendor 총계**: 11 → **13** (+ Eightfold·Syndio·ServiceNow·Visier는 vendor page 미생성, use case에서 참조)

## [2026-04-12] ingest + update | G 시리즈 (G2+G1+G3+G4) | touched: ~18 pages | new: 4 sources, 4 vendors (Sana Labs·SKT·SAP SuccessFactors·Douzone·2 stubs), 1 usecase; updated: SK Group use case (major), 3 Moderna use cases, F2 synthesis, index, log
- **G2 (missing entities)**:
  - [[sana-labs]] stub — Galileo Learn OEM 파트너 + Workday customer 확인
  - [[skt]] stub — SK AX 합작 파트너
- **G1 (depth boost)**:
  - [[hr-brew-ibm-moderna-2025-06]] 신규 (원문 fetch 실패, summary 기반) — IBM AskHR 270k 직원, Moderna Patel "agentic vision" 인용
  - [[sk-ax-insight-ai-recruitment-2024]] 신규 (직접 fetch) — **조기수 팀장**, **1차 면접 AI 100% 자동화**, **3개 계열사 (SK C&C, SKT, SK 브로드밴드)**, 2025 그룹 확대 + SaaS 대외 확산 계획
  - [[sk-group-aict-ai-recruitment]] 대폭 업데이트: confidence 0.15 → 0.25
  - [[moderna-ask-hr-routing]] 업데이트: 0.65 → 0.70
  - [[moderna-self-review-gpt]] 업데이트: 0.30 → 0.40
  - [[moderna-benefits-equity-gpts]] 업데이트: 0.30 → 0.40
- **G3 (KR category expansion)**:
  - [[taxwatch-douzone-one-ai-2024-12]] 신규 (Tier 2 한국 세무 매체) — 더존비즈온 ONE AI 연말정산 end-to-end 자동화
  - [[douzone-bizon]] 신규 vendor (국내 ERP dominant)
  - [[douzone-one-ai-year-end-tax]] 신규 use case — **5. Total Rewards → Payroll Operations → Year-end Tax Settlement** (한국 특유 영역 최초 수집)
  - **KR region 커버리지**: 2 (Talent Acquisition only) → 3 (Talent Acquisition + Total Rewards)
- **G4 (F2 synthesis counter-evidence)**:
  - [[bersin-successfactors-leapfrog-2024-10]] 신규 (Tier 1) — Delta/Pepsi consolidation 증거
  - [[sap-successfactors]] 신규 vendor — Workday strategic peer
  - [[workday-as-customer-paradox]] §8~§9 대폭 확장 — "Workday vs SuccessFactors" 이분법으로 re-framing, 5~6번째 클라이언트 질문 추가
- **핵심 insight 상승**:
  - F2 synthesis가 "universal Workday 패턴" → "suite 벤더별 전략 이분법"으로 성숙화
  - 평균 confidence 변화 추산: 3개 Moderna 보강 + SK 보강으로 개선, 신규 Douzone·SAP SF 추가 일부 상쇄, 대략 0.28 → 0.33 예상 (다음 lint에서 정확 측정)

## [2026-04-12] synthesis | Workday가 벤더이자 고객인 패러독스 | [[workday-as-customer-paradox]]
- Cross-entity insight: Workday가 Paradox(채용)·Sana/Galileo Learn(L&D)의 customer임을 wiki 데이터로 확인
- 근거: [[paradox-clients-stories-2026-04]] (Workday 2년 23,000시간), [[bersin-ld-revolution-2025-06]] (Workday internal leadership academy)
- 컨설팅 insight: "all-in-one HCM의 한계"에 대한 직접 증거, multi-vendor HR AI stack 정당화
- 3가지 클라이언트 질문 + 한 줄 pull quote 제공
- 한계 고지: sample 2건뿐, Workday 공식 statement 없음, TCO 분석 없음

## [2026-04-12] ingest | E1 + E2 — 기존 use case 보강 + 한국 사례 확보 | touched: ~18 pages | new: 5 sources, 2 vendors, 1 company, 2 usecases; updated 3 existing usecases | contradictions: 0
- **E1 boost sources 신규** (4):
  - [[chipotle-newsroom-ava-cado-2024-10]] — Tier 4, Chipotle 공식 PR (CHRO Eskenazi quote + "Ava Cado" 브랜딩 확보)
  - [[bersin-ld-revolution-2025-06]] — Tier 1 (COI disclosure), Bersin의 Docebo/Sana/Cornerstone 시장 분석, Workday Sana customer 공개
  - [[gloat-unilever-success-story-2024]] — Tier 3, WebSearch summary 기반 (원문 직접 fetch 필요), Unilever 2024 update metric 확보
  - (IBM/Moderna HR Brew 2025-06 = research only, 미수집)
- **E1 use cases 업데이트**:
  - [[chipotle-paradox-olivia]]: confidence 0.10 → **0.35**, "Ava Cado" 이름·CHRO quote·다국어 확인
  - [[unilever-flex-gloat-talent-marketplace]]: confidence 0.05 → **0.25**, last_confirmed 2019 → 2024, 65k users·41% 생산성 수치 추가
  - [[bersin-galileo-learn-ai-native-lms]]: confidence 0.10 → **0.25**, Workday 외부 customer 확인, 시장 포지션 표 추가
- **E2 한국 사례 신규** (2 sources, 2 vendors, 1 company, 2 usecases):
  - Sources: [[sk-ax-ai-recruitment-service-2024]], [[aitimes-wantedlab-recruiting-agent-2025-10]]
  - Vendors: [[sk-ax]], [[wantedlab]]
  - Company: [[sk-group]]
  - Use cases:
    - [[sk-group-aict-ai-recruitment]] — 1. Talent Acquisition, KR region, **AICT (AI Competency Test)** concept, 2024 하반기 신입 공채, confidence 0.15
    - [[wantedlab-ai-recruiting-agent]] — 1. Talent Acquisition, KR region, 2025-10 출시 LLM 에이전트, confidence 0.20
- **KR region 커버리지**: 0 → **2건** (I-3 info item 부분 해결)
- **평균 confidence**: 0.25 → **0.29** (소폭 상승, 신규도 여전히 Tier 3 위주지만 기존 3건 upgrade)

## [2026-04-12] ingest | D 단계 — 5개 빈 카테고리 채우기 | touched: 16 pages | new: 4 sources, 3 vendors, 2 companies, 5 usecases | contradictions: 0
- **Source A**: [[hr-brew-moderna-total-rewards-2025-05]] — Tier 2 (WebSearch summary 기반, 직접 fetch 차단)
- **Source B**: [[paradox-clients-stories-2026-04]] — Tier 3, Paradox 공식 고객 페이지 (40+ 고객 fetched)
- **Source C**: [[i4cp-unilever-flex-2019-12]] — Tier 2, 매우 stale (76개월)
- **Source D**: [[bersin-galileo-learn-2025-05]] — Tier 3 (⚠ Bersin의 벤더 역할, 독립 분석 아님)
- **Vendors 신규**: [[paradox]], [[gloat]], [[josh-bersin-co]]
- **Companies 신규**: [[unilever]], [[chipotle]]
- **Use cases 신규** (5개, 빈 카테고리 각 1건):
  1. 1. Talent Acquisition: [[chipotle-paradox-olivia]] — confidence 0.10, stub 경계
  2. 2. Onboarding & Transitions: [[unilever-flex-gloat-talent-marketplace]] — confidence 0.05 (stale penalty)
  3. 3. Learning & Development: [[bersin-galileo-learn-ai-native-lms]] — confidence 0.10
  4. 4. Performance & Talent Mgmt: [[moderna-self-review-gpt]] — confidence 0.30
  5. 5. Total Rewards: [[moderna-benefits-equity-gpts]] — confidence 0.30
- Quality note: 5건 모두 confidence < 0.4로 lint warning 대상. **breadth(5개 카테고리 채움)는 달성했으나 depth(Tier 1·2 교차 검증)는 다음 라운드 과제**.
- 카테고리 커버리지 상승: 2/7 → **7/7** (모든 대그룹에 최소 1건)
- `⚠️ 자사 보고` 마커 적극 활용 (Moderna 케이스 모두)

## [2026-04-12] lint | 첫 전수 점검 | critical: 5, warning: 9, info: 4 | auto-fixable: 4
- Report: [[lint-2026-04-12]]
- Critical 하이라이트:
  - C-1 Broken wikilinks 4건 (`[[../../CLAUDE...]]`) — Obsidian relative path 미지원 → auto-fix 가능
  - C-2 Workday Illuminate LLM 800B/70B contradiction 여전히 unresolved
- Warning 하이라이트:
  - W-1 금지어 5건 탐지 (모두 의도적 불확실성 표시이나 엄격 리라이트 권장)
  - W-4 `⚠️ 자사 보고` 마커가 CLAUDE.md 스키마에 미정의 — 공식화 필요
- Info: 카테고리 커버리지 2/7, 국내(KR) 0건, stub ratio 33%
- Health: Avg confidence 0.33, 카테고리 커버리지 29%

## [2026-04-12] ingest | Moderna Ask HR routing case (Unleash 2025-06-27 + Constellation 2024-04-24 + Moderna blog 2024-04-24) | touched: 6 pages | new: 3 sources, 1 company, 1 vendor, 1 usecase | contradictions: 0
- Source A: [[unleash-moderna-hr-it-merger-2025-06]] — Tier 2, HR+IT 병합 맥락 + Franklin "work in progress" caveat
- Source B: [[constellation-moderna-chatgpt-enterprise-2024-04]] — Tier 1, 수치 중심 but 독립 검증 아님 명시
- Source C: [[moderna-blog-openai-2024-04]] — Tier 3, 자사 self-report (mChat/ChatGPT Enterprise 타임라인)
- Company: [[moderna]] — 신규 생성 (첫 company 페이지), 조직도 Mermaid 포함
- Vendor: [[openai]] — 신규 stub 생성
- Use case: [[moderna-ask-hr-routing]] — confidence 0.65 (최초 0.4 이상 케이스), Mermaid 3개(process/system/org), A·E 섹션 fact-rich, C·D 섹션 대부분 미공개
- Quality report: 자사 self-report를 분석가가 전달한 성격임을 명시, "⚠️ 자사 보고" 마커 도입, Franklin caveat을 Consulting Angle에 반영
- 대비 확인: Workday stub case(0.10) vs Moderna case(0.65) — 가드레일이 fact 풍부도에 따라 confidence를 자연스럽게 반영

## [2026-05-06] ingest | PwC Korea HR AI 추가 자료 fact-check + 6 신규 use case + 1 misattribution 정정 | touched: 8 pages | new: 6 usecases | contradictions: 1 resolved

### 컨텍스트
사용자가 PwC Korea HR AI 컨설팅 문서 추가 분량 (sections 2.10 근태·2.11 복리후생·2.12 급여 + Anaplan/Workday/Mastercard/Businessolver 확장) 제출. fact-check 후 통합.

### 검증 절차
2개 background research agent 병렬 실행:
- Agent 1: Legion·Nayya·Businessolver Sofia·Silver 4 벤더 검증
- Agent 2: Mastercard Unlocked 벤더 귀속 (Gloat vs Eightfold) + IBM HiRo + SK하이닉스 One Resume 검증

### 검증 결과 — 주요 발견

1. **🚨 Mastercard "Unlocked" 벤더 misattribution (CRITICAL)**:
   - **이전 wiki 상태**: [[eightfold-ai-talent-intelligence]]에 Mastercard 4개 metric (93%·42%·1M·24h)이 Eightfold reference로 등재
   - **검증 결과**: Unlocked = **Gloat 도입** (2022~ Project Possible 후속). Gloat 공식 case study + Mastercard 2025 newsroom + Josh Bersin 블로그 3출처 교차 확인
   - **PwC 자료가 정확** (벤더는 Gloat). 기존 wiki의 추론 오류
   - **조치**: Eightfold 페이지에서 4 metric 행 삭제 + [!contradiction] 콜아웃 추가 + 신규 [[mastercard-unlocked-gloat-talent-marketplace]] 페이지로 분리

2. **PwC 자료 디테일 오류 2건 정정**:
   - "Mastercard $20M" → 실제 $21M (Gloat 공식, PwC 반올림 오기)
   - "Mastercard 360,000 hours" → Schneider Electric 메트릭과 혼동, 실제 100K (2022) → 1M (2025)
   - "Legion Mercy Health $30M" → **Misattribution**, 실제 Works/Trusted Health 사례 (Legion 아님)
   - "Legion $195M Series C 2024" → 누적 funding 합계, 단일 라운드 아님 (2021 Series C $50M + 2024 Riverwood $50M + 2024 SVB debt $50M)
   - "Nayya $55M Series B 2022" → 실제 Series C, Series B는 $37M (2021)

3. **신규 use case 6건**:
   | Use case | Vendor | Confidence | 신규성 |
   |---|---|---|---|
   | [[businessolver-sofia-agentic-benefits]] | Businessolver | 0.65 | ✅ 가장 깨끗한 검증 — 모든 metric이 자사 발표와 일치 |
   | [[nayya-benefits-decision-support]] | Nayya | 0.50 | ⚠️ funding 라운드 정정 caveat 명시 |
   | [[legion-wfm-hourly-workforce]] | Legion Technologies | 0.55 | ⚠️ Mercy misattribution + funding 누적 caveat 명시 |
   | [[mastercard-unlocked-gloat-talent-marketplace]] | Gloat | 0.65 | 🚨 기존 Eightfold 등재 정정으로 분리 |
   | [[ibm-hiro-promotion-agent]] | IBM watsonx Orchestrate | 0.55 | IBM AskHR 생태계 specialist agent |
   | [[sk-hynix-pwc-one-resume-employee-search]] | PwC + SK internal | 0.18 | 공개 출처 0건, 5-agent retention과 동일 묶음 처리 |

4. **검토 후 wiki 등재 거부**:
   - Silver (FSA/HSA AI Claim Agent): 회사 규모 매우 작음, Tier 1·2 미디어 0건, FSA/HSA는 미국 IRS 세제 특화 → 한국 적용성 0

### 영향
- use case: 126 → 132 (신규 6)
- 카테고리 분포: Total Rewards +2, Onboarding +1, Performance +1, EX +2
- contradictions: 1 unresolved → 0 (Mastercard Eightfold→Gloat 정정 완료)
- confidence 분포: 신규 6건 평균 0.51 (production·stub 혼합)

### Quality report
- ✅ 가장 깨끗: Businessolver Sofia (모든 metric 자사 발표와 일치)
- ⚠️ caveat 다수: Legion (Mercy misattribution + funding), Nayya (funding 라운드)
- 🚨 critical 정정: Mastercard Unlocked (Eightfold → Gloat)

### 사용자 액션 권장
- PwC 컨설팅 자료 수정 의견 전달 권장: Mercy Health $30M misattribution + funding 라운드 오기 + Mastercard "$20M / 360K hours" 디테일
