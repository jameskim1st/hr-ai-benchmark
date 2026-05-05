---
name: Microsoft
type: company
industry: [tech, cloud]
region: [global]
headquarters: Redmond, Washington, USA
size_employees: 228000
public: true
ticker: MSFT
ingested_first: 2026-05-05
last_confirmed: 2026-04-01
---

# Microsoft

글로벌 최대 cloud·OS·productivity 기업. **HR AI는 두 축**: (1) 자체 HR 운영을 위한 People Skills + Skills Agent + Glint Copilot 사용, (2) M365 Copilot/Viva 생태계로 글로벌 HR Tech 시장 reshape. Bersin이 People Skills를 "HR Tech 시장 변경"으로 평가. LinkedIn 공동 개발 **16,000-skill taxonomy** 보유 — Eightfold·Gloat의 외부 vendor 모델과 직접 경쟁.

## HR AI 전략 / 핵심 테마

- **M365 native option**: 기존 M365 Copilot/Viva 사용 KR 대기업 다수에 추가 도입 부담 적은 vendor 선택지
- **활동 기반 자동 스킬 추론**: 직원 self-update 부담 해소 — 한국 대기업 갈증 큰 영역
- **default ON 전략**: Glint Copilot 2026-03 platform-wide default ON — 사용자 선택권 차감하지만 adoption 가속
- **자체 사용 dogfooding**: Microsoft "Employee Signals" twice-yearly로 자사 HR에 사용

## 📊 Microsoft HR AI Use Cases

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  primary_category AS "카테고리",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE contains(company, "Microsoft") OR contains(vendor, "Microsoft")
SORT confidence DESC
```

## Consulting Angle

- **KR HRMS RFP 시장 game-changer**:
  - 기존 Eightfold·Gloat·Beamery 외부 vendor 대비 **M365 native option** 등장
  - 이미 M365 도입 KR 대기업 → 추가 도입 비용·통합 부담 적음
  - 2026 Q3-Q4 People Skills vs Eightfold 비교 RFP 필수 슬라이드
- **한국 자체 LLM과의 경쟁**: Hyperclova X·KT Mi:dm·SKT A.X 대비 — Korean 직무·전문 용어 fit POC 필수
- **default ON 패턴**: Glint Copilot 2026-03 default ON은 한국 prudent governance 컨텍스트에서 risk — KR 도입 시 explicit opt-in 권장
- **데이터 거버넌스 trade-off**: M365 활동 기반 추론은 데이터 주권 (한국 외 데이터 이동) 검증 필수
