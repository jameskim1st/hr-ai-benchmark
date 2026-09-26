# HR Taxonomy (대/중/소 그룹)

모든 use case 페이지는 frontmatter의 `primary_category`(대그룹), `subcategory`(중그룹), `tags`(소그룹)에 아래 값을 사용한다. **디렉토리로 카테고리를 고정하지 않고 태그로 관리**한다 — 하나의 use case가 여러 카테고리에 걸치는 경우가 많기 때문.

### 대그룹 7개

1. **Talent Acquisition** — 채용·인력확보
2. **Onboarding & Transitions** — 온보딩·발령·이동·퇴직
3. **Learning & Development** — 교육·역량·스킬
4. **Performance & Talent Management** — 평가·승진·핵심인재·후계
5. **Total Rewards** — 보상·급여·복리후생
6. **Employee Experience & HR Ops** — EX·HR 운영·근태·Core HR
7. **Strategic Workforce & Governance** — 인사기획·People Analytics·노사·거버넌스

### 중그룹 / 소그룹

#### 1. Talent Acquisition
- **Sourcing & Attraction**: JD 생성, employer branding, passive candidate mining, 채용 마케팅
- **Screening & Assessment**: Resume parsing, skills matching, chat screening, video interview 분석, bias audit
- **Interview & Selection**: 질문 생성, interview copilot, scorecard 자동화, reference check
- **Offer & Pre-boarding**: Offer letter 생성, 협상 시뮬레이터, 문서 수집
- **Executive Search (핵심인재 채용)**: Referral·Search Firm·Direct Sourcing
- **Early-career Pipeline**: 대졸 정기/수시 채용, 장학생 선발·관리, 인턴십, 산학협력

#### 2. Onboarding & Transitions
- **New-hire Onboarding**: 개인화 온보딩 플랜, 30·60·90 체크인, 시스템 프로비저닝
  - *Mentoring Program*: 멘토 매칭, Phase1~Final 관리, 체크인 봇
- **Internal Mobility**: Talent marketplace, 사내공모, Redeployment/재배치, Project Staffing
- **Global Mobility**: 주재원 선발·발령·파견·귀임
- **Offboarding**: Exit interview 분석, 지식 이관, alumni 네트워크
  - *Mandatory Retirement*: 정년퇴직, 임금피크, 정년연장 신청

#### 3. Learning & Development
- **Skills & Capabilities**: Skills ontology, skills gap 분석, skills inference, 직무전문성 진단
- **Content & Delivery**: 과정 자동 생성, adaptive learning path, AI tutor/coach, 마이크로러닝
- **Performance Support**: Workflow-embedded copilot, just-in-time 지식
- **Language & Certification**: 어학관리, 자격 관리

#### 4. Performance & Talent Management
- **Goal & Performance**: OKR/목표 생성, 연속 피드백 요약, 리뷰 초안, calibration 분석, 1:1 지원
- **Succession & Leadership**: HiPo 식별, 후계자 추천, 리더십 assessment, 최고 기술전문가 관리(TLE류)
- **Coaching**: AI 코치(BetterUp 류), manager copilot, LMD 지원

#### 5. Total Rewards
- **Compensation**: Pay strategy/보상기획, Pay equity, comp benchmarking, offer modeling
  - *Equity & Stock Programs*: 우리사주, 자사주, RSU, 스톡옵션, ESPP
- **Payroll Operations**:
  - *Payroll Execution*: 정기급여, 상여(PS/PI), 비정기 급여
  - *Year-end Tax Settlement*: 연말정산, 수정신고
  - *Retirement Settlement & Pension*: 퇴직정산, DC/DB 연금, 중도인출
  - *Accruals & Reserves*: 퇴직·연차·상여 충당금, 인건비 마감
  - *Garnishment & Deductions*: 채권압류, 공제
- **Benefits & Wellbeing**:
  - *Health & Insurance*: 의료비, 보험, 산재
  - *Flexible Benefits*: 복지포인트, 포인트몰 추천
  - *Wellbeing & Mental Health*: 웰니스 챗봇, EAP triage
  - *Life Events*: 경조사, 휴직, 학자금
  - *Perks & Facilities*: 식대, 통신비, 기숙사, 동호회, 숙면보조, 차량유지
- **Recognition**: 사내/사외 포상, 장기근속, peer recognition

#### 6. Employee Experience & HR Ops
- **Core HR & Employee Records**: Master data 유지보수, 문서·학위·어학·가족 등록, 개인정보 거버넌스, One Resume, 경력 소개서
- **Employee Self-service**: Ask HR 챗봇, 정책 Q&A, case deflection, 제증명
- **HR Service Delivery**: 티켓 분류/라우팅, 지식베이스 유지, 인사 문의응답
- **Time, Attendance & Absence**:
  - *Daily Time & Attendance*: 근태 기록, 이상 탐지, 카드키
  - *Shift & Overtime*: 교대 최적화, 52시간 컴플라이언스
  - *Leave & Return-to-work*: 휴직 관리, 복직 re-onboarding, 연차
