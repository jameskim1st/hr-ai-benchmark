---
name: Johnson & Johnson
type: company
industry: [pharma, healthcare, consumer]
region: [global]
headquarters: New Brunswick, New Jersey, USA
size_employees: 130000
public: true
ticker: JNJ
ingested_first: 2026-04-12
last_confirmed: 2025
---

# Johnson & Johnson

글로벌 제약·의료·소비재 기업. 130,000 직원. **wiki 최고 수준 학술 검증 사례**: MIT CISR + IS Journal이 Digital Talent Platform의 AI 스킬 추론(60~70%)·내부 배치 8%↑·이탈 3.2%↓를 독립 검증.

## 📊 J&J HR AI Use Cases (Live)

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  primary_category AS "카테고리",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE contains(company, "Johnson") OR contains(company, "J&J")
SORT confidence DESC
```

## 핵심 — 학술 검증 ⭐

| 지표 | 값 | 검증 |
|---|---|---|
| AI 스킬 추론 비율 | **60~70%** | MIT CISR + IS Journal |
| 내부 배치 증가 | **8%** (YoY) | IS Journal 2025 |
| 디지털 역할 이탈 감소 | **3.2%** (vs 전사) | IS Journal 2025 |
| 자발적 학습 참여 증가 | **20%** | IS Journal 2025 |

**마이다스아이티(Nature, 채용 예측)와 J&J(MIT CISR, 스킬 추론)**: wiki의 **양대 학술 사례**.

## Consulting Angle

- **"스킬 기반 인사관리" 전환의 gold standard**: HRIS 데이터에서 60~70% 스킬 자동 추론이 학술적으로 입증
- **4,000명→전사 확장**의 단계적 전개 패턴이 한국 대기업 pilot-first 문화와 fit
- Textio 고객으로도 등장 (JD 개선으로 여성 지원 90,000명 추가)

## Related
- Use cases: [[jnj-digital-talent-platform-skills-ai]]
