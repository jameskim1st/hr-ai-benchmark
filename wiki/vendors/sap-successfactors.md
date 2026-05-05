---
name: SAP SuccessFactors
type: vendor
vendor_type: hrms
category: [hrms, suite, ai-platform]
headquarters: Palo Alto, California, USA (SAP SE 본사: Walldorf, Germany)
parent: SAP SE
founded: 2001               # SuccessFactors 창립, SAP 인수 2011
public: true
ticker: SAP                 # SAP SE
products:
  - SAP SuccessFactors HCM Suite
  - Talent Intelligence Hub
  - Joule (SAP AI agent)
  - Career and Talent Development
  - Global Payroll + "Explain Pay Slip" AI
ingested_first: 2026-04-12
last_confirmed: 2024-10-01
---

# SAP SuccessFactors

SAP의 클라우드 HCM 플랫폼. **Workday와 양대 글로벌 HCM 벤더**. 10,000+ 고객, 200+ 국가, 290M+ 사용자 (Tier 3 벤더 주장, [[bersin-successfactors-leapfrog-2024-10]]에서 인용).

## AI 전략 — Joule 통합 + Talent Intelligence Hub

### 2024 2H Release (Bersin 2024-10 분석 기준)
- **Joule** 지능형 에이전트에 **30+ 새 AI use case** 통합 (이전 63건 + 30 = 93+)
- **Explain Pay Slip AI**: ⚠ 벤더 주장 — HR service center 문의의 **~70% 해결**
- **Open Skills Architecture**: Lightcast, Korn Ferry, Degreed, Techwolf 등 3rd party skills 벤더 통합
- **Career and Talent Development** 제품 출시 — succession planning + internal marketplace 통합

### WalkMe 번들
- SAP의 $1.5B WalkMe 인수 → digital adoption coaching 번들 제공

## ★ Workday와의 전략 대조

이 vendor의 **가장 중요한 wiki insight**는 [[workday]] 와의 전략 차이:

| | Workday | SAP SuccessFactors |
|---|---|---|
| 내부 HR 팀 사용 패턴 | Paradox(채용) + Sana(L&D) multi-vendor | (Delta/Pepsi) 3rd party 버리고 Talent Intelligence hub로 consolidation |
| Skills 통합 | _미공개_ | Open Architecture: Lightcast·Korn Ferry·Degreed·Techwolf 파트너십 |
| AI 배포 strategy | Illuminate 자체 플랫폼 + 고객이 point solution 병행 허용 | Joule + 3rd party 교체 유도 |

→ 자세한 분석: [[workday-as-customer-paradox]]

## 확인된 Consolidation 고객

[[bersin-successfactors-leapfrog-2024-10]] 에서 Bersin이 전달:

- **Delta Air Lines** — Talent Intelligence Hub를 end-to-end 플랫폼으로 채택. Gloat·Eightfold 등 3rd party 버림
- **PepsiCo** — 동일 패턴

⚠️ 주의: 이 사례는 Bersin이 SAP를 통해 전달받은 것 — **Delta·PepsiCo 공식 소스는 본 wiki 미확보**. Tier 1 매체를 거쳤지만 독립 검증은 아님.

## HR 도메인 매핑

SuccessFactors는 HR 대그룹 **거의 전 영역 커버** (suite 특성):

| 카테고리 | SF 관련 기능 |
|---|---|
| 1. Talent Acquisition | Recruiting Management, Onboarding |
| 2. Onboarding & Transitions | Onboarding, Internal Marketplace (Career and Talent Development) |
| 3. Learning & Development | SAP SuccessFactors Learning |
| 4. Performance & Talent Management | Performance & Goals, Succession |
| 5. Total Rewards | Global Payroll + "Explain Pay Slip" AI, Compensation |
| 6. EX & HR Ops | Employee Central, Joule assistant |
| 7. Strategic Workforce | Workforce Analytics, Talent Intelligence Hub |

## Consulting Angle

### SAP 선택이 합리적인 경우
- **한 벤더로 HR 전체 통합** 선호 (예: Delta/Pepsi 패턴)
- 3rd party 벤더 관리·계약·통합 부담이 큰 조직
- 기존 SAP ERP 도입 기업 (S/4HANA와의 연동 이점)

### SAP vs Workday 선택의 핵심 질문
1. 우리 조직은 **consolidation** (SF) vs **best-of-breed** (Workday) 중 어느 철학에 맞나?
2. Skills 시스템은 내부 개발·외부 파트너 중 무엇을 선호?
3. 2년 후 AI 기능 성숙도 경로는 어느 벤더가 빠를까? (현재 Bersin은 SuccessFactors에 더 긍정적, Workday Illuminate는 일부 agent가 demo 상태)

### 반면교사
- SAP SuccessFactors는 **S/4HANA 의존성**이 있어서 기존 SAP ERP가 없는 조직에는 도입 비용 높음
- WalkMe 번들 같은 "부가 기능"이 실제로 value를 주는지 독립 검증 필요

## Related
- Vendor strategic peer: [[workday]]
- Sources: [[bersin-successfactors-leapfrog-2024-10]]
- Synthesis: [[workday-as-customer-paradox]] (counter-evidence)
- Related vendors being displaced (SF 관점): [[gloat]], Eightfold, Phenom, Beamery
