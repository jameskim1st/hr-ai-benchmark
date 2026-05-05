---
type: synthesis
topic: cross-entity-insight
generated_at: 2026-04-12
last_updated: 2026-04-12
entities_referenced:
  - workday
  - paradox
  - josh-bersin-co
  - sana-labs
  - sap-successfactors        # ★ 2026-04-12 updated: G4 counter-evidence
counter_entities:
  - sap-successfactors
  - delta-air-lines           # mentioned but no page
  - pepsico                   # mentioned but no page
derived_from_usecases:
  - workday-illuminate-job-architecture
  - workday-illuminate-employee-sentiment
  - chipotle-paradox-olivia
  - bersin-galileo-learn-ai-native-lms
tags: [cross-entity, hcm-strategy, best-of-breed, multi-vendor, consulting-angle, suite-vs-unbundled]
consulting_priority: high
---

# Workday는 벤더인가 고객인가 — HR AI 생태계의 패러독스

> **2026-04-12 업데이트**: 본 synthesis는 **Workday 패턴**을 핵심으로 시작했으나, G4 라운드에서 발견된 **SAP SuccessFactors 반대 패턴**(Delta·Pepsi의 consolidation)을 반영해 "universal truth"가 아닌 **"suite 벤더별 전략 이분법"** 으로 re-framing되었다. §8 섹션 참조.

> 🎯 **컨설팅 insight 요약**: 글로벌 HCM(Human Capital Management) 최대 벤더 Workday는 자사 **Workday Illuminate** AI 플랫폼을 홍보하면서도, **동시에 여러 point solution HR AI 벤더의 고객**으로 등장한다. 한편 SAP SuccessFactors 고객(Delta·Pepsi)은 오히려 point solution을 버리고 suite로 consolidation한다. 이 **수평 대조**가 "HCM 도입 = HR AI 해결"이라는 단순 가정을 깬다. 컨설팅 현장에서 multi-vendor vs consolidation 선택은 **벤더·고객·문화에 따라 다르며**, 기본 가정은 "고민해야 할 결정"이다.

---

## 1. 관찰 — wiki에서 데이터로 확인된 사실

### 1-1. Workday의 vendor 역할 (자사 Illuminate AI 플랫폼)

[[workday]] vendor 페이지에 기록된 Workday Illuminate는 **10+ HR 도메인 에이전트**를 보유:

- **Job Architecture Intelligence / Agent** — [[workday-illuminate-job-architecture]]
- **Employee Sentiment Agent** — [[workday-illuminate-employee-sentiment]]
- Budget/Operations Monitoring, Upgraded Assistant, Business Process Copilot Agent, Case Agent, Document Intelligence for Contingent Labor, Performance Agent
- Planned: Recruiter Agent, Succession Agent (2024-09 Bersin 분석 시점엔 demo 상태)

**⚠️ 벤더 주장 (Workday 마케팅)**: 70 million users의 HR·finance 데이터에 최적화된 LLM 기반 플랫폼. 파라미터 수 contradiction 있음 (800B vs 70B, [[lint-2026-04-12]] C-2 참고).

### 1-2. Workday의 customer 역할 — wiki에서 2건 확인됨

#### (a) Paradox Olivia의 customer (2년 23,000시간 절약)

[[paradox-clients-stories-2026-04]] 에 기록된 고객 리스트에 **Workday가 명시적으로 등장**:

> ⚠️ **Paradox 벤더 주장**: "Workday — 2년간 23,000시간 절약" (Workday 자체 채용팀이 Paradox Olivia를 사용)

즉 세계 최대 HCM 벤더의 **내부 채용 조직이 자사의 Illuminate Recruiter Agent가 아니라 Paradox를 선택**했다는 사실.

#### (b) Sana / Galileo Learn의 customer (internal leadership academy)

[[bersin-ld-revolution-2025-06]] 에서 Josh Bersin이 처음으로 공개한 Sana 외부 고객:

> ✅ **Bersin 2025-06 확인**: Sana/Galileo Learn의 첫 외부 공개 customer는 **Workday internal leadership academy**

Workday가 자사 learning 솔루션이 아니라 Sana(Josh Bersin Co.가 OEM)의 AI-native 학습 플랫폼을 사내 leadership 개발에 쓰고 있다는 것.

---

## 2. 이 관찰이 중요한 이유 — 4가지 분석

### 2-1. All-in-one HCM의 한계에 대한 직접 증거

Workday는 **글로벌 Fortune 500 HR 영역에서 가장 우세한 HCM 플랫폼**이다. 그런 Workday조차 **자사 채용 기능 대신 외부 point solution**을 쓴다는 것은, 가장 강력한 suite 벤더의 자사 사용에서도 "하나의 플랫폼으로 모든 것을 덮는다"가 성립하지 않는다는 의미.

