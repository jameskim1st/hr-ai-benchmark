---
type: deliverable
topic: hr-ai-usecase-collection-detailed
generated_at: 2026-04-13
purpose: 컨설팅 프로젝트용 HR AI Use Case 집 — 프로세스·시스템·데이터 도식 포함 상세 버전
tags: [deliverable, consulting-deck, dual-view, solution-architecture, mermaid]
---

# HR AI Use Case 집 — 상세 버전 (프로세스·시스템·데이터 도식 포함)

> **이 문서의 특징**: 각 대표 사례에 대해 **프로세스 플로우(As-is→To-be) + 시스템 아키텍처 + 데이터 흐름**을 Mermaid 도식으로 시각화. 모든 도식의 실선 = 소스 확인 Fact, 점선 = 미확인.

---

# ━━━ 1. Talent Acquisition (채용) ━━━

## 1-1. Chipotle "Ava Cado" — Paradox Olivia (conf 0.55)

### 도입 배경 (Pain Point)
3,500+ 매장의 General Manager가 채용 행정(스크리닝·스케줄링·오퍼)에 과도한 시간 소모 → 매장 운영에 집중 못 함

### 🔵 Process Flow (As-is → To-be)

```mermaid
flowchart LR
    subgraph "Before (As-is)"
        B1[지원자 지원] --> B2[매니저가 수동 스크리닝]
        B2 --> B3[전화로 면접 스케줄]
        B3 --> B4[면접]
        B4 --> B5[수동 오퍼]
    end
    subgraph "After (To-be) — Ava Cado"
        A1[지원자] -->|career channel| Ava["Ava Cado<br/>(4개국어 AI)"]
        Ava -->|자동 스크리닝<br/>+ 정보 수집| A1
        Ava -->|인터뷰 슬롯 제안| Cal[GM 캘린더]
        Cal --> GM[General Manager]
        GM -->|면접 + 결정| Hire[채용 결정]
        Hire --> Ava2[Ava Cado<br/>오퍼 자동 발송]
    end
    classDef fact fill:#dcfce7,stroke:#16a34a
    classDef before fill:#fee2e2,stroke:#dc2626
    class B1,B2,B3,B4,B5 before
    class A1,Ava,Cal,GM,Hire,Ava2 fact
```
_범례: 빨간 = Before, 녹색 = After (Chipotle PR + CNBC 확인)_

### 🟢 System Architecture

```mermaid
flowchart TB
    subgraph "Chipotle HR Tech Stack"
        Career["채용 페이지<br/>(3,500+ 매장)"] --> Paradox["Paradox Olivia<br/>(SaaS)"]
        Paradox --> |"4개국어<br/>영·스·불·독"| Chat["Conversational<br/>AI Engine"]
        Chat --> Schedule["Interview<br/>Scheduling API"]
        Schedule --> GCal["GM 캘린더<br/>연동"]
        Chat --> Offer["Offer Letter<br/>자동 생성"]
    end
    subgraph "미확인 영역"
        Paradox -.->|ATS 연동?| ATS[(ATS)]
        Paradox -.->|HRIS 연동?| HRIS[(Core HRIS)]
    end
    classDef fact fill:#dcfce7
    classDef unknown fill:#fef9c3,stroke-dasharray: 5 5
    class Career,Paradox,Chat,Schedule,GCal,Offer fact
    class ATS,HRIS unknown
```

### 📊 기대효과 (Before → After)

| 지표 | Before | After | 변화 | 검증 수준 |
|---|---|---|---|---|
| Time-to-hire | **12일** | **3.5일** | **71%↓** | ✅ CNBC 독립 확인 |
| 지원 완료율 | **50%** | **85%** | **+35pt** | ✅ CNBC 독립 확인 |
| 스케줄링 시간 | 수동 (시간~일) | **자동 (분)** | — | ⚠ Paradox 주장 |
| 커버 규모 | — | **3,500+ 매장** | — | ✅ Chipotle PR |
| Bias audit | — | _미공개_ | — | ❓ |

---

## 1-2. 🇰🇷 SK Group AICT + AI 면접 100% (conf 0.40)

### 도입 배경
SK 그룹 전사 OI(Operational Innovation) 비용 절감. 기존 채용 프로세스(서류 1주, 코딩 테스트)가 AI 시대에 부적합

### 🔵 Process Flow

