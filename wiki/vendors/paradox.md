---
name: Paradox
type: vendor
page_type: vendor
vendor_type: point-solution       # 채용 특화 point solution
category: [conversational-ai, recruiting, ats]
headquarters: Scottsdale, Arizona, USA
founded: 2016
public: false
products:
  - Olivia (대화형 AI 채용 어시스턴트)
  - Conversational ATS
  - Text-to-apply
ingested_first: 2026-04-12
last_confirmed: 2026-04-12
---

# Paradox

대화형 AI 기반 채용 자동화 벤더. 주력 제품 **Olivia**는 후보자와 대화형 interface로 지원·스크리닝·스케줄링을 처리. **고볼륨·시급 채용(식음료·소매·hospitality)** 영역에서 특히 강함.

## 제품 범위 (HR 도메인 매핑)

| 제품/기능 | HR 카테고리 |
|---|---|
| Olivia conversational apply | 1. Talent Acquisition → Sourcing & Attraction |
| Conversational screening | 1. Talent Acquisition → Screening & Assessment |
| Interview scheduling automation | 1. Talent Acquisition → Interview & Selection |
| Text-to-apply | 1. Talent Acquisition → Sourcing & Attraction |

전 영역이 **1. Talent Acquisition**에 집중 — point solution의 교과서적 예.

## 주요 고객 (공개된 것)

[[paradox-clients-stories-2026-04]] 에서 확인된 40+ 고객사 중 대표:

### 식음료·소매 (주력 버티컬)
- **Chipotle** — ⚠️ 벤더 주장: 75% time-to-hire 감소
- **7-Eleven** — ⚠️ 벤더 주장: 50% time-to-hire, 주 40,000시간 절약
- **Captain D's** — ⚠️ 벤더 주장: 75% 이직률 감소
- **Sodexo** — ⚠️ 벤더 주장: 60% time-to-fill 감소
- **Flynn Group** — ⚠️ 벤더 주장: time-to-hire 13~14일 → 4일

### 대기업·제조
- **General Motors** — ⚠️ 벤더 주장: 연 $2M 절약
- **Johnson Controls** — ⚠️ 벤더 주장: 89% 지원 완료율
- **Medtronic** — ⚠️ 벤더 주장: 3개월 6,000 인터뷰

### 헬스케어
- **Essentia Health** — ⚠️ 벤더 주장: 스케줄된 인터뷰 100% 증가

### 기술 기업
- **Workday** (채용팀이 직접 Paradox 사용 — 흥미로운 교차) — ⚠️ 벤더 주장: 2년 23,000시간 절약
- **Dell** — ⚠️ 벤더 주장: 후보자당 2~3시간 → 30초~1분

## 독립 검증 상태

- **Chipotle 건**: Tier 2 HR Dive (2024-10-25) + CNBC (2025-07-28) 보도 확보 — 12일→3.5일, 지원 완료율 50%→85% ([[chipotle-paradox-olivia]])
- 그 외 고객 metric은 Paradox 자체 주장 (위 목록)
- Bersin·Gartner·Forrester 등의 독립 분석 레퍼런스는 미확보

## Consulting Angle

- **강점**: 고볼륨 시급 채용에 **명확한 가치** (업종 matching)
- **약점**: 정규직·지식노동자 채용엔 fit이 낮을 가능성 (주장과 반례 모두 없음)
- **리스크**: Chipotle 외 metric은 벤더 자체 주장이라 **제안서 단독 인용 위험**. 독립 검증 소스 확보 후 사용 권장.
- **파생 질문**: 한국 시급 채용 시장(편의점·카페·delivery)에 적용 가능한가? 국내 벤더(마이다스아이티·원티드)와 비교는?

## 관련 use cases

```dataview
TABLE WITHOUT ID file.link AS "Use Case", company AS "고객", primary_category AS "대그룹", evidence_grade AS "등급", depth AS "depth"
FROM "wiki/usecases" OR "wiki/enterprise-ai"
WHERE contains(vendor, "Paradox")
SORT evidence_grade ASC
```
> 목록은 Dataview 자동 생성 — 손으로 갱신하지 않음

## Related
- Use cases: 상단 Dataview 표 (자동 생성 — 손으로 갱신하지 않음)
- Sources: [[paradox-clients-stories-2026-04]] · [[hrdive-chipotle-paradox-2024-10]] · [[cnbc-chipotle-ava-cado-2025-07]]
- Referenced companies: [[chipotle]], [[walmart]], [[workday]]