이는 컨설팅 논의에서 반복되는 다음 가정에 대한 직접적 반례:
- "Workday(또는 SAP SuccessFactors, Oracle HCM)만 잘 쓰면 HR AI는 저절로 해결된다"
- "HCM 벤더의 AI 기능은 point solution을 대체한다"
- "하나의 suite 안에서 모든 AI 기능을 쓰면 통합 문제가 없다"

### 2-2. Best-of-breed vs Suite의 실증적 균형

HR tech 전략 논의에서 오래된 2축:
- **Suite 전략**: 하나의 큰 벤더(Workday·SAP·Oracle)로 통합
- **Best-of-breed 전략**: 영역별 point solution 조합 (Eightfold·Paradox·Gloat 등)

이 관찰은 **Workday 자체가 best-of-breed 전략을 쓴다**는 증거. 즉 세계 최대 suite 벤더가 내부에서는 multi-vendor stack을 구축한다. 이건 컨설팅 덱에서 "suite vs best-of-breed"를 단순 양자택일로 제시하기 어렵게 만드는 **강력한 nuance**.

### 2-3. Time-to-market pressure의 현실

Bersin의 2024-09 분석 ([[bersin-workday-illuminate-2024-09]])에 따르면 Workday Illuminate는:
- Budget/Operations Monitoring, Job Architecture Intelligence, Upgraded Assistant **출시됨**
- **Recruiter Agent, Succession Agent는 demo 상태 (2024-09 기준)**

즉 Workday Illuminate의 Recruiter Agent가 **자사 채용팀이 기다리기엔 너무 늦게 출시**되고 있어서, Paradox라는 **훨씬 성숙한 point solution**을 채용에 우선 채택한 것. "전략"이 아니라 "필요에 의한 선택"일 수 있음.

이는 다른 HCM 고객 조직에도 같은 딜레마를 시사: **Workday Illuminate의 대기 vs Paradox 같은 기존 솔루션 즉시 도입**의 선택. Workday 자체가 후자를 택했다는 점이 중요한 단서.

### 2-4. "Suite 벤더의 AI 기능 약속"에 대한 의심

HCM 벤더들은 "AI 기능은 플랫폼 기본에 포함되어 언제든 활성화 가능"이라고 마케팅한다. 하지만 Workday의 자사 사용 패턴은 이것이 **약속과 현실 사이의 gap**이 크다는 것을 보여준다.

컨설팅 클라이언트에게: 벤더의 "AI 포함" 주장을 "**언제·얼마나 성숙하게·무엇이 빠져 있는지**" 검증 없이 받아들이면, 실제 배포에서는 여전히 point solution이 필요하다는 사실을 나중에 발견하게 됨.

---

## 3. 컨설팅 insight — 클라이언트에게 직접 적용

### 3-1. Workday 도입 프로젝트에 반드시 질문할 것

Workday HCM 도입·확장을 검토하는 클라이언트에게 다음 3가지 질문을 **반드시 던진다**:

1. **"Illuminate의 어떤 에이전트가 production이고 어떤 것이 demo인가?"**
   - 답: Workday 세일즈팀에게 직접 물어보고, 각 에이전트의 GA(General Availability) 일자·deployment 수를 요구
2. **"Workday 자체 HR 팀은 어떤 HR AI 도구를 쓰는가?"**
   - 답: Workday 자체가 Paradox 사용. 이 사실만으로 "Workday만으로 충분"이라는 주장 약화
3. **"Illuminate가 충분히 성숙한 시점까지 대기할 수 있는 영역은? 지금 당장 point solution이 필요한 영역은?"**
   - 답: 이 wiki에서 **Talent Acquisition은 Paradox, L&D는 Sana/Galileo, Talent Marketplace는 Gloat**라는 명확한 point solution이 있음

### 3-2. Multi-vendor stack을 기본 가정으로

이 synthesis의 핵심 컨설팅 입장:

> **"단일 HCM으로 HR AI가 해결된다는 약속은 세계 최대 벤더의 자사 사용 패턴으로 반증된다. Multi-vendor HR AI stack을 전제로 프로젝트를 설계하라."**

### 3-3. 벤더 선택의 "deferred decision" 패턴

대안 전략: "Workday(또는 SAP·Oracle)의 AI 기능이 성숙할 때까지 기다린다"는 **deferred decision**. 이 wiki의 증거가 말해주는 것:

- **2024-09** Workday Illuminate 출시 후 **1.5년**이 지난 **2026-04** 현재까지도 Recruiter Agent의 외부 deployment case를 wiki가 찾지 못함
- Workday 자체가 그 기간 동안 Paradox를 사용
- Deferred decision은 사실상 **"point solution을 쓰지 않는다"가 아니라 "HCM 벤더의 약속을 믿고 기다린다"**이며, 기다리는 동안 경쟁사는 이미 배포·운영·학습 중

