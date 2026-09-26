#!/usr/bin/env python3
"""
One-shot batch script: inject **Before/After** Process content into 21 vendor
use case pages. Three patterns:
  (1) NO Solution Architecture, NO ### A. → insert full block before "## Impact"
  (2) HAS Solution Architecture but NO ### A. → insert "### A. Process" inside SA
  (3) HAS ### A. but bad format → replace existing A. content
"""
import re
from pathlib import Path

BASE = Path(__file__).parent.parent
UC = BASE / "wiki" / "usecases"

# Each entry: slug → (before, [after_steps], hitl, frequency, source_note)
PROCESSES = {
    "beamery-atkins-realis-skills-architecture": (
        "정적 직무 기술서·수동 skills 매핑 (4~6개월 소요), 부서별 분절된 skills 데이터",
        [
            "기존 직무 기술서·HRIS·프로젝트 이력 등 fragmented data 업로드",
            "Beamery Skills Inference 엔진이 role별 핵심 skill 추출 (⚠️ 벤더 주장 90% 정확도)",
            "Dynamic Job Architecture 자동 생성 — role/family/proficiency level 매핑",
            "HRBP·HR tech 팀이 taxonomy 검토·승인",
            "Workday/SAP SuccessFactors로 동기화하여 채용·내부이동·L&D에 활용",
            "시장·내부 시그널 변화 시 skills blueprint 자동 갱신",
        ],
        "HR/COE가 inferred skills taxonomy의 role mapping 승인",
        "초기 17일 구축 후 continuous refresh",
        "Beamery Job Architecture product page",
    ),
    "deloitte-workforce-analyzer-salesforce": (
        "역할별 AI 영향도를 수기 워크숍·인터뷰로 6~12개월에 걸쳐 평가",
        [
            "조직의 job catalog·task inventory를 Workforce Analyzer에 로드",
            "GenAI 엔진이 role별 task 분해·AI 자동화/증강 가능성 점수화",
            "시나리오 모델링 — task automation 비율·재배치 영향·skills gap 시뮬레이션",
            "Workforce Planner+ 모듈이 우선순위·도입 로드맵 추천",
            "HR·전략·재무 리더가 시나리오 비교·승인",
            "Salesforce 사례에서는 skills data와 결합해 reskilling 결정에 활용",
        ],
        "비즈니스 리더가 AI 영향 시나리오를 검토·전략 결정",
        "adhoc (전사 AI 전략 수립 시)",
        "Deloitte HC AI Suite press release",
    ),
    "hirevue-ai-assessment-bias-audit": (
        "AI 채용 알고리즘이 inference time에 학습되거나 bias 점검 없이 운영",
        [
            "HireVue의 competency·game-based 알고리즘은 lab에서 학습·테스트 후 lock (static·deterministic)",
            "외부 감사기관(DCI Consulting Group)이 인종·성별·교차 카테고리별 disparate impact 분석",
            "NYC Local Law 144 등 규제 요건에 맞춰 bias audit table 생성 (~300건)",
            "결과 공개·AI Explainability Statement 게시",
            "알고리즘 업데이트는 명시적 재학습·재감사 절차 거쳐야만 가능",
            "고객사는 자사 사용 결과로 추가 fairness monitoring 수행",
        ],
        "외부 감사인이 알고리즘 결과 검증, HR/legal team이 사용 가능 여부 결정",
        "annual + 알고리즘 변경 시",
        "HireVue press release on DCI bias audit",
    ),
    "microsoft-employee-self-service-agent": (
        "직원이 HR/IT 문의 시 다중 portal·ticket 시스템을 거치며 응답 지연",
        [
            "직원이 M365 Copilot 비즈니스 채팅에서 \"Employee Self-Service\" 선택",
            "자연어로 질문 입력 (휴가 신청·급여·복리후생·장비 요청 등)",
            "Agent가 SharePoint 정책 KB·Workday/SAP/ServiceNow connector 조회",
            "authoritative 응답 또는 action form 제시 (휴가신청·transfer 요청 등)",
            "직원이 form 제출 → 배후 시스템 워크플로 트리거",
            "미해결 시 Agent가 자동으로 ticket 생성·HR 담당자에 라우팅",
        ],
        "복잡 case는 HR agent에게 escalate, manager는 transfer/profile 변경 승인",
        "daily (일상 self-service)",
        "Microsoft Adoption — Employee Self-Service Agent product page",
    ),
    "pwc-ai-upskilling-65k": (
        "컨설턴트가 ad-hoc 외부 강의·자율학습으로 AI 역량 습득, 일관성·실무 적용 부족",
        [
            "PwC가 My AI 프로그램 출범 — Responsible AI·prompting·leadership 커리큘럼 설계",
            "ChatPwC (사내 GenAI tool) 액세스 부여 — risk-free playground 제공",
            "GenAI Super User Network (약 350명 자원자)가 팀별 워크숍·prompting party 진행",
            "직원이 hackathon·게임쇼식 경쟁·라이브 실습에 참여",
            "학습 시간·use case 제출 추적 (자발적 360,000+ 시간 기록)",
            "우수 use case는 클라이언트 프로젝트 자산으로 승격",
        ],
        "Super User가 facilitation, Responsible AI 팀이 use case 검토",
        "continuous (ongoing program)",
        "PwC US $1B AI Investment press release",
    ),
    "textio-tmobile-inclusive-jd": (
        "채용 매니저가 JD를 자유 작성, gendered language·전형적 표현으로 다양성 후보 풀 제한",
        [
            "채용 매니저/리크루터가 Workday ATS에서 JD 작성 시작",
            "Textio 플러그인이 실시간으로 단어·구문 분석 (수백만 hiring docs 학습)",
            "편향·가독성 기반 Textio Score 산출 + 대안 표현 제안",
            "작성자가 제안 수용/거절하며 점수 ≥90 목표",
            "90+ 점수 도달 시 ATS에 자동 게시",
            "응답률·다양성 지표로 ROI 추적 (T-Mobile: 여성 후보 +17%, time-to-fill -5일)",
        ],
        "채용 매니저가 모든 제안에 대해 accept/reject",
        "event-driven (모든 JD 작성 시)",
        "T-Mobile case study (Textio)",
    ),
    "accenture-ai-learning-workforce": (
        "분절된 LMS·외부 partner 콘텐츠가 개인화 없이 카탈로그형으로 제공",
        [
            "직원 skills profile·role·우선순위 영역을 LearnVantage에 입력",
            "AI recommendation 엔진이 Accenture·Stanford Online·Udacity 등 콘텐츠 큐레이션",
            "개인화된 learning journey + Nanodegree/academy track 추천",
            "일상 워크플로 내 AI coaching·real-time feedback 제공",
            "진척도/완료/지연 모듈 추적, ecosystem partner별 필터링",
            "완료 인증서·skill 인증이 직원 profile에 반영",
        ],
        "L&D 팀이 priority skill area 정의, manager가 학습 시간 승인",
        "daily (in-flow learning)",
        "Accenture LearnVantage product page",
    ),
    "hsbc-eightfold-gloat-multi-vendor": (
        "14만 직원 대상 내부공모는 manager 추천·비공식 네트워크 의존, 글로벌 가시성 부재",
        [
            "HSBC middleware가 HRIS·ATS·LMS·skills 데이터를 통합",
            "Eightfold이 1.6B+ profile 기반 skills inferencing 수행 (기반 skill graph)",
            "Gloat marketplace에 inferred skills로 직원·기회 매칭",
            "직원이 project·gig·job·mentorship 검색·지원 (인도 tech팀 우선 → 14만 확장)",
            "AI가 매칭 점수·career path 추천",
            "매니저·HR이 매칭 결과 검토·승인",
        ],
        "매니저가 internal candidate 인터뷰·승인",
        "continuous (rolling marketplace)",
        "Gloat HSBC case study",
    ),
    "phenom-merck-kgaa-talent-marketplace": (
        "내부 후보자가 지원해도 결과 통보 없이 발표로 알게 되는 등 candidate experience 미흡",
        [
            "직원이 MyGrowth 포털에서 profile 생성·skills 입력 (200,000+ skills)",
            "Phenom AI가 inferred skills로 jobs·gigs·learning·mentor 매칭",
            "개인 dashboard에서 추천 기회·learning(29,000+ 콘텐츠)·mentor 1,000+ 표시",
            "직원이 gig/job/mentor 신청 → 매니저·HR에 routing",
            "채용 매니저가 internal candidate 검토·피드백",
            "결과·진행상황을 candidate에게 자동 통지",
        ],
        "매니저가 internal candidate 평가·결정",
        "continuous",
        "Phenom 2025 Talent Experience Award Winners",
    ),
    "qualtrics-adidas-employee-experience-ai": (
        "분기/연간 engagement 설문 후 manager가 보고서 수기 분석 (160+ hours/cycle)",
        [
            "직원이 Continuous Listening 설문 응답 — Qualtrics가 conversational AI로 follow-up 질문",
            "Qualtrics Assist for EX가 sentiment·테마 분석, manager별 personalized insight 생성",
            "매니저별 dashboard에 팀 specific feedback + action recommendation 제시",
            "xFlow workflow가 HRIS·ticketing 시스템과 연동해 자동 alert·action",
            "Predictive retention 분석으로 at-risk 직원 식별",
            "매니저가 추천 action 실행, 다음 cycle에서 효과 측정",
        ],
        "매니저가 AI action recommendation 채택·실행",
        "continuous + cycle-based",
        "Adidas/Allstate Qualtrics (Benefit News)",
    ),
    "ericsson-degreed-ai-skills-upskilling": (
        "5년 전 300명 과학자 한정 LMS, role-기반 정적 커리큘럼",
        [
            "직원이 Degreed에서 skill profile·proficiency 입력 (97% 활성화)",
            "AI가 role·proficiency 기반 personalized learning path 추천",
            "직원이 micro-learning·course·role-play·coaching 소비 (월 64% 재방문)",
            "Career Hub talent marketplace가 skill 매칭으로 internal mobility/gig 제공",
            "AI nudge·real-time coaching이 일상 워크플로에 embed",
            "Skill acquisition을 job ad·career path와 연동하여 30,000명 AI 업스킬링",
        ],
        "매니저가 development plan 검토, L&D팀이 priority skill 정의",
        "daily",
        "Degreed Ericsson case study",
    ),
    "nestle-paradox-recruiting": (
        "후보자가 career site에서 긴 지원 form 작성, 리크루터가 수동 스크리닝/스케줄링",
        [
            "후보자가 career site/모바일에서 Olivia chatbot과 대화 시작",
            "Olivia가 knockout 질문 (자격·근무가능시간·work auth)으로 스크리닝",
            "통과 후보에게 FAQ (급여·복지·문화 — 500+ Q&A) 응답 + interview slot 제안",
            "채용 매니저 캘린더와 동기화하여 interview 자동 예약",
            "리마인더·재스케줄링·offer letter·I9·start date 모두 conversational",
            "결과가 ATS로 자동 통합되어 hiring funnel에 반영",
        ],
        "채용 매니저가 인터뷰·offer 결정",
        "continuous (모든 지원)",
        "Paradox Nestlé case study",
    ),
    "servicenow-now-assist-hr": (
        "HR 케이스가 분류·라우팅·해결까지 다단계 manual ticket 처리",
        [
            "직원이 ServiceNow employee portal/Teams에서 HR 요청 제출",
            "Now Assist가 case 내용 분석 → criticality 분류 (non-critical/critical)",
            "Non-critical case는 HR knowledge base·catalog 조회하여 자동 해결",
            "Hiring 영역에서는 Schedule Interview agent·Create Job Requisition agent가 conversational 처리",
            "Critical/판단 필요 케이스는 HR agent에 라우팅하며 context summary 제공",
            "HR agent가 검토·해결, 결과로 KB 업데이트",
        ],
        "critical case·judgment-required 단계에서 HR agent 개입",
        "daily (case 발생 시 즉시)",
        "ServiceNow Agentic AI for HRSD",
    ),
    "visier-vee-people-analytics": (
        "HRBP·매니저가 People analytics 질문에 데이터 팀 ticket 의존, 답변 수일 소요",
        [
            "사용자가 Visier People 또는 Microsoft Teams에서 Vee와 자연어로 채팅",
            "Vee가 자연어 질문을 Visier query로 변환",
            "조직의 people data로 query 실행 (proprietary customer data는 LLM 학습 미사용)",
            "narrative 답변·차트·요약·자동 보고서 생성",
            "사용자가 chart·data point 기반으로 후속 질문 가능",
            "응답에 Visier governance·permission 모델 적용",
        ],
        "사용자가 답변 검토·해석·의사결정",
        "daily (ad-hoc 질의)",
        "Visier Vee product page",
    ),
    "cathay-pacific-hirevue": (
        "졸업생 trainee 채용에 3개월 소요, in-person 면접 no-show율 높음",
        [
            "지원자가 온라인 지원 → ATS에서 HireVue 초대 발송",
            "후보자가 mobile/web으로 on-demand video 인터뷰 녹화 (graduate 90% 응답률)",
            "HireVue가 응답·언어 사용 (콜로키얼/슬랭 포함) 평가하여 점수 산출",
            "채용팀이 score·video 검토 후 최종 라운드 후보 shortlist",
            "통과 후보만 in-person 최종 평가에 초대",
            "Cathay 채용 매니저의 인사말 영상으로 employer branding 강화",
        ],
        "채용팀이 HireVue score 검토, 최종 면접관이 합격 결정",
        "event-driven (graduate/cabin crew intake)",
        "HireVue Cathay Pacific case study",
    ),
    "eightfold-ai-talent-intelligence": (
        "채용·내부이동·후계 별도 시스템, 정적 직무 기술서·resume keyword 매칭",
        [
            "회사 HRIS·ATS·LMS 데이터를 Eightfold에 연결",
            "Capabilities Matrix가 직원 skill·capability·aspiration·work pattern 모델링 (1.6B+ profile 기반)",
            "Job Intelligence Engine이 role 정의·job architecture 자동 생성·refresh",
            "채용·internal mobility·succession·career에 unified 매칭 점수 제공",
            "Agentic AI가 sourcing·screening·interview scheduling 등 워크플로 자율 실행",
            "결과/feedback이 self-learning engine에 반영되어 매칭 정확도 개선",
        ],
        "리크루터·매니저가 매칭 후보 검토·결정, 단계별 checkpoint",
        "continuous",
        "Eightfold Talent Intelligence Platform product page",
    ),
    "emirates-hirevue-volume-hiring": (
        "Pandemic 후 1만 명 cabin crew 재채용 필요, 전통 face-to-face 채용으로는 timeline 불가",
        [
            "글로벌 후보자가 Emirates 채용 페이지에서 지원 → HireVue 초대",
            "후보자가 English 어학 평가 (15분 객관식) 응시 — 가장 큰 탈락 관문",
            "situational prompt에 대한 video 응답 녹화 (수초간 준비)",
            "HireVue가 verbal·written 응답을 채점 (⚠️ 벤더 주장 non-verbal cues 포함)",
            "통과자만 assessment day 초대 (시간·비용 대폭 절감)",
            "최종 채용 결정은 in-person assessor",
        ],
        "HR assessor가 영상 검토·최종 결정, 채용 매니저 승인",
        "event-driven (대량 cabin crew intake)",
        "HireVue Emirates Group case study",
    ),
    "fuel50-lennox-internal-mobility": (
        "내부이동이 매니저 referral·HR 큐레이션에 의존, 직원 가시성·career path 불투명",
        [
            "직원이 Fuel50에서 Talent DNA (Talents/Skills/Values/Agility/Fit) 작성",
            "AI가 ethically-enhanced 매칭으로 gigs·projects·mentorships·lateral moves 추천",
            "직원이 즉시 검색·지원 가능, 매니저 추천 불필요",
            "매니저는 gig 게시·applicant 풀 관리·프로젝트 talent pool 구축",
            "Career path·coaching·mentor 매칭으로 retention 강화",
            "Lennox: 4,800건 internal move, 평균 +5개월 tenure",
        ],
        "매니저가 gig applicant 선발·승인",
        "continuous",
        "Fuel50 Talent Marketplace product page",
    ),
    "mcdonalds-paradox-recruiting": (
        "매장 매니저가 종이/이메일로 지원 처리, 지원 시간 10분, 시간 부족으로 채용 누수",
        [
            "후보자가 매장 sign·광고·Alexa/Google Assistant (Apply Thru)로 시작",
            "텍스트 번호 발송 → Olivia가 즉시 conversational 스크리닝 시작",
            "기본 work history·available shift 질문 (지원 시간 10분→2분)",
            "통과 후보에게 매장 매니저 캘린더 기반 interview slot 제시",
            "COVID 기간엔 video로 추가 질문 응답",
            "매장 매니저가 in-person 인터뷰에서 hire 결정 (McHire 플랫폼 통합)",
        ],
        "매장 매니저가 in-person interview·hire 결정",
        "continuous (대량 시간제 채용)",
        "Paradox McHire launch press release",
    ),
    "syndio-pay-equity-ai": (
        "보상 결정 시 매니저·HR이 spreadsheet·외부 market data로 ad-hoc 판단, equity 위반 사후 발견",
        [
            "회사가 compensation·workforce·HRIS data를 Syndio에 연결",
            "PayEQ가 protected class 그룹별 pay gap 분석·통계적 검증",
            "매니저가 Teams/Slack/ATS에서 offer·raise 결정 시 Syndi 호출",
            "Syndi agentic AI가 internal equity·budget·market 균형 추천 + 설명 제공",
            "매니저가 추천 채택/divergence 결정 (이유 캡처 → decision intelligence)",
            "Expertise on Demand AI가 pay gap 보고·규제 컴플라이언스 가이드",
        ],
        "매니저·comp 팀이 모든 pay 결정 검토·실행",
        "event-driven (offer·raise·promotion) + 정기 audit",
        "Syndio Syndi launch press release",
    ),
    "workday-illuminate-employee-sentiment": (
        "engagement 설문 결과를 People 팀이 quarterly로 분석·매니저에게 PPT 배포, action 지연",
        [
            "Workday HCM 내 engagement·pulse·feedback·exit data가 Illuminate에 자동 공급",
            "Employee Sentiment Agent가 feedback 데이터를 continuous 분석",
            "팀·코호트별 sentiment trend·driver·이상 신호 추출",
            "매니저 Workday 워크플로에 proactive insight 푸시",
            "매니저가 추천 action (1:1·recognition·career conversation) 실행",
            "결과 데이터가 다시 agent learning loop에 반영",
        ],
        "매니저가 sentiment insight 검토·action 결정",
        "continuous (real-time monitoring)",
        "Workday Illuminate Expansion announcement",
    ),
}


