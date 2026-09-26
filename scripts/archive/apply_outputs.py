#!/usr/bin/env python3
"""126 use case의 output 필드를 frontmatter에 일괄 적용.

각 entry: slug → output (1-2문장).
vendor_type 라인 직후에 output 라인 삽입. 이미 있으면 replace.
"""
import re
from pathlib import Path

BASE = Path(__file__).parent.parent
UC = BASE / "wiki" / "usecases"

OUTPUTS = {
    # ===== Batch 1 (high-conf 43) =====
    "jpmorgan-llm-suite-redeployment": "직원의 자연어 요청에 대한 LLM 응답 (분석·보고서 초안, 회의 요약, 이메일·코드 생성) + annual performance review 초안. 모두 직원·매니저 검토 후 사용",
    "workday-peakon-illuminate-employee-voice": "60+ 언어 pulse 서베이의 자동 테마·sentiment·driver 추출 + 부서별 매니저 dashboard (강점·기회·이슈 highlight) + 이탈/번아웃 risk 선제 alert",
    "accenture-mass-genai-reskilling": "직원별 GenAI 학습 이수 기록 + AI literacy 인증 등급 + 사업부 AI 역량 dashboard. CEO Sweet 거버넌스로 미이수자 exit timeline 산정의 input",
    "cisco-ai-workforce-consortium-skills-evolution": "ICT 직무·AI 스킬 evolution 정량 보고서 (78% AI 포함, top 10 fastest-growing 중 7개 AI) + AI Skills Glossary 표준 + AI Workforce Playbook + 200+ curated learning recommendation 리스트 (PDF 발간물)",
    "ibm-hr-workforce-reduction-agentic": "HR 운영 KPI 자율 처리 결과 (AskHR 80+ 태스크, learning ops 자동화, screening·comp·attrition 분석) + 200명 HR transactional role 폐지·재배치 결정 근거. 절감 budget을 엔지니어·영업 신규 채용에 재투자",
    "korea-ai-basic-act-hr-compliance": "_N/A_ (규제 framework, AI 시스템 자체 없음 — HR 영역 AI 도입 기업이 준수해야 할 컴플라이언스 가이드 문서)",
    "walmart-openai-certification": "740K frontline 직원에게 OpenAI Certification 다층 모듈 (basics → prompt engineering) 무료 access + Me@Walmart 디바이스 학습 콘텐츠 + 50,000명 reskilling 대상자에게 드론 기술자·로봇 수퍼바이저 전환용 인증서",
    "anaplan-workforce-analyst-ai-agents": "자연어 query에 대한 narrative 답변 (지역별 이직률·보류 채용 등) + 시나리오별 재무 영향 시뮬레이션 결과 (채용 동결·조직 개편·재배치) + position-level 정밀 인건비 계획 + AI 권고안",
    "cisco-ai-assistant-hr-agentic": "직원 PTO·정책 Q&A 응답 + 매니저용 time-off notification 메시지 자동 작성 (drafting + outbound action). HR case 열지 않고 처리",
    "ibm-charlie-learning-ops-agent": "학습 enrollment 모니터링 alert (저조 코스) + event 홍보 메시지 자동 생성·배포 + virtual class 출석부 자동 캡처 (100% 정확도) + pre-event comms 자동 발송. L&D admin 대상 백오피스 자동화 산출물",
    "jpmorgan-ai-made-easy-upskilling": "직원별 AI fundamentals·prompt engineering·컴플라이언스 모듈 이수 기록 + 직무별 use case 인증서. 신입 분석가는 prompt engineering 필수 수료증",
    "microsoft-people-skills-inferred-ontology": "직원별 dynamic 스킬 프로파일 (이메일·문서·미팅 텔레메트리 자동 추론, LinkedIn 16K taxonomy 매핑) + 매니저용 Skills Agent의 internal talent 매칭 + Workforce Insights agent의 workforce planning insight",
    "moderna-ask-hr-routing": "직원 자연어 HR 질문에 대한 도메인 분류 라우팅 (performance·career·benefits 등 specialized GPT 분기) + 해당 specialized GPT가 생성한 정책·복리후생·커리어 Q&A 응답",
    "amazon-connections-daily-pulse": "1.5M 직원에 대한 attrition·engagement 예측 점수 + 행동 (non-response trend)·태도 (응답 sentiment) 변화 신호 + 매니저·HR risk alert. 사람 action은 별도",
    "deloitte-zora-ai-hc-suite": "클라이언트 workforce 세그먼트별 AI 영향평가 리포트 (Workforce Analyzer) + 시나리오 기반 인력 재배치 계획 (Workforce Planner+) + 300+ HR workflow library + HR AI maturity 진단 점수 + ready-to-deploy agents",
    "ibm-blue-match-internal-mobility": "opt-in 직원 ~42K에게 personalized 내부 직무 추천 리스트 (스킬·경력·성과·근무지·블로그/코드/forum footprint 기반) + peer 이동 패턴 학습으로 신규 posting 시 매칭 직원 알림",
    "kb-bank-ai-hr-deep-change": "1,100+ 영업점 직원 인사 배치안 (출퇴근·자격증·업무 경력·육아 고충 등 수십 변수 다변량 최적화). HR 검토·조정 후 매니저·직원 통보. 2025 PB·RM 상담 직원에게는 AI 활용 추천",
    "jnj-digital-talent-platform-skills-ai": "130K+ 직원별 inferred 스킬 그래프 (HRIS·채용DB·LMS·프로젝트에서 60~70% 자동 추론, 0~5 proficiency) + MySkills 플랫폼의 본인 스킬 갭·추천 학습/이동 + 임원 dashboard region·BU별 capability heatmap",
    "chipotle-paradox-olivia": "지원자별 4개국어 (영·스·불·독) 대화형 screening 결과 + 매장 매니저 캘린더 연동 인터뷰 슬롯 예약 + offer letter 자동 발송. ⚠️ 자사 보고: time-to-hire 75% 단축",
    "commonwealth-bank-ai-workforce": "50K ChatGPT Enterprise 응답 + 17.5K M365 Copilot 응답 + ChatIT (Teams 기반 IT 지원) 응답 + Future Workforce Program 스킬 개발·커리어 전환 매칭 ($90M AUD 3개년)",
    "deloitte-2026-human-capital-trends-meta": "_N/A_ (분석 리포트 — 13,000+ leader 서베이 기반 HR 트렌드·AI maturity 모델·예측 분석 PDF. AI 추론 시스템 없음)",
    "jpmorgan-llm-suite-employee-productivity": "200K+ 직원 자연어 요청에 대한 LLM 답변 (문서 요약·이메일/보고서 초안·아이디어·코드) + 성과 리뷰 초안. 직원 검토·편집 후 사용",
    "lg-chatexaone-group-rollout": "LG 그룹 5만+ 임직원 자연어 query에 대한 사내 RAG 응답 (사내 규정·프로젝트·기술 문서, 출처 표시) + multi-format 이해 (PPTX·PDF·CSV·도표·수식) + SQL 생성 + 22개 언어 코드",
    "linkedin-learning-ai-coaching": "학습자별 AI Coach와의 대화형 Q&A·요약·심화 답변 + role-play scenario (피드백·면접·negotiation 모의) feedback 텍스트 + LinkedIn 16K skills profile 자동 갱신",
    "lloyds-banking-workday-genai-hr": "67,000명 직원 HR 정책 Q&A 응답 (휴가·복리후생 등 고볼륨 정책 — 파일럿에서 12-15% 자동 응답) + 복잡 문의는 HR 담당자 라우팅. AI Academy 학습 콘텐츠도 산출",
    "mercy-health-ai-nursing-workforce": "일별 간호사 교대 스케줄 최적화안 (코어 69%·내부 유연 23%·계약직 8% 인력 소스별 배정) + 관리자 승인용 권고안 + Dragon Copilot AI 임상 문서화 (정확도 30→90%)",
    "microsoft-viva-glint-copilot-sentiment": "engagement 서베이 open-end 코멘트 자동 합성 + 반복 테마 탐지 + 속성별 (부서·재임기간·매니저) sentiment slice + 산업/규모 benchmark 비교 + Team/Executive 리포트 \"Copilot Highlights\" 섹션",
    "siemens-servicenow-hr-gbs": "360K 직원의 HR·재무·구매 요청에 대한 단일 \"My Services\" 포털 응답 (월 110,000건) + AI 에이전트 자동 인테이크·라우팅·해결 + 복잡 케이스 담당자 라우팅",
    "walmart-ai-frontline-workforce": "2.3M 직원 HR 단일 통합 (Workday) + Paradox Olivia 프론트라인 채용 자동 screening·일정 (60→18일) + 1.5M 직원용 AI 도구 응답 + Manager Academy 이수 기록 + 50K 리스킬링 매칭",
    "walmart-ask-sam-workforce-ai": "매장 associate 음성 query에 대한 음성·텍스트 답변 (가격·재고·통로·정책) + 매장 지도 overlay + WFM 시스템 연동 schedule 조회·교대 요청 액션 + GenAI 정책 step-by-step 가이드. 90만 associate, 주 300만+ query",
    "bosch-rob-hr-ai-assistant": "360,000 직원의 HR 셀프서비스 응답 (계좌 정보 업데이트, 회사 정책, 커리어 정보) + 감성 지능 기반 escalation 신호 (복잡·민감 문의 시 HR 담당자). MS Teams 채널, 25개국 다국어",
    "dbs-bank-hr-ai-talent-analytics": "JIM: 이력서 스크리닝 + 면접 일정 자동 조율 + 초기 후보자 평가 (32→8일). 이탈 예측 모델: 직원별 이탈 가능성 점수 + HRBP alert. iGrow: 직원 스킬·포부 분석 기반 10K+ 내부 과정 매칭 커리어 경로",
    "goldman-sachs-gs-ai-assistant": "지식노동자 자연어 요청에 대한 LLM 멀티모델 답변 (GPT-4o/o3-mini, Gemini 2.0, Claude 3.7 라우팅) — 문서 요약·리서치 노트·규제 문서 분석·코드·다국어 번역. 사내 방화벽 격리",
    "ibm-predictive-attrition-comp-ai": "270K 직원 monthly flight risk 점수 (34+ 변수 6개월 예측, ⚠️ 자사 보고 95% 정확도) + 매니저용 권장 action menu (raise/promotion/training/mentoring) + per-employee salary 인상 추천액 + supporting factors. 매니저 권고 무시 시 attrition 2배",
    "midas-inair-ai-assessment-korea": "지원자별 3개 과제(성향파악·전략게임·영상면접) 종합 성과역량 예측 점수 + HR 담당자 면접·합격 결정용 참고 리포트. KAIST가 Scientific Reports에 검증한 채용 1년 후 업무 성과 예측",
    "pulmuone-duribun-hr-chatbot": "7K 직원 HR 6개 영역 (근태·복리후생·학습·평가·승진·보상) 자연어 질문에 대한 24/365 RAG 답변 (출처 표시, hallucination 최소화) + 복잡 case는 HR 팀 escalation",
    "sap-successfactors-1h-2026-joule-agents": "5개 Joule Agent별 산출물 — Performance & Goals: 매니저용 1:1 대화 포인트, Career: 학습/이동/멘토 추천 + 후계자 후보, HR Service: 정책 Q&A (60% deflection 벤더 주장), People Intelligence: 매니저 dashboard, Payroll: pay Q&A",
    "schneider-electric-gloat-talent-marketplace": "135,000+ 직원에게 스킬·관심 기반 Open Talent Market 매칭 — gig work, career transitions, mentorship 추천. ⚠️ 벤더 주장: 360K+ 시간 unlocked, $15M+ 절감",
    "shinhan-bank-ai-one-platform": "14,000+ 직원의 단일 AI ONE 인터페이스 출력 — 40+ 업무비서 task 결과 (AI-STUDIO·AI-OCR·R비서) + Speech-to-AI 음성 응답. ⚠️ 자사 보고: 1인당 일 30분+ 절감, 향후 상담→전산처리 80% 자동화 목표",
    "sk-cc-adot-biz-hr-recruitment": "자기소개서별 경력·핵심 역량 키워드 추출 + 직무 적합성·리스크 요인 점수 + AI 면접 (영상 응답 분석) + 후보자 맞춤 면접 질문 자동 생성. ⚠️ 자사 보고: 수천 건 4시간 (90% 단축)",
    "sk-group-aibiz-25-companies": "SK 그룹 25개 멤버사·약 8만 명에게 A.Biz platform 표준 LLM 응답 (HR 정책 Q&A + 자동화 워크플로) + HR 담당자가 no-code agent builder로 자체 구축한 챗봇. 국가핵심기술 보유사는 자체 LLM 'A.X' 격리",
    "woori-bank-175-ai-agents": "5대 영역 (고객관계·자산·내부통제·고객상담·업무자동화) 29개 업무에서 175개 에이전트별 산출물 — 코어뱅킹·CRM·콜센터·내부통제 시스템 임베드 액션. ⚠️ 자사 보고: 업무처리 속도 30% 향상 기대",
    "workday-agent-system-of-record-asor": "AI 에이전트의 거버넌스 메타데이터 (owner·purpose·scope·권한) + Workday admin console dashboard (1st-party + 3rd-party 에이전트 통합 관리) + 활동 로그·outcome 분석·감사 추적. AI 추론 산출물 아닌 거버넌스 자체가 output",

    # ===== Batch 2 (mid-conf 56) =====
    "amazon-hr-ai-restructuring": "HR 부서 자동화 산출물 — 채용 screening·티켓 라우팅·정책 Q&A·분석 리포트 자동 생성 + HR 인력 15% 감축 의사결정 입력 (구체 산출물 형태 미공개)",
    "betterup-ai-coaching-twilio": "매니저별 Whole Person Assessment 점수 + 개인화 6개월 learning path + AI coach 대화형 nudge·micro-intervention + behavior change → 비즈니스 KPI(retention·promotion) 매핑 dashboard",
    "deloitte-claude-470k-employees": "회계·감사·컨설팅 직무별 문서 합성·코드 생성·클라이언트 자료 분석 결과물 + 회계사·개발자 특화 Claude 응답 (Trustworthy AI framework 검증 통과)",
    "hyundai-mobis-moai-platform": "사내 1,000만 건 매뉴얼·도면·기술문서 RAG 검색 답변 + 출처 표시 (R&D·IT·품질·영업·생산 영역, HR Q&A는 2025+ 확장 예정)",
    "ibm-askhr-watsonx": "직원 자연어 요청에 대한 80+ HR 태스크 처리 — 정책 Q&A 답변 + 매니저용 salary budget 배분 제안 + recognition 메시지 자동 생성·포인트 부여 + expense 자동 처리",
    "ibm-watsonx-orchestrate-ta-agent": "JD 초안 자동 생성 + 후보자 매칭 리스트 (사내 + ThisWay 8,500+ community) + hiring manager 자격자 alert + 자동 intro 메시지·면접 일정 + Knockri 면접 design·feedback",
    "jobkorea-hiring-center-talent-agent": "채용 담당자 자연어 의도 입력에 대한 후보자 매칭 추천 리스트 + 추천 사유 (잡코리아 후보자 DB·공고 맥락 기반)",
    "korea-electric-power-hr-bot": "지원자 채용 상담 24/7 챗봇 응답·일정 안내 + 직원 역량·업무 이력 기반 적재적소 인사 배치 추천 (HR·부서장 검토용) + 2025-Q4부터 사내 규정·법규·문서 작성 GenAI 산출물",
    "mirae-asset-ai-assistant-platform": "직원 자연어 query에 대한 부서별 매뉴얼·노하우 RAG 답변 + 출처 + 부서·직원이 No-code로 자체 생성한 전용 챗봇 인스턴스 (HyperCLOVA X Dash 기반)",
    "novartis-gloat-skills-marketplace": "직원별 개인화 추천 — 잡 기회·프로젝트/기그·멘토십·러닝 콘텐츠 (스킬 온톨로지 + 비즈니스 우선순위 결합)",
    "sap-joule-performance-goals-agent": "매니저용 직원별 성과 대화 자료 — 맞춤 인사이트 + 목표 진척 업데이트 + 개인화 대화 포인트 (SuccessFactors + SAP Business Data Cloud 데이터 통합)",
    "siemens-reskilling-internal-mobility": "My Learning World 학습자별 적응형 학습 경로 추천 (100,000+ 학습 기회·41 capability) + AI 채용·이동 포탈의 후보자-역할 매칭 점수",
    "sk-hynix-ask-ai-interview": "직무별 AI 영상면접 질문 출제 + 지원자 영상 답변 평가 + 정량·정성 통합 AI 종합 역량 Report (서류·SKCT·면접·논문·LinkedIn 크롤 통합) — 미래 동료 peer + 면접관용",
    "tcs-infosys-ai-reskilling-india": "직원 AI 역량 인증·proficiency tag (NVIDIA AI Enterprise·Azure OpenAI 커리큘럼 수료) + 인증된 인력 풀의 클라이언트 RFP staffing 매칭",
    "workday-sana-for-workday-lms": "HRD 입력 4일 내 멀티모달 코스 초안 (텍스트·비디오·음성, 30+ 언어) + 학습자 conversational 수강 답변·요약·실습 (Workday HCM 마스터 데이터 통합)",
    "docebo-ai-learning-lazboy": "AI 자동 생성 신규 과정 outline·퀴즈·요약 + 직무·이력 기반 adaptive 다음 과정 추천 + AI virtual coach 대화 답변 + L&D dashboard KPI (active learner·completion)",
    "fujitsu-hr-ai-skills-career": "직원별 스킬 갭 분석 + 내부 공모 매칭 추천 + Fujitsu Learning Experience 자율 학습 경로 + Kozuchi AI 일상 업무 보조 응답 (월 69K 활성·일 380K 사용)",
    "hitachi-skye-hr-ai-assistant": "직원 정책·복리후생 문의에 대한 사업부·국가·역할별 개인화 답변 + IT 서비스 티켓 자동 생성·휴가 요청 자동 처리 + 복잡 케이스 HR 에스컬레이션",
    "hyundai-steel-hip-platform": "사내 매뉴얼·기술·HR·재무·총무 정책 RAG 검색 답변 + 출처 표시 (12K 직원 사내 챗봇)",
    "ibm-watson-recruitment": "후보자별 requisition 대비 success score (gender·race·age·ethnicity 억제) + recruiter용 ranked shortlist + supporting factor 설명 (84% prediction 정확도 벤더 주장)",
    "jpmorgan-goldman-sachs-hr-ai": "knowledge worker용 LLM portal 산출물 — 문서 요약·이메일 초안·Excel/data 분석·번역·코드 (모델 선택형, audit trail) + JPM ML 채용 도구의 후보자 confidence score",
    "meta-ai-performance-review-mandate": "매니저용 직원별 PSC 평가 rubric 점수 (AI-driven impact 항목) + 부서별 AI adoption 분포 리포트 + Metamate가 작성한 코드 commit (agent-assisted 비율 라벨)",
    "moderna-benefits-equity-gpts": "직원 혜택·equity 질문에 대한 자연어 답변 (Benefits Assistant GPT — 의료/401k 가이드, Equity Comp GPT — vesting·RSU·ESPP 용어 설명)",
    "moderna-self-review-gpt": "직원 본인의 성과 data·프로젝트·목표 입력에 대한 연말 self-review 초안 요약문 (직원 검토·편집 후 제출)",
    "nps-ai-innovation-taskforce": "다중 산출물 — AI 사원의 가입자 상담·홍보 자동 응답 + AI 규정비서의 사내 임직원 규정 Q&A + AI 수어 영상 (청각장애 가입자용 multimodal 안내)",
    "posco-dx-110-agents-hr": "인사·구매·경영분석 사무 영역 110개 에이전트의 도메인별 자동화 산출물 (계열사 공통 활용, 2026 launch 예정 — 구체 산출물 형태 미공개)",
    "sk-group-aict-ai-recruitment": "지원자 서류 AI 스크리닝 결과 + AICT 점수 (프롬프트·문제 해결·결과물 평가) + 1차 AI 면접 평가 보고서 + 합격/불합격 자동 고지 + OT 안내 (시간당 1,000명 처리)",
    "tampa-general-visier-people-analytics": "공석율·이직 패턴·에이전시 비용 통합 분석 dashboard + 인력 투자 우선순위 인사이트 (HR + Finance) + Visier Vee 자연어 Q&A 응답 (12K FTE 기반)",
    "workday-illuminate-performance-review-agent": "매니저용 직원별 성과 리뷰 first draft (Workday HCM + 타 시스템 데이터 자동 통합) — 매니저 검토·수정 후 제출",
    "beamery-atkins-realis-skills-architecture": "Skills Inference 엔진의 role별 핵심 skill 추출 (90% 적합도) + Dynamic Job Architecture (role/family/proficiency) + Workday/SAP 동기화용 skills taxonomy (1,200 JD → 40 역할 통합)",
    "coca-cola-southwest-perceptyx-activate": "리더별 개인화 Intelligent Nudge (팀별 설문 결과 + 리더십 원칙 기반) + 액션 플랜 자동 추적 + HR 집계 dashboard (1,191 플랜·1,871 활동)",
    "deloitte-workforce-analyzer-salesforce": "역할별 AI disruption 영향도 점수 + task automation/증강 가능성 시나리오 + 인력 수급 시뮬레이션 + reskilling 우선순위 로드맵 + 300+ agentic HR 워크플로 라이브러리",
    "hirevue-ai-assessment-bias-audit": "후보자 비디오 면접·게임 평가의 competency 점수 (시각 단서 미사용) + 알고리즘 disparate impact 분석 보고서 (인종·성별·교차 ~300건, DCI Consulting 외부 감사) + AI Explainability Statement",
    "hitachi-ema-agentic-hr-onboarding": "신입 IT 계정·200+ 시스템 자동 프로비저닝 (ServiceNow·Jira·Okta·Teams·Google Chat) + 개인화 온보딩 콘텐츠 + 20+ HR 유스케이스 1차 응답 + 복잡 케이스 HR 에스컬레이션",
    "kogas-hybrid-genai-platform": "직원 query에 대한 보안 민감도 자동 분류 + 사내 LLM 응답 (보안 영역) 또는 상용 LLM 응답 (전문지식) 통합 답변 — 문서 초안·규정 검토·단순 행정",
    "korea-gov-ai-hr-public-sector": "공무원용 보고서·민원 답변·보도자료 초안 (망분리 환경 내 삼성SDS·네이버클라우드 LLM + 법령·지침·민원 RAG) — 공무원 최종 검토·결재",
    "lotte-job-based-hr-reform": "_N/A_ (전통 HR 개혁, AI 미공개)",
    "microsoft-employee-self-service-agent": "직원 HR/IT 문의에 대한 authoritative 답변 또는 action form (휴가·급여·복리후생·장비) + 배후 시스템 워크플로 트리거 + 미해결 시 자동 ticket 생성·HR 라우팅",
    "pwc-ai-upskilling-65k": "65,000명 GenAI 업스킬링 인증·시간 추적 (자발적 360,000+ 시간) + Super User 워크숍 산출물 + ChatPwC playground 결과물 + 클라이언트 프로젝트로 승격된 우수 use case",
    "t-mobile-textio-dei-hiring": "JD 작성 시 실시간 Textio Score (0~100) + 성 중립적 언어 개선 제안 + 기준 미달 시 게시 차단 (Workday ATS 인라인 통합)",
    "textio-tmobile-inclusive-jd": "실시간 단어·구문 편향·가독성 분석 Textio Score + 대안 표현 제안 + 90+ 점수 도달 시 ATS 자동 게시 (T-Mobile 여성 지원 +17%, J&J +90K 여성 지원자)",
    "toshiba-microsoft-copilot-viva": "회의 트랜스크립트 요약 + 이메일·회의 따라잡기 응답 + PPT 초안 + 개인 활동 패턴 기반 Copilot 사용 자동 추천 (Viva Insights 분석) — 1인당 월 5.6시간 절감",
    "accenture-ai-learning-workforce": "직원별 개인화 learning journey + Stanford·Udacity·Accenture 콘텐츠 큐레이션 + Nanodegree/academy 추천 + 일상 워크플로 내 AI coaching·real-time feedback + skill 인증",
    "adp-assist-payroll-ai": "급여 데이터 이상 플래그 + 자동 수정 제안 + 자연어 분석 query에 대한 차트·인사이트 + 규정 변경 자동 모니터링·컴플라이언스 태스크 (급여 사이클당 30분 절감)",
    "clap-ai-performance-korea": "주관식 평가 코멘트 자동 요약·정제 + AI 피드백 텍스트 + 원온원 미팅 요약 + 서술형 리뷰 초안 + 직원별 AI 성장 리포트 (한국 중견기업용 SaaS)",
    "cultureamp-ai-coach-asana": "매니저용 구조화 성과 리뷰 가이드 (과거 피드백·동료 리뷰 통합) + engagement 결과 기반 개인화 액션 플랜 + 대화형 코칭 응답 (People Science 1.5B 응답 데이터 기반)",
    "greetinghr-ats-ai-korea": "AI 후보자 매칭 추천 리스트 + 인재풀 분류·관리 + 면접 일정 자동 조율 + 채용 데이터 분석 dashboard (한국 중소기업 ATS, 채용 소요 65% 단축)",
    "hsbc-eightfold-gloat-multi-vendor": "Eightfold의 1.6B+ profile 기반 skills inference + Gloat marketplace의 직원-기회 매칭 점수 + career path 추천 + 매니저용 internal candidate 리스트 (140K 직원 enrolled)",
    "lg-uplus-jihye-employee-agent": "이메일 자동 번역 + PDF/Word 파일 요약 + 코드 리뷰·오류 사전 탐지 결과 + 사내 코드 분석 (LG U+ 통신사 기술사무직 파일럿)",
    "phenom-merck-kgaa-talent-marketplace": "직원별 inferred skills 매칭 추천 — 내부 jobs·gigs·learning (29K+ 콘텐츠)·mentor (1K+) + candidate 자동 통지 + 200,000+ 스킬 ontology",
    "qualtrics-adidas-employee-experience-ai": "engagement 설문의 sentiment·테마 분석 + 매니저별 personalized insight + dashboard에 팀 specific feedback·action recommendation + at-risk 직원 retention 예측 + xFlow 자동 alert",
    "samsung-fire-employee-rag-chatbot": "직원 query에 대한 보험 약관·특약·사내 규정 RAG 답변 + 출처 표시 (2026 추진)",
    "spring-health-general-mills-ai-eap": "직원 wellness assessment 결과 + 최적 치료 경로 추천 (therapy/coaching/자가관리) + 정밀 직원-치료사 매칭 + 증상 추적·재평가 (이용률 1%→26%, 우울증 58% 개선)",
    "ukg-ai-workforce-scheduling-healthcare": "AI 최적 교대 스케줄 추천 (자격증·노동법·선호도 반영) + Workforce Intelligence Hub 통합 뷰 (스케줄·타임·채용·급여·성과) + Bryte AI 급여 인사이트·복리후생 모델링·셀프서비스 응답",
    "viven-ai-digital-twin-coworker": "부재 동료의 Digital Twin이 query에 대해 과거 발언·결정·전문성 기반 답변 + 출처 표시 + 동료 복귀 시 처리 case 요약 보고 (stealth 직후, customer deployment 0건)",
    "zapier-enboarder-ai-onboarding": "입사 확정 이벤트 기반 자동화 온보딩 여정 — 신규 입사자에게 단계별 콘텐츠 (기대치·리소스·관계·커뮤니케이션) + 채용 관리자에게 개인화 액션 nudge·체크인 + HR dashboard 완료율·Time-to-productivity",

    # ===== Batch 3 (low-conf 27) =====
    "15five-kona-reup-ai-manager-coaching": "1:1 미팅 자동 전사·요약·액션 아이템 + 매니저 대상 실시간 코칭 팁 + HR 대시보드용 매니저 행동 변화 추적 지표",
    "allegis-group-holistic-ai-governance": "전사 AI 시스템 인벤토리 (500~600개 등록) + 시스템별 리스크 분류·완화 전략 레지스트리 + NYC LL144 바이어스 감사 리포트 (고객사 컴플라이언스 대시보드)",
    "bersin-galileo-learn-ai-native-lms": "기존 콘텐츠 (PDF·영상·SCORM)에서 자동 변환된 코스·assessment·simulation·polls + Galileo 사이드 패널 agent의 대화형 튜터 응답 (\"AI Josh\" persona)",
    "betterworks-nextgen-ai-performance": "역할·팀·회사 우선순위 기반 SMART 목표 추천안 + 평가 편향 (recency·halo) 탐지 알림 + 매니저용 일관성 보정된 리뷰 초안",
    "ericsson-degreed-ai-skills-upskilling": "직원 스킬 프로필 기반 personalized learning path 추천 + Career Hub 내부 gig·mobility 매칭 + Maestro AI 코치/시뮬레이션 응답 (월 64% 재방문)",
    "flex-korea-hr-ai-saas": "수기 근무표 OCR 변환 결과 (디지털 스케줄·연장/야간/휴일 가산임금 자동 산출액) + 노동법·세법 질의 AI 에이전트 상담 답변",
    "gs-caltex-aiu-platform": "사내 정유·안전 매뉴얼·정책 자연어 질의에 대한 GenAI 응답 (사내 RAG 기반 실무 정보)",
    "lattice-ai-performance-summarization": "360도 피드백·리뷰 자동 요약 + 핵심 트렌드 도출 + 자연어 목표 진척 분석 + Slack/Teams 내 개인별 이탈 리스크 알림",
    "lgcns-agentic-ai-hr": "수만 건 자기소개서·인적성 분석 결과 적합 인재 추천 리스트 + 지원자별 맞춤 면접 질문 자동 생성 (Knowledge Lake → Hub → Refiner → Router 4컴포넌트)",
    "nestle-paradox-recruiting": "Olivia 챗봇의 후보자 conversational 스크리닝 결과 + FAQ 응답 + 채용 매니저 캘린더 동기 인터뷰 자동 예약·리마인더 + offer letter·I9 대화형 처리",
    "salesforce-orgvue-org-design-ai": "8,000개 직위를 83개 역할 클러스터로 자동 분류한 결과 + 조직설계·SWP·리스킬링 의사결정용 클러스터 인사이트 (분 단위 산출)",
    "servicenow-now-assist-hr": "HR 케이스 맥락 자동 요약 + 직원 셀프서비스 KB 답변 (case deflection) + 케이스 라우팅 결정 + AI 작성 resolution note 초안 + Schedule Interview/Job Requisition 에이전트 conversational 처리",
    "unilever-flex-gloat-talent-marketplace": "직원 스킬·purpose 프로필 기반 사내 프로젝트·역할·gig 추천 매칭 (매니저 승인 불필요) + 미매칭 직원 대상 develop할 스킬 갭 추천",
    "visier-vee-people-analytics": "자연어 workforce 질의에 대한 narrative 답변 + 자동 생성 chart·요약·대시보드 + Org Design 변경 영향 narrative 설명 (Teams/웹 인터페이스)",
    "workday-illuminate-job-architecture": "HR 매니저 대시보드용 skill gap·직무 통합 기회·역할 부적합 직원 식별 결과 + job ladder 자동 생성·관리 추천",
    "cathay-pacific-hirevue": "후보자 on-demand video 응답 점수 (언어/콜로키얼 평가 포함) + 채용팀 검토용 shortlist + in-person 최종평가 진출자 결정",
    "douzone-one-ai-year-end-tax": "연말정산 대상자 자동 식별 리스트 + 국세청 간소화 PDF 자동 다운로드·반영 + 세액 예측 결과·직원 안내문 + 홈택스 자동신고·지급명세서 + HR용 총괄현황판",
    "eightfold-ai-talent-intelligence": "직원/후보 Capabilities Matrix 기반 채용·내부이동·후계 통합 매칭 점수 + AI Interviewer 1차 비동기 면접 결과 + Job Intelligence Engine의 자동 생성 role 정의·job architecture",
    "emirates-hirevue-volume-hiring": "영어 평가 점수 (15분 객관식) + situational video 응답 채점 결과 (verbal/written, 벤더 주장 non-verbal cues 포함) + assessment day 진출 후보 shortlist",
    "fuel50-lennox-internal-mobility": "직원 Talent DNA 기반 gig·project·mentorship·lateral move 추천 매칭 + 매니저용 applicant 풀·project talent pool + 직원 career path·mentor 매칭",
    "mcdonalds-paradox-recruiting": "Olivia의 후보자 conversational 스크리닝 (work history·shift) 결과 + 매장 매니저 캘린더 기반 면접 slot 자동 제시 + McHire ATS 통합 hiring funnel 기록",
    "paychex-flex-agentic-workforce": "타임카드 자동 스코어링·승인 결과 (이상 케이스만 매니저 플래그) + 노동법·휴식·공정근무법 준수 최적 교대표 자동 생성 + PTO 패턴 분석·피크 기간 인력부족 예측 알림",
    "samsung-multicampus-ai-learning": "직원 부서·직급·직무·관심 키워드·수강 이력 기반 맞춤형 사내 교육 콘텐츠 추천 목록 (삼성U 멀티캠퍼스 모바일·웹)",
    "sk-hynix-pwc-5agent-retention": "퇴사 위험 등급 (Green/Yellow/Red) + 위험 요인 Summary (LLM+XAI) + 5개 에이전트 (Structura/Cognita/Chronos/Sentio/Agora)별 상세 분석 + 등급별 맞춤 retention action 권고 (면담·보상·경력 개발)",
    "syndio-pay-equity-ai": "protected class별 pay gap 분석 결과 + offer/raise/promotion 시점의 internal equity·budget·market 균형 추천 + 국가별 pay transparency 규제 컴플라이언스 가이드·법률 메모 답변",
    "wantedlab-ai-recruiting-agent": "자연어 쿼리 기반 후보자 검색 결과 (기본 탐색 풀 + 자기소개서·프로젝트 정성 분석 고급 탐색) + 후보별 역량·경험 판단 + 추천 사유 reasoning",
    "workday-illuminate-employee-sentiment": "직원 피드백 데이터의 continuous 분석 결과 (팀·코호트별 sentiment trend·driver·이상 신호) + 매니저 워크플로 내 proactive insight 푸시 + 추천 action (1:1·recognition·career conversation)",
}


