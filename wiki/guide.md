---
title: "LLM Wiki 구조 가이드 — 언제든 다시 볼 수 있는 설명서"
created_at: 2026-04-12
purpose: 이 wiki가 어떻게 생겼고 어떻게 작동하는지, 처음 보는 사람도 이해할 수 있도록 정리한 문서
---

# 🧭 HR AI Benchmark Wiki — 구조 가이드

> 이 문서는 **"내가 이 wiki를 한동안 안 보다가 다시 왔을 때"** 바로 이해할 수 있도록 쓴 가이드입니다. 처음부터 끝까지 읽으면 전체 그림이 잡힙니다.

---

## 1. 이 wiki가 뭔지 한마디로

**HR 부문에 AI를 적용한 실제 사례들을 계속 모아서 정리해두는 살아있는 자료집**입니다.

- "살아있다" = 새로운 기사·보고서가 나올 때마다 업데이트됨
- "자료집" = 컨설팅 프로젝트에서 벤치마크·제안서 reference로 바로 쓸 수 있음
- "AI가 관리" = 사람(나)이 원본 자료를 넣어주면, Claude(AI)가 요약·분류·교차참조·모순 체크를 자동으로 함

이걸 **LLM Wiki 패턴** (Karpathy, 2026)이라고 부릅니다.

---

## 2. 전체 구조 — 큰 그림

이 wiki는 **3개의 층(layer)**으로 돼 있습니다:

```
┌──────────────────────────────────────────────────┐
│                    CLAUDE.md                       │
│              (규칙서 / 설계도)                      │
│   "어떻게 분류하고, 어떻게 쓰고, 뭘 금지할지"        │
└──────────────────────────────────────────────────┘
          ↕ Claude가 이 규칙을 따름
┌──────────────────────────────────────────────────┐
│                    wiki/                           │
│           (Claude가 만들고 유지하는 자료)             │
│     요약·분석·도식·교차참조가 여기에 축적됨            │
└──────────────────────────────────────────────────┘
          ↑ wiki가 이것을 참조
┌──────────────────────────────────────────────────┐
│                    raw/                            │
│              (원본 / 변경 금지)                      │
│      기사·보고서·벤더 문서의 원본 그대로 보관          │
└──────────────────────────────────────────────────┘
```

### 각 층의 역할

