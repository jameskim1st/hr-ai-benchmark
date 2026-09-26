---
name: Josh Bersin Co.
type: vendor
page_type: vendor
vendor_type: point-solution       # Galileo Learn 제품 관점
category: [analyst-firm, learning-platform, ai-agent]
headquarters: USA
founded: 2018
public: false
products:
  - Galileo (AI agent for HR leaders)
  - Galileo Learn (AI-native corporate learning platform)
  - HR Capability Model (프레임워크)
  - Research & Advisory
ingested_first: 2026-04-12
last_confirmed: 2025-05-21
---

# Josh Bersin Co.

> ⚠ **이중 역할 주의**: Josh Bersin은 본 wiki에서 **Tier 1 HR 분석가** 소스로 분류되지만, Josh Bersin Co.는 동시에 **Galileo / Galileo Learn이라는 상용 AI 제품의 제조사·판매자**. 이 페이지는 **vendor 관점**이며, Bersin의 독립 분석 글은 별도로 Tier 1 소스로 다룹니다.

## 제품

### Galileo
- HR 리더용 AI agent (일반 리서치 어시스턴트)
- 2024년부터 운영

### Galileo Learn (2025-05 런칭)
- AI-native 기업 학습 플랫폼
- Galileo agent에 통합됨
- ⚠️ 벤더 주장: Sana Labs AI foundation 기반
- ⚠️ 벤더 주장: 700+ 코스, 96-level HR Capability Model 매핑, 60+ 언어
- 가격: $495/year per person

## HR 도메인 매핑

| 제품 | 카테고리 |
|---|---|
| Galileo Learn | 3. Learning & Development → Content & Delivery |
| Galileo Learn | 3. Learning & Development → Skills & Capabilities (HR Capability Model 활용) |
| Galileo agent | 6. EX & HR Ops → HR Service Delivery (HR 리더 대상) |

## 독립 deployment 사례 (2026-04 현재)

- **Josh Bersin Co. 자체** — 8년된 HR academy를 Galileo Learn으로 5개월에 재전환, 750 learning objects 생성 ([[bersin-galileo-learn-2025-05]])
- **외부 customer deployment**: **Workday internal leadership academy** — Bersin 2025-06 follow-up에서 첫 외부 customer로 확인 ([[bersin-ld-revolution-2025-06]], [[bersin-galileo-learn-ai-native-lms]]). 실증 ROI metric은 여전히 미공개
- 참고: AI foundation 파트너 [[sana-labs]]는 2025-11 Workday에 인수됨 ([[workday-sana-for-workday-lms]]) — Galileo Learn OEM 관계의 향후 변화는 소스 미공개

## Consulting Angle

- **이 vendor를 클라이언트에 제시할 때**:
  - Josh Bersin의 "분석가 브랜드"와 "vendor 브랜드"를 **명시적으로 구분**해서 제시
  - 실증 ROI metric 부재를 솔직히 고지 — deployment 2건(Bersin Co. 자체 + Workday 리더십 아카데미) 모두 정량 효과 미공개
- **반면교사**: "분석가가 제품을 만들면 독립성이 훼손되는가?"라는 근본적 질문. 이 페이지 존재 자체가 논의 자료.

## 관련 use cases

```dataview
TABLE WITHOUT ID file.link AS "Use Case", company AS "고객", primary_category AS "대그룹", evidence_grade AS "등급", depth AS "depth"
FROM "wiki/usecases" OR "wiki/enterprise-ai"
WHERE contains(vendor, "Josh Bersin Co.")
SORT evidence_grade ASC
```
> 목록은 Dataview 자동 생성 — 손으로 갱신하지 않음

## Related
- Use cases: 상단 Dataview 표 (자동 생성 — 손으로 갱신하지 않음)
- Vendor: [[sana-labs]] (OEM)
- Sources: [[bersin-galileo-learn-2025-05]] · [[bersin-ld-revolution-2025-06]]
- 별도 Tier 1 Bersin 분석 글(독립): 향후 ingest 시 구분해서 별도 소스로 관리
