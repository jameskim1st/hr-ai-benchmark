---
name: Unilever
type: company
industry: [fmcg, consumer-goods]
region: [global]
headquarters: London, UK / Rotterdam, Netherlands
size_employees: 128000
revenue_usd_b: 60
public: true
ticker: UL
ceo: Hein Schumacher (2023-07~)
ingested_first: 2026-04-12
last_confirmed: 2026-05-06
---

# Unilever

글로벌 FMCG 대기업. **HR AI 선도사** — 2019년 Gloat 기반 FLEX Experiences talent marketplace로 시작 → 2024-09 Accenture GenWizard 전사 GenAI 전환으로 무게중심 이동. CEO **Hein Schumacher** (2023-07~). 자체 AI 연구센터 **Horizon3 Labs** 운영.

## 조직 규모
- 약 128,000명 직원, 190개국
- $60B+ 연매출
- 400+ 브랜드

## HR AI 주요 사례

### 1. FLEX Experiences (Gloat 기반, 2019~ 활성)
- **파트너**: [[gloat]] (NY 기반 talent marketplace 벤더, 2026 Workforce OS·Agentic HR로 확장)
- **목적**: 직원 ↔ 단·장기 프로젝트 AI 매칭
- **2019-12 출시 시점**: 30,000+ 직원, 90+ 개국, 95% 사용자 endorsement ([[i4cp-unilever-flex-2019-12]])
- **2024 누적 메트릭** (Gloat 케이스 스터디 + i4cp 업데이트):
  - **90,000+ 직원 등록** (3x 확장)
  - **누적 700,000+ 시간 capacity unlock** (2019: 26K hrs → 2024: 700K)
  - "최근 2개월간 300,000+ 시간 unlock" — 정상 운영 활발
  - 95% 직원 endorsement 유지
  - ⚠️ 자사 보고: 41% 생산성 증가, 20% 내부 협업 시간 증가, 67% opportunities → 여성 직원
- **rebrand·sunset 흔적 없음** — 여전히 활성 운영

### 2. Accenture GenWizard 전사 GenAI 파트너십 (2024-09 확장, 무게중심 이동)
- 파트너: Accenture (GenWizard 플랫폼, 350+ 특허·사전 구축 GenAI 도구)
- **23,000명 직원 GenAI 트레이닝**
- **500+ AI 프로젝트 배포**, 그중 **330+ 라이브** (2024년 말 기준)
- "Horizon3 Labs" — Unilever 자체 글로벌 AI 연구센터
- 출처: Tier 2 Computer Weekly·CIO Inc·Tier 3 Accenture Newsroom

### 3. AI 채용 파이프라인 (HireVue + Pymetrics, 2016~ 코어 유지)
- ⚠️ 자사 보고:
  - Time-to-hire **4개월 → 4주** (90% 단축)
  - **16% 다양성 증가**
- **2025 신규**: 탈락 후보자에게 **GenAI 개인화 피드백** 추가

### 4. 추가 협업 (2025-2026)
- **Vector Institute 협업** (2025) — AI R&D 거버넌스
- **Google Cloud agentic AI deal** (2025-2026, Tier 2 CIO Dive) — 차세대 agentic AI 기반

## Hein Schumacher CEO 시기 HR AI 전략 (2023-07~)
- FLEX는 유지하되 **무게중심을 전사 GenAI(Accenture GenWizard)로 이동**
- 자체 AI R&D 인프라 구축 (Horizon3 Labs · Vector Institute · Google Cloud)
- Reactive talent marketplace → Proactive workforce AI transformation

## HR 대그룹 커버리지 (Unilever 수집 현황)

```dataview
TABLE WITHOUT ID
  primary_category AS "HR 대그룹",
  length(rows) AS "Use Case 수",
  rows.file.link AS "페이지들"
FROM "wiki/usecases"
WHERE company = "Unilever"
GROUP BY primary_category
```

## 📊 Unilever HR AI Use Cases (Live)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  primary_category AS "대그룹",
  subcategory AS "중그룹",
  stage AS "단계",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE company = "Unilever"
SORT confidence DESC
```

## Consulting Angle

- **"내부 인력 재배치"의 글로벌 대표 reference**: 한국 대기업(특히 계열사 간 이동이 필요한 그룹사)에 proof-point. 단 2019~2024 5년 운영으로 90K 도달 — 5년 시간 horizon 인정 필요
- **2024 무게중심 이동 시사점**: Unilever는 talent marketplace에서 **전사 GenAI 변환**으로 진화 — 한국 대기업 컨설팅 시 "talent marketplace는 시작점, 종착점 아님" 메시지
- **Accenture-GenWizard 23K 트레이닝 + 500+ 프로젝트** — 한국 대기업 mass GenAI reskilling reference (Accenture 자사 사례 [[accenture-mass-genai-reskilling]]와 연결)
- **주의점**:
  - FLEX의 "매니저 승인 불필요" 원칙이 한국 연공 문화에서 작동할지 미검증
  - DEI 효과(여성 직원 67% opportunities) 부분은 한국 적용 시 별도 설계 필요
  - Unilever는 2019년 pre-COVID 시점에 이미 디지털 HR 인프라가 성숙 — 한국 대기업이 0에서 시작해 같은 수준에 도달하려면 "talent marketplace 도입"만으로는 부족, **skills ontology + 직무 체계 재설계** 선행 필수
- **반면교사 / 포지셔닝**:
  - 컨설팅 제안 시 "Unilever처럼" 대신 **"Unilever 5년 경로의 단축 버전 + Accenture GenWizard 가속화"** 권장
  - Hein Schumacher CEO의 무게중심 이동은 "talent marketplace 단독 ROI는 한계, 전사 GenAI와 결합 필수" 시사

## Related
- Vendor: [[gloat]]
- Use cases: [[unilever-flex-gloat-talent-marketplace]]
- Companies (mass GenAI reference): [[accenture-mass-genai-reskilling]]
- Sources: [[i4cp-unilever-flex-2019-12]] · [[accenture-unilever-genai-2024-09]] (신규) · [[gloat-unilever-customer-success-2024]] (신규)
