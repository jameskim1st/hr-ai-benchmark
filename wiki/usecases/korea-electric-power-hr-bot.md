---
title: "한국전력 — HR-Bot 채용 챗봇 + AI 인사추천 시스템"
slug: korea-electric-power-hr-bot
primary_category: Strategic Workforce & Governance
subcategory: Workforce Planning
tags: [korea-electric-power, kepco, hr-bot, saltlux, public-sector, recruitment-chatbot, ai-staffing-recommendation, korean-public, 2024-evaluation, korea]
company: 한국전력
industry: [public, energy]
region: [kr]
employee_class: [전임직, 기술사무직]
vendor: [솔트룩스]
vendor_type: [point-solution]
output: "지원자 채용 상담 24/7 챗봇 응답·일정 안내 + 직원 역량·업무 이력 기반 적재적소 인사 배치 추천 (HR·부서장 검토용) + 2025-Q4부터 사내 규정·법규·문서 작성 GenAI 산출물"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [summarization-qa, recommendation-ranking]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: [kr-high-impact-review, eu-annex-iii]
kr_law: AI 기본법 고영향 AI (인사 배치 추천) + 공공기관 개인정보 가이드라인
kr_union: 노조·직원 투명성 process 필요 (페이지 명시; process 미공개)
kr_language: 한국어 네이티브 (솔트룩스 한국 NLP)
kr_vendor: 솔트룩스 (한국 NLP 벤더) — 단일 벤더 lock-in 지적
frequency: monthly
first_seen: 2024-01-01
last_confirmed: 2026-04-01
confidence: 0.8
evidence_grade: A
corroborated_by: 2
freshness: fresh
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/nate-asiatoday-kepco-ai-transformation-2025-09.md, sources/saltlux-kepco-hr-bot-case-undated.md, sources/startuptoday-kepco-ai-talent-recommendation-2024-03.md]
related_usecases:
  - kb-bank-ai-hr-deep-change
  - shinhan-bank-ai-staffing-algorithm
  - korean-public-sector-hr-ai
related_vendors: []
---

## Summary

한국전력의 **AI 인재추천 시스템** — 공공기관으로는 처음으로 AI를 활용해 주요 보직 인재를 추천받음(2024-03 발표, 전년 말부터 활용): 기존 기본 인사정보·사내 평판·인사권자 직관 기반 추천에서 벗어나 HR 데이터·직무 데이터 기반으로 추천 [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]]. HR 분석 전담부서 신설 + 전력연구원 데이터 사이언스랩이 구현, 관련 특허 4건 출원(자연어 기반 인재 추천·감정 분류·직무 역량별 인재 추천 등); 자체 개발 감정 분류 AI는 다면평가 서술형 평가의 긍·부정·중립 분류에 활용 [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]]. 2025-09: 사내 규정·법규·문서 작성·조회를 AI로 지원하는 시스템 구축 착수(계약 약 8억원, 스마트폰 앱 포함) — 12월 시험 운영 후 이듬해 3월 전 직원 개방 **목표** [[sources/nate-asiatoday-kepco-ai-transformation-2025-09]]. **HR-Bot(솔트룩스) 채용 챗봇**은 벤더 사례 페이지가 홈페이지로 리다이렉트되어 raw 미확보 — 세부는 _미공개 (not disclosed)_ [[sources/saltlux-kepco-hr-bot-case-undated]]. 기존 "2024 경영평가 인사혁신 부문 가점", "직원 수", "공공기관 AI 도입률" 등은 인용 소스에 없어 삭제 (2026-09-27 grounding 점검).

## Problem / Why (도입 배경)

- **Before (baseline)**: 주요 보직 후보자 추천이 기본 인사정보·사내 평판·인사권자 직관에 의존 — 제한된 후보자 추천으로 실용성 한계 [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]]; 직원들이 규정·업무 절차를 일일이 찾아 실무에 적용 [[sources/nate-asiatoday-kepco-ai-transformation-2025-09]]
- **Pain point**: 경험·직관 의존 인사 방식 탈피, 데이터 기반 HR [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]]
- **Trigger**: 2023-09 취임한 김동철 사장의 추천으로 알려짐 [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]]

