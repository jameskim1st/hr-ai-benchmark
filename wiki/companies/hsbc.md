---
name: HSBC
type: company
industry: [finance, banking]
region: [eu, global]
headquarters: London, UK
size_employees: 275000
public: true
ticker: HSBA
ingested_first: 2026-04-12
last_confirmed: 2025
---

# HSBC

글로벌 대형 은행. 275,000 직원. **가장 복잡한 멀티벤더 HR AI 스택**: Eightfold AI(채용) + Gloat(내부 이동, 140k 등록) + SAP SuccessFactors(Core HRIS) + Accenture(구현). [[workday-as-customer-paradox]] synthesis의 실제 대기업 배포 증거.

## 📊 HSBC HR AI Use Cases (Live)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  primary_category AS "카테고리",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE contains(company, "HSBC")
SORT confidence DESC
```

## Consulting Angle

- **Multi-vendor HR AI stack의 교과서**: SAP SF(suite) + Eightfold+Gloat(point solutions) 병행 — "suite만으로 불충분" 증거
- **한국 금융(KB·신한·하나·우리) 적용**: 대부분 SAP SF 또는 Workday 사용 → HSBC 패턴이 가장 현실적 경로
- **Fortune Europe**: HSBC가 다른 유럽 은행보다 **30% 더 많은 AI 채용 공고** 게시

## Related
- Use cases: [[hsbc-eightfold-gloat-multi-vendor]]
- Synthesis: [[workday-as-customer-paradox]]
