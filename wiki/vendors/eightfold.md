---
name: Eightfold
type: vendor
slug: eightfold
website: https://eightfold.ai
hq: Santa Clara, California, USA
founded: 2016
founders: Ashutosh Garg, Varun Kacholia (둘 다 ex-Google)
industry: [hr-tech, talent-intelligence, point-solution]
ingested_first: 2026-05-05
last_confirmed: 2026-05-05
---

# Eightfold AI

## 회사 개요

- **본사**: Santa Clara, California, USA
- **설립**: 2016년 (Ashutosh Garg, Varun Kacholia 공동창업 — 둘 다 ex-Google)
- **직원**: ~700명 (2024 LinkedIn 추정)
- **자금**: Total funding $410M+ (Series F 2024). Valuation $2.1B (last reported)
- **모기업**: 독립 (Capital One Ventures·SoftBank Vision Fund 2·Foundation Capital 투자)
- **분사**: ✅ **Viven AI** ($35M seed, 2025-10 stealth exit) — Eightfold 공동창업자가 분사한 별도 회사 ([[viven-ai-digital-twin-coworker]]). PwC 자료에서 "Digital Twin = Eightfold"로 잘못 인용된 사례 정정 필수

## HR AI 제품 lineup (2026 기준)

- **Talent Intelligence Platform** — 채용·내부이동·후계·learning 통합. Capabilities Matrix가 ⚠️ 벤더 주장 1.6B+ profile 기반 skills inferencing
- **AI Interviewer** (2025) — 자동 1차 면접, ⚠️ 벤더 주장 time to first interview 90%↓
- **Job Intelligence Engine** — role 정의·job architecture 자동 생성·refresh
- **Agentic AI** (Cultivate 2025 발표) — sourcing·screening·interview scheduling 자율 워크플로

## 핵심 고객사

### 글로벌
- **Mastercard**: ⚠️ 자사 보고 93% 등록률·42% 월 engagement·24h 인터뷰 스케줄링·1M project hours ([[eightfold-ai-talent-intelligence]])
- **HSBC**: 140K 직원 multi-vendor 스택 (Eightfold + Gloat) ([[hsbc-eightfold-gloat-multi-vendor]])
- **Bayer, Allegis, Tata Consultancy Services** (Eightfold 공식 customer page)

### 한국
- _미공개_ — 본 wiki 기준 0건

## 분석가 포지션

- ✅ Gartner Peer Insights: **4.6/5** (Tier 1 독립, [[eightfold-ai-talent-intelligence]])
- ⚠️ Bersin (Tier 1): SAP가 Eightfold를 "displace 대상"으로 지목 (Delta·PepsiCo가 Eightfold 버리고 SF로 통합, [[bersin-successfactors-leapfrog-2024-10]])
- Gartner Magic Quadrant: Talent Acquisition 카테고리 등재 _미공개_ (Talent Intelligence는 별도 emerging category)

## 가격·도입 모델

- **모델**: SaaS subscription, PEPM 또는 module 기반
- **직원당 비용**: _미공개_ (대형 enterprise 시장 추정 $500K~수백만 단위 연간, NDA)
- **도입 기간**: TA module 6~12개월, 통합 모듈 12~18개월

## KR 시장 현황

- **한국 reference**: 0건
- **한국어·로컬화**: 한국어 skills ontology·직무 체계 fit _미검증_ ([[eightfold-ai-talent-intelligence]] 컨설팅 angle 명시)
- **KR sales partner**: Deloitte 글로벌 alliance — Korea 별도 _미공개_

## 컨설팅 RFP 차별화 포인트

### 강점
1. Capabilities Matrix가 가장 큰 skills graph 보유 (⚠️ 벤더 주장 1.6B profile)
2. **Mastercard 정량 adoption 데이터** (93% 등록·42% 월 engagement) — KR 대기업 internal mobility ROI reference
3. Deloitte alliance — implementation partner 확보

### 약점·risk
1. SAP·Workday consolidation 압박 — best-of-breed point solution displaced 위험
2. 모든 metric이 ⚠️ 자사 보고 또는 벤더 주장, Tier 1 독립 검증 부분 부족
3. **한국어 ontology fit 미검증** — 한국 직무 체계(직군·직급)와의 매핑 실증 사례 0건

## 2026 신규 announcement

- Agentic AI 발표 (Cultivate 2025) — sourcing·screening·scheduling 자율화
- HSBC 멀티벤더 스택에서 TA 담당 ([[hsbc-eightfold-gloat-multi-vendor]])
- ⚠️ **Viven AI 분사** (2025-10) — "Digital Twin" 컨셉을 가져갔으나 Eightfold 본체와 별개

## 관련 use cases

```dataview
TABLE WITHOUT ID file.link AS "Use Case", company AS "기업", confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE contains(vendor, "Eightfold")
SORT confidence DESC
```

## Sources

- [Eightfold customer stories](https://eightfold.ai/customers/customer-stories/) — Tier 3
- [PR Newswire 2025 Cultivate](https://www.prnewswire.com/news-releases/talent-intelligence-to-talent-advantage-eightfold-ai-revolutionizes-hr-through-agentic-ai-302449233.html) — Tier 3
- [Mastercard AI culture story 2025](https://www.mastercard.com/us/en/news-and-trends/stories/2025/ai-culture-adoption-experimentation.html) — Tier 4
- [[bersin-successfactors-leapfrog-2024-10]] — Tier 1 (경쟁사 관점)
- [[hsbc-eightfold-gloat-multi-vendor]] — cross-confirmed
