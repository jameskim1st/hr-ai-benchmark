# HR AI Benchmark — Index

> 이 페이지는 `scripts/build_index.py`가 생성한다 (마지막 생성 2026-09-27). 손으로 편집하지 말 것. 규칙은 [[CLAUDE|CLAUDE.md]] + `.claude/rules/`.

## 규모

| 유형 | 건수 | 비고 |
|---|---|---|
| use case (HR 프로세스 AI 도입 사례) | **118** | public 116 · KR 22 |
| enterprise-ai (전사 GenAI 플랫폼 — 참고) | 15 | use case 카운트에서 제외 |
| reference (법령·리포트·맥락) | 4 | |
| sources | 300 | raw 스냅샷 연결 295 |
| companies / vendors | 20 / 15 | |
| syntheses | 15 | lint·digest·compare·research 포함 |

근거 등급: A 41 · B 30 · C 42 · D 5  ｜  depth: full 15 · partial 80 · stub 23  ｜  freshness: fresh 66 · stale 47 · unverified 5

등급 정의: **A** 독립(Tier 1·2) 소스 2개 이상 · **B** 독립 1개 · **C** 벤더·자사 보고만 · **D** 미검증/소스 없음. 제안서 인용은 A·B + depth full 권장.

## 🧭 진입점

- 📖 [[guide]] · 📤 [[guide-html-export]] · 📋 [[dashboard]] · 🔎 [[taxonomy-crosswalk]] (SHRM·Bersin·AIHR 대응표)
- 📚 카테고리: [[01-talent-acquisition]] · [[02-onboarding-transitions]] · [[03-learning-development]] · [[04-performance-talent-management]] · [[05-total-rewards]] · [[06-employee-experience-hr-ops]] · [[07-strategic-workforce-governance]] · [[taxonomy-crosswalk]]
- 🛠 운영: `/hr-ingest` `/hr-lint` `/hr-verify` `/hr-research` `/hr-digest` `/hr-compare` · 빌드 `python scripts/build_all.py`

## 📊 카테고리별 Use Cases

```dataview
TABLE WITHOUT ID primary_category AS "카테고리", length(rows) AS "건수", length(filter(rows, (r) => r.evidence_grade = "A" OR r.evidence_grade = "B")) AS "A·B 등급"
FROM "wiki/usecases"
GROUP BY primary_category
SORT length(rows) DESC
```

### 1. Talent Acquisition (18건)

```dataview
TABLE WITHOUT ID file.link AS "Use Case", company AS "기업", vendor AS "벤더", evidence_grade AS "등급", depth AS "depth", region AS "지역"
FROM "wiki/usecases"
WHERE primary_category = "Talent Acquisition"
SORT evidence_grade ASC, confidence DESC
```

<details><summary>정적 목록 (Dataview 없을 때)</summary>

- [[jobkorea-hiring-center-talent-agent]] — 잡코리아 (웍스피어) · A/partial
- [[sk-cc-adot-biz-hr-recruitment]] — SK C&C · A/partial
- [[sk-hynix-ask-ai-interview]] — SK하이닉스 · A/stub
- [[chipotle-paradox-olivia]] — Chipotle Mexican Grill · A/partial
- [[midas-inair-ai-assessment-korea]] — _다수 (기아, KB증권, 신한은행, CJ, LIG넥스원, GS리테일 등)_ · A/partial
- [[ibm-watson-recruitment]] — IBM · B/stub
- [[wantedlab-ai-recruiting-agent]] — _N/A (product, no specific customer deployment yet)_ · B/partial
- [[greetinghr-ats-ai-korea]] — 그리팅 (Greeting HR) · B/stub
- [[mcdonalds-paradox-recruiting]] — McDonald's · B/full
- [[nestle-paradox-recruiting]] — Nestlé · B/full
- [[sk-group-aict-ai-recruitment]] — SK Group · B/partial
- [[ibm-watsonx-orchestrate-ta-agent]] — IBM · C/partial
- [[cathay-pacific-hirevue]] — Cathay Pacific · C/partial
- [[eightfold-ai-talent-intelligence]] — _다수 (specific names in vendor page)_ · C/partial
- [[emirates-hirevue-volume-hiring]] — Emirates · C/partial
- [[hirevue-ai-assessment-bias-audit]] — _다수 (major financial institution 등)_ · C/partial
- [[hsbc-eightfold-gloat-multi-vendor]] — HSBC · C/partial
- [[lgcns-agentic-ai-hr]] — LG CNS (자사 + 고객사) · C/full

