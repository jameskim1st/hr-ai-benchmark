---
name: Workday
type: vendor
page_type: vendor
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

## 2025-2026 주요 변화 (wiki 수집 기준)
- **Peakon Employee Voice + Illuminate AI** (2024-12): open-end 코멘트 요약·테마 추출 — [[workday-peakon-illuminate-employee-voice]]
- **Performance Review Agent** 발표 (2025-09 Rising, 2026 GA 예정) — [[workday-illuminate-performance-review-agent]]
- **Sana 인수** (2025-11, $1.1B) → 2026-03-17 "Sana for Workday" 공개, Sana conversational UI가 신규 front door — [[workday-sana-for-workday-lms]], [[sana-labs]]
- **Agent System of Record (ASOR)** GA (2026-02-18): 1st/3rd-party 에이전트를 사람 직원과 동일 방식으로 거버넌스 — [[workday-agent-system-of-record-asor]]

## Confirmed Customers
- **Lloyds Banking Group** — Workday HCM (2018) + Skills Cloud (2020) 위에 HR 정책 Q&A GenAI 파일럿 (2024~) — [[lloyds-banking-workday-genai-hr]]
- **Walmart** — Workday HCM을 2.3M 직원 단일 HRIS로 운영 (Paradox·OpenAI와 병행) — [[walmart-ai-frontline-workforce]]
- Illuminate agent 자체의 named customer는 _미공개_ (press release는 "early access customers"로만 익명 언급)
- 국내 reference customer: _미공개_ (수집 소스 기준)

## 알려진 한계 / 관찰
- Bersin 스스로 "Workday admits its UI needs help" 인용 — UI/UX가 기존 약점이었고 Illuminate가 이를 겨냥한다는 프레이밍
- 6종 신규 HR 에이전트 어느 것도 2025-09 press release에서 정량 지표를 제공받지 못함 — PR의 정량 지표(계약 실행 65% 단축 등)는 기존 에이전트에 대한 것 ([[workday-illuminate-pr-2025-09]], [[workday-illuminate-performance-review-agent]] 참조)

## Consulting Angle
- Workday HCM을 이미 쓰는 대기업 클라이언트에게는 "기존 플랫폼 안에서 AI 기능을 켜는" 경로로 제시 가능 — 단, **Illuminate agent 단위의 독립 검증 ROI 사례는 부재**를 정직하게 고지해야 함. Lloyds의 GenAI 가치(£50M, 2025)는 전사 GenAI 수치이며 Workday agent 단독 효과가 아님.
- Workday를 새로 도입하려는 클라이언트에게 AI capability만을 근거로 제안하는 것은 위험. 독립 검증된 사례가 확보되기 전까지는 "AI는 부가 가치, 핵심 의사결정 기준 아님"으로 배치.
- 국내 대기업 대상 제안 시 주의점: 국내 reference customer가 공개된 것이 없다(현재까지 수집한 소스 기준).

## Related Use Cases

```dataview
TABLE WITHOUT ID file.link AS "Use Case", company AS "고객", primary_category AS "대그룹", evidence_grade AS "등급", depth AS "depth"
FROM "wiki/usecases" OR "wiki/enterprise-ai"
WHERE contains(vendor, "Workday")
SORT evidence_grade ASC
```
> 목록은 Dataview 자동 생성 — 손으로 갱신하지 않음

## Related
- Vendor strategic peer: [[sap-successfactors]] · 인수 자회사: [[sana-labs]]
- Synthesis: [[workday-as-customer-paradox]]
- Sources: [[bersin-workday-illuminate-2024-09]] · [[workday-illuminate-pr-2025-09]] · [[workday-asor-ga-2026-02]] · [[hr-brew-workday-sana-2026-03]]