## Solution Architecture

### A. Process — AI 인재추천

- **Before**: 기본 인사정보·사내 평판·인사권자 직관 기반 후보자 추천 [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]]
- **After** (⚠️ 자사 보고 [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]]):
  1. HR 데이터·직무 데이터를 AI가 분석
  2. 주요 보직 인재 후보 추천 (자연어 기반·직무 역량별 추천 특허)
  3. 인사권자 결정 — 검토 절차 세부 _미공개 (not disclosed)_
  4. 병행: 감정 분류 AI가 다면평가 서술형 평가의 긍·부정·중립 맥락을 분류해 피드백에 반영
- **HITL**: _미공개 (not disclosed)_ — 기존 "HR + 부서장 최종 결정" 서술은 소스에 없음

### A. Process — HR-Bot (채용 챗봇)

- _미공개 (not disclosed)_ — 솔트룩스 사례 페이지 raw 미확보(홈페이지 리다이렉트), 검색 스니펫 기반 요약은 인용 불가 [[sources/saltlux-kepco-hr-bot-case-undated]]. 기존 "24/7 채용 상담·단순 반복 채용업무 자동화·escalation" 서술은 근거 미확보로 삭제.

### A. Process — 사내 규정·법규·문서 GenAI (계획)

- ⚠️ 자사 보고: 사내 규정·법규·문서 작성·조회 AI 지원 시스템 구축 착수(2025-09, 약 8억원), 스마트폰 앱 개발 병행, 12월 시험 운영 → 이듬해 3월 전 직원 개방 목표 [[sources/nate-asiatoday-kepco-ai-transformation-2025-09]]

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS**: _미공개 (not disclosed)_
- **AI 시스템 배치**: AI 인재추천 시스템 — 한전 자체 개발(전력연구원 데이터 사이언스랩) [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]]; HR-Bot 벤더는 frontmatter 기준 솔트룩스이나 raw 미확보 [[sources/saltlux-kepco-hr-bot-case-undated]]
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: _미공개 (not disclosed)_
- **사용자 접점**: GenAI 시스템은 스마트폰 앱 개발 추진 [[sources/nate-asiatoday-kepco-ai-transformation-2025-09]]; 인재추천 dashboard 등 _미공개_
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: HR 데이터·직무 데이터 [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]]; 다면평가 서술형 평가 텍스트 [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]]; 사내 규정·법규·문서(GenAI, 계획) [[sources/nate-asiatoday-kepco-ai-transformation-2025-09]]
- **데이터 규모**: _미공개 (not disclosed)_
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context**: 자연어처리 기반 기술 [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]] — 방식 세부 _미공개_
- **데이터 거버넌스**: _미공개 (not disclosed)_
- **민감정보 처리**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **모델 유형**: 인재 추천(자연어·직무 역량 기반) + 감정 분류(긍·부정·중립) [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]]; GenAI(규정·문서) _미공개_ [[sources/nate-asiatoday-kepco-ai-transformation-2025-09]]
- **제공 방식**: 자체 개발(특허 출원) [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]]
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: _미공개 (not disclosed)_ — 추천 정확도·활용 규모 소스에 없음

### E. Organization

- **오너십**: 한전 HR 분석 전담부서(2023 신설) + 전력연구원 데이터 사이언스랩 [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]]; 김동철 사장 추천 [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]]
- **참여 역할·팀 규모**: _미공개 (not disclosed)_
- **파트너**: HR-Bot 벤더 솔트룩스 (raw 미확보) [[sources/saltlux-kepco-hr-bot-case-undated]]

## Impact / Metrics (기대효과)

### 기대효과 요약
⚠️ 기대효과 수치 미공개 — 인용 소스에 추천 정확도·활용 규모·시간 절감 수치가 없음. "공공기관 최초 AI 인재추천"이라는 포지셔닝이 주된 가치 [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]].