```mermaid
flowchart LR
    subgraph "Before"
        B1[서류 제출] --> B2[HR 수동 심사<br/>1주]
        B2 --> B3[코딩 테스트]
        B3 --> B4[인간 면접관<br/>1차 면접]
        B4 --> B5[2차 면접]
        B5 --> B6[합격 통보]
    end
    subgraph "After — A.Biz HR"
        A1[서류 제출] --> A2[AI 자동 심사<br/>4시간]
        A2 --> A3["AICT<br/>(AI 활용 능력 평가)"]
        A3 --> A4["AI 1차 면접<br/>★ 100% 자동<br/>(진행·평가·보고서)"]
        A4 --> A5[2차 면접<br/>사람]
        A5 --> A6[AI 합격/불합격<br/>고지 + OT 안내]
    end
    classDef before fill:#fee2e2
    classDef fact fill:#dcfce7
    classDef highlight fill:#fbbf24,stroke:#92400e
    class B1,B2,B3,B4,B5,B6 before
    class A1,A2,A3,A5,A6 fact
    class A4 highlight
```
_노랑 강조: 1차 면접 AI 100% 자동화 = 이 사례의 가장 과감한 포인트_

### 🟢 System Architecture

```mermaid
flowchart TB
    App[지원자] --> Portal["SK 채용 포털"]
    Portal --> ABHR["A.Biz HR<br/>(SK AX + SKT 합작)"]
    ABHR --> Screen["LLM 기반<br/>서류 스크리닝"]
    ABHR --> AICT["AICT 엔진<br/>(프롬프트·문제해결·결과물)"]
    ABHR --> AIInt["AI 면접<br/>(진행·평가·보고서)"]
    Screen --> Result[결과]
    AICT --> Result
    AIInt --> Result
    Result --> HR[HR 담당자<br/>최종 확인]
    ABHR -.->|Foundation model?| LLM["SKT A.X LLM?<br/>(미확인)"]
    classDef fact fill:#dcfce7
    classDef unknown fill:#fef9c3,stroke-dasharray: 5 5
    class App,Portal,ABHR,Screen,AICT,AIInt,Result,HR fact
    class LLM unknown
```

### 📊 기대효과

| 지표 | Before | After | 검증 |
|---|---|---|---|
| 서류 심사 시간 | **1주** | **4시간** | ✅ 한국 경제지 7곳 |
| 결과 발표 | 수주 | **마감 2일 후** | ✅ 서울경제 |
| 처리 속도 | 사람 기준 | **100배 빠름** | ⚠ 벤더 주장 |
| 1차 면접 | 인간 면접관 | **AI 100%** | ✅ SK AX 인사이트 |
| AICT 내용 | 코딩 테스트 | **AI 활용 능력 평가** | ✅ Fact |

---

# ━━━ 2. Onboarding & Transitions (온보딩·이동) ━━━

## 2-1. Schneider Electric — Open Talent Market, $15M (conf 0.50)

### 도입 배경
**직원 50%가 퇴직 사유로 "내부 성장 기회 부족"** — wiki 전체에서 가장 강력한 Before 데이터

### 🔵 Process Flow

```mermaid
flowchart LR
    subgraph "Before"
        B1[직원] --> B2{내부 기회<br/>보이나?}
        B2 -->|안 보임 50%| B3[퇴직]
        B2 -->|보임| B4[수동 지원]
    end
    subgraph "After — Open Talent Market"
        A1[직원] -->|프로필 작성<br/>스킬·관심·포부| Profile[(Profile DB)]
        Opp[조직 내 기회<br/>gig/career/mentorship] --> Gloat[Gloat AI<br/>Matching]
        Profile --> Gloat
        Gloat -->|추천| A1
        A1 -->|자율 선택<br/>매니저 승인 불필요| Project[프로젝트 참여]
    end
    classDef before fill:#fee2e2
    classDef fact fill:#dcfce7
    class B1,B2,B3,B4 before
    class A1,Profile,Opp,Gloat,Project fact
```

### 🟢 System Architecture