def build_section(slug, before, after_steps, hitl, freq, source):
    """Build the Solution Architecture / A. Process block."""
    after_md = "\n".join(f"  {i+1}. {step}" for i, step in enumerate(after_steps))
    return f"""## Solution Architecture

### A. Process

- **Before**: {before}
- **After**:
{after_md}
- **HITL**: {hitl}
- **Frequency**: {freq}
- **Source**: {source}

"""


def build_a_only(slug, before, after_steps, hitl, freq, source):
    """Just the A. Process subsection (no SA wrapper)."""
    after_md = "\n".join(f"  {i+1}. {step}" for i, step in enumerate(after_steps))
    return f"""### A. Process

- **Before**: {before}
- **After**:
{after_md}
- **HITL**: {hitl}
- **Frequency**: {freq}
- **Source**: {source}

"""


def update_page(slug, data):
    fp = UC / f"{slug}.md"
    if not fp.exists():
        print(f"SKIP {slug}: file not found")
        return False
    text = fp.read_text(encoding="utf-8")

    has_sa = "## Solution Architecture" in text
    has_a = bool(re.search(r"^### A\.", text, re.MULTILINE))

    if not has_sa and not has_a:
        # Pattern 1: Insert full SA block before "## Impact"
        block = build_section(slug, *data)
        new_text, n = re.subn(
            r"(\n## Impact)",
            f"\n{block}\\1",
            text,
            count=1,
        )
        if n == 0:
            print(f"FAIL {slug}: no '## Impact' anchor found")
            return False
        fp.write_text(new_text, encoding="utf-8")
        print(f"P1   {slug}: SA+A inserted before Impact")
        return True

    if has_sa and not has_a:
        # Pattern 2: Insert "### A. Process" right after "## Solution Architecture"
        block = build_a_only(slug, *data)
        # Replace "## Solution Architecture\n" + optional next 1-2 lines (subtitle) with SA + new A.
        # Simpler: insert immediately after the SA heading.
        new_text, n = re.subn(
            r"(## Solution Architecture[^\n]*\n+)",
            f"\\1{block}",
            text,
            count=1,
        )
        if n == 0:
            print(f"FAIL {slug}: SA heading regex failed")
            return False
        fp.write_text(new_text, encoding="utf-8")
        print(f"P2   {slug}: A inserted after SA heading")
        return True

    if has_a:
        # Pattern 3: Replace existing A. section content (everything between "### A." and next "###" or "##")
        block = build_a_only(slug, *data)
        new_text, n = re.subn(
            r"### A\.[^\n]*\n.*?(?=\n###\s|\n##\s)",
            block.rstrip() + "\n",
            text,
            count=1,
            flags=re.DOTALL,
        )
        if n == 0:
            print(f"FAIL {slug}: A.section regex failed")
            return False
        fp.write_text(new_text, encoding="utf-8")
        print(f"P3   {slug}: existing A. replaced")
        return True


def main():
    ok, fail = 0, 0
    for slug, data in PROCESSES.items():
        if update_page(slug, data):
            ok += 1
        else:
            fail += 1
    print(f"\nDone: {ok} updated, {fail} failed")


if __name__ == "__main__":
    main()
