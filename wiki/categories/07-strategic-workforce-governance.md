---
title: "7. Strategic Workforce & Governance"
primary_category: Strategic Workforce & Governance
category_number: 7
---

# 7. Strategic Workforce & Governance (인사기획·People Analytics·거버넌스)

인력계획·조직설계·People Analytics·노사·컴플라이언스·HR Tech governance를 포괄. 경영층 의사결정과 가까운 영역.

## 중그룹 / 소그룹

- **Workforce Planning** — 정기/수시 인력계획, Job Architecture, scenario/capacity modeling
- **Org Design** — 정기/수시 조직개편, 조직 현황 분석
- **People Analytics** — HR 현황·역량 분석, attrition 예측, text-to-SQL HR 분석
  - *Retention Management* — Retention 인력 리스트·리포트·면담 (운영+분석 통합)
- **DEI** — Bias 감사, 포용성 분석, 대표성 dashboard
- **Employee Relations & Labor**
  - *Contract Management* — 근로계약 (기술사무직/전임직/계약직), 임원계약
  - *Awards & Recognition Admin*
  - *Discipline* — 징계 관리, 유사사례 검색
  - *Labor Relations* — 노사관계, 단협, 고충처리
- **Compliance & Risk** — 정책 초안, 규제 모니터링 (EU AI Act, NYC LL144, 개인정보법)
- **HR Tech Governance** — Vendor risk, 권한 체계, AI 모델 governance, HR-in-the-loop 설계

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
WHERE primary_category = "Strategic Workforce & Governance"
SORT confidence DESC, last_confirmed DESC
```

## 🛠 이 카테고리의 벤더 분포 (Live)

```dataview
TABLE WITHOUT ID
  vendor AS "벤더",
  length(rows) AS "Use Case 수"
FROM "wiki/usecases"
WHERE primary_category = "Strategic Workforce & Governance"
FLATTEN vendor
GROUP BY vendor
SORT length(rows) DESC
```

---

## 🔜 다음 ingest 우선순위

- **Visier People Analytics AI**
- **Crosschq referential analytics**
- **EU AI Act 대응 사례** (HR high-risk 시스템 분류)
- **NYC LL144 bias audit 실제 공시 사례**
- **Workday Budget/Operations Monitoring Agent** (벤더 페이지에만 언급, 전용 use case 미생성)

---

## 🧭 다른 카테고리로

- [[01-talent-acquisition]]
- [[02-onboarding-transitions]]
- [[03-learning-development]]
- [[04-performance-talent-management]]
- [[05-total-rewards]]
- [[06-employee-experience-hr-ops]]
- **7. Strategic Workforce & Governance** ← 현재