</details>

### 2. Onboarding & Transitions (8건)

```dataview
TABLE WITHOUT ID file.link AS "Use Case", company AS "기업", vendor AS "벤더", evidence_grade AS "등급", depth AS "depth", region AS "지역"
FROM "wiki/usecases"
WHERE primary_category = "Onboarding & Transitions"
SORT evidence_grade ASC, confidence DESC
```

<details><summary>정적 목록 (Dataview 없을 때)</summary>

- [[ibm-blue-match-internal-mobility]] — IBM · A/partial
- [[mastercard-unlocked-gloat-talent-marketplace]] — Mastercard · A/stub
- [[schneider-electric-gloat-talent-marketplace]] — Schneider Electric · A/partial
- [[novartis-gloat-skills-marketplace]] — Novartis · A/partial
- [[unilever-flex-gloat-talent-marketplace]] — Unilever · B/stub
- [[fuel50-lennox-internal-mobility]] — Lennox · C/partial
- [[phenom-merck-kgaa-talent-marketplace]] — Merck KGaA · C/partial
- [[zapier-enboarder-ai-onboarding]] — Zapier · C/partial

</details>

### 3. Learning & Development (18건)

```dataview
TABLE WITHOUT ID file.link AS "Use Case", company AS "기업", vendor AS "벤더", evidence_grade AS "등급", depth AS "depth", region AS "지역"
FROM "wiki/usecases"
WHERE primary_category = "Learning & Development"
SORT evidence_grade ASC, confidence DESC
```

<details><summary>정적 목록 (Dataview 없을 때)</summary>

- [[microsoft-people-skills-inferred-ontology]] — Microsoft · A/full
- [[walmart-openai-certification]] — Walmart · A/partial
- [[accenture-mass-genai-reskilling]] — Accenture · A/partial
- [[fujitsu-hr-ai-skills-career]] — Fujitsu · A/full
- [[jpmorgan-ai-made-easy-upskilling]] — JPMorgan Chase · A/partial
- [[tcs-infosys-ai-reskilling-india]] — TCS · A/stub
- [[walmart-ai-frontline-workforce]] — Walmart · A/partial
- [[jnj-digital-talent-platform-skills-ai]] — Johnson & Johnson · A/partial
- [[siemens-reskilling-internal-mobility]] — Siemens · A/partial
- [[accenture-ai-learning-workforce]] — Accenture · B/stub
- [[ibm-charlie-learning-ops-agent]] — IBM · B/partial
- [[bersin-galileo-learn-ai-native-lms]] — _N/A (product, single known deployment = vendor itself)_ · B/full
- [[docebo-ai-learning-lazboy]] — La-Z-Boy · B/partial
- [[pwc-ai-upskilling-65k]] — PwC · B/partial
- [[linkedin-learning-ai-coaching]] — _다수 (LinkedIn Learning Premium·Enterprise 고객)_ · C/stub
- [[workday-sana-for-workday-lms]] — _다수 (Workday Learning 고객, Klarna·MTV·Polestar 등 Sana 기존 고객)_ · C/partial
- [[samsung-multicampus-ai-learning]] — 삼성전자 · C/stub
- [[ericsson-degreed-ai-skills-upskilling]] — Ericsson · D/partial

</details>

### 4. Performance & Talent Management (11건)

```dataview
TABLE WITHOUT ID file.link AS "Use Case", company AS "기업", vendor AS "벤더", evidence_grade AS "등급", depth AS "depth", region AS "지역"
FROM "wiki/usecases"
WHERE primary_category = "Performance & Talent Management"
SORT evidence_grade ASC, confidence DESC
```

<details><summary>정적 목록 (Dataview 없을 때)</summary>