| 층 | 누가 쓰나 | 누가 읽나 | 수정 가능? |
|---|---|---|---|
| **raw/** | 사람(나)이 기사·PDF·클립을 넣음 | Claude가 읽음 | ❌ 절대 수정 금지 |
| **wiki/** | Claude가 쓰고 유지 | 사람·Claude 모두 읽음 | ✅ Claude가 필요 시 재작성 |
| **CLAUDE.md** | 사람+Claude가 합의해서 작성 | Claude가 규칙으로 따름 | ✅ 합의 하에 수정 |

**비유**: raw/는 **서류 캐비닛** (원본 보관), wiki/는 **화이트보드** (정리·분석 결과), CLAUDE.md는 **업무 매뉴얼** (화이트보드에 뭘 어떻게 적을지 규칙).

---

## 3. 폴더 구조 — 무엇이 어디에 있나

```
c:\AI\AI-HR\Benchmark\
│
├── CLAUDE.md                ← 📜 규칙서 (taxonomy·템플릿·ingest 프로토콜)
│
├── raw/                     ← 📦 원본 자료 (읽기만, 수정 금지)
│   ├── articles/            ← 웹 기사·블로그 (Obsidian Web Clipper 등)
│   ├── reports/             ← Gartner·McKinsey 같은 PDF 리포트
│   ├── vendors/             ← 벤더 공식 문서·제품 페이지
│   └── feeds/               ← RSS·뉴스 자동 수집 dump
│
├── wiki/                    ← 📝 Claude가 만드는 자료 (핵심!)
│   ├── index.md             ← 전체 목차 (카테고리·기업·벤더·소스 목록)
│   ├── log.md               ← 작업 이력 (언제 뭘 했는지 타임라인)
│   ├── dashboard.md         ← Obsidian Dataview 대시보드 (자동 집계)
│   ├── guide.md             ← 이 문서! (구조 설명서)
│   │
│   ├── usecases/            ← ★ 핵심 자산: HR AI 사례 1건 = 1페이지
│   ├── companies/           ← 도입 기업 1곳 = 1페이지
│   ├── vendors/             ← HR 테크 벤더 1곳 = 1페이지
│   ├── sources/             ← 원본 소스 1건 = 1요약 페이지
│   ├── categories/          ← HR 대그룹 7개 = 7개 카테고리 뷰 페이지
│   └── syntheses/           ← 분석·lint 리포트·cross-entity 인사이트
│
├── .claude/commands/        ← 슬래시 커맨드 (/hr-ingest 등)
├── .obsidian/               ← Obsidian 설정
└── scripts/                 ← 보조 스크립트
```

---

## 4. wiki/ 안의 5가지 자료 유형 — 서로 어떻게 연결되나

wiki/ 안에는 **5종류의 페이지**가 있고, 이들이 `[[wikilink]]`로 서로 연결됩니다.

### 4-1. 관계도 (큰 그림)

```
                    ┌─────────────┐
                    │  categories │
                    │  (7개 HR    │
                    │   대그룹)   │
                    └──────┬──────┘
                           │ "이 카테고리의 use case들"
                           ↓
  ┌────────────┐    ┌──────────────┐    ┌──────────┐
  │  companies │←──→│   usecases   │←──→│  vendors  │
  │  (도입기업) │    │ (★ HR AI    │    │ (HR 테크  │
  │            │    │   사례 1건)  │    │  벤더)    │
  └────────────┘    └──────┬───────┘    └──────────┘
                           │ "이 사례의 근거"
                           ↓
                    ┌──────────────┐
                    │   sources    │
                    │ (원본 소스   │
                    │  요약)       │
                    └──────────────┘
                           │ "원본은 여기"
                           ↓
                    ┌──────────────┐
                    │    raw/      │
                    │ (원본 그대로)│
                    └──────────────┘
```

그리고 **syntheses** (분석 결과물)는 여러 usecase·vendor를 가로질러 생기는 cross-entity 인사이트:

```
  usecases ──┐
  vendors  ──┼──→ syntheses (예: "Workday는 벤더인가 고객인가")
  companies──┘
```

### 4-2. 각 유형 설명

#### ① usecases/ — 핵심 자산 (현재 81건)

**"어떤 기업이 어떤 HR 기능에 AI를 어떻게 적용했는가"** 1건 = 1페이지.

예시: `moderna-ask-hr-routing.md` = "Moderna가 Ask HR이라는 중앙 GPT로 직원 질문을 routing하는 사례"

각 페이지에 들어있는 것:
- **frontmatter** (YAML) — 분류 태그, 신뢰도 점수, 소스 리스트 등 메타데이터
- **Summary** — 3~5줄 핵심
- **Problem / Why** — 왜 이걸 했는지
- **Solution Architecture (A~F)** — 가장 중요한 부분:
  - A. Process (프로세스 — 어떤 업무 흐름이 바뀌었나)
  - B. System (시스템 — 무엇 위에 돌아가나)
  - C. Data (데이터 — 뭘 넣고 뭘 빼나)
  - D. Model (모델 — 어떤 AI를 쓰나)
  - E. Organization (조직 — 누가 만들고 운영하나)
  - F. Diagrams (도식 — Mermaid 다이어그램)
- **Impact / Metrics** — 효과 수치
- **Governance & Risk** — 리스크·편향·규제
- **Contradictions** — 소스 간 모순
- **Consulting Angle** — 컨설팅에서 어떻게 쓸 수 있나

#### ② companies/ — 도입 기업 페이지 (현재 14곳)

**"한 기업의 HR AI 전체 현황"**을 한 곳에서 보는 홀리스틱 뷰.

예시: `moderna.md` = Moderna의 조직 구조(HR+IT 병합), AI 타임라인(mChat→ChatGPT Enterprise→3000 GPT), 관련 use case 목록

**핵심 기능**: Dataview 쿼리가 해당 기업의 모든 use case를 자동 수집해서 보여줌. 새 use case가 추가되면 기업 페이지에 자동 반영 (수동 편집 불필요).

#### ③ vendors/ — HR 테크 벤더 페이지 (현재 13곳)

**"이 벤더가 뭘 팔고, 누가 쓰고, 어떤 HR 영역을 커버하는지"** 정리.

예시: `paradox.md` = Paradox의 Olivia 제품, 40+ 고객 레퍼런스, Chipotle·7-Eleven 등 주요 사례, 한국 적용 가능성

특이 사례: `workday.md`는 **벤더이면서 동시에 다른 벤더의 고객**으로 등장 (Paradox·Sana 사용). 이런 교차 관계가 synthesis의 재료가 됨.

#### ④ sources/ — 소스 요약 페이지 (현재 51건)

**"원본 기사·보고서 1건을 요약하고, 신뢰도를 매기고, 무엇이 빠져있는지 기록한 것"**.

예시: `bersin-workday-illuminate-2024-09.md` = Josh Bersin의 Workday Illuminate 분석 기사 요약. Tier 1(독립 분석가), 핵심 인용 3개, 한계 4가지.

각 소스에는 **Tier (신뢰도 등급)**가 붙음:

| Tier | 의미 | 예시 |
|---|---|---|
| **1** | 독립 분석기관·권위 있는 연구 | Gartner, McKinsey, Josh Bersin |
| **2** | HR 전문 매체·리서치 | HR Brew, AIHR, HR Dive, AI타임스 |
| **3** | 벤더가 직접 낸 자료 | Workday blog, Paradox clients page |
| **4** | 기업의 직접 발표·채용공고 등 | Chipotle 공식 press release |

**중요 원칙**: Tier 3(벤더) 자료는 "벤더가 하는 말"이므로 `⚠️ 벤더 주장:` 접두사를 붙여서 다른 팩트와 구분합니다.

#### ⑤ syntheses/ — 분석 결과물 (현재 10건)

**"여러 use case·vendor를 가로질러 발견한 인사이트"**.

예시: `workday-as-customer-paradox.md` = "Workday가 자사 Illuminate 대신 Paradox·Sana를 쓴다는 사실 + SAP SuccessFactors 고객은 반대로 3rd party를 버린다는 반증" → **"suite 벤더 선택 = vendor 철학 선택"**이라는 컨설팅 인사이트.

Lint 리포트(건강점검 결과)도 여기에 들어갑니다.

---

## 5. 분류 체계 (Taxonomy) — HR 카테고리가 어떻게 나뉘는가

모든 use case는 **7개 대그룹 + 26개 중그룹 + 80개 소그룹**으로 분류됩니다.

### 대그룹 7개 (한 눈에)

```
 ┌─ 1. Talent Acquisition        채용·인력확보
 │    └─ Sourcing, Screening, Interview, Offer, Executive Search, Early-career
 │
 ├─ 2. Onboarding & Transitions   온보딩·이동·퇴직
 │    └─ New-hire, Internal Mobility, Global Mobility, Offboarding
 │
 ├─ 3. Learning & Development     교육·역량·스킬
 │    └─ Skills, Content & Delivery, Performance Support, Language
 │
 ├─ 4. Performance & Talent Mgmt  평가·승진·핵심인재
 │    └─ Goal & Performance, Succession, Coaching
 │
 ├─ 5. Total Rewards              보상·급여·복리후생
 │    └─ Compensation, Payroll Ops(연말정산·퇴직정산·충당금), Benefits, Recognition
 │
 ├─ 6. Employee Experience & Ops  EX·HR운영·근태
 │    └─ Core HR, Self-service, HR Service, Time/Attendance, Listening, Culture, Comms
 │
 └─ 7. Strategic Workforce & Gov  인사기획·PA·노사·거버넌스
      └─ Planning, Org Design, Analytics, DEI, Employee Relations, Compliance, HR Tech Gov
```

### 분류 방식

use case는 **frontmatter에 태그로** 분류합니다 (폴더로 나누지 않음):

```yaml
primary_category: Employee Experience & HR Ops   # 대그룹 (1개)
subcategory: Employee Self-service               # 중그룹 (1개)
tags: [ask-hr, chatbot, case-deflection]         # 소그룹 (여러 개 가능)
```

왜 폴더가 아니라 태그? → **하나의 사례가 여러 카테고리에 걸칠 수 있어서**. 예: Moderna Ask HR은 HR Ops이면서 동시에 Benefits 관련이기도 함.

### 추가 분류 축 (다차원 태깅)

카테고리 외에 다음 축도 frontmatter에 붙음:

| 축 | 의미 | 값 예시 |
|---|---|---|
| `industry` | 산업 | pharma, finance, restaurant |
| `region` | 지역 | na, eu, kr, global |
| `employee_class` | 직원 유형 | 기술사무직, 전임직, all |
| `frequency` | 실행 주기 | daily, annual, adhoc |
| `stage` | 배포 단계 | pilot, production, stub |
| `vendor_type` | 벤더 유형 | hrms, point-solution, foundation-model |
| `confidence` | 신뢰도 (0~1) | 0.65 |

→ Obsidian Dataview에서 어느 축으로든 재조합 가능. "한국 제약사가 채용에 쓴 AI 사례" 같은 즉석 필터.

---

## 6. 신뢰도 (Confidence) — 이 사례를 얼마나 믿을 수 있나

모든 use case에는 **0.0~1.0 사이의 신뢰도 점수**가 붙어 있습니다.

### 계산 방식 (단순화)

```
신뢰도 = 소스 점수 합계 + 최신성 보정 - 모순 감점
```

| 소스 등급 | 기여 점수 | 이유 |
|---|---|---|
| Tier 1 (분석기관) | +0.35 | 독립적·전문적 분석 |
| Tier 2 (HR 매체) | +0.20 | 독립적 보도 |
| Tier 3 (벤더 자료) | +0.10 | 이해관계 편향 감안 |
| Tier 4 (기업 발표) | +0.15 | 자사 보고지만 공식 |

| 최신성 | 보정 | 이유 |
|---|---|---|
| 6개월 이내 | +0.10 | 매우 최신 |
| 6~12개월 | 0 | 보통 |
| 12~24개월 | -0.15 | 낡아감 |
| 24개월 초과 | -0.30 | 오래됨 |

| 모순 (contradiction) | 감점 | |
|---|---|---|
| unresolved 1건당 | -0.20 | 모순이 해결 안 됨 |

### 신뢰도의 현실적 의미

| 점수 | 의미 | 제안서에 쓸 수 있나? |
|---|---|---|
| **0.7+** | 여러 독립 소스로 교차 검증됨 | ✅ "검증된 reference case"로 인용 |
| **0.4~0.69** | 일부 검증, 일부 벤더 주장 | ⚠️ "참고 사례"로만, 조건 명시 |
| **0.2~0.39** | 대부분 벤더 주장 또는 단일 소스 | ❌ "시장 동향" 수준으로만 |
| **0~0.19** | stub (정보 매우 부족) | ❌ 인용 금지 |

### 현재 wiki의 신뢰도 분포

```
0.70  ████████████████████  moderna-ask-hr-routing
0.40  ██████████████        moderna-self-review-gpt
0.40  ██████████████        moderna-benefits-equity-gpts
0.35  ████████████          chipotle-paradox-olivia
0.25  █████████             workday-illuminate-job-architecture
0.25  █████████             unilever-flex-gloat
0.25  █████████             bersin-galileo-learn
0.25  █████████             sk-group-aict-ai-recruitment
0.20  ███████               wantedlab-ai-recruiting-agent
0.20  ███████               douzone-one-ai-year-end-tax
0.10  ████                  workday-illuminate-employee-sentiment (stub)
```

---

## 7. Fact 표기 체계 — "이 문장을 얼마나 믿을 수 있나"

wiki 안의 모든 문장은 다음 5단계 중 하나로 분류됩니다:

| 표기 | 의미 | 예시 |
|---|---|---|
| ✅ **Fact** | 독립 소스에서 확인됨 | "Moderna는 3,000+ GPT를 보유한다 (Unleash 2025-06)" |
| ⚠️ **벤더 주장** | 벤더가 자기 제품에 대해 한 말 | "⚠️ 벤더 주장: Paradox가 time-to-hire 75% 감소" |
| ⚠️ **자사 보고** | 기업이 자기 도입 사례로 공개한 것 | "⚠️ 자사 보고: Moderna VP가 '주 120 대화' 발표" |
| ❓ **미공개** | 정보가 없음 | "_미공개 (not disclosed)_" |
| 🚫 **금지** | 추측으로 채우기 | "보통 이런 시스템은..." ← 이렇게 쓰면 안 됨 |

**가장 중요한 원칙**: **"모르는 걸 아는 척하는 것이 가장 위험하다."** 정보가 없으면 `_미공개_`로 당당히 표시하고, 나중에 소스가 추가되면 자연히 채워집니다.

### Pain Point(도입 배경)와 기대효과에 대한 표기 원칙

모든 use case 페이지에는 **두 가지 핵심 섹션**이 있습니다:

- **"## Problem / Why (도입 배경)"** — 이 AI를 왜 도입했는가? Before(이전 상태)·Pain Point(핵심 문제)·Trigger(결정 계기)를 구체적으로
- **"## Impact / Metrics (기대효과)"** — 도입 후 무엇이 좋아졌는가? Before→After 형식 + 기대효과 요약 1~2줄

| 상황 | 어떻게 쓸 것인가 |
|---|---|
| **기업 배포 사례 + 구체 수치 있음** | Before: X → After: Y (Z% 변화, 출처 명시) |
| **기업 배포 사례 + 수치 없음** | "⚠️ 기대효과 수치 미공개. 정성적으로는 [효과 설명]" |
| **벤더 주장 수치만 있음** | "Before: _미공개_ → After: ⚠️ 벤더 주장 Z% 감소 (baseline 미공개)" |
| **벤더 제품 (특정 기업 도입 아님)** | "벤더 제품이므로 기대효과는 도입 기업별 상이. 벤더가 주장하는 일반 ROI: [수치]" |
| **아무 정보 없음** | "⚠️ 기대효과 미공개" — 빈 섹션 금지 |

---

## 8. 4가지 주요 작업 (Operation) — wiki를 어떻게 운영하나

### 8-1. Ingest (소스 넣기) — `/hr-ingest`

새 기사·보고서가 생기면 wiki에 반영하는 작업.

```
사람이 raw/에 기사 저장
      ↓
Claude가 읽고 분류
      ↓
wiki/sources/ 에 요약 생성
      ↓
wiki/usecases/ 에 새 use case 생성 또는 기존 업데이트
      ↓
wiki/vendors/, companies/ 업데이트
      ↓
모순 체크 (기존 주장과 충돌하면 [!contradiction] 표시)
      ↓
wiki/index.md, log.md 갱신
      ↓
사용자에게 결과 보고
```

**1건의 소스가 보통 5~15개 wiki 페이지를 건드림**.

### 8-2. Lint (건강점검) — `/hr-lint`

wiki 전체의 품질을 점검하는 작업. 찾아내는 것들:

1. 오래된 주장 (12개월 이상 재확인 안 된 것)
2. 낮은 신뢰도 (0.4 미만)
3. 고아 페이지 (다른 곳에서 링크 안 되는 페이지)
4. 깨진 링크
5. 금지어 (추측 표현)
6. 해결 안 된 모순
7. 빈 카테고리
8. 벤더 주장 접두사 누락
...등 11가지 항목

### 8-3. Query (질문) — `/hr-digest`

wiki 내용만으로 질문에 답하는 작업. 예: "채용 AI 사례 중 한국 대기업은?" → wiki 검색 → 답변 + citation.

### 8-4. Compare (비교) — `/hr-compare`

두 벤더·기업·use case를 나란히 비교하는 작업. 예: "Workday vs SAP SuccessFactors AI 전략 비교" → 비교표 + Consulting Angle.

---

## 9. 페이지 간 네비게이션 — "어떻게 타고 다니나"

Obsidian에서 `[[페이지이름]]` 을 클릭하면 해당 페이지로 바로 이동합니다.

### 3가지 주요 진입 경로

```
경로 1: 카테고리별 보기 (HR 기능 축)
─────────────────────────────────
index.md → 카테고리 선택 (예: "1. Talent Acquisition")
       → 01-talent-acquisition.md (카테고리 뷰)
       → Dataview 표에서 use case 클릭
       → chipotle-paradox-olivia.md (use case 상세)
       → 기업명 클릭 → chipotle.md (기업 홀리스틱 뷰)


경로 2: 기업별 보기 (기업 축)
─────────────────────────────────
index.md → Companies 섹션에서 기업 선택
       → moderna.md (기업 페이지)
       → Dataview "HR 대그룹 커버리지" 표에서 use case 클릭
       → moderna-ask-hr-routing.md
       → 벤더명 클릭 → openai.md (벤더 뷰)


경로 3: 벤더별 보기 (벤더 축)
─────────────────────────────────
index.md → Vendors 섹션에서 벤더 선택
       → paradox.md (벤더 페이지)
       → 고객 리스트에서 기업·use case 클릭
       → chipotle-paradox-olivia.md
```

### 교차 진입 (어디서든 어디로든)

```
                 ┌── use case ──┐
                 │              │
     category ←─┤              ├─→ source
                 │              │
     company  ←─┤              ├─→ vendor
                 │              │
                 └── synthesis ─┘
```

**모든 페이지가 모든 페이지로 연결 가능**. Obsidian Graph view (Ctrl+G)에서 이 관계를 시각적으로 볼 수 있음.

---

## 10. Obsidian에서 핵심 기능 3가지

### 10-1. Dataview — 자동 업데이트 표

wiki 안의 모든 표(카테고리별 use case, 기업별 커버리지 등)는 **Dataview 쿼리**로 생성됩니다. 이 표들은 **파일이 추가·수정되면 자동으로 업데이트**됨 — 수동 편집 불필요.

예: `WHERE primary_category = "Talent Acquisition"` → Talent Acquisition 카테고리의 모든 use case를 자동 표시.

### 10-2. Graph View (Ctrl+G) — 관계도

모든 `[[wikilink]]` 연결이 시각적으로 보임. 노드 = 페이지, 엣지 = 링크. 클러스터가 보이면 관련 페이지 그룹.

### 10-3. Backlinks — 역참조

아무 페이지에서 `Ctrl+Shift+B` → 이 페이지를 링크하고 있는 다른 모든 페이지 목록. "이 벤더를 사용하는 use case가 몇 개지?" 같은 질문에 바로 답.

---

## 11. Hallucination 방지 (가장 중요한 규칙)

이 wiki의 **가장 핵심적인 규칙**은: **"없는 것을 있는 것처럼 포장하지 않는다."**

구체적으로:
- 소스에 없는 내용은 절대 추가하지 않음 → `_미공개_` 로 표시
- "아마도", "보통", "일반적으로" 같은 추측 표현 금지
- 벤더 주장에는 반드시 `⚠️ 벤더 주장:` 접두사
- 도식(Mermaid)도 소스에서 확인된 노드만 포함 (점선 = 미확인, 실선 = 확인)
- 기업 자체 보고에는 `⚠️ 자사 보고:` 접두사 (독립 검증과 구분)

**3중 가드레일**:
1. **템플릿 수준** — 페이지 작성 시 금지어·표기 규칙 적용
2. **Ingest 수준** — 소스 처리 시 Hallucination self-check 단계
3. **Lint 수준** — 정기 점검으로 금지어·미검증 주장 탐지

---

## 12. 현재 상태 스냅샷 (2026-05-05 최종)

```
총 wiki 페이지     : ~170
━━━━━━━━━━━━━━━━━━━━━
Use cases          : 81  (이전 라운드 70 + 신규 11)
Sources            : 51
Companies          : 14  (Walmart·IBM·JPMorgan·Amazon·Siemens·Meta·Deloitte·HSBC·J&J·Schneider·Moderna·Unilever·Chipotle·SK)
Vendors            : 13
Categories         :  7  (100% 커버, 최소 7건/카테고리)
Syntheses          : 10  (lint 4 + insight 4 + HTML 산출물 mockup 2)
Dashboard          :  1  (Dataview 10개 쿼리)
HTML 산출물         :  1  (hr-ai-usecase-collection.html, ~250KB, 단일 파일)
━━━━━━━━━━━━━━━━━━━━━
평균 신뢰도         : 0.36
confidence ≥ 0.50  : 15/81 (19%)  ← 제안서에 "검증된 reference"로
confidence ≥ 0.40  : 33/81 (41%)  ← 제안서에 "참고 사례"로
학술 검증 사례      :  2  ⭐ (J&J MIT CISR + 마이다스아이티 Nature)
━━━━━━━━━━━━━━━━━━━━━
🇺🇸 NA             : ~28건
🇪🇺 EU             : ~13건
🇰🇷 KR             : 11건 (SK AICT·마이다스 inAIR·원티드 AI agent·더존 ONE AI·LG CNS·롯데·플렉스·삼성 멀티캠퍼스·그리팅·CLAP·공공)
🌏 APAC            : ~10건
🌍 Global          : ~15건
━━━━━━━━━━━━━━━━━━━━━
산업 커버           : 9+ (Tech·Finance·Consulting·Pharma·Manufacturing·Retail·Healthcare·Aviation·Telecom)
Cross-entity insight: 4건 (Workday paradox, Korean SI 비교, TA 벤더 비교, Industry/Region landscape)
산출물 파이프라인    : extract_v3.py → build_html_v6.py (2-step, [[guide-html-export]] 참조)
```

---

## 13. Quick Reference — 자주 하는 것

| 하고 싶은 것 | 어떻게 |
|---|---|
| **새 기사 넣기** | raw/에 저장 → `/hr-ingest raw/articles/xxx.md` |
| **건강점검** | `/hr-lint` |
| **특정 카테고리 보기** | Obsidian에서 `wiki/categories/06-employee-experience-hr-ops.md` 열기 |
| **특정 기업 전체 보기** | Obsidian에서 `wiki/companies/moderna.md` 열기 |
| **벤더 비교** | `/hr-compare Workday vs SAP SuccessFactors` |
| **약한 사례 찾기** | `wiki/dashboard.md` → "Low-confidence use cases" 표 |
| **한국 사례만** | Dashboard → "국내(KR) 사례" 쿼리 |
| **모순 현황** | Dashboard → "Unresolved Contradictions" 섹션 |

---

## 14. 다음 라운드에서 할 수 있는 것

| 우선순위 | 내용 | 효과 |
|---|---|---|
| 🔴 높음 | 기존 사례에 Tier 1·2 소스 추가 | 평균 신뢰도 0.35 → 0.45+ |
| 🔴 높음 | Performance(4건)·Total Rewards(5건) 보강 | 약세 카테고리 해소 |
| 🟡 중간 | 한국 L&D·Performance·EX 사례 확보 | KR 7건→12건+ |
| 🟡 중간 | Company page 확충 (주요 10곳) | Holistic view 활성화 |
| 🟡 중간 | RSS 자동 수집 스크립트 세팅 | raw/ 자동 축적 |
| 🔵 낮음 | Oracle HCM 패턴 조사 | F2 synthesis 완성 |
| 🔵 낮음 | 금지어 일괄 리라이트 | lint warning 해소 |

---

> 이 문서는 wiki가 성장하면서 **같이 업데이트**해야 합니다. 현재 상태 스냅샷(§12)은 2026-05-05 기준이며, 다음 major ingest 후 갱신 필요.
