---
name: Amazon
type: company
industry: [tech, retail, logistics]
region: [global]
headquarters: Seattle, Washington, USA
size_employees: 1500000
public: true
ticker: AMZN
ingested_first: 2026-04-12
last_confirmed: 2025-10-16
---

# Amazon

세계 최대 e-commerce + 클라우드(AWS) 기업. 1.5M+ 직원. **HR AI의 가장 극단적 사례**: PXT(HR 부서) 10,000명 중 **최대 15% 감축** 발표. 동시에 250,000명 계절직 채용 — "white-collar 자동화 + blue-collar 대량 채용"의 극적 대비.

## 📊 Amazon HR AI Use Cases (Live)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  primary_category AS "카테고리",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE contains(company, "Amazon")
SORT confidence DESC
```

## Consulting Angle

- **"HR이 AI의 대상이 된다"의 반면교사**: wiki의 다른 사례는 모두 "HR이 AI를 도입", Amazon만 "HR 자체가 축소"
- **$100B AI 투자**: 기업 역사상 가장 큰 AI 투자와 HR 감축이 동시 발생
- **한국 시사점**: 국내 대기업이 AI 도입 시 HR 부서 자체의 미래를 논의해야 한다는 경고

## Related
- Use cases: [[amazon-hr-ai-restructuring]]
