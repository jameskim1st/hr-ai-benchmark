---
name: Accenture
type: company
industry: [consulting, it-services]
region: [global]
headquarters: Dublin, Ireland (HQ); Operating worldwide
size_employees: 770000
public: true
ticker: ACN
ingested_first: 2026-05-05
last_confirmed: 2026-03-01
---

# Accenture

글로벌 최대 컨설팅·IT 서비스 기업. **HR AI mass reskilling의 canonical reference** — 30명(2022-11) → 550,000+(2025-FY) GenAI trained = 18,300x 확장. AI/data 인력 40,000 → 77,000 (+93%). 연간 ~$1B L&D 투자. CEO Julie Sweet 2026-03: "AI 미사용 직원 승진·고용 risk + non-adaptable exit compression timeline".

## HR AI 전략 / 핵심 테마

- **Mass mandatory reskilling**: 컨설팅 업종 특성상 직원 AI literacy = 직접 매출 영향
- **CEO 직접 driving**: Sweet CEO 발언 강도 — KR 컨설팅 deck 강력 hook
- **AI/data 인력 +93%**: 신규 채용 + 내부 reskilling 결합 패턴
- **클라이언트 IP 자산**: myConcerto·myWizard·Synops 등 자체 AI HR 플랫폼 (외부 판매)

## 📊 Accenture HR AI Use Cases

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  primary_category AS "카테고리",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE contains(company, "Accenture") OR contains(vendor, "Accenture")
SORT confidence DESC
```

## Consulting Angle

- **KR 그룹 HRD 센터 직접 reference (Top 5)**:
  - 삼성인력개발원·LG Aspire·SK mySUNI·현대인재개발원 RFP에 reference
  - 550K·$1B·3년 timeline은 가장 강력한 hook
- **Sweet "exit non-adaptable" 발언 KR adaptation**: 노조·노동법 sensitivity로 "성장 기회·재배치"로 reframe 권장
- **컨설팅 vs 일반 기업 fit 차별**: 컨설팅 = AI 직접 판매하는 특수 업종 → KR 제조·금융·유통 적용 강도 차별 필요
- **본 wiki vs Deloitte/Accenture 글로벌 자산**: 한국 시장 fit·local data 차별화로 positioning
