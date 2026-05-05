---
name: Siemens
type: company
industry: [manufacturing, energy, tech]
region: [eu, global]
headquarters: Munich, Germany
size_employees: 320000
public: true
ticker: SIE
ingested_first: 2026-04-12
last_confirmed: 2025
---

# Siemens

글로벌 산업 자동화·에너지 기업. 320,000 직원, 190+ 국가. **제조업 HR AI 대표 사례**: 300,000 직원 리스킬링(Future Skills Initiative) + 20% 내부 이동 증가 + ServiceNow GBS 통합.

## 📊 Siemens HR AI Use Cases (Live)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  primary_category AS "카테고리",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE contains(company, "Siemens")
SORT confidence DESC
```

## Consulting Angle

- **독일 제조업의 "리스킬링 중심" 접근**: AI로 사람 자르기보다 역할 전환 (vs Amazon 패턴과 정반대)
- **Betriebsrat(종업원 협의회)** 환경에서의 단계적·협의적 AI 도입: EU·한국(노사관계) 참고
- **한국 제조업(삼성전자·현대·LG)** 리스킬링 전략의 reference

## Related
- Use cases: [[siemens-reskilling-internal-mobility]], [[siemens-servicenow-hr-gbs]]
