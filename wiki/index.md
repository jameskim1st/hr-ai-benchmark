# HR AI Benchmark — Index

이 페이지는 wiki 전체의 **카탈로그**입니다. **110건 use case · 59건 source · 20개 company · 13개 vendor · 7개 카테고리 100% 커버 · 10개 synthesis** (2026-05-05 라운드 6 갱신, 기업별 depth 보강).
세부 스키마와 규칙은 [[CLAUDE|CLAUDE.md]] 참조.

## 🧭 주요 진입점

- 📖 **[[guide]]** — 이 wiki 구조 가이드 (처음 보거나 잊어버렸을 때)
- 📤 **[[guide-html-export]]** — Interactive HTML 산출물 생성 가이드 (클라이언트 공유용)
- 📋 **[[dashboard]]** — Dataview 기반 건강 대시보드
- 📚 **카테고리별 보기**: [[01-talent-acquisition]] · [[02-onboarding-transitions]] · [[03-learning-development]] · [[04-performance-talent-management]] · [[05-total-rewards]] · [[06-employee-experience-hr-ops]] · [[07-strategic-workforce-governance]]

---

## 📊 카테고리별 Use Cases (Dataview 자동)

### 전체 카테고리 분포

```dataview
TABLE WITHOUT ID
  primary_category AS "카테고리",
  length(rows) AS "건수",
  round(sum(rows.confidence) / length(rows), 2) AS "평균 신뢰도"
FROM "wiki/usecases"
GROUP BY primary_category
SORT length(rows) DESC
```

### 1. Talent Acquisition (~15건)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  company AS "기업",
  vendor AS "벤더",
  confidence AS "신뢰도",
  region AS "지역"
FROM "wiki/usecases"
WHERE primary_category = "Talent Acquisition"
SORT confidence DESC
```

### 2. Onboarding & Transitions (~7건)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  company AS "기업",
  vendor AS "벤더",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE primary_category = "Onboarding & Transitions"
SORT confidence DESC
```

### 3. Learning & Development (~12건)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  company AS "기업",
  vendor AS "벤더",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE primary_category = "Learning & Development"
SORT confidence DESC
```

### 4. Performance & Talent Management (~10건)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  company AS "기업",
  vendor AS "벤더",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE primary_category = "Performance & Talent Management"
SORT confidence DESC
```

### 5. Total Rewards (~8건)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  company AS "기업",
  vendor AS "벤더",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE primary_category = "Total Rewards"
SORT confidence DESC
```

### 6. Employee Experience & HR Ops (~18건)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  company AS "기업",
  vendor AS "벤더",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE primary_category = "Employee Experience & HR Ops"
SORT confidence DESC
```

### 7. Strategic Workforce & Governance (~11건)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  company AS "기업",
  vendor AS "벤더",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE primary_category = "Strategic Workforce & Governance"
SORT confidence DESC
```

---

## 🏢 Companies · 🛠 Vendors · 📄 Sources

### Companies (Dataview 자동)

```dataview
TABLE WITHOUT ID
  file.link AS "기업",
  industry AS "산업",
  region AS "지역"
FROM "wiki/companies"
SORT file.name ASC
```

### Vendors (Dataview 자동)

```dataview
TABLE WITHOUT ID
  file.link AS "벤더",
  vendor_type AS "유형"
FROM "wiki/vendors"
SORT file.name ASC
```

### Sources (최근 발행 순)

```dataview
TABLE WITHOUT ID
  file.link AS "Source",
  tier AS "Tier",
  publication_date AS "발행"
FROM "wiki/sources"
SORT publication_date DESC
LIMIT 20
```

---

## 🧩 Syntheses (8건)

### 컨설팅 Insight
- ⭐ [[industry-region-landscape]] — **산업별·지역별 HR AI Landscape** (70건 기반 전체 조감도, Mermaid quadrant chart)
- ⭐ [[workday-as-customer-paradox]] — Workday vs SAP SF 전략 이분법 (G4 counter-evidence 포함)
- ⭐ [[korean-3-si-hr-ai-comparison]] — 🇰🇷 한국 3대 SI + HR tech 벤더 비교 + 클라이언트별 추천
- ⭐ [[talent-acquisition-6-vendor-comparison]] — 채용 AI 6개 솔루션 비교 + 4축 분석

### Lint Reports
- [[lint-2026-04-12-round4]] — **4차 lint (70건 전수)**, avg conf 0.35, 모든 카테고리 4건+
- [[lint-2026-04-12-round3]] — 3차 lint (22건)
- [[lint-2026-04-12-round2]] — 2차 lint (10건)
- [[lint-2026-04-12]] — 첫 lint (3건)

---

## 🔎 Quick Filters (Dataview)

### 🇰🇷 한국 사례

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  primary_category AS "카테고리",
  company AS "기업",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE contains(region, "kr")
SORT confidence DESC
```

### 🏆 신뢰도 Top 10

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  company AS "기업",
  primary_category AS "카테고리",
  confidence AS "신뢰도"
FROM "wiki/usecases"
SORT confidence DESC
LIMIT 10
```

### 📋 제안서 즉시 투입 가능 (confidence ≥ 0.50)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  company AS "기업",
  primary_category AS "카테고리",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE confidence >= 0.50
SORT confidence DESC
```
