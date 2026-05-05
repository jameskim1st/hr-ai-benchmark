---
name: Unilever
type: company
industry: [fmcg, consumer-goods]
region: [global]
headquarters: London, UK / Rotterdam, Netherlands
size_employees: 128000
revenue_usd_b: 60
public: true
ticker: UL
ingested_first: 2026-04-12
last_confirmed: 2019-12-17        # i4cp 소스 기준 — 더 최신 소스 필요
---

# Unilever

글로벌 FMCG 대기업. **Internal talent marketplace (FLEX Experiences)** 도입의 **가장 자주 인용되는 reference case**. Gloat와의 파트너십은 2019년부터 시작돼 장기 운영 중.

## 조직 규모
- 약 128,000명 직원, 190개국
- $60B+ 연매출
- 400+ 브랜드

## HR AI 주요 사례

### FLEX Experiences (2019~ 현재)
- **파트너**: [[gloat]] (NY 기반 AI talent marketplace 벤더)
- **목적**: 직원 ↔ 단·장기 프로젝트 AI 매칭
- **2019-12 기준 규모**: 30,000+ 직원, 90+ 개국, 95% 사용자 endorsement ([[i4cp-unilever-flex-2019-12]])
- **다른 소스에서 보고된 확장 수치** (본 wiki 미검증): 90,000+ 직원, 300k 시간 unlocked, 41% 생산성 증가, COVID 대응 8,300명 재배치

### Named HR Leader (당시)
- **Jeroen Wels** — Executive VP of HR, Categories, and Organizations (2019 기준)

## HR 대그룹 커버리지 (Unilever 수집 현황)

```dataview
TABLE WITHOUT ID
  primary_category AS "HR 대그룹",
  length(rows) AS "Use Case 수",
  rows.file.link AS "페이지들"
FROM "wiki/usecases"
WHERE company = "Unilever"
GROUP BY primary_category
```

## 📊 Unilever HR AI Use Cases (Live)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  primary_category AS "대그룹",
  subcategory AS "중그룹",
  stage AS "단계",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE company = "Unilever"
SORT confidence DESC
```

## Consulting Angle

- **"내부 인력 재배치"의 글로벌 대표 레퍼런스**. 한국 대기업(특히 계열사 간 이동이 필요한 그룹사)에 proof-point로 사용 가능.
- **주의점**:
  - Unilever FLEX의 "매니저 승인 불필요" 원칙이 한국 연공 문화에서 작동할지 미검증
  - DEI 효과(여성 직원 참여율) 부분은 한국 적용 시 별도 설계 필요
  - 현재 wiki의 주요 소스가 **2019년 기준 (76개월 stale)** — 최신 data로 업데이트하지 않으면 제안서 사용 시 리스크

- **반면교사 리스크**:
  - Unilever는 2019년 pre-COVID 시점에 이미 디지털 HR 인프라가 성숙했음
  - 한국 대기업이 0에서 시작해 같은 수준에 도달하려면 "talent marketplace 도입"만으로는 부족 — 먼저 **skills ontology 구축, 직무 체계 재설계**가 선행돼야 함
  - 컨설팅 제안 시 "Unilever처럼" 대신 "Unilever 경로의 5년 단축 버전"으로 포지셔닝 권장

## Related
- Vendor: [[gloat]]
- Sources: [[i4cp-unilever-flex-2019-12]]
