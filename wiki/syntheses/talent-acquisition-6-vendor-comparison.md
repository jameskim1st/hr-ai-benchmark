---
type: synthesis
topic: ta-vendor-comparison
generated_at: 2026-04-12
entities_referenced:
  - paradox
  - eightfold-ai
  - midas-it
  - sk-ax
  - wantedlab
  - lgcns-agentic-ai-hr
tags: [talent-acquisition, vendor-comparison, recruiting, ai-assessment, conversational-ai]
consulting_priority: high
---

# 채용 AI 6개 벤더/솔루션 비교표

> 🎯 **컨설팅 도구**: 본 비교표는 wiki에 수집된 6개 Talent Acquisition AI 사례를 나란히 놓고, **어떤 클라이언트에 어떤 솔루션이 적합한지** 판단하기 위한 reference입니다. 제안서 "벤더 비교" 슬라이드의 직접적 재료.

---

## 1. 한 눈 비교표

| 축 | Paradox Olivia | Eightfold AI | 🇰🇷 마이다스아이티 | 🇰🇷 SK AX AICT | 🇰🇷 LG CNS | 🇰🇷 원티드랩 |
|---|---|---|---|---|---|---|
| **접근법** | 대화형 AI (지원자 대면) | Skills intelligence (매칭) | 시뮬레이션 역량 예측 | AI 활용 능력 평가 | 서류 분석+면접 질문 생성 | LLM 인재 검색 |
| **핵심 기능** | Chat screening, 스케줄링, 오퍼 | AI Interviewer, Digital Twin, skills matching | 성향파악·전략게임·영상면접 | AICT 필기 + AI 1차 면접 | 자기소개서·인적성 분석 → 추천·질문 | 자연어 검색, 추천 사유 제시 |
| **대표 고객** | **Chipotle** (3,500매장), GM, 7-Eleven | Deloitte 제휴, Gartner 4.6/5 | ★ **기아·KB증권·신한·CJ** 등 10+ | **SK C&C·SKT·SK브로드밴드** | **LG 그룹 (추정)** | 3.5만 기업 (채용 플랫폼) |
| **핵심 metric** | ⚠ 75% time-to-hire↓ | ⚠ 90% time-to-first-interview↓ | ★ **Nature 논문: 면접관보다 정확** | ⚠ 100배 빠름, 1,000명/시간 | ⚠ 26% 생산성↑ | (신제품, metric 없음) |
| **학술 검증** | 🚫 | 🚫 | ★ **✅ KAIST + Nature** | 🚫 | 🚫 | 🚫 |
| **주력 산업** | 식음료·소매·hospitality | 전 산업 (enterprise) | 전 산업 (대기업·공공) | IT·통신 (SK 그룹) | IT·서비스 (LG 그룹) | 전 산업 (SMB~mid) |
| **HITL 수준** | Screening 자동, 채용결정 사람 | Recommend-only | **평가는 AI, 결정은 사람** | **1차 면접까지 AI 100%** | Recommend-only | Recommend-only |
| **한국 대응** | 🚫 (한국어 미확인) | 🚫 (한국 ref 없음) | ✅ 한국 특화 | ✅ 한국 특화 | ✅ 한국 특화 | ✅ 한국 특화 |
| **wiki confidence** | 0.35 | 0.20 | **0.50** ★ | 0.25 | 0.25 | 0.20 |

---

## 2. 4가지 축으로 분석

### 축 1: "무엇을 자동화하나?" — 채용 프로세스 커버리지

```
채용 흐름:  JD 작성 → 소싱 → 스크리닝 → 평가 → 면접 → 오퍼 → 온보딩
                        ↑           ↑        ↑       ↑      ↑
원티드랩 ──────────────┘           │        │       │      │
Paradox ───────────────────────────┘        │       │      │
마이다스아이티 ──────────────────────────────┘       │      │
SK AX AICT ─────────────────────────────────────────┘      │
Eightfold ────────────────────────────(전 과정 커버 주장)───┘
LG CNS ────────────────────────┘────────────┘
```

### 축 2: "얼마나 과감한가?" — AI Autonomy 수준