- [[clap-ai-performance-korea]] — 디웨일 (CLAP) · A/stub
- [[meta-ai-performance-review-mandate]] — Meta · A/partial
- [[ibm-hiro-promotion-agent]] — IBM · B/stub
- [[sap-joule-performance-goals-agent]] — _다수 (SAP SuccessFactors 고객)_ · B/partial
- [[betterup-ai-coaching-twilio]] — Twilio · B/partial
- [[moderna-self-review-gpt]] — Moderna · B/partial
- [[workday-illuminate-performance-review-agent]] — _다수 (Workday 고객)_ · B/partial
- [[lattice-ai-performance-summarization]] — _다수 (Lattice 고객 — 개별 고객 미확인)_ · C/partial
- [[betterworks-nextgen-ai-performance]] — Colgate-Palmolive · C/partial
- [[cultureamp-ai-coach-asana]] — Asana · C/partial
- [[15five-kona-reup-ai-manager-coaching]] — ReUp Education · D/partial

</details>

### 5. Total Rewards (9건)

```dataview
TABLE WITHOUT ID file.link AS "Use Case", company AS "기업", vendor AS "벤더", evidence_grade AS "등급", depth AS "depth", region AS "지역"
FROM "wiki/usecases"
WHERE primary_category = "Total Rewards"
SORT evidence_grade ASC, confidence DESC
```

<details><summary>정적 목록 (Dataview 없을 때)</summary>

- [[nayya-benefits-decision-support]] — _다수 (미국 직원 1,000명 초과 고용주 대상 MetLife 채널 + 직접 고객)_ · A/partial
- [[douzone-one-ai-year-end-tax]] — _N/A (product, 다수 중소·중견기업 대상)_ · B/full
- [[moderna-benefits-equity-gpts]] — Moderna · B/stub
- [[businessolver-sofia-agentic-benefits]] — _다수 (Businessolver 고객 — Fortune 1000 다수, 구체 명단 일부 비공개)_ · C/partial
- [[spring-health-general-mills-ai-eap]] — General Mills · C/partial
- [[adp-assist-payroll-ai]] — ADP · C/partial
- [[syndio-pay-equity-ai]] — _다수 (300+ 고객, 30% Fortune Most Admired)_ · C/partial
- [[paychex-flex-agentic-workforce]] — _다수 (800K 고객)_ · D/partial
- [[ukg-ai-workforce-scheduling-healthcare]] — KC CARE Health Center · D/partial

</details>

### 6. Employee Experience & HR Ops (23건)

```dataview
TABLE WITHOUT ID file.link AS "Use Case", company AS "기업", vendor AS "벤더", evidence_grade AS "등급", depth AS "depth", region AS "지역"
FROM "wiki/usecases"
WHERE primary_category = "Employee Experience & HR Ops"
SORT evidence_grade ASC, confidence DESC
```

<details><summary>정적 목록 (Dataview 없을 때)</summary>

- [[hitachi-skye-hr-ai-assistant]] — Hitachi · A/partial
- [[pulmuone-duribun-hr-chatbot]] — 풀무원 · A/partial
- [[cisco-ai-assistant-hr-agentic]] — Cisco · A/partial
- [[korea-gov-ai-hr-public-sector]] — 인사혁신처 / 행정안전부 · A/full
- [[lloyds-banking-workday-genai-hr]] — Lloyds Banking Group · A/partial
- [[walmart-ask-sam-workforce-ai]] — Walmart · A/partial
- [[bosch-rob-hr-ai-assistant]] — Bosch · A/full
- [[moderna-ask-hr-routing]] — Moderna · A/partial
- [[amazon-connections-daily-pulse]] — Amazon · A/partial
- [[sap-successfactors-1h-2026-joule-agents]] — _다수 (SAP SuccessFactors 고객)_ · B/partial
- [[workday-peakon-illuminate-employee-voice]] — _다수 (Workday Peakon 고객, Workday 자사 도입 포함)_ · B/partial
- [[ibm-askhr-watsonx]] — IBM · B/partial
- [[legion-wfm-hourly-workforce]] — _다수 (Dollar General, Cinemark, Five Below 등 시급직 다수 산업)_ · B/partial
- [[servicenow-now-assist-hr]] — _다수 (구체 고객명 미공개)_ · B/partial
- [[siemens-servicenow-hr-gbs]] — Siemens · B/full
- [[microsoft-viva-glint-copilot-sentiment]] — Microsoft · C/partial
- [[sk-hynix-one-resume-employee-search]] — SK하이닉스 · C/stub · 🔒
- [[viven-ai-digital-twin-coworker]] — _N/A (vendor product, stealth exit 직후 customer 0건)_ · C/partial
- [[coca-cola-southwest-perceptyx-activate]] — Arca Continental Coca-Cola Southwest Beverages · C/stub
- [[qualtrics-adidas-employee-experience-ai]] — adidas · C/stub
- [[flex-korea-hr-ai-saas]] — 플렉스팀 · C/partial
- [[microsoft-employee-self-service-agent]] — Microsoft · C/full
- [[workday-illuminate-employee-sentiment]] — _N/A_ · C/stub

