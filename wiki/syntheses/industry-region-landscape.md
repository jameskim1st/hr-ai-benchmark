---
type: synthesis
topic: industry-region-landscape
generated_at: 2026-04-12
tags: [landscape, industry-comparison, region-comparison, consulting-overview]
consulting_priority: high
---

# HR AI 산업별·지역별 Landscape — 70건 Use Case 기반 분석

> 🎯 **컨설팅 도구**: 70건 use case를 산업·지역 축으로 cross-cut해 "어떤 산업이 HR AI를 가장 적극적으로 쓰는가", "지역별 패턴 차이는 무엇인가"를 데이터로 보여주는 synthesis.

---

## 1. 산업별 HR AI 성숙도 매트릭스

```mermaid
quadrantChart
    title 산업별 HR AI 성숙도 (규모 vs 다양성)
    x-axis "단일 영역 집중" --> "다영역 확산"
    y-axis "소규모 pilot" --> "대규모 production"
    Tech (Meta·Amazon·Salesforce): [0.7, 0.9]
    Finance (JPMorgan·HSBC·DBS): [0.6, 0.8]
    Consulting (Deloitte·PwC·Accenture): [0.8, 0.7]
    Pharma (Moderna·J&J·Novartis): [0.7, 0.6]
    Manufacturing (Siemens·Bosch·Hitachi): [0.5, 0.5]
    Retail (Walmart·Chipotle·McDonald's): [0.3, 0.9]
    Healthcare (Mercy·Tampa General): [0.3, 0.6]
    Aviation (Cathay·Emirates): [0.2, 0.5]
    Korean (SK·LG CNS·마이다스): [0.4, 0.6]
```

### 산업별 요약

| 산업 | 사례 수 | 주요 HR 영역 | 대표 기업 | 핵심 패턴 |
|---|---|---|---|---|
| **Tech** | ~8 | EX(Meta·Amazon) + L&D + Governance | Meta·Amazon·Salesforce·Microsoft | "전 직원에게 AI 배포 → HR 자체도 AI 대상" |
| **Finance** | ~7 | TA + EX + Analytics | JPMorgan·Goldman·HSBC·DBS·Lloyds·CBA | "멀티모델 방화벽 격리 구조" + 채용 억제 |
| **Consulting** | ~5 | L&D + EX + Workforce Planning | Deloitte·Accenture·PwC | "자사 적용 → 고객 판매" self-dogfooding |
| **Pharma** | ~5 | EX + L&D + TA | Moderna·J&J·Novartis·Pfizer | "학술 검증(J&J MIT) + 전사 GPT(Moderna)" |
| **Manufacturing** | ~5 | L&D + EX | Siemens·Bosch·Hitachi·Toshiba | "300k 리스킬링 + ServiceNow HR 통합" |
| **Retail/F&B** | ~5 | TA + EX | Walmart·Chipotle·McDonald's·Nestlé | "고볼륨 채용 AI + 매장 어시스턴트" |
| **Healthcare** | ~3 | Workforce Planning | Mercy·Tampa General·Providence | "간호사 부족 → AI 스케줄링/예측 → $30M 절감" |
| **Aviation** | 2 | TA | Cathay Pacific·Emirates | "대량 채용의 시간 단축 (90%+)" |
| 🇰🇷 **Korean** | ~9 | TA + TR + EX | SK·마이다스아이티·더존·LG CNS | "그룹 SI가 구축 + 평가 전문 벤더" |

---

## 2. 지역별 HR AI 패턴

### North America (~25건)
- **특징**: 가장 공격적인 AI 도입. Amazon·Walmart 규모의 대량 배포.
- **핵심 패턴**: "AI가 HR 인력 자체를 줄인다" (Amazon 15%, IBM "couple hundred")
- **규제**: NYC LL144 bias audit, 주별 법률. HireVue가 선제 대응.
- **벤더 생태계**: Paradox·HireVue·Eightfold·BetterUp·15Five 등 point solution 풍부

