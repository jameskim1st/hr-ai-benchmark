---
title: HR AI Benchmark Dashboard
cssclasses:
  - dashboard
---

# 🧭 HR AI Benchmark — Dashboard

이 페이지는 **Obsidian + Dataview** 플러그인이 설치돼 있을 때 자동으로 채워집니다.
플러그인이 없으면 아래 코드 블록이 그대로 표시됩니다 — 그 경우 [설정 가이드](../CLAUDE.md) 또는 본 대시보드 하단의 설치 안내를 참고하세요.

Wiki 원칙·스키마는 [[CLAUDE|CLAUDE.md]] 참고. Index 전체 보기는 [[index]].

---

## 🚨 주의 필요 (Needs Attention)

### Low-confidence use cases (0.4 미만 — 보강 필요)
```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  confidence AS "신뢰도",
  primary_category AS "대그룹",
  stage AS "단계",
  last_confirmed AS "마지막 확인"
FROM "wiki/usecases"
WHERE confidence < 0.4
SORT confidence ASC
```

### Stub use cases (공개 정보 부족)
```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  vendor AS "벤더",
  length(sources) AS "소스 수",
  last_confirmed AS "마지막 확인"
FROM "wiki/usecases"
WHERE stage = "stub"
SORT last_confirmed DESC
```

### Stale claims (12개월 이상 재확인 안 됨)
```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  last_confirmed AS "마지막 확인",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE date(last_confirmed) < date(today) - dur(12 months)
SORT last_confirmed ASC
```

---

## 📊 Inventory

### 카테고리별 Use Case 수 (대그룹)
```dataview
TABLE WITHOUT ID
  primary_category AS "대그룹",
  length(rows) AS "건수",
  round(sum(rows.confidence) / length(rows), 2) AS "평균 신뢰도"
FROM "wiki/usecases"
GROUP BY primary_category
SORT length(rows) DESC
```

### 벤더별 Use Case 수
```dataview
TABLE WITHOUT ID
  vendor AS "벤더",
  length(rows) AS "건수",
  round(sum(rows.confidence) / length(rows), 2) AS "평균 신뢰도"
FROM "wiki/usecases"
FLATTEN vendor
GROUP BY vendor
SORT length(rows) DESC
```

### 산업별 Use Case 수
```dataview
TABLE WITHOUT ID
  industry AS "Industry",
  length(rows) AS "건수"
FROM "wiki/usecases"
FLATTEN industry
GROUP BY industry
SORT length(rows) DESC
```

### Stage 분포
```dataview
TABLE WITHOUT ID
  stage AS "Stage",
  length(rows) AS "건수"
FROM "wiki/usecases"
GROUP BY stage
SORT length(rows) DESC
```

---

## 🆕 Recent Activity

### 최근 ingest된 use cases (last_confirmed 내림차순)
```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  primary_category AS "대그룹",
  vendor AS "벤더",
  confidence AS "신뢰도",
  last_confirmed AS "마지막 확인"
FROM "wiki/usecases"
SORT last_confirmed DESC
LIMIT 15
```

### 최근 수집된 sources
```dataview
TABLE WITHOUT ID
  file.link AS "Source",
  tier AS "Tier",
  source_type AS "유형",
  publication_date AS "발행",
  author AS "저자"
FROM "wiki/sources"
SORT publication_date DESC
LIMIT 15
```

---

## 🏢 Consulting Quick-Pick

### 제안서 즉시 투입 가능 (confidence ≥ 0.7 & 최근 6개월)
```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  company AS "기업",
  vendor AS "벤더",
  primary_category AS "대그룹",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE confidence >= 0.7
  AND date(last_confirmed) >= date(today) - dur(6 months)
SORT confidence DESC
```

### 국내(KR) 사례
```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  company AS "기업",
  industry AS "산업",
  confidence AS "신뢰도",
  last_confirmed AS "마지막 확인"
FROM "wiki/usecases"
WHERE contains(region, "kr")
SORT last_confirmed DESC
```

---

## 🔴 Unresolved Contradictions

```dataview
LIST
FROM "wiki/usecases"
WHERE contains(file.content, "[!contradiction]") AND contains(file.content, "unresolved")
```

> 자세한 내용은 각 페이지의 `## Contradictions` 섹션 참조. 해결 후 `상태: unresolved` → `상태: resolved`로 바꾸고 `sources:` 리스트에 해결 근거 추가.

---

## 📋 Schema Reference

| 필드 | 값 종류 |
|---|---|
| `primary_category` | Talent Acquisition · Onboarding & Transitions · Learning & Development · Performance & Talent Management · Total Rewards · Employee Experience & HR Ops · Strategic Workforce & Governance |
| `stage` | announced · pilot · production · sunset · stub |
| `frequency` | daily · monthly · annual · adhoc |
| `region` | na · eu · apac · kr · global |
| `vendor_type` | hrms · ats · lxp · talent-marketplace · point-solution · foundation-model · internal-build |
| `tier` (sources) | 1 (분석기관) · 2 (HR 미디어) · 3 (벤더) · 4 (실사례 신호) |

상세: [[CLAUDE#2 HR Taxonomy 대 중 소 그룹|CLAUDE.md §2]]

---

## ⚙ Dataview 설치 안내

이 대시보드의 쿼리가 코드 블록으로만 보인다면 Dataview 플러그인이 아직 설치되지 않은 것입니다.

1. `Ctrl+,` (Settings) → **Community plugins** → "Turn on community plugins"
2. **Browse** → "Dataview" 검색 → **Install** → **Enable**
3. 이 페이지 새로고침 (`Ctrl+P` → "Reload app without saving")

Dataview가 활성화되면 위 모든 표가 자동으로 채워집니다.
