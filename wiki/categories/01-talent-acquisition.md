---
title: "1. Talent Acquisition"
primary_category: Talent Acquisition
category_number: 1
status: empty
---

# 1. Talent Acquisition (채용·인력확보)

채용 전 과정을 다루는 대그룹. HR AI use case가 가장 자주 등장하는 영역 중 하나이며, 벤더 생태계도 가장 성숙함 (Eightfold·Paradox·HireVue·Beamery·Phenom 등).

## 중그룹 / 소그룹

- **Sourcing & Attraction** — JD 생성, employer branding, passive candidate mining
- **Screening & Assessment** — Resume parsing, skills matching, chat screening, video interview 분석, bias audit
- **Interview & Selection** — 질문 생성, interview copilot, scorecard 자동화, reference check
- **Offer & Pre-boarding** — Offer letter 생성, 협상 시뮬레이터, 문서 수집
- **Executive Search (핵심인재 채용)** — Referral, Search Firm, Direct Sourcing
- **Early-career Pipeline** — 대졸 정기/수시 채용, 장학생 선발·관리, 인턴십, 산학협력

---

## 📊 이 카테고리의 Use Cases (Live)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  subcategory AS "중그룹",
  company AS "기업",
  vendor AS "벤더",
  stage AS "단계",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE primary_category = "Talent Acquisition"
SORT confidence DESC
```

> 🚨 **현재 이 카테고리에 수집된 use case가 없습니다.** 위 쿼리는 Obsidian에서 빈 표로 표시됩니다. Dataview 플러그인이 설치돼 있지 않으면 코드 블록만 보일 수 있습니다.

## 리서치 공백 — 다음 ingest 우선순위

이 카테고리가 비어있다는 것은 "수집이 부족"하다는 뜻. 다음 후보 소스:

- **AIHR** (Tier 2) — "generative AI in talent acquisition" 시리즈
- **McKinsey / HBR** (Tier 1) — 채용 AI 관련 기사
- **HireVue / Paradox / Eightfold** (Tier 3) — 벤더 customer story
- **SHRM / HR Dive** (Tier 2) — 기업 사례 보도
- **국내 사례** — 원티드랩 AI 매칭, 삼성/LG 채용 AI 도입 보도

---

## 🧭 다른 카테고리로

- **1. Talent Acquisition** ← 현재
- [[02-onboarding-transitions]] _(미생성)_
- [[03-learning-development]] _(미생성)_
- [[04-performance-talent-management]] _(미생성)_
- [[05-total-rewards]] _(미생성)_
- [[06-employee-experience-hr-ops]]
- [[07-strategic-workforce-governance]] _(미생성)_

Wiki 원칙·전체 taxonomy: [[CLAUDE|CLAUDE.md §2]]
