---
title: "3. Learning & Development"
primary_category: Learning & Development
category_number: 3
---

# 3. Learning & Development (교육·역량·스킬)

역량 개발·교육 콘텐츠·스킬 관리를 포괄. AI가 콘텐츠 생성·개인화 추천·적응형 학습 경로 설계에 적용되는 영역.

## 중그룹 / 소그룹

- **Skills & Capabilities** — Skills ontology, skills gap 분석, skills inference, 직무전문성 진단
- **Content & Delivery** — 과정 자동 생성, adaptive learning path, AI tutor/coach, 마이크로러닝
- **Performance Support** — Workflow-embedded copilot, just-in-time 지식
- **Language & Certification** — 어학관리, 자격 관리

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
WHERE primary_category = "Learning & Development"
SORT confidence DESC, last_confirmed DESC
```

## 🛠 이 카테고리의 벤더 분포 (Live)

```dataview
TABLE WITHOUT ID
  vendor AS "벤더",
  length(rows) AS "Use Case 수"
FROM "wiki/usecases"
WHERE primary_category = "Learning & Development"
FLATTEN vendor
GROUP BY vendor
SORT length(rows) DESC
```

---

## 🔜 다음 ingest 우선순위

현재 수집된 것이 부족함. 다음 후보:
- **Cornerstone·SAP SuccessFactors Learning AI 기능** (전통 LMS의 AI 확장)
- **Microsoft Viva Learning + Copilot** (flow-embedded 대표)
- **Docebo AI, Degreed AI, 360Learning AI** (LXP)
- **국내**: 휴넷·멀티캠퍼스·크리데일 AI 학습 기능

---

## 🧭 다른 카테고리로

- [[01-talent-acquisition]]
- [[02-onboarding-transitions]]
- **3. Learning & Development** ← 현재
- [[04-performance-talent-management]]
- [[05-total-rewards]]
- [[06-employee-experience-hr-ops]]
- [[07-strategic-workforce-governance]]
