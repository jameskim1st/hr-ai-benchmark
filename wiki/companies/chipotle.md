---
name: Chipotle Mexican Grill
type: company
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
- **⚠️ 벤더 주장**: 75% time-to-hire 감소 (출처: [[paradox-clients-stories-2026-04]])
- **독립 검증**: **없음** — Paradox 자체 주장 외 Tier 1·2 확보 안 됨

## HR 대그룹 커버리지 (Chipotle 수집 현황)

```dataview
TABLE WITHOUT ID
  primary_category AS "HR 대그룹",
  length(rows) AS "Use Case 수",
  rows.file.link AS "페이지들"
FROM "wiki/usecases"
WHERE company = "Chipotle Mexican Grill"
GROUP BY primary_category
```

## 📊 Chipotle HR AI Use Cases (Live)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  primary_category AS "대그룹",
  subcategory AS "중그룹",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE company = "Chipotle Mexican Grill"
SORT confidence DESC
```

## 이 페이지의 한계
- 현재 본 wiki는 **Paradox 벤더 페이지 외 Chipotle에 대한 독립 소스 0건**. 즉 Chipotle의 HR AI 운영 전략 전반에 대한 정보 없음. 이 페이지는 "Paradox 사용" 사실 기록용 stub에 가까움.
- 보강 필요: Chipotle 공식 press release, HR Dive/SHRM 커버리지, 10-K의 workforce management 언급

## Consulting Angle

- 한국 **시급직 채용 자동화** 컨설팅의 reference로 참고 가능 (편의점·카페·delivery)
- 단, Chipotle이 Paradox에만 의존하는지 다른 HR tech stack은 무엇인지 **확인 불가** → 전체 HR 전략의 한 조각으로만 다뤄야 함

## Related
- Vendor: [[paradox]]
- Use cases: [[chipotle-paradox-olivia]]
- Sources: [[paradox-clients-stories-2026-04]]
