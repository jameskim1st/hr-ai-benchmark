---
name: Walmart
type: company
industry: [retail]
region: [na, global]
headquarters: Bentonville, Arkansas, USA
size_employees: 2300000
revenue_usd_b: 648
public: true
ticker: WMT
ingested_first: 2026-04-12
last_confirmed: 2025-10-02
---

# Walmart

세계 최대 리테일러. 2.3M 직원, 10,500+ 매장. **HR AI 최대 규모 배포**: Ask Sam(900k 사용자, 주 3M 질문) + 1.5M 직원 AI 도구 + 50k 리스킬링 + AI Interview Coach.

## HR AI 전략 — "People-led, Tech-powered"

Walmart의 HR AI 접근은 **"사람이 주도하고 기술이 지원"**이라는 프레이밍이 핵심. AI를 "사람 대체"가 아닌 "사람 강화"로 포지셔닝.

## 📊 Walmart HR AI Use Cases (Live)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  primary_category AS "카테고리",
  subcategory AS "중그룹",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE contains(company, "Walmart")
SORT confidence DESC
```

## HR 대그룹 커버리지

```dataview
TABLE WITHOUT ID
  primary_category AS "HR 대그룹",
  length(rows) AS "Use Case 수",
  rows.file.link AS "페이지들"
FROM "wiki/usecases"
WHERE contains(company, "Walmart")
GROUP BY primary_category
```

## 핵심 수치

| 지표 | 값 | 출처 |
|---|---|---|
| Ask Sam 사용자 | **900,000명** | HR Executive |
| 주간 질문 수 | **3,000,000+** | HR Executive |
| AI 도구 배포 대상 | **1,500,000 매장 직원** | Walmart Corporate |
| 리스킬링 계획 | **50,000명** (캐셔→기술직) | 보도 |
| Workday HCM 절약 | **$35M/년** | Workday |

## Consulting Angle

- **리테일 HR AI의 교과서**: 전 세계에서 가장 큰 규모의 HR AI 배포 + 리스킬링 병행
- **"People-led, Tech-powered"** 프레이밍: 한국 대기업 CHRO에게 AI 도입 narrative 전략의 모범 사례
- **한국 리테일(이마트·롯데마트·GS리테일) 적용**: 매장 직원 대상 음성 AI 어시스턴트 개념 참고

## Related
- Use cases: [[walmart-ask-sam-workforce-ai]], [[walmart-ai-frontline-workforce]]
