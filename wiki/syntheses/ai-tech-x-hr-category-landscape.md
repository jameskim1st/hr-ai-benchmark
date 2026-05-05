---
title: "AI 기술 유형 × HR 카테고리 Landscape (5×7 매트릭스, 126 cases)"
type: synthesis
created_at: 2026-05-05
slug: ai-tech-x-hr-category-landscape
---

# AI 기술 유형 × HR 카테고리 Landscape

## 요약

126 use case를 5 AI 기술 유형(생성형·판별예측·인식·의사결정최적화·자동화) × 7 HR 카테고리로 cross-tabulation 한 결과. **생성형이 압도적**(EX & HR Ops 32건 등 80%+ 사례에 포함). 의사결정·최적화는 단 3건 — KR/글로벌 모두 진정한 optimization 알고리즘 적용은 희소.

## 매트릭스 (R10 시점, 126 cases)

| HR 카테고리 | 생성형 | 판별·예측 | 인식 | 의사결정·최적화 | 자동화 | total |
|---|---|---|---|---|---|---|
| **Employee Experience & HR Ops** | **32** | 14 | 3 | 0 | 4 | 53 |
| **Strategic Workforce & Governance** | 19 | **20** | 1 | 2 | 5 | 47 |
| **Talent Acquisition** | 16 | **20** | 3 | 0 | 1 | 40 |
| **Learning & Development** | 17 | 11 | 0 | 0 | 1 | 29 |
| **Performance & Talent Mgmt** | 10 | 6 | 1 | 0 | 0 | 17 |
| **Total Rewards** | 5 | 6 | 0 | 1 | 1 | 13 |
| **Onboarding & Transitions** | 5 | 6 | 0 | 0 | 2 | 13 |
| **컬럼 합계** | **104** | **83** | **8** | **3** | **14** | — |

(use case 1건이 다수 type 가능, 합계 ≠ 126)

## 7가지 핵심 insight

### 1. 생성형 AI가 HR 영역 전반 dominant
104건 (82.5%)이 generative 포함. 특히 **Employee Experience & HR Ops 32건**으로 단연 1위 — Ask-HR chatbot·정책 Q&A·메일 작성 등 daily summarization-qa 패턴이 KR 컨설팅 deck의 first-pitch 영역.

### 2. Talent Acquisition + Strategic Workforce에서 판별·예측 강세 (각 20건)
- TA: 후보자 매칭·이력서 screening·success prediction (HireVue·Eightfold·Watson Recruitment·마이다스)
- Strategic Workforce: attrition prediction·retention 분석·workforce planning (IBM Predictive·Visier·Anaplan)
- → **AI tech consulting framework**: TA = "screening AI", Strategic = "people analytics AI"

### 3. 의사결정·최적화 (3건) 극희소
- ✅ Mercy Health (간호사 schedule optimization)
- ✅ KB Bank HR Deep Change (multi-variable ML 인사이동 — 진정한 LP/optimization 알고리즘)
- ✅ UKG AI Workforce Scheduling (constraint-based)
- → **"AI = 최적화"라는 클라이언트 오해 정정**: 대부분 AI는 분류·생성·예측. 진짜 optimization 알고리즘은 schedule·shift·매칭 specific 영역만

### 4. 인식 (8건) — 영상·음성·OCR 매우 niche
- 영상면접 (HireVue·SK하이닉스 A!SK·마이다스)
- 음성 인식 (Walmart Ask Sam·Mercy Health·Cathay Pacific)
- OCR (신한 AI ONE·플렉스 한국)
- → **인식 AI는 대부분 sensor 시 활용** — 일반 HR 시스템에서는 채용·콜센터·문서 디지털화에 한정

