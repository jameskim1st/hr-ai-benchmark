---
title: "4. Performance & Talent Management"
primary_category: Performance & Talent Management
category_number: 4
---

# 4. Performance & Talent Management (평가·후계·핵심인재)

성과 평가·승진·핵심인재·후계·코칭을 포괄. AI가 리뷰 초안·calibration 분석·HiPo 식별·manager copilot 등에 적용되는 영역.

## 중그룹 / 소그룹

- **Goal & Performance** — OKR/목표 생성, 연속 피드백 요약, 리뷰 초안, calibration 분석, 1:1 지원
- **Succession & Leadership** — HiPo 식별, 후계자 추천, 리더십 assessment, 최고 기술전문가 관리
- **Coaching** — AI 코치 (BetterUp 류), manager copilot, LMD 지원

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
WHERE primary_category = "Performance & Talent Management"
SORT confidence DESC, last_confirmed DESC
```

## 🏢 이 카테고리에 활동 중인 기업 (Live)

```dataview
TABLE WITHOUT ID
  company AS "기업",
  length(rows) AS "Use Case 수",
  rows.file.link AS "Use Cases"
FROM "wiki/usecases"
WHERE primary_category = "Performance & Talent Management"
GROUP BY company
SORT length(rows) DESC
```

---

## 🔜 다음 ingest 우선순위

- ~~15Five Kona~~ → [[15five-kona-reup-ai-manager-coaching]] ✅ 생성 완료
- ~~Lattice AI~~ → [[lattice-ai-performance-summarization]] ✅ 생성 완료
- ~~Betterworks~~ → [[betterworks-nextgen-ai-performance]] ✅ 생성 완료
- ~~Workday Illuminate Performance Agent~~ → [[workday-illuminate-performance-review-agent]] ✅ 생성 완료
- ~~Culture Amp AI Coach~~ → [[cultureamp-ai-coach-asana]] ✅ 생성 완료
- ~~SAP Joule Performance Agent~~ → [[sap-joule-performance-goals-agent]] ✅ 생성 완료
- **다음**: Glint/Viva Insights, Leapsome AI, Perdoo OKR AI, PerformYard AI

---

## 🧭 다른 카테고리로

- [[01-talent-acquisition]]
- [[02-onboarding-transitions]]
- [[03-learning-development]]
- **4. Performance & Talent Management** ← 현재
- [[05-total-rewards]]
- [[06-employee-experience-hr-ops]]
- [[07-strategic-workforce-governance]]
