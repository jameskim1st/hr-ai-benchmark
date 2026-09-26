---
name: Sana Labs
type: vendor
page_type: vendor
vendor_type: foundation-model
category: [ai-platform, learning, foundation-model]
headquarters: Stockholm, Sweden
founded: 2016
public: false
products:
  - Sana AI (일반 AI agent platform)
  - Sana Learning (AI-native LMS)
ingested_first: 2026-04-12
last_confirmed: 2025-06-01
stub: true
---

# Sana Labs

> ⚠ **Stub**: 이 페이지는 다른 페이지에서의 참조 해소를 위해 생성된 stub입니다. Sana Labs 단독 리서치는 다음 ingest 라운드에서 보강 필요.

스웨덴 Stockholm 기반 AI 학습 플랫폼 스타트업. 2016년 창립. **Josh Bersin Co.의 Galileo Learn OEM 파트너**로 wiki에 처음 등장. Bersin이 "All-AI native" 카테고리의 대표로 지목한 플랫폼.

> **2025-11 Workday가 $1.1B에 인수** — 2026-03-17 첫 통합 제품 **"Sana for Workday"** 공개 (Sana conversational interface = Workday 신규 UI front door, Sana Learn = AI-native LMS). ⚠️ 벤더 주장: 코스 생성 4개월 → 4일, engagement 275% lift. 상세: [[workday-sana-for-workday-lms]], 출처 [[hr-brew-workday-sana-2026-03]].

## wiki 상의 역할

Sana Labs는 본 wiki에서 **다른 use case의 기반 기술 제공자**로 등장:

- [[bersin-galileo-learn-ai-native-lms]] — Galileo Learn의 AI foundation을 제공 (OEM 관계)
- [[bersin-ld-revolution-2025-06]] — Bersin이 3-way LMS 비교에서 "All-AI native" 대표로 지목
- [[workday-sana-for-workday-lms]] — Workday 인수 후 첫 통합 제품 (2026-03)

## 알려진 customer (본 wiki 기준)

- **Workday** internal leadership academy — [[bersin-ld-revolution-2025-06]]에서 처음 공개됨. 이 사실은 [[workday-as-customer-paradox]] synthesis의 핵심 근거 중 하나. 이후 2025-11 Workday가 Sana를 인수하여 고객 → 모회사로 전환.
- **Klarna·MTV·Polestar** 등 Sana 기존 고객 — [[workday-sana-for-workday-lms]] company 필드 기준
- **Josh Bersin Co.** — Galileo Learn OEM 파트너 관계

## 미공개 / 보강 필요 (stub)

- ❓ Sana Labs 자체 제품과 OEM 관계의 분리 — Sana AI·Sana Learning이 Galileo Learn과 같은 것인지 별개인지 불명
- ❓ Klarna·MTV·Polestar 외 고객 명단·규모
- ❓ Workday 인수 후 Galileo Learn OEM 관계 지속 여부
- ❓ 자체 LLM 개발 vs 상용 API 래핑
- ❓ 가격·scale
- ❓ 독립 Tier 1·2 분석 (Gartner·Forrester LMS Magic Quadrant 등)

## 관련 use cases

```dataview
TABLE WITHOUT ID file.link AS "Use Case", company AS "고객", primary_category AS "대그룹", evidence_grade AS "등급", depth AS "depth"
FROM "wiki/usecases" OR "wiki/enterprise-ai"
WHERE contains(vendor, "Sana")
SORT evidence_grade ASC
```
> 목록은 Dataview 자동 생성 — 손으로 갱신하지 않음

## Related
- Vendor relationship: [[josh-bersin-co]] (OEM) · [[workday]] (모회사, 2025-11~)
- Use cases: 상단 Dataview 표 (자동 생성 — 손으로 갱신하지 않음)
- Synthesis: [[workday-as-customer-paradox]]
- Sources: [[bersin-ld-revolution-2025-06]] · [[hr-brew-workday-sana-2026-03]]