### Europe (~12건)
- **특징**: GDPR + 종업원대표(Betriebsrat/Works Council) 환경에서 **단계적·협의적** 도입
- **핵심 패턴**: Siemens·Bosch 독일 제조업의 "리스킬링 중심" 접근 (AI로 사람 자르기보다 역할 전환)
- **규제**: EU AI Act 2026-08 high-risk 의무 시작. HR 채용·평가 = Annex III 고위험.
- **벤더**: SAP SuccessFactors + Gloat·Beamery + Textio DEI

### Korea (~9건)
- **특징**: "그룹 SI가 만든다" — 삼성SDS·LG CNS·SK AX. 대기업 전용 경로.
- **핵심 패턴**: 채용 평가(마이다스아이티 Nature 검증) + 급여/세무(더존비즈온) + 채용 프로세스(SK AICT)
- **규제**: 채용절차공정화법·개인정보보호법. EU AI Act만큼 명시적이진 않으나 실질 제약 있음.
- **공백**: L&D·Performance·EX 카테고리에 한국 사례 아직 희소

### APAC (~10건, KR 제외)
- **일본** (Hitachi·Fujitsu·Toshiba): "Microsoft Copilot + 자체 AI" hybrid. 조심스러운 도입.
- **싱가포르** (DBS): 금융 선도. People Analytics + TA AI.
- **호주** (CBA): AI 45명 대체→번복 **반면교사** 사례. 노조 영향력 강함.
- **인도** (TCS·Infosys): 100만명+ 리스킬링. AI가 IT 서비스 업계를 재편.

---

## 3. 컨설팅 클라이언트별 "어떤 사례를 보여줄 것인가"

### 한국 대기업 CHRO

| 핵심 메시지 | 보여줄 사례 | 이유 |
|---|---|---|
| "학술 검증된 채용 AI" | 마이다스아이티 inAIR (Nature) | CHRO가 가장 신뢰할 수 있는 근거 |
| "글로벌 대기업도 이렇게 한다" | Moderna Ask HR (0.70) + IBM AskHR (270k) | Scale + structure 둘 다 증명 |
| "한국 SI가 이미 하고 있다" | SK AX AICT + LG CNS 에이전틱 AI | 경쟁 그룹 자극 |
| "주의할 점도 있다" | Amazon 15% HR 감축 + CBA 번복 | 반면교사로 균형 |

### 글로벌 기업 한국 법인장

| 핵심 메시지 | 보여줄 사례 | 이유 |
|---|---|---|
| "글로벌 suite만으로 불충분" | 더존비즈온 연말정산 + HSBC multi-vendor | 한국 특유 영역 + multi-vendor stack |
| "Workday vs SAP 선택의 함의" | Workday paradox synthesis | 벤더 선택 = 전략 선택 |

### 헬스케어 CHRO

| 핵심 메시지 | 보여줄 사례 | 이유 |
|---|---|---|
| "간호사 부족의 AI 해법" | Mercy Health ($30M) + Tampa General (agency -70%) | 헬스케어 특유 ROI |
| "스킬 추론으로 인력 재배치" | J&J (MIT CISR, 60-70% 추론) | 학술 검증 + 같은 pharma/healthcare |

---

## 4. 전체 landscape 한 줄 요약

> **"HR AI는 2025~2026년 현재, 채용(15건)과 직원 경험(17건)에서 가장 활발하고, 학술 검증(J&J·마이다스아이티)부터 대규모 감축(Amazon·Meta)까지 스펙트럼이 넓으며, 지역별로 NA는 공격적·EU는 규제 중심·한국은 SI 중심·APAC은 다양한 패턴을 보인다. 컨설팅 프로젝트에서는 이 70건을 산업·지역·규모·벤더 축으로 재조합해 클라이언트 맞춤 벤치마크를 즉시 생성할 수 있다."**

---

## 5. 관련 wiki 페이지

