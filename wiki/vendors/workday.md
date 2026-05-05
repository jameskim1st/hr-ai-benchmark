---
name: Workday
type: vendor
category: [hrms, financial-mgmt]
vendor_type: hrms
headquarters: Pleasanton, California, USA
founded: 2005
public: true
ticker: WDAY
products:
  - Workday HCM
  - Workday Financial Management
  - Workday Illuminate (AI platform)
ingested_first: 2026-04-12
last_confirmed: 2025-09-16
---

# Workday

대형 HRMS / Financial Management 클라우드 벤더. 엔터프라이즈 HCM(Human Capital Management) 시장의 top-tier 플레이어.

## AI Platform — Workday Illuminate
- **브랜드 런칭**: 2024년 9월, Josh Bersin의 분석에 따르면 "개별 AI 기능에서 플랫폼 전반의 AI 기반 인프라로 전환"의 신호 ([[bersin-workday-illuminate-2024-09]])
- **⚠️ 벤더 주장 (Bersin 전달)**: Workday는 "70 million users의 HR·finance 데이터에 최적화된 대형 LLM"을 운영한다고 주장 — 파라미터 수는 **원 기사 내부에 800B와 70B가 동시 등장하여 미해결**
- **독립 검증**: 파라미터 수·학습 데이터·아키텍처 등 기술 세부사항에 대한 Tier 1·2 독립 검증 확보 **없음**

## HR 도메인 Illuminate Agents (공개된 것)
| Agent | 출처 | 카테고리 매핑 |
|---|---|---|
| Budget/Operations Monitoring | [[bersin-workday-illuminate-2024-09]] | 7. Strategic Workforce → People Analytics |
| Job Architecture Intelligence / Agent | [[bersin-workday-illuminate-2024-09]] · [[workday-illuminate-pr-2025-09]] | 7. Workforce Planning → Job Architecture |
| Upgraded Assistant (Copilot-like) | [[bersin-workday-illuminate-2024-09]] | 6. EX & HR Ops → Employee Self-service |
| Business Process Copilot Agent | [[workday-illuminate-pr-2025-09]] | 6. HR Ops → HR Service Delivery |
| Case Agent | [[workday-illuminate-pr-2025-09]] | 6. HR Ops → HR Service Delivery |
| Document Intelligence for Contingent Labor | [[workday-illuminate-pr-2025-09]] | 7. Employee Relations → Contract Management |
| Employee Sentiment Agent | [[workday-illuminate-pr-2025-09]] | 6. EX → Listening & Engagement |
| Performance Agent | [[workday-illuminate-pr-2025-09]] | 4. Performance → Goal & Performance |
| Recruiter Agent (demo, planned) | [[bersin-workday-illuminate-2024-09]] | 1. Talent Acquisition |
| Succession Agent (demo, planned) | [[bersin-workday-illuminate-2024-09]] | 4. Succession & Leadership |

## Confirmed Customers
- _미공개 (공개된 고객 사례 없음; press release는 "early access customers"로만 익명 언급)_

## 알려진 한계 / 관찰
- Bersin 스스로 "Workday admits its UI needs help" 인용 — UI/UX가 기존 약점이었고 Illuminate가 이를 겨냥한다는 프레이밍
- 6종 HR 에이전트 어느 것도 2025-09 press release에서 정량 지표를 제공받지 못함 ([[workday-illuminate-pr-2025-09]] 참조)

## Consulting Angle
- Workday HCM을 이미 쓰는 대기업 클라이언트에게는 "기존 플랫폼 안에서 AI 기능을 켜는" 경로로 제시 가능 — 단, 지금 시점(2026-04)에서는 **실제 ROI 사례 부재**를 정직하게 고지해야 함.
- Workday를 새로 도입하려는 클라이언트에게 AI capability만을 근거로 제안하는 것은 위험. 독립 검증된 사례가 확보되기 전까지는 "AI는 부가 가치, 핵심 의사결정 기준 아님"으로 배치.
- 국내 대기업 대상 제안 시 주의점: 국내 reference customer가 공개된 것이 없다(현재까지 수집한 소스 기준).

## Related Use Cases
- [[workday-illuminate-job-architecture]] (confidence 0.25, contradiction 있음)
- [[workday-illuminate-employee-sentiment]] (stub, confidence 0.10)