```
Recommend-only     Assess          Decide           Full Auto
(추천만)           (평가)          (결정보조)        (완전자동)
    │                │                │                │
원티드랩          마이다스아이티      Paradox         SK AX AICT
Eightfold         LG CNS           (screening)      (1차면접)
```

**SK AX가 가장 과감** — 1차 면접까지 AI 100%. **이건 양날의 검**: 빠르지만 bias·공정성 리스크도 가장 큼.

### 축 3: "얼마나 신뢰할 수 있나?" — 검증 수준

```
  학술 검증     Tier 1 분석     Tier 2 매체     벤더 자체
      │            │               │              │
마이다스아이티   (없음)         원티드랩(AI타임스)  Paradox
  (Nature)                    LG CNS(LG미디어)   Eightfold
                              SK AX(ZDNet)      SK AX(공식)
```

**마이다스아이티의 Nature 논문이 유일한 학술 검증** — 나머지 5개는 모두 벤더 자체 주장 또는 매체 전달 수준.

### 축 4: "어떤 클라이언트에 맞나?"

| 클라이언트 유형 | 최적 솔루션 | 이유 |
|---|---|---|
| **한국 대기업 공채** | 🇰🇷 마이다스아이티 + SK AX (또는 LG CNS) | 학술 검증 + 대규모 처리 |
| **한국 중견기업 채용** | 🇰🇷 원티드랩 | 비용 합리적, 360만 풀 접근 |
| **글로벌 다국적 고볼륨** | Paradox | 다국어, 식음료·소매 특화 |
| **글로벌 skills-based 전환** | Eightfold | Skills intelligence + Deloitte 제휴 |
| **한국 공공기관** | 🇰🇷 마이다스아이티 | Nature 논문 = 공정성 근거 |
| **AI-forward 실험적 조직** | SK AX AICT (또는 마이다스아이티+SK 병행) | 가장 과감한 자동화 |

---

## 3. 컨설팅 사용법 — "이 비교표를 어떻게 쓰나"

### 시나리오 A: 한국 대기업 CHRO가 "채용 AI 도입하고 싶다" 할 때

1. **§2 축 1~4를 순서대로 보여줌** — "무엇을 자동화할지, 얼마나 과감할지, 어떤 검증이 있는지, 우리 유형에 맞는 건 뭔지"
2. **마이다스아이티의 Nature 논문을 첫 번째로 제시** — "학술 검증이 있는 유일한 옵션"
3. **SK AX의 "1차 면접 완전 자동화"를 도전적 옵션으로 제시** — "가장 과감하지만 bias 리스크도 가장 큼"
4. **"두 가지를 병행할 수도 있다"** — 평가는 마이다스아이티(검증됨), 프로세스 자동화는 SK AX(빠름)

### 시나리오 B: 글로벌 기업이 "한국 법인 채용 AI" 검토할 때

1. **Paradox·Eightfold의 한국 대응 미확인** 사실을 먼저 고지
2. **한국어·한국 문화·법규(채용절차공정화법) 대응**이 핵심 필터 → 국내 벤더 우위
3. **"글로벌 벤더 + 한국 벤더 병행"** 가능성 검토: 글로벌 표준은 Eightfold, 한국 법인은 마이다스아이티

---

## 4. 한계 및 주의

- **6개 중 5개가 벤더 자체 주장 metric** — 마이다스아이티만 학술 검증
- **Paradox와 Eightfold의 한국 레퍼런스 0건** — 한국 적용 가능성은 추정일 뿐
- **비용 비교 불가** — 6개 벤더 모두 가격 미공개 (RFP 기반)
- **"최적" 판단은 클라이언트 context 의존** — 이 표는 **판단 기준(framework)**이지 **답(answer)**이 아님

---

## 5. 관련 wiki 페이지

- [[chipotle-paradox-olivia]], [[eightfold-ai-talent-intelligence]], [[midas-inair-ai-assessment-korea]], [[sk-group-aict-ai-recruitment]], [[lgcns-agentic-ai-hr]], [[wantedlab-ai-recruiting-agent]]
- Vendor: [[paradox]], [[midas-it]], [[sk-ax]], [[wantedlab]]
- 한국 전체 비교: [[korean-3-si-hr-ai-comparison]]