```mermaid
flowchart TB
    subgraph "Schneider Electric HR Stack"
        HRIS["Oracle Fusion / Taleo<br/>(Core HRIS)"] --> Gloat["Gloat Platform<br/>(Talent Marketplace)"]
        LMS["Cornerstone<br/>(Learning)"] --> Gloat
        Gloat --> Match["AI Matching<br/>Engine"]
        Match --> Rec["기회 추천<br/>(gig·career·mentorship)"]
        Match --> Gap["스킬 gap 추천<br/>(미매칭 시)"]
    end
    Emp[직원 135,000] --> Gloat
    classDef fact fill:#dcfce7
    class HRIS,Gloat,LMS,Match,Rec,Gap,Emp fact
```
_Bersin 2019 + SHRM 2025에서 Oracle Fusion/Taleo/Cornerstone 통합 확인_

### 📊 기대효과

| 지표 | Before | After | 검증 |
|---|---|---|---|
| "내부 기회 부족" 퇴직 사유 | **50%** | 개선 (수치 미공개) | ⚠ 자사 보고 → Bersin Tier 1 |
| Unlocked capacity | 0 | **360,000+ 시간** | ⚠ Gloat 주장 |
| 비용 절감 | 0 | **$15M+** | ⚠ Gloat 주장 |
| 초기 등록률 | — | **75% → 89%** | ✅ Bersin 확인 |

---

# ━━━ 3. Learning & Development (교육·역량) ━━━

## 3-1. J&J — Digital Talent Platform, MIT CISR ⭐⭐ (conf 0.60)

### 도입 배경
디지털 역량 인력의 이탈이 높고, 직원 스킬 가시성이 부족해 내부 이동·학습 추천이 어려움

### 🔵 Process Flow + 🟣 Data Flow (학술 논문에서 확인된 아키텍처)

```mermaid
flowchart TB
    subgraph "Data Sources (확인됨)"
        HRIS[(HRIS<br/>인사 기본 정보)]
        RecDB[(채용 DB<br/>채용 이력)]
        LMS[(LMS<br/>학습 이력)]
        PM[(Project Mgmt<br/>프로젝트 참여)]
    end
    subgraph "AI Processing"
        HRIS --> Infer["AI Skills Inference<br/>NLP + ML"]
        RecDB --> Infer
        LMS --> Infer
        PM --> Infer
        Infer -->|60~70% 자동 추론| SkillDB[(스킬 프로필<br/>DB)]
        Self[직원 자기보고<br/>30~40%] --> SkillDB
    end
    subgraph "Output"
        SkillDB --> Match["내부 기회<br/>매칭"]
        SkillDB --> Learn["학습 경로<br/>추천"]
        Match --> Emp[직원]
        Learn --> Emp
    end
    classDef fact fill:#dcfce7,stroke:#16a34a
    class HRIS,RecDB,LMS,PM,Infer,SkillDB,Self,Match,Learn,Emp fact
```
_범례: 전체 녹색 = MIT CISR + IS Journal 학술 검증. 이 도식의 모든 노드가 Tier 1 학술 소스에서 확인됨._

### 📊 기대효과 (전부 학술 검증 ⭐)

| 지표 | Before | After | 변화 | 검증 |
|---|---|---|---|---|
| 스킬 추론 | 직원 자기보고 100% | **AI 60~70%** + 자기보고 30~40% | 자동화 | ✅ MIT CISR |
| J&J Learn 접근 | _미공개_ | Technology 직원 **90%+** | — | ✅ MIT CISR |
| 자발적 학습 참여 | _baseline_ | **+20%** | — | ✅ IS Journal |
| 내부 배치 | 2023 수준 | 2024: **+8%** (YoY) | — | ✅ IS Journal |
| 디지털 역할 이탈 | 전사 평균 | **3.2% 낮음** | — | ✅ IS Journal |

---

# ━━━ 4. Performance & Talent Management (평가·인재) ━━━

## 4-1. BetterUp + Twilio — AI 코칭 (conf 0.45)

### 도입 배경
리더십 코칭은 효과가 있지만 비용이 높아 소수 임원만 받을 수 있음 → AI로 전 직원 확장

### 🔵 Process Flow

```mermaid
flowchart LR
    subgraph "Before"
        B1[소수 임원] --> B2[Human Coach<br/>1:1, 고비용]
        B2 --> B3[코칭 세션]
        B3 --> B4[행동 변화]
    end
    subgraph "After — BetterUp AI"
        A1[전 직원<br/>Twilio 8,000명] --> AI["BetterUp Grow<br/>(AI-only)"]
        A1 --> Hybrid["BetterUp<br/>(Human+AI)"]
        AI -->|실시간 가이던스<br/>역할별 맞춤| A1
        Hybrid -->|Deep coaching<br/>+ AI 인사이트| A1
        AI --> Data["Talent Intelligence<br/>Dashboard"]
        Hybrid --> Data
    end
    classDef before fill:#fee2e2
    classDef fact fill:#dcfce7
    class B1,B2,B3,B4 before
    class A1,AI,Hybrid,Data fact
```

