---
title: "6. Employee Experience & HR Ops"
primary_category: Employee Experience & HR Ops
category_number: 6
---

# 6. Employee Experience & HR Ops (EX & HR 운영)

직원 경험(EX)과 HR 운영(Core HR·셀프서비스·티켓·근태 등)을 포괄하는 대그룹. HR AI에서 가장 볼륨이 큰 영역 중 하나로, chatbot·case deflection·정책 Q&A·근태 이상 탐지 등이 여기 들어옵니다.

## 중그룹 / 소그룹

- **Core HR & Employee Records** — Master data 유지보수, 문서·학위·어학·가족 등록, 개인정보 거버넌스
- **Employee Self-service** — Ask HR 챗봇, 정책 Q&A, case deflection, 제증명
- **HR Service Delivery** — 티켓 분류/라우팅, 지식베이스 유지, 인사 문의응답
- **Time, Attendance & Absence**
  - Daily Time & Attendance (근태 기록·이상 탐지·카드키)
  - Shift & Overtime (교대 최적화·52시간 컴플라이언스)
  - Leave & Return-to-work (휴직 관리·복직 re-onboarding·연차)
- **Listening & Engagement** — Pulse 설문, sentiment/ONA, 이직 예측
- **Culture & OD** — 조직문화 진단, 가치체계, 변화관리
- **Comms & Change** — 내부 커뮤니케이션 생성, announcement 개인화

---

## 📊 이 카테고리의 Use Cases (Live)

아래 표는 Dataview로 자동 생성됩니다. 새 use case가 ingest되면 자동 반영됨.

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
WHERE primary_category = "Employee Experience & HR Ops"
SORT confidence DESC, last_confirmed DESC
```

## 🏢 이 카테고리에 활동 중인 기업 (Live)

**주의**: 아래 "기업" 컬럼의 이름을 클릭하면 해당 기업의 "홀리스틱 뷰" 페이지로 이동합니다 (예: `moderna` 클릭 → [[moderna]] 로 이동).

```dataview
TABLE WITHOUT ID
  company AS "기업",
  length(rows) AS "해당 카테고리 Use Case 수",
  rows.file.link AS "Use Cases"
FROM "wiki/usecases"
WHERE primary_category = "Employee Experience & HR Ops"
GROUP BY company
SORT length(rows) DESC
```

## 🛠 이 카테고리의 벤더 분포 (Live)

```dataview
TABLE WITHOUT ID
  vendor AS "벤더",
  length(rows) AS "Use Case 수"
FROM "wiki/usecases"
WHERE primary_category = "Employee Experience & HR Ops"
FLATTEN vendor
GROUP BY vendor
SORT length(rows) DESC
```

## 📆 이 카테고리 타임라인

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  first_seen AS "첫 발견",
  last_confirmed AS "마지막 확인"
FROM "wiki/usecases"
WHERE primary_category = "Employee Experience & HR Ops"
SORT first_seen DESC
```

---

## 🧭 다른 카테고리로

- [[01-talent-acquisition]]
- [[02-onboarding-transitions]] _(미생성)_
- [[03-learning-development]] _(미생성)_
- [[04-performance-talent-management]] _(미생성)_
- [[05-total-rewards]] _(미생성)_
- **6. Employee Experience & HR Ops** ← 현재
- [[07-strategic-workforce-governance]] _(미생성)_

Wiki 원칙·전체 taxonomy: [[CLAUDE|CLAUDE.md §2]]
대시보드: [[dashboard]]