def yaml_escape(s):
    """YAML 문자열 escape — double quote 안에 들어갈 형태."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def update_page(slug, output_text):
    fp = UC / f"{slug}.md"
    if not fp.exists():
        print(f"SKIP {slug}: not found")
        return False
    text = fp.read_text(encoding="utf-8")

    new_line = f'output: "{yaml_escape(output_text)}"\n'

    # Pattern A: existing output line — replace
    pat_existing = re.compile(r'^output:\s*.*\n', re.MULTILINE)
    if pat_existing.search(text):
        new_text = pat_existing.sub(new_line, text, count=1)
        fp.write_text(new_text, encoding="utf-8")
        return True

    # Pattern B: insert after vendor_type line
    pat_vendor = re.compile(r"^(vendor_type:.*\n)", re.MULTILINE)
    m = pat_vendor.search(text)
    if not m:
        print(f"FAIL {slug}: no vendor_type line")
        return False
    new_text = pat_vendor.sub(m.group(1) + new_line, text, count=1)
    fp.write_text(new_text, encoding="utf-8")
    return True


def main():
    ok, fail = 0, 0
    for slug, output in OUTPUTS.items():
        if update_page(slug, output):
            ok += 1
        else:
            fail += 1
    print(f"Outputs applied: {ok}/{len(OUTPUTS)}")


if __name__ == "__main__":
    main()
