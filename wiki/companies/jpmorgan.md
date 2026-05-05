---
name: JPMorgan Chase
type: company
industry: [finance, banking]
region: [na, global]
headquarters: New York, USA
size_employees: 310000
revenue_usd_b: 177
public: true
ticker: JPM
ingested_first: 2026-04-12
last_confirmed: 2025-10-15
---

# JPMorgan Chase

미국·글로벌 최대 은행. 310,000+ 직원. **LLM Suite를 200,000 직원에 8개월 만에 배포**, AI 기반 성과 리뷰 초안 작성, ML 채용 도구 특허 출원. CEO Jamie Dimon의 "모든 프로세스에 AI 주입" 방침이 HR에도 직접 적용.

## 📊 JPMorgan HR AI Use Cases (Live)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  primary_category AS "카테고리",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE contains(company, "JPMorgan") OR contains(company, "JPM")
SORT confidence DESC
```

## Consulting Angle

- **금융권 HR AI의 flagship**: $2B AI 연간 투자, American Banker 혁신상
- **"채용을 자제하라"** 지시: AI 주입과 동시에 인력 증가 억제 → 금융 산업 패턴
- **한국 금융(KB·신한·하나·우리) 적용**: JPMorgan 수준의 AI 전사 배포를 목표로 할 때 reference

## Related
- Use cases: [[jpmorgan-llm-suite-employee-productivity]], [[jpmorgan-goldman-sachs-hr-ai]]