### 📊 기대효과

| 지표 | Before (non-coached) | After (coached) | 변화 | 검증 |
|---|---|---|---|---|
| 고성과 평가 확률 | baseline | **+32%** | — | ⚠ 벤더 주장 (Twilio 8k) |
| 이탈률 | baseline | **5x 낮음** | — | ⚠ 벤더 주장 |
| 비용/인 | Human coaching 비용 | **70% 절감** (AI-only) | — | ⚠ 벤더 주장 |
| 만족도 | — | **95%** (Grow) | — | ✅ Inc.com 보도 |

---

# ━━━ 5. Total Rewards (보상·복리후생) ━━━

## 5-1. Spring Health + General Mills — EAP 1%→26% (conf 0.30)

### 도입 배경
전통 EAP(Employee Assistance Program) 활용률이 **1%**로 극히 낮음

### 🔵 Process Flow

```mermaid
flowchart LR
    subgraph "Before (전통 EAP)"
        B1[직원] -->|전화·이메일| B2[EAP 상담사]
        B2 --> B3[대기 수일~수주]
        B3 --> B4[상담 세션]
        style B1 fill:#fee2e2
        style B2 fill:#fee2e2
        style B3 fill:#fee2e2
        style B4 fill:#fee2e2
    end
    subgraph "After (Spring Health AI)"
        A1[직원] -->|앱 접근| AI["Spring Health<br/>AI 매칭"]
        AI -->|즉시 매칭| Coach["적합 치료사<br/>/ 코치"]
        Coach --> Session["세션<br/>(평균 1.4~2.46회)"]
        Session --> Result["개선<br/>우울 58% / 불안 49%"]
        style A1 fill:#dcfce7
        style AI fill:#dcfce7
        style Coach fill:#dcfce7
        style Session fill:#dcfce7
        style Result fill:#dcfce7
    end
```

### 📊 기대효과

| 지표 | Before | After | 변화 | 검증 |
|---|---|---|---|---|
| EAP 활용률 | **1%** | **26%** | **26배↑** | ⚠ 벤더 주장 |
| 우울 개선 | — | **58%** (2.46세션) | — | ⚠ 벤더 주장 |
| 불안 개선 | — | **49%** (1.4세션) | — | ⚠ 벤더 주장 |
| 절약 | — | **$1,070/참가자** | — | ⚠ 벤더 주장 |

---

# ━━━ 6. Employee Experience & HR Ops ━━━

## 6-1. Moderna — Ask HR Routing ⭐⭐ (conf 0.70, wiki 최고)

### 🔵 Process Flow (routing)

```mermaid
flowchart LR
    E[직원] -->|자연어 질문| A["Ask HR<br/>(centralized GPT)"]
    A -->|performance 질문| P[Performance GPT]
    A -->|career 질문| C[Career GPT]
    A -->|benefits 질문| B[Benefits GPT]
    P --> E
    C --> E
    B --> E
    A -.->|fallback 미확인| HR[인간 HR 팀]
    classDef fact fill:#dcfce7,stroke:#16a34a
    classDef unknown stroke-dasharray: 5 5
    class E,A,P,C,B fact
    class HR unknown
```

### 🟢 System Architecture (2-layer 구조)

```mermaid
flowchart TB
    User[Moderna 직원<br/>5,000명] --> CGE[ChatGPT Enterprise]
    CGE --> AskHR["Ask HR Custom GPT"]
    AskHR --> Spec["Specialized GPTs<br/>(performance/career/benefits)"]
    CGE -.->|관계 미확인| mChat[mChat<br/>2023~ OpenAI API]
    Spec -.->|연동 미공개| HRIS[(Core HRIS)]
    Spec -.->|연동 미공개| BenSys[(Benefits 시스템)]
    classDef fact fill:#dcfce7,stroke:#16a34a
    classDef unknown stroke-dasharray: 5 5,fill:#fef9c3
    class User,CGE,AskHR,Spec fact
    class mChat,HRIS,BenSys unknown
```

### 🏢 Org Structure (HR+IT 병합)

