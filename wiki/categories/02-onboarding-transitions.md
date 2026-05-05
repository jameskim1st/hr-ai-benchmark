---
title: "2. Onboarding & Transitions"
primary_category: Onboarding & Transitions
category_number: 2
---

# 2. Onboarding & Transitions (온보딩·이동·퇴직)

신입 온보딩부터 사내 이동·주재원·퇴직까지 "사람이 조직 안에서 옮겨 다니는 모든 것"을 포괄. AI가 매칭·추천·개인화에 강점을 보이는 영역.

## 중그룹 / 소그룹

- **New-hire Onboarding** — 개인화 온보딩 플랜, 30/60/90 체크인, 시스템 프로비저닝
  - *Mentoring Program* — 멘토 매칭, Phase1~Final 관리
- **Internal Mobility** — Talent marketplace, 사내공모, Redeployment, Project Staffing
- **Global Mobility** — 주재원 선발·발령·파견·귀임
- **Offboarding** — Exit interview 분석, 지식 이관, alumni 네트워크
  - *Mandatory Retirement* — 정년퇴직, 임금피크, 정년연장

---

## 📊 이 카테고리의 Use Cases (Live)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  subcategory AS "중그룹",
  company AS "기업",
  vendor AS "벤더",
  stage AS "단계",
  confidence AS "신뢰도",
  last_confirmed AS "마지막 확인"
FROM "wiki/usecases"
WHERE primary_category = "Onboarding & Transitions"
SORT confidence DESC, last_confirmed DESC
```

## 🏢 이 카테고리에 활동 중인 기업 (Live)

```dataview
TABLE WITHOUT ID
  company AS "기업",
  length(rows) AS "Use Case 수",
  rows.file.link AS "Use Cases"
FROM "wiki/usecases"
WHERE primary_category = "Onboarding & Transitions"
GROUP BY company
SORT length(rows) DESC
```

## 🛠 이 카테고리의 벤더 분포 (Live)

```dataview
TABLE WITHOUT ID
  vendor AS "벤더",
  length(rows) AS "Use Case 수"
FROM "wiki/usecases"
WHERE primary_category = "Onboarding & Transitions"
FLATTEN vendor
GROUP BY vendor
SORT length(rows) DESC
```

---

## 🧭 다른 카테고리로

- [[01-talent-acquisition]]
- **2. Onboarding & Transitions** ← 현재
- [[03-learning-development]]
- [[04-performance-talent-management]]
- [[05-total-rewards]]
- [[06-employee-experience-hr-ops]]
- [[07-strategic-workforce-governance]]
