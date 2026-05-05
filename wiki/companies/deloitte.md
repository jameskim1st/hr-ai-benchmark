---
name: Deloitte
type: company
industry: [consulting, professional-services]
region: [global]
headquarters: London, UK (Deloitte Touche Tohmatsu Limited)
size_employees: 470000
public: false
ingested_first: 2026-04-12
last_confirmed: 2025-10-06
---

# Deloitte

글로벌 Big 4 컨설팅. 470,000 직원, 150개국. **Anthropic Claude를 역대 최대 규모로 전사 배포** + **Workforce Analyzer/Planner+ AI 솔루션을 직접 판매** — "컨설턴트이자 벤더이자 자사 도입 기업" 3중 역할.

## 📊 Deloitte HR AI Use Cases (Live)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  primary_category AS "카테고리",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE contains(company, "Deloitte") OR contains(company, "Salesforce")
SORT confidence DESC
```

## Consulting Angle

- **Big 4의 "자사 적용 → 고객 판매" 패턴**: Accenture(32% 완료↑)·PwC(65k upskilling)와 함께 "consulting firms AI 군비 경쟁"
- **470k Claude = foundation model 선택의 전략적 의미**: Moderna→OpenAI, IBM→watsonx, **Deloitte→Anthropic**
- **Workforce Analyzer: 컨설팅이 제품이 되는 시대**: 300+ HR workflow를 AI로 재설계한 library를 Salesforce에 판매

## Related
- Use cases: [[deloitte-claude-470k-employees]], [[deloitte-workforce-analyzer-salesforce]]
