---
name: IBM
type: company
industry: [tech, it-services]
region: [global]
headquarters: Armonk, New York, USA
size_employees: 270000
public: true
ticker: IBM
ingested_first: 2026-04-12
last_confirmed: 2025-10-24
---

# IBM

글로벌 IT 서비스·AI 기업. 270,000 직원. **AskHR은 엔터프라이즈 HR AI에서 가장 오래되고 가장 큰 규모의 배포 사례** (연 2.1M 대화, 80+ 태스크 자동화). 자체 watsonx를 기반으로 HR AI를 내부 배포하며, 동시에 외부에 HR AI 솔루션을 판매하는 **벤더이자 고객**.

## 📊 IBM HR AI Use Cases (Live)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  primary_category AS "카테고리",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE contains(company, "IBM")
SORT confidence DESC
```

## 핵심 수치

| 지표 | 값 | 출처 |
|---|---|---|
| AskHR 대상 | **270,000명** | HR Brew |
| 연간 대화 | **2,100,000** | IBM case study |
| 자동화 태스크 | **80+** | IBM case study |
| HR 인력 영향 | "couple hundred" 업무 대체 | CEO Krishna |
| 역할 전환 | 필리핀 phone agent → AI specialist | HR Brew |

## Consulting Angle

- **"HR AI maturity의 최종 형태"**: FAQ 챗봇 → routing → **agentic 자동화**로 진화한 유일한 사례
- **"replaced but elevated"** 프레이밍: Krishna CEO 발언 + 필리핀 직원 역할 전환 = HR 직무 재설계의 reference
- **한국 대기업 적용**: 수만~수십만 직원 규모에서 AskHR 수준을 목표로 할 때 전제조건(자체 AI 플랫폼·대규모 HR 데이터·직무 재설계 의지) 정리

## Related
- Use cases: [[ibm-askhr-watsonx]]
- Vendor relationship: IBM watsonx (자체 제품을 자체에 적용)