```mermaid
flowchart TD
    CEO[Moderna CEO] --> CPDO["Tracey Franklin<br/>Chief People &<br/>Digital Technology Officer"]
    CPDO --> People[People Function]
    CPDO --> Tech[Digital Technology]
    People -.->|협업| GPT[Custom GPT 팀]
    Tech -.->|협업| GPT
    classDef fact fill:#dcfce7
    class CEO,CPDO,People,Tech fact
    classDef unknown fill:#fef9c3,stroke-dasharray: 5 5
    class GPT unknown
```

## 6-2. IBM — AskHR Agentic (conf 0.45)

### 🔵 Process Flow (agentic — 작업 수행 수준)

```mermaid
flowchart LR
    Emp[IBM 직원<br/>270,000명] -->|자연어 요청| AskHR[AskHR Agent<br/>watsonx Orchestrate]
    AskHR -->|정책 Q&A| Ans[답변]
    AskHR -->|compensation<br/>guidance| Mgr[매니저에<br/>budget 배분 제안]
    AskHR -->|recognition| Rec[watsonx 메시지 생성<br/>+ 포인트 부여]
    AskHR -->|expense| Exp[자동 처리]
    AskHR -.->|복잡 케이스| Human[HR Specialist]
    classDef fact fill:#dcfce7
    classDef unknown stroke-dasharray: 5 5
    class Emp,AskHR,Ans,Mgr,Rec,Exp fact
    class Human unknown
```

### ⚡ HR AI Maturity 3단계 비교

```mermaid
flowchart LR
    subgraph "Stage 1: FAQ 챗봇"
        S1[직원 질문] --> FAQ[규칙 기반<br/>FAQ 답변]
    end
    subgraph "Stage 2: Routing GPT (Moderna)"
        S2[직원 질문] --> Route["Ask HR<br/>(분기)"]
        Route --> Spec[Specialized<br/>GPTs]
    end
    subgraph "Stage 3: Agentic (IBM)"
        S3[직원 요청] --> Agent["AskHR Agent<br/>(작업 수행)"]
        Agent --> Action["compensation 제안<br/>recognition 생성<br/>expense 처리"]
    end
    style S1 fill:#fee2e2
    style FAQ fill:#fee2e2
    style S2 fill:#fef9c3
    style Route fill:#fef9c3
    style Spec fill:#fef9c3
    style S3 fill:#dcfce7
    style Agent fill:#dcfce7
    style Action fill:#dcfce7
```
_빨간→노랑→녹색: HR AI maturity 진화. 대부분 기업이 Stage 1~2, IBM이 유일하게 Stage 3._

---

# ━━━ 7. Strategic Workforce & Governance ━━━

## 7-1. Amazon — HR 부서 15% 감축 (conf 0.45)

### 🔵 Impact Flow

```mermaid
flowchart TD
    AI["$100B AI 투자<br/>(2025)"] --> Auto["HR 업무 자동화<br/>(채용·분석·운영)"]
    Auto --> Cut["PXT 조직<br/>15% 감축<br/>(~1,500명)"]
    Auto --> Hire["250,000명<br/>계절직 채용<br/>(warehouse)"]
    Cut --> Reinvest["프로그래머·영업<br/>AI 엔지니어 채용 증가"]
    style Cut fill:#fee2e2,stroke:#dc2626
    style Hire fill:#dcfce7,stroke:#16a34a
    style Reinvest fill:#dbeafe,stroke:#2563eb
```
_빨간 = 감축, 녹색 = 채용, 파란 = 재투자. "White-collar 자동화 + Blue-collar 채용"의 구조적 이중성._

---

# ━━━ 🇰🇷 한국 특화 ━━━

## KR-1. LG CNS — 에이전틱 AI HR (아키텍처 공개 유일 사례)

### 🟢 System Architecture (4-Component, 국내 유일 공개)

```mermaid
flowchart TB
    Data["수만 건<br/>자기소개서·인적성·인사문서"] --> KL["Knowledge Lake<br/>(지식 저장소)"]
    KL --> Hub["Hub<br/>(중앙 허브)"]
    Hub --> Refiner["Refiner<br/>(정제·분석)"]
    Refiner --> Router["Router<br/>(라우팅·추천)"]
    Router --> Rec["적합 인재 추천"]
    Router --> Q["면접 질문<br/>자동 생성"]
    Rec --> HR[인사 담당자]
    Q --> HR
    classDef fact fill:#dcfce7
    class Data,KL,Hub,Refiner,Router,Rec,Q,HR fact
```
_범례: 전체 녹색 = LG 공식 보도에서 확인. **국내 HR AI 중 유일하게 아키텍처 컴포넌트명을 공개한 사례.**_