</details>

### 7. Strategic Workforce & Governance (31건)

```dataview
TABLE WITHOUT ID file.link AS "Use Case", company AS "기업", vendor AS "벤더", evidence_grade AS "등급", depth AS "depth", region AS "지역"
FROM "wiki/usecases"
WHERE primary_category = "Strategic Workforce & Governance"
SORT evidence_grade ASC, confidence DESC
```

<details><summary>정적 목록 (Dataview 없을 때)</summary>

- [[kb-bank-ai-hr-deep-change]] — KB국민은행 · A/partial
- [[korea-electric-power-hr-bot]] — 한국전력 · A/partial
- [[moel-ai-labor-law-consultation]] — 고용노동부 (대한민국 정부) · A/full
- [[nps-ai-innovation-taskforce]] — 국민연금공단 · A/partial
- [[posco-dx-110-agents-hr]] — 포스코DX (포스코 그룹) · A/stub
- [[sk-group-aibiz-25-companies]] — SK 그룹 (25개 멤버사) · A/partial
- [[amazon-hr-ai-restructuring]] — Amazon · A/partial
- [[ibm-hr-workforce-reduction-agentic]] — IBM · A/partial
- [[ibm-predictive-attrition-comp-ai]] — IBM · A/stub
- [[jpmorgan-llm-suite-redeployment]] — JPMorgan Chase · A/partial
- [[dbs-bank-hr-ai-talent-analytics]] — DBS Bank · A/partial
- [[deloitte-zora-ai-hc-suite]] — Deloitte · B/partial
- [[workday-agent-system-of-record-asor]] — _다수 (Workday HCM 고객)_ · B/partial
- [[mercy-health-ai-nursing-workforce]] — Mercy Health · B/partial
- [[visier-vee-people-analytics]] — Providence (healthcare, 주요 고객) · B/partial
- [[workday-illuminate-job-architecture]] — _N/A (product capability, no specific customer disclosed)_ · B/partial
- [[allvoices-vera-ai-er-copilot]] — _다수 (AllVoices 고객 — Fortune·SMB 혼합, 구체 명단 부분 비공개)_ · C/partial
- [[anaplan-workforce-analyst-ai-agents]] — _다수 (Anaplan 고객 — Fresenius·Canada Goose·Cinemark·healthcare provider 등)_ · C/stub
- [[diligent-vault-active-integrity-speakup]] — _다수 (Diligent + Vault Platform 고객 — 글로벌 enterprise 비중 높음)_ · C/partial
- [[hr-acuity-oliver-ai-er-companion]] — _다수 (HR Acuity 고객 — 개별 고객명 원문 미확인)_ · C/full
- [[navex-ethicspoint-nca-compliance]] — _다수 (NAVEX 13,000+ 조직 — Fortune 100 다수)_ · C/full
- [[sk-hynix-pwc-5agent-retention]] — SK하이닉스 · C/stub · 🔒
- [[sodales-spire-energy-labor-relations]] — Spire Inc. · C/partial
- [[waymo-hr-acuity-er-case-management]] — Waymo · C/stub
- [[yelp-hr-acuity-er-documentation]] — Yelp · C/stub
- [[salesforce-orgvue-org-design-ai]] — Salesforce · C/partial
- [[beamery-atkins-realis-skills-architecture]] — AtkinsRéalis · C/partial
- [[deloitte-workforce-analyzer-salesforce]] — Salesforce (named customer) · C/stub
- [[t-mobile-textio-dei-hiring]] — T-Mobile · C/full
- [[tampa-general-visier-people-analytics]] — Tampa General Hospital · C/partial
- [[allegis-group-holistic-ai-governance]] — Allegis Group · D/partial