- **Listening & Engagement**: Pulse 설문, sentiment/ONA, 이직 예측 (신호 수집 관점)
- **Culture & OD**: 조직문화 진단, 가치체계, 변화관리 nudge
- **Comms & Change**: 내부 커뮤니케이션 생성, announcement 개인화

#### 7. Strategic Workforce & Governance
- **Workforce Planning**: 정기/수시 인력계획, Job Architecture(직무체계), scenario/capacity modeling, 수시 충원
- **Org Design**: 정기/수시 조직개편, 조직 현황 분석
- **People Analytics**: HR 현황·역량·Time 분석, attrition 예측, text-to-SQL HR 분석
  - *Retention Management*: Retention 인력 리스트·리포트·면담 운영 (운영+분석 통합)
- **DEI**: Bias 감사, 포용성 분석, 대표성 dashboard
- **Employee Relations & Labor**:
  - *Contract Management*: 근로계약(기술사무직/전임직/계약직), 임원계약, 서약서
  - *Awards & Recognition Admin*: 사내/사외/장기근속 포상 운영
  - *Discipline*: 징계 관리, 유사사례 검색
  - *Labor Relations*: 노사관계, 단협, 고충처리
- **Compliance & Risk**: 정책 초안, 규제 모니터링(EU AI Act, NYC LL144, 개인정보법), 감사 로그
- **HR Tech Governance**: Vendor risk 평가, 권한 체계, 코드 관리, AI 모델 governance, HR-in-the-loop 설계

---

# AI 기술 유형 태그

모든 use case의 frontmatter에는 카테고리 외에도 다음 축 태그가 붙는다:

- `industry`: pharma, finance, tech, manufacturing, retail, public, consulting, energy, logistics
- `region`: na, eu, apac, kr, global
- `employee_class`: 기술사무직, 전임직, 계약직, 임원, all
- `frequency`: daily, monthly, annual, adhoc (프로세스 실행 주기 — AI ROI 판단에 활용)
- `stage`: announced, pilot, production, sunset
- `vendor_type`: hrms, ats, lxp, talent-marketplace, point-solution, foundation-model, internal-build
- `ai_tech_type`: 사용된 AI 기술 5 대분류 (use case 1건이 다수 type 가능)
- `ai_tech_subtype`: 13 소분류 (subtype은 반드시 자기 부모 type과 함께 표기)

### `ai_tech_type` / `ai_tech_subtype` taxonomy (PwC 양식)

분류 기준·실수 사례·실전 매핑은 **`기타/ai_technology_categories.md`**를 ground truth로 사용. 신규 use case 작성·기존 use case 갱신 시 모두 이 reference doc의 정의를 따른다.

| 대분류 (top-level) | ID | 소분류 (subtype) | ID |
|---|---|---|---|
| ① 생성형 (Generative) | `generative` | 텍스트 생성 | `text-generation` |
| | | 요약·재작성·질의응답 ⭐ | `summarization-qa` |
| | | 멀티모달 생성·이해 | `multimodal` |
| | | 정보 추출 | `information-extraction` |
| ② 판별·예측 (Predictive) | `predictive` | 예측 | `prediction` |
| | | 군집·분류 | `clustering-classification` |
| | | 추천·랭킹 | `recommendation-ranking` |
| ③ 인식 (Recognition) | `recognition` | OCR | `ocr` |
| | | 음성 인식 | `speech-recognition` |
| ④ 의사결정·최적화 (Decision·Optimization) | `decision-optimization` | 최적화 | `optimization` |
| ⑤ 자동화 (Automation) | `automation` | RPA | `rpa` |

**핵심 분류 원칙** (reference doc 발췌 — 자주 혼동되는 지점):

1. **요약·재작성·질의응답이 압도적 다수** — chatbot·정책 Q&A·메일/보고서 작성은 거의 모두 `summarization-qa`. `text-generation`은 자유 창작에만.
2. **예측 vs 군집·분류** — 미래 확률적 ML 추론(이탈·매출 예측)만 `prediction`. 규칙 기반 binary 판정은 `clustering-classification`.
3. **최적화** — LP·휴리스틱·강화학습 등 알고리즘이 들어가야 `optimization`. 단순 판정은 분류.
4. **RPA** — 봇이 화면·시스템 조작하는 경우만. AI agent의 텍스트 자동 작성은 RPA 아님.
5. **멀티모달** — 텍스트+이미지/음성/영상 동시. PDF→텍스트만 뽑는 건 `information-extraction`.
6. **정보 추출** — 비정형 텍스트(이력서·메일)에서 구조화 필드 추출 (NER 류).

Dataview 쿼리로 어떤 축으로든 재조합 가능하게 유지하는 것이 목적.

---