### 5. 자동화 (14건, RPA 11건) — 실제 시스템 조작은 selective
- IBM AskHR (expense·티켓), ServiceNow Now Assist HR, MS Self-Service, Cisco AI Assistant, Hitachi EMA, SK A.Biz, 우리은행 175, 포스코DX 110 등
- ⚠️ 주의: AI agent의 텍스트 자동 생성은 RPA가 아닌 generative — 진정한 RPA는 **봇이 화면·키보드·시스템 API 조작**
- → KR 컨설팅에서 "RPA 카테고리"로 잘못 분류되는 일반 챗봇 빈번 — reference doc `기타/ai_technology_categories.md` 명시

### 6. Performance & Talent Mgmt + Total Rewards 약세 (각 17·13건)
- Performance: 평가 보조 (Lattice·Workday Illuminate Performance Review·SAP Joule Performance)
- Total Rewards: pay equity (Syndio)·payroll Q&A (SAP Joule Payroll·ADP Assist)·comp recommendation (IBM)
- → **카테고리 자체가 stable·민감 영역** — 새로운 AI 도입보다 기존 systems augmentation. KR 컨설팅 "차세대 평가·보상 AI" 제안 시 사례 부족 caveat

### 7. Onboarding (13건) 가장 작은 영역
- Internal mobility (IBM Blue Match·Schneider·HSBC·Phenom·Eightfold·Gloat·Fuel50)
- Talent marketplace 카테고리 + agentic onboarding (Hitachi EMA·Zapier Enboarder)
- → 도입 사례 적지만 **AI 가장 직접적 가치 입증 가능 영역** (이직 비용 회피·skill matching)

## KR 컨설팅 활용 시나리오

### 시나리오 1 — "우리 회사에 AI HR을 어떤 카테고리로 도입할까?"
1. EX & HR Ops 챗봇 (생성형) — 가장 안전·검증된 first AI HR
2. TA 스크리닝 (판별·예측) — 한국 채용 시즌 (3월·9월) 직접 가치
3. Strategic People Analytics (판별·예측) — 한국 경영진 가장 갈증 큰 영역

### 시나리오 2 — "RPA를 도입하고 싶다"
- 진정한 RPA (봇이 시스템 조작)는 14건 — IBM·ServiceNow·MS 등 mature reference
- "AI agent로 메일 자동 작성"은 generative + summarization-qa로 분류 (RPA 아님)
- → 클라이언트 의도 명확화 필수

### 시나리오 3 — "AI 최적화로 비용 절감"
- 진짜 optimization은 3건 — schedule·shift·인사이동 multi-variable matching에 한정
- 일반 HR 영역 비용 절감 = chatbot deflection (생성형)·predictive attrition (판별예측) 위주
- → 클라이언트가 "AI 최적화"라고 표현해도 실제는 generative/predictive 가능성 큼

## KR cases breakdown (regional sub-analysis)

KR 21건의 카테고리 분포:
- EX & HR Ops 12건 (KR 사내 챗봇 dominance)
- Strategic Workforce 8건 (한국 AI 기본법·portfolio governance)
- Talent Acquisition 8건 (마이다스·SK·잡코리아 등)
- Total Rewards 2건·Performance 1건·L&D 1건 — KR에서 매우 약한 영역
- → **KR 컨설팅 white space**: Performance·Total Rewards·L&D AI 도입은 글로벌 사례를 KR client에 적용하는 컨설팅 가치 큰 영역

## 관련 데이터

```dataview
TABLE WITHOUT ID
  primary_category AS "HR 카테고리",
  ai_tech_type AS "AI 기술",
  length(rows) AS "건수"
FROM "wiki/usecases"
WHERE ai_tech_type
FLATTEN ai_tech_type
GROUP BY primary_category + " × " + ai_tech_type
SORT length(rows) DESC
LIMIT 30
```

## 다음 라운드 데이터 갱신

- 매 라운드 신규 use case 등록 시 본 매트릭스 재계산
- AI tech type axis 변경 시 본 synthesis 우선 갱신
- KR 신규 사례가 Performance·Total Rewards 영역에 도입되면 white space 갱신