</details>

## 🏢 Companies (20)

- [[accenture]]
- [[amazon]]
- [[chipotle]]
- [[cisco]]
- [[deloitte]]
- [[hsbc]]
- [[ibm]]
- [[jnj]]
- [[jpmorgan]]
- [[kb-bank]]
- [[meta]]
- [[microsoft]]
- [[moderna]]
- [[schneider-electric]]
- [[shinhan-bank]]
- [[siemens]]
- [[sk-group]]
- [[sk-hynix]]
- [[unilever]]
- [[walmart]]

## 🧩 Vendors (15)

- [[douzone-bizon]]
- [[eightfold]]
- [[flex-korea]]
- [[gloat]]
- [[hirevue]]
- [[josh-bersin-co]]
- [[midas-it]]
- [[openai]]
- [[paradox]]
- [[sana-labs]]
- [[sap-successfactors]]
- [[sk-ax]]
- [[skt]]
- [[wantedlab]]
- [[workday]]

## 🏗 Enterprise-AI (전사 GenAI 플랫폼 — HR 전용 use case 아님) (15)

- [[commonwealth-bank-ai-workforce]] — Commonwealth Bank of Australia · C
- [[deloitte-claude-470k-employees]] — Deloitte · B
- [[goldman-sachs-gs-ai-assistant]] — Goldman Sachs · A
- [[gs-caltex-aiu-platform]] — GS칼텍스 (GS 그룹) · C
- [[hyundai-mobis-moai-platform]] — 현대모비스 · A
- [[hyundai-steel-hip-platform]] — 현대제철 · A
- [[jpmorgan-llm-suite-employee-productivity]] — JPMorgan Chase · A
- [[kogas-hybrid-genai-platform]] — 한국가스공사 · B
- [[lg-chatexaone-group-rollout]] — LG (LG전자·LG이노텍·LG디스플레이 등 그룹 5만+) · A
- [[lg-uplus-jihye-employee-agent]] — LG U+ · B
- [[mirae-asset-ai-assistant-platform]] — 미래에셋증권 · B
- [[samsung-fire-employee-rag-chatbot]] — 삼성화재 · A
- [[shinhan-bank-ai-one-platform]] — 신한은행 · A
- [[toshiba-microsoft-copilot-viva]] — Toshiba · C
- [[woori-bank-175-ai-agents]] — 우리은행 · A

## 📜 Reference (법령·리포트·맥락) (4)

- [[cisco-ai-workforce-consortium-skills-evolution]] — report
- [[deloitte-2026-human-capital-trends-meta]] — report
- [[korea-ai-basic-act-hr-compliance]] — regulation
- [[lotte-job-based-hr-reform]] — context

## 🧪 Syntheses (15)

- [[llm-wiki-landscape-2026-09]] — research-note · 2026-09-27
- [[system-review-2026-09-27]] — system-review · 2026-09-27
- [[hr-ai-usecase-collection-detailed]] — deliverable · 2026-04-13
- [[hr-ai-usecase-collection-mockup]] — deliverable · 2026-04-13
- [[industry-region-landscape]] — synthesis · 2026-04-12
- [[korean-3-si-hr-ai-comparison]] — synthesis · 2026-04-12
- [[lint-2026-04-12-round2]] — lint-report · 2026-04-12
- [[lint-2026-04-12-round3]] — lint-report · 2026-04-12
- [[lint-2026-04-12-round4]] — lint-report · 2026-04-12
- [[lint-2026-04-12]] — lint-report · 2026-04-12
- [[talent-acquisition-6-vendor-comparison]] — synthesis · 2026-04-12
- [[workday-as-customer-paradox]] — synthesis · 2026-04-12
- [[ai-tech-x-hr-category-landscape]] — synthesis · 
- [[er-ai-vendor-landscape-korea-2026-05]] — synthesis · 
- [[kr-conglomerate-ai-standardization-vs-distribution]] — synthesis · 

## 📚 Sources (300)

```dataview
TABLE WITHOUT ID file.link AS "Source", tier AS "Tier", publisher AS "Publisher", publication_date AS "발행", snapshot_quality AS "raw"
FROM "wiki/sources"
WHERE !deprecated
SORT publication_date DESC
```