---

## 4. 역질문 — 이 synthesis가 다루지 못한 것

솔직히 말해서 이 synthesis에는 반증 가능성이 있는 부분이 있다:

### 4-1. Sample size 문제
- wiki가 확인한 "Workday as customer" 사례는 **단 2건** (Paradox + Sana)
- 이걸로 "HCM 벤더가 일반적으로 point solution을 쓴다"를 결론 내는 건 과한 일반화

**반박 가능성**: SAP·Oracle HCM 등 다른 suite 벤더가 자사 AI만 쓰고 있다면, Workday만 특수한 케이스일 수 있음. 이는 별도 ingest 과제.

### 4-2. Workday의 공식 statement 부재
- Workday가 "우리는 Paradox·Sana도 함께 쓴다"고 **공식 인정**한 바 없음
- Paradox·Bersin이 각자 자기 쪽에서 공개한 정보
- Workday가 왜 이를 설명하지 않는지도 의미 있는 질문

### 4-3. 이 패턴이 고객에게도 유효한가?
- Workday 자체는 **테크 회사**이므로 여러 AI 시스템을 운영할 기술적 역량 충분
- 전통적 대기업 고객(제조·금융)은 multi-vendor stack 운영 부담이 더 클 수 있음
- 이 synthesis의 권고가 **모든 industry에 적용되는 것은 아님**

### 4-4. Cost perspective 부재
- 이 wiki에는 multi-vendor 접근의 **총 비용(TCO)** 분석 없음
- Paradox·Sana·Workday를 동시 구독하는 비용이 Workday 단독보다 반드시 높음
- 가격 vs 기능 trade-off는 여전히 클라이언트 사안

---

## 5. 다음 리서치 과제 (이 synthesis를 강화하려면)

1. **SAP SuccessFactors, Oracle HCM 자체 사용 패턴** — 같은 패러독스가 이들에게도 존재하는지 확인
2. **Workday Paradox 도입 타임라인** — 언제부터 썼는지, Illuminate 출시 전후 어느 시점에 도입 결정했는지
3. **Workday Illuminate의 GA 상태** — 2026-04 현재 각 에이전트의 외부 deployment 수를 Workday IR·사용자 컨퍼런스 자료에서 확인
4. **Gartner / Forrester analyst 시각** — best-of-breed vs suite 시장 전망 tier 1 독립 분석
5. **Customer TCO 비교** — Workday 단독 vs Workday + Paradox + Sana의 실제 비용 차이

---

## 6. 관련 wiki 페이지

### Direct evidence
- [[workday]] (벤더)
- [[paradox]] (Workday를 customer로 기재)
- [[josh-bersin-co]] (Sana OEM 관계)
- [[chipotle-paradox-olivia]] (Paradox 주력 사용 사례)
- [[bersin-galileo-learn-ai-native-lms]] (Workday를 customer로 언급)
- [[workday-illuminate-job-architecture]], [[workday-illuminate-employee-sentiment]] (Workday 자사 AI)

### Sources
- [[paradox-clients-stories-2026-04]]
- [[bersin-ld-revolution-2025-06]]
- [[bersin-workday-illuminate-2024-09]]
- [[workday-illuminate-pr-2025-09]]

### Related syntheses
- [[lint-2026-04-12-round2]] — 이 synthesis의 data 공급원 확인된 lint 라운드

---

## 7. Pull Quote — 덱에 쓸 수 있는 한 줄

> **"The world's largest HCM vendor uses Paradox for recruiting and Sana for learning, not its own Illuminate AI. Plan for multi-vendor HR AI, even inside 'all-in-one' suites."**

> **"세계 최대 HCM 벤더 Workday는 자사 Illuminate가 아니라 Paradox로 채용하고 Sana로 학습한다. '올인원' 플랫폼 안에서도 multi-vendor HR AI는 현실이다."**

---

## 8. ★ Counter-evidence — SuccessFactors 패턴 (2026-04-12 업데이트)

G4 리서치에서 이 synthesis의 **단순 narrative를 복잡화하는 반대 증거** 발견:

### 8-1. Delta Air Lines + PepsiCo의 consolidation 사례

[[bersin-successfactors-leapfrog-2024-10]] 에서 Josh Bersin이 전달:

> "**Delta Air Lines and Pepsi** are using SuccessFactors Talent Intelligence hub as their new **end-to-end platform**, with each company reporting they **no longer felt the need to use some of these other third party products**"

명시적으로 언급된 "other third party products":
- **Gloat** (talent marketplace)
- **Eightfold** (talent intelligence)
- **Phenom** (talent experience)
- **Beamery** (recruitment marketing)

