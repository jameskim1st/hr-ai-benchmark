---
name: Chipotle Mexican Grill
type: company
page_type: company
industry: [restaurant, food-service, retail]
region: [na]
headquarters: Newport Beach, California, USA
size_employees: 110000
public: true
ticker: CMG
ingested_first: 2026-04-12
last_confirmed: 2026-04-12
---

# Chipotle Mexican Grill

미국 멕시칸 fast-casual 레스토랑 체인. 약 3,500+ 매장, 110,000명 이상 직원. **고볼륨 시급직 채용** 케이스로 Paradox Olivia의 레퍼런스 중 가장 자주 인용되는 사례.

## HR AI 주요 사례

### Paradox Olivia 기반 채용 자동화
- **파트너**: [[paradox]] (대화형 AI 채용 플랫폼)
- **자사 브랜딩**: "Ava Cado" — 2024-10-22 Chipotle 공식 발표, CHRO Ilene Eskenazi 인용 ([[chipotle-newsroom-ava-cado-2024-10]])
- **⚠️ 벤더+회사 공동 주장**: 75% time-to-hire 감소 (출처: [[paradox-clients-stories-2026-04]], [[chipotle-newsroom-ava-cado-2024-10]])
- **독립 소스**: Tier 2 **HR Dive (2024-10-25)** + **CNBC (2025-07-28)** 확보 — CNBC에서 12일→3.5일, 지원 완료율 50%→85% 수치 확인 ([[hrdive-chipotle-paradox-2024-10]], [[cnbc-chipotle-ava-cado-2025-07]]). bias audit·편향 독립 검증은 여전히 부재

## HR 대그룹 커버리지 (Chipotle 수집 현황)

```dataview
TABLE WITHOUT ID
  primary_category AS "HR 대그룹",
  length(rows) AS "Use Case 수",
  rows.file.link AS "페이지들"
FROM "wiki/usecases" OR "wiki/enterprise-ai"
WHERE company = "Chipotle Mexican Grill"
GROUP BY primary_category
```

## 📊 Chipotle HR AI Use Cases (Live)

```dataview
TABLE WITHOUT ID file.link AS "Use Case", primary_category AS "대그룹", evidence_grade AS "등급", depth AS "depth", stage AS "단계", last_confirmed AS "확인"
FROM "wiki/usecases" OR "wiki/enterprise-ai"
WHERE company = "Chipotle Mexican Grill" OR contains(company, "Chipotle") OR contains(tags, "chipotle")
SORT evidence_grade ASC, last_confirmed DESC
```
> 목록은 Dataview 자동 생성 — 손으로 갱신하지 않음

## 이 페이지의 한계
- 본 wiki의 Chipotle 소스는 **채용(Ava Cado) 1건에 집중** — Chipotle의 HR AI 운영 전략 전반(채용 외 영역)에 대한 정보 없음.
- 보강 필요: SHRM 커버리지, 10-K의 workforce management 언급, Paradox 외 HR tech stack

## Consulting Angle

- 한국 **시급직 채용 자동화** 컨설팅의 reference로 참고 가능 (편의점·카페·delivery)
- 단, Chipotle이 Paradox에만 의존하는지 다른 HR tech stack은 무엇인지 **확인 불가** → 전체 HR 전략의 한 조각으로만 다뤄야 함

## Related
- Vendor: [[paradox]]
- Use cases: 상단 Dataview 표 (자동 생성 — 손으로 갱신하지 않음)
- Sources: [[chipotle-newsroom-ava-cado-2024-10]] · [[hrdive-chipotle-paradox-2024-10]] · [[cnbc-chipotle-ava-cado-2025-07]] · [[paradox-clients-stories-2026-04]]