## KR-2. 더존비즈온 — ONE AI 연말정산 (한국 특유 영역)

### 🔵 Process Flow (End-to-End)

```mermaid
flowchart LR
    Start[연말정산<br/>시즌 시작] -->|대상자 식별| Target[대상자 DB]
    Target -->|자동 안내| Emp[직원]
    Emp -->|간소화 자료| NTS["국세청 간소화<br/>PDF 자동 다운로드"]
    NTS --> Valid["데이터 검증<br/>세액 예측"]
    Emp -->|추가 증빙| OC["원챔버<br/>업로드"]
    OC --> Valid
    Valid --> Result[결과 안내]
    Result --> HR{"HR 모니터링<br/>총괄현황판"}
    HR -->|확정| Homtax["홈택스<br/>자동신고"]
    Homtax --> Report["요약보고서<br/>지급명세서"]
    classDef fact fill:#dcfce7,stroke:#16a34a
    class Start,Target,Emp,NTS,Valid,OC,Result,HR,Homtax,Report fact
```
_**글로벌 벤더(Workday·SAP)가 구조적으로 들어올 수 없는 한국 특유 영역.**_

---

# ━━━ 교차 분석 ━━━

## 기업 × 카테고리 매트릭스

| 기업 | 1.TA | 2.Onb | 3.L&D | 4.Perf | 5.TR | 6.EX | 7.Gov |
|---|---|---|---|---|---|---|---|
| **Moderna** | | | | ★ | ★ | ⭐⭐ | |
| **Walmart** | | | ★ | | | ⭐ | |
| **IBM** | | | | | | ⭐ | |
| **JPMorgan** | ★ | | | | | ★ | |
| **Siemens** | | | ⭐ | | | ★ | |
| **Chipotle** | ⭐ | | | | | | |
| **Schneider** | | ⭐ | | | | | |
| **J&J** | | | ⭐⭐ | | | | |
| **HSBC** | ★ | ★ | | | | | |
| **Meta** | | | | ⭐ | | | |
| **Amazon** | | | | | | | ⭐ |
| **Deloitte** | | | | | | ★ | ★ |
| 🇰🇷 **SK Group** | ⭐ | | | | | | |
| 🇰🇷 **마이다스아이티** | ⭐ | | | | | | |
| 🇰🇷 **더존비즈온** | | | | | ★ | | |
| 🇰🇷 **LG CNS** | ★ | | | | | | |
| **BetterUp** | | | | ⭐ | | | |
| **Spring Health** | | | | | ★ | | |

범례: ⭐⭐ = 최고 검증, ⭐ = 대표 사례, ★ = 추가 사례

---

## HR AI Maturity Scale — 기업 포지셔닝

```mermaid
quadrantChart
    title HR AI 성숙도 (자동화 수준 vs HR 영역 커버)
    x-axis "단일 영역" --> "다영역 통합"
    y-axis "보조/추천" --> "자율/Agentic"
    Moderna (Ask HR + GPTs): [0.65, 0.45]
    IBM (AskHR watsonx): [0.35, 0.85]
    Walmart (Ask Sam + Tools): [0.55, 0.40]
    Chipotle (Ava Cado): [0.20, 0.70]
    Siemens (reskill+GBS): [0.60, 0.35]
    SK Group (AICT): [0.25, 0.80]
    J&J (Skills AI): [0.50, 0.30]
    Meta (AI mandate): [0.75, 0.25]
    Amazon (PXT cut): [0.30, 0.90]
```
_해석: 오른쪽 위 = 다영역+고자동화(IBM), 왼쪽 위 = 단일 영역+고자동화(SK AICT·Chipotle), 오른쪽 아래 = 다영역+보조 수준(Meta·Siemens)_

---

> **이 문서의 모든 도식은 소스에서 확인된 Fact만 포함합니다.**
> 실선 = 소스 확인, 점선 = 미확인, 빨간 = Before(도입 전), 녹색 = After(도입 후).
> 상세 페이지: [[dashboard]] → 각 use case 클릭.
