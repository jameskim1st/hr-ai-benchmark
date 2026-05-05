---
title: "5. Total Rewards"
primary_category: Total Rewards
category_number: 5
---

# 5. Total Rewards (보상·급여·복리후생)

보상 전략·급여 실행·연말정산·복리후생·포상 등 전체 보상 영역. 한국에서는 특히 **연말정산·퇴직정산·충당금 관리** 같은 payroll operations가 중요.

## 중그룹 / 소그룹

- **Compensation** — Pay strategy/보상기획, Pay equity, comp benchmarking, offer modeling
  - *Equity & Stock Programs* — 우리사주, 자사주, RSU, 스톡옵션, ESPP
- **Payroll Operations**
  - *Payroll Execution* — 정기급여, 상여(PS/PI), 비정기 급여
  - *Year-end Tax Settlement* — 연말정산 (한국 특유)
  - *Retirement Settlement & Pension* — 퇴직정산, DC/DB 연금
  - *Accruals & Reserves* — 퇴직·연차·상여 충당금
  - *Garnishment & Deductions* — 채권압류, 공제
- **Benefits & Wellbeing**
  - *Health & Insurance*, *Flexible Benefits*, *Wellbeing & Mental Health*, *Life Events*, *Perks & Facilities*
- **Recognition** — 사내/사외 포상, 장기근속, peer recognition

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
WHERE primary_category = "Total Rewards"
SORT confidence DESC, last_confirmed DESC
```

## 🛠 이 카테고리의 벤더 분포 (Live)

```dataview
TABLE WITHOUT ID
  vendor AS "벤더",
  length(rows) AS "Use Case 수"
FROM "wiki/usecases"
WHERE primary_category = "Total Rewards"
FLATTEN vendor
GROUP BY vendor
SORT length(rows) DESC
```

---

## 🔜 다음 ingest 우선순위

- ~~UKG payroll AI~~ → [[ukg-ai-workforce-scheduling-healthcare]] ✅ 생성 완료
- ~~Paychex agentic WFM~~ → [[paychex-flex-agentic-workforce]] ✅ 생성 완료
- ~~Spring Health EAP~~ → [[spring-health-general-mills-ai-eap]] ✅ 생성 완료
- **다음**: Ceridian Dayforce AI Workspace (Pay Clarity agent), Workday Payroll Agent (2025-09 PR)
- **다음**: Fidelity, Carta equity platform AI, Hinge Health / Lyra 웰빙 AI
- **한국**: 연말정산 AI (더존 외 사례), 복지포인트/포인트몰 AI 추천

---

## 🧭 다른 카테고리로

- [[01-talent-acquisition]]
- [[02-onboarding-transitions]]
- [[03-learning-development]]
- [[04-performance-talent-management]]
- **5. Total Rewards** ← 현재
- [[06-employee-experience-hr-ops]]
- [[07-strategic-workforce-governance]]
