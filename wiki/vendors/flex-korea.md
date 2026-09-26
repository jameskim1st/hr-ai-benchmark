---
name: 플렉스 (flex)
type: vendor
page_type: vendor
vendor_type: hrms
category: [hrms, payroll, time-attendance, korean-vendor]
headquarters: Seoul, South Korea
founded: 2017
public: false
valuation_usd_m: 500           # 2025년 기업가치 5000억원
products:
  - flex (올인원 HR 플랫폼)
  - flex mini (소상공인용)
ingested_first: 2026-04-12
last_confirmed: 2025-08-01
stub: true
---

# 플렉스 (flex)

> ⚠ **Stub**: 이 페이지는 다른 페이지 참조 해소 + 국내 HR tech 벤더 landscape 기록용 stub. AI 기능 세부·고객 사례 보강 필요.

국내 올인원 HR SaaS 스타트업. 근태·급여·계약·결재 등 HR 업무 통합 플랫폼. **2025년 기업가치 5,000억원** (Series B-1 100억 투자 유치). 2025년까지 **AI 기술을 제품에 본격 통합**해 "도구 → 지능형 동료" 전환을 선언 (flex 공식 블로그 2025-05-28).

## HR 도메인 매핑

| 기능 | 카테고리 |
|---|---|
| 근태관리 | 6. EX & HR Ops → Time, Attendance & Absence |
| 급여 자동화 | 5. Total Rewards → Payroll Operations |
| 전자계약·결재 | 7. Employee Relations → Contract Management |
| HR 데이터 통합 | 6. Core HR & Employee Records |

## AI 전략 (2025)
- "내부에서 검증되고 발전해온 AI 기술을 제품에 본격적으로 통합" (flex blog 2025-05-28)
- 2025 발표 기능: **OCR 기반 수기 근무표 자동변환** + **노동법·세법 AI 에이전트 상담** 순차 도입 — "SaaS → Service as a Software" 선언 ([[flex-korea-hr-ai-saas]], 출처 [[flex-korea-hr-saas-2025]]; 6만+ 기업 가입·ARR 300억원은 ⚠️ 자사 보고)
- foundation model·아키텍처 _미공개_
- AI 채용·성과·분석 기능 출시는 소스에 없음

## 관련 use cases

```dataview
TABLE WITHOUT ID file.link AS "Use Case", company AS "고객", primary_category AS "대그룹", evidence_grade AS "등급", depth AS "depth"
FROM "wiki/usecases" OR "wiki/enterprise-ai"
WHERE company = "플렉스팀" OR contains(vendor, "flex") OR contains(tags, "flex")
SORT evidence_grade ASC
```
> 목록은 Dataview 자동 생성 — 손으로 갱신하지 않음

## 국내 HR SaaS 시장에서의 위치
- **시프티(Shiftee)** — 근태 특화 경쟁사
- **페이히어(PayHere)** — 급여 특화
- **그리팅(Greeting)** — 채용 특화
- **CLAP** — 성과관리 특화
- **더존비즈온** — ERP 기반 전통 강자 (중소·중견)

flex는 "올인원"을 지향하며 각 특화 경쟁사의 기능을 통합하는 전략.

## Related
- Use cases: 상단 Dataview 표 (자동 생성 — 손으로 갱신하지 않음)
- Source: [[flex-korea-hr-saas-2025]]
- 경쟁 벤더: [[douzone-bizon]], [[wantedlab]], [[sk-ax]]