즉 SAP SuccessFactors 고객은 **Workday 자사 패턴과 정반대**:
- **SF 패턴**: point solution 버리고 suite로 **consolidation**
- **Workday 패턴**: suite 벤더 자체가 point solution을 **병행 사용**

### 8-2. 대조표 (확장)

| 축 | Workday 패턴 | SuccessFactors 패턴 |
|---|---|---|
| **증거 출처** | [[paradox-clients-stories-2026-04]] + [[bersin-ld-revolution-2025-06]] | [[bersin-successfactors-leapfrog-2024-10]] |
| **사례 기업** | Workday (자사 채용팀 + leadership academy) | Delta Air Lines, PepsiCo |
| **채용 AI** | Paradox Olivia 사용 | SF Talent Intelligence Hub (Eightfold·Gloat 버림) |
| **Learning AI** | Sana / Galileo Learn 사용 | SF Learning (내부) |
| **철학** | Best-of-breed (suite 벤더 자체가 실천) | Consolidation (고객이 추구) |
| **Skills 통합** | Workday Illuminate 독자 | Open Architecture (Lightcast, Korn Ferry, Degreed, Techwolf) |
| **Market signal** | "suite가 만능은 아니다" | "suite가 3rd party를 대체한다" |

### 8-3. 왜 벤더마다 패턴이 다른가 — 가설

1. **제품 성숙도**: SuccessFactors는 2024-10 release로 **30+ 새 AI use case + 63 prior**. Workday Illuminate의 일부 에이전트가 아직 demo 상태인 점과 대조. **성숙도 gap**이 현재 전략 차이를 만들 수 있음.
2. **기업 철학**: SAP는 "통합 suite + S/4HANA 연계", Workday는 "**cloud-first openness**"를 강조해 온 역사가 있음
3. **Go-to-market**: SAP는 **consolidation**을 pitch하는 것이 유리 (3rd party 교체 → SF 매출 증가). Workday는 **integration-friendly**를 pitch하는 것이 유리.
4. **Sample bias**: 각 벤더는 자신에게 유리한 customer story를 선택적으로 공개. Workday가 Paradox 쓴다는 사실도, Delta가 Eightfold 버렸다는 사실도 **"벤더가 보여주고 싶은 것"**만 wiki에 들어왔을 가능성.

### 8-4. 재정의된 컨설팅 프레임

원래 synthesis의 권고는 **"multi-vendor stack을 기본 가정으로"** 였다. G4 counter-evidence 이후에는 다음과 같이 재정의:

> **"Suite 벤더 선택은 동시에 vendor strategy 선택이다. Workday를 선택하면 'best-of-breed + 자체 suite' 혼합을 준비하고, SuccessFactors를 선택하면 '고객이 3rd party를 버리는 consolidation'을 준비하라. 중간은 없다 — **벤더 자체가 철학이다**."**

### 8-5. 클라이언트에 추가로 물어야 할 질문

기존 §3-1의 3개 질문에 더해:

4. **"우리 조직은 SF 스타일 consolidation이 문화적으로 맞는가, Workday 스타일 best-of-breed가 맞는가?"**
   - SF 스타일: 단일 벤더 관리·거버넌스가 편한 대기업에 fit
   - Workday 스타일: 빠른 실험·point solution 수용이 편한 tech 조직에 fit
5. **"Delta·Pepsi가 왜 3rd party를 버렸는지"가 우리에게도 적용되는가?**
   - Gloat·Eightfold·Phenom·Beamery를 **이미 사용 중인** 조직이라면 SF가 주장하는 대체 효과가 실제인지 검증 필요
6. **Workday가 언제부터 자사 Illuminate Recruiter Agent로 Paradox를 대체할 계획인가?**
   - 이 질문에 Workday는 답이 어려울 것 — 이 불확실성 자체가 의사결정 변수

---

## 9. Sample size 및 한계 (강화)

§4에서 원래 지적한 한계에 더해:

- **Workday 패턴 샘플**: 2건 (Paradox + Sana)
- **SF 패턴 샘플**: 2건 (Delta + Pepsi)
- **Oracle HCM 패턴**: **확인된 사례 0건** (G4 리서치에서 발견 못 함 — 미수집)
- **SAP 주장의 반박 관점**: Gloat·Eightfold·Phenom·Beamery 측의 반박은 본 wiki 미수집
- **지역 편향**: 모두 미국 기업 사례. 유럽·아시아·한국 기업 패턴은 다를 수 있음

→ **다음 리서치 우선순위**:
1. Oracle HCM 고객의 AI 벤더 사용 패턴
2. Gloat·Eightfold 측의 counter-narrative (SF에게 고객을 잃었다는 주장에 대한 반박)
3. Delta·Pepsi 공식 자료에서 consolidation 이유 직접 확인
4. 한국 대기업(삼성·LG·현대·SK)의 suite vs best-of-breed 패턴