- [[korean-3-si-hr-ai-comparison]] — 한국 벤더 심층 비교
- [[talent-acquisition-6-vendor-comparison]] — 채용 AI 벤더 비교
- [[workday-as-customer-paradox]] — Suite vs point solution 전략
- [[dashboard]] — 전체 실시간 대시보드
- [[guide]] — wiki 구조 가이드

---

## 금융 산업 HR AI — JPMorgan·Goldman 관찰 (2026-09-27 병합)

> 舊 `jpmorgan-goldman-sachs-hr-ai` 합본 페이지(삭제)의 산업 공통 인사이트를 이관. 기업별 사실은 [[jpmorgan-llm-suite-redeployment]] · [[goldman-sachs-gs-ai-assistant]] 참조.
> 출처: CNBC 2025-10-15 https://www.cnbc.com/2025/10/15/jpmorgan-chase-goldman-sachs-ai-hiring.html · HR Executive https://hrexecutive.com/jpmorgan-ceo-we-have-displaced-people-from-ai-and-we-offer-them-other-jobs/ · HR Dive https://www.hrdive.com/news/banks-ramp-up-ai-hiring-roi-efficiency-gains-evident-insights/746724/

### 금융 산업 공통 Pain Point·Trigger

- **Before**: 투자은행·자산관리·리테일금융의 **인건비가 총비용의 50%+** — 금융 산업에서 AI 자동화의 ROI가 가장 큰 이유 (❓ 병합 전 페이지 기술, 개별 출처 귀속 없음)
- **Pain point**: (1) AI 역량 인력 확보 경쟁 치열, (2) 기존 HR 프로세스(채용·온보딩·분석)에 과도한 인력 투입, (3) 데이터 보안·규제 준수 하에서 AI 도입이 다른 산업보다 복잡
- **Trigger**: 2024~2025 금융 산업 전반에서 "**AI 도입을 안 하면 경쟁에서 뒤처진다**"는 공감대 형성. JPMorgan CEO Dimon의 "모든 프로세스에 AI 주입" 방침이 HR에도 적용 (⚠️ 자사 보고 — CEO 발언, CNBC·HR Executive 전달)
- 양사 모두 **AI로 채용을 줄이면서 AI 인력을 늘리는** 구조적 전환 — "HR 인력 축소 + AI 기술 인력 확대"라는 workforce composition 변화가 핵심 기대효과

### 금융 산업 전체 Insight

| 지표 | 값 | 출처 | 표기 |
|---|---|---|---|
| 은행권 AI 기술자 증가 (model dev·platform eng·PM) | **13%** (JPMorgan·Wells Fargo·Citi 주도) | HR Dive | ✅ Fact (Tier 2 보도) |
| Goldman GitHub Copilot 개발자 효율 | **~20%** (12,000 개발자) | CNBC 2025-10-15 | ⚠️ 자사 보고 |
| Goldman GS AI 사용자 | **10,000명** (파일럿) | CNBC 2025-10-15 | ✅ Fact |

### 왜 금융이 HR AI의 "canary in the coal mine"인가

1. **높은 인건비** → AI 대체 ROI가 가장 큰 산업
2. **규제 환경** → compliance·risk management에 AI governance 성숙
3. **데이터 풍부** → 성과·보상·이직 데이터가 가장 구조화됨
4. **경쟁 압력** → "옆 은행이 AI 쓰면 우리도"

### 한국 금융 시사점

- KB증권·신한은행이 이미 마이다스아이티 inAIR 도입 ([[midas-inair-ai-assessment-korea]])
- 국내 금융 HR AI는 **채용 평가**에서 시작 → **JPMorgan 패턴(ML 기반 sourcing, 채용 억제)으로 진화** 가능성
- 금감원·금융위 규제(AI 활용 가이드라인)와의 정합성 확인 필요
- Dimon "displaced but offered other jobs"는 IBM Krishna "replaced but elevated"와 같은 패턴 — 한국 노동법·노조 컨텍스트에서는 "감원"보다 "재배치·reskilling" frame 권장 ([[jpmorgan-llm-suite-redeployment]] Consulting Angle 참조)
