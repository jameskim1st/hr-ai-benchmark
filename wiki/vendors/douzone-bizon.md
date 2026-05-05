---
name: 더존비즈온 (Douzone Bizon)
type: vendor
vendor_type: hrms
category: [erp, hrms, payroll, korean-vendor, accounting]
headquarters: Seoul, South Korea
founded: 1977
public: true
ticker: "012510.KQ"
products:
  - 더존 ERP / Smart A
  - 원챔버
  - ONE AI (AI 통합 제품군)
  - ONE AI 연말정산
  - Smart HR / 급여
ingested_first: 2026-04-12
last_confirmed: 2024-12-10
---

# 더존비즈온 (Douzone Bizon)

> 국내 ERP·회계·급여·HR 시장의 de facto dominant player (중소·중견기업 부문). 상장사(코스닥). 본 wiki에서는 **한국 Total Rewards → Payroll Operations → Year-end Tax Settlement** 영역의 AI 대표 벤더로 등장.

## 핵심 정체성
- 국내 ERP·급여·세무 소프트웨어 시장 점유율 최상위권
- 수십만 중소·중견기업 고객 base
- 2024년부터 **ONE AI** 브랜드로 AI 기능 통합 전략 전개

## AI 제품: ONE AI 시리즈

### ONE AI 연말정산 (본 wiki 최초 수집)
- **2024년 출시** (정확 일자 미공개, 2024-12 TaxWatch 기사 기준 운영 중)
- **기능 범위**: 대상자 선정 → 안내 → 자료 입력 → 검토 → 결과 안내 **end-to-end**
- **핵심 기능**:
  - 국세청 간소화 자료(PDF) 자동 다운로드 + 반영
  - 연말정산 데이터 검증 + 세액 예측
  - 홈택스 자동신고
  - 원챔버 연동 (추가 증빙 제출)
  - 총괄현황판 (전사 진행상황)
  - 요약보고서·지급명세서 자동신고
- **타겟**: 중소·중견기업 HR·인사담당자
- 출처: [[taxwatch-douzone-one-ai-2024-12]]

### 기타 ONE AI 제품군
- _미공개_ (현재 wiki 확보 소스가 연말정산 하나뿐)

## HR 도메인 매핑

| 제품 | 카테고리 |
|---|---|
| ONE AI 연말정산 | 5. Total Rewards → Payroll Operations → **Year-end Tax Settlement** |
| 더존 Smart HR | 6. HR Ops → Core HR & Employee Records |
| 더존 급여 | 5. Total Rewards → Payroll Operations → Payroll Execution |

**5. Total Rewards**가 주 영역, 특히 한국 특유 연말정산·세무가 핵심 moat.

## 확인된 customer

- ⚠️ 벤더 주장: "**1000개 기업 추가 계약**" ([[taxwatch-douzone-one-ai-2024-12]], 2024-12)
- 구체 customer 이름 공개 없음 (중소·중견기업 대상 특성상 개별 publicizing 드묾)

## 한국 Total Rewards 영역에서의 전략적 위치

- **글로벌 벤더(Workday·SAP SuccessFactors)가 다루지 않는 영역** — 연말정산·국세청 홈택스 연동은 한국 세법 특화이며 글로벌 suite의 Korea Payroll 모듈로 커버되기 어려움
- 즉 더존비즈온의 AI 연말정산은 **한국 시장의 de facto 대체 불가** 영역
- 이는 **"글로벌 HCM suite + 국내 특화 보완"**이라는 한국 대기업 현실 HR 스택의 필수 조각

## Consulting Angle

### 이 벤더가 컨설팅 프로젝트에 등장하는 시나리오
1. **국내 중견기업 HR 디지털화 로드맵** — 이미 더존 ERP·급여 쓰는 기업의 AI 확장
2. **글로벌 HCM 도입 프로젝트의 "Korea Payroll gap"** — Workday·SAP 도입 시 연말정산 영역 어떻게 보완할지
3. **한국 특유 compliance 자동화** — 연말정산·원천세·4대보험·퇴직정산 등 법정 프로세스의 AI 적용

### 주의
- 2024-12 단일 소스 기반 — 구체 efficacy·customer case study 부족
- LLM foundation·아키텍처 불명
- 독립 Tier 1 분석 부재 (국내 HR tech 분석가 생태계 자체가 미성숙)

## Related
- Use case: [[douzone-one-ai-year-end-tax]]
- Source: [[taxwatch-douzone-one-ai-2024-12]]
- 경쟁 영역: [[sap-successfactors]] Global Payroll (전 세계), [[workday]] Payroll (한국 특화 불완전)