- ⚠️ 자사 보고:
  - 공공기관 최초 AI 인재추천 시스템 (2023 말 활용 개시) [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]]
  - 특허 4건 출원 [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]]
  - 사내 규정·법규·문서 GenAI: 2025-12 시험 운영 → 2026-03 전 직원 개방 목표 (계획) [[sources/nate-asiatoday-kepco-ai-transformation-2025-09]]
  - 경영평가 가점·직원 수·활용률: _미공개 (not disclosed)_ (기존 수치는 인용 소스에 없음)

## Governance & Risk

- ⚠️ 주요 보직 인재 추천 AI의 explainability — 노조·직원 투명성 process _미공개_
- ⚠️ 한국 AI 기본법 고영향 AI 검토 대상(배치·승진 관여, `kr-high-impact-review`) — 인적감독 절차 소스에 없음
- ⚠️ 감정 분류 AI의 다면평가 반영 — 오분류 시 평가 공정성 리스크, 검증 결과 _미공개_ [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]]
- ⚠️ "공공기관 최초" 주장은 한전 발표 기준 [[sources/startuptoday-kepco-ai-talent-recommendation-2024-03]]
- ⚠️ 솔트룩스 HR-Bot은 근거 미확보 — 벤더 lock-in 논의는 raw 확보 후

## Contradictions

> [!note] 2026-09-27 grounding — (1) 솔트룩스 HR-Bot 사례(24/7 채용 챗봇)는 raw가 홈페이지 리다이렉트로 미확보 → 세부 _미공개_. (2) "직원 수 수치", "공공기관 AI 도입률 수치", "2024 경영평가 인사혁신 부문 가점", "HR+부서장 검토", "한전 SSO", "디지털혁신 본부", "정부 클라우드/on-prem 추정", "솔트룩스 RAG·intent classifier 추정"은 인용 소스에 없어 삭제·_미공개_. (3) 규정·문서 GenAI는 2025-09 기준 "목표"(계획)이므로 미래형 유지. (4) 인재추천 활용 개시 시점은 2023년 말(2024-03 발표 기준 "지난해 말") — frontmatter first_seen 2024-01-01과 대체로 정합.

## Consulting Angle

- **한국 공공기관 AI 인사 reference (1순위)**:
  - 공공기관 AI 도입 사례 중 개별 case로 식별 — 한전이 가장 잘 문서화 (도입률 통계는 인용 소스에 없음)
  - 한국전력공사·한국도로공사·국민연금·한국가스공사 등 공공기관 AI 도입 컨설팅의 baseline
- **2026 Q3-Q4 KR 공공·금융 컨설팅 deck**:
  - 한전 (공공, 주요 보직 인재추천) + KB AI HR Deep Change [[kb-bank-ai-hr-deep-change]] (금융, 영업점 배치) — 한국 인사 AI 양대 reference
  - 정부 경영평가 KPI 정합성 angle은 공공기관 임원 motivator — 단, 한전의 가점 사실은 인용 소스에서 미확인
- **한국 vendor·자체 개발 활용**: 한전은 인재추천을 자체 개발(특허) — 글로벌 vendor 대신 국내 역량 활용 패턴; 솔트룩스 HR-Bot은 raw 확보 후 보강
- **반면교사**:
  - "최초" 주장 — 외부 인용 시 "한전 발표(2024-03) 기준" 명시
  - 공공기관 AI 인사 추천 결과의 직원·노조 투명성 process 부재 시 risk
  - 벤더 의존 여부는 HR-Bot raw 확보 후 판단
- **2025-12 시험 운영 → 2026-03 전 직원 개방 목표 생성형 AI**: 사내 규정·법규·문서 작성 AI — 신한 AI ONE [[shinhan-bank-ai-one-platform]]·미래에셋 AI Assistant [[mirae-asset-ai-assistant-platform]] 패턴과 유사
