---
title: "Microsoft Viva Glint Copilot — engagement 서베이 open-end NLP 자동 합성"
slug: microsoft-viva-glint-copilot-sentiment
primary_category: Employee Experience & HR Ops
subcategory: Listening & Engagement
tags: [microsoft, viva, glint, copilot, sentiment-analysis, employee-survey, open-end-nlp, copilot-highlights, engagement]
company: Microsoft
industry: [tech, cloud]
region: [global]
employee_class: [all]
vendor: [Microsoft]
vendor_type: [hrms]
output: "engagement 서베이 open-end 코멘트 자동 합성 + 반복 테마 탐지 + 속성별 (부서·재임기간·매니저) sentiment slice + 산업/규모 benchmark 비교 + Team/Executive 리포트 \"Copilot Highlights\" 섹션"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [summarization-qa, clustering-classification]
stage: production
visibility: public
case_type: adoption
regulatory_exposure: []
kr_law: 개인정보보호법(소그룹 slice 재식별) + 매니저 평가 활용 시 AI 기본법 고영향
kr_union: 노조 민감 영역 명시 (소그룹 재식별·익명성) — 근로자대표 협의 필요
kr_language: 한국어 NLP(존댓말·방언·업계용어) 품질 미검증 — POC 4주 필요 (페이지 명시)
kr_vendor: 미확인 (국내 파트너 확인 필요)
frequency: monthly
first_seen: 2024-09-01
last_confirmed: 2026-04-01
confidence: 0.35
evidence_grade: C
corroborated_by: 0
freshness: fresh
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04.md]
related_usecases:
  - amazon-connections-daily-pulse
  - microsoft-people-skills-inferred-ontology
related_vendors: []
---

## Summary

Microsoft Viva Glint에 Copilot 임베드 — 서베이 코멘트 요약(Copilot comment summarization) + 2026-04 GA된 **Copilot Highlights**(Team Summary·Executive Summary 리포트 안에 강점·기회·점수 변화·benchmark 비교 AI 요약, 다국어) [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]. **2026-04-30부터 Copilot 제어가 M365 Admin Center로 이관되며 admin toggle 제거, 플랫폼 레벨 default ON** [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]. 속성별 sentiment slice·테마 탐지·Microsoft 자체 사용 현황은 인용 소스에 없음 → _미공개_ (2026-09-27 grounding 점검).

## Problem / Why (도입 배경)

- **Before**: 벤더 제품이므로 특정 기업의 도입 배경은 고객별 상이. 🚫 일반론: 대규모 서베이의 open-end 코멘트 코딩에 HRBP 팀이 수작업 투입 (직원 수·소요 기간 수치 근거 미확보 — 2026-09-27 grounding 점검)
- **Pain point**: 매니저·리더가 데이터에서 action으로 넘어가는 속도 — Highlights는 코멘트 요약보다 낮은 응답자 수 조건에서 동작해 더 많은 리더가 활용 가능 ⚠️ 벤더 주장 [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]
- **Trigger**: Copilot Highlights GA·Copilot 제어 M365 Admin Center 이관 (2026-04) [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]; Glint의 LinkedIn → Viva 통합 경위는 인용 소스에 없음

## Solution Architecture

### A. Process (프로세스)

- **Before**: _미공개 (not disclosed)_ — 도입 전 프로세스는 인용 소스에 없음 (🚫 일반론: 수작업 코멘트 코딩·리포트 작성)
- **After** ⚠️ 벤더 주장 [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]:
  1. 서베이 응답 수집 — 응답자는 서베이 내 Copilot으로 코멘트 문장을 다듬을 수 있음 (속성 기반 로그인·개인화 링크 응답자 제외)
  2. Copilot comment summarization — 일정 수 이상의 응답자가 있을 때 코멘트 요약
  3. Copilot Highlights — Team Summary·Executive Summary 리포트 안에 강점·기회·점수 변화·benchmark 비교를 AI 요약 (사용자 설정 언어로 생성)
  4. 매니저·리더가 Highlights를 보고 action으로 이동
  - 속성별 sentiment slice·반복 테마 탐지 서술은 인용 소스에 없어 제거 (2026-09-27)
- **HITL**: 매니저·리더가 요약을 검토 후 action [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]; 검토 절차 세부 _미공개_
- **Frequency**: 서베이 주기에 종속 — Engagement 서베이·Viva Pulse·standalone Copilot 서베이 [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]; 고객별 상이

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS**: _미공개 (not disclosed)_ — Viva Glint은 M365 내 employee listening 제품 [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]
- **AI 시스템 배치**: ⚠️ 벤더 주장: Viva Glint 내장 Copilot (Copilot Highlights·comment summarization·서베이 내 Copilot) [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: Viva Pulse 서베이·Glint Copilot Impact 템플릿 [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]; Viva Feature Access Management(VFAM)로 접근 제어 [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]; Outlook·Teams·Power BI 연동은 인용 소스에 없음 _미공개_
- **사용자 접점**: Team Summary·Executive Summary 리포트 내 Copilot Highlights (매니저·리더 대시보드) [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]
- **인증·권한**: Copilot 접근은 M365 Admin Center(VFAM)에서 관리, 2026-04-30부터 단일 제어점 [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]; 역할별 RBAC 세부 _미공개_

### C. Data (데이터)

- **입력 데이터 소스**: 서베이 결과(점수·benchmark) 및 코멘트 [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]; 직원 메타데이터 활용 범위 _미공개_
- **데이터 규모**: _미공개 (not disclosed)_
- **전처리·정제**: _미공개 (not disclosed)_ — comment summarization은 "더 많은 응답자 수"를 요구한다는 서술만 [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]
- **학습 vs RAG vs In-context**: _미공개 (not disclosed)_
- **데이터 거버넌스**: Microsoft가 'Data, privacy, and security for Microsoft 365 Copilot in Viva Glint' 문서 제공 [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]; 내용 세부 _미공개_
- **민감정보 처리**: _미공개 (not disclosed)_ — anonymity threshold 서술은 인용 소스에 없어 제거

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **모델 유형**: LLM (요약 생성 — Copilot Highlights·comment summarization) [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]; sentiment classifier 여부 _미공개_
- **제공 방식**: Microsoft 365 Copilot in Viva Glint [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]; 백엔드 _미공개_
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: _미공개 (not disclosed)_ — bias·hallucination 테스트 결과 미공개
- **로드맵 (preview)**: Employee Feedback Agent — 대화형 질문으로 경험 데이터 수집 ⚠️ 벤더 주장 (preview, 변경 가능) [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]

### E. Organization & Team (조직·팀 구조)

- **오너십**: Microsoft 벤더 제품 — 고객사 HR·People Science 팀이 운영 주체 (고객별 상이); Microsoft 자체 사용 현황은 인용 소스에 없음 _미공개_
- **참여 역할**: _미공개 (not disclosed)_
- **거버넌스 체계**: M365 관리자가 Copilot 접근 제어 [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]
- **파트너**: _미공개 (not disclosed)_


## Impact / Metrics (기대효과)

### 기대효과 요약
매니저·리더가 서베이 결과에서 action으로 더 빨리 이동 (⚠️ 벤더 주장). 시간 단축·고객 성과 수치 _미공개_.

- 2026-04 Copilot Highlights GA (다국어) [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]
- 2026-04-30 M365 Admin Center 이관·default ON [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]
- Copilot 측정 문항 7개 추가 → Copilot Impact 템플릿 21문항 [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]
- standalone 시간 단축 metric _공식 미공개_

## Governance & Risk

- ⚠️ default ON 전환(2026-04-30) — 기존 admin toggle 제거로 조직 차원의 opt-out 통제가 M365 Admin Center(VFAM)로 이동 [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]]; 국내 도입 시 사전 설정 필요
- ⚠️ 직원 코멘트 요약의 익명성 — 응답자 수 조건 외 anonymity 세부 _미공개_; 소그룹 재식별 위험 검토 필요
- ⚠️ benchmark 비교의 한국 시장 fit 미검증
- ⚠️ 벤더 뉴스레터 1건만 인용 — 고객 성과·독립 검증 없음

## Contradictions

> [!note] 2026-09-27 grounding — 인용 소스(Viva Glint 2026-04 뉴스레터)에 없는 속성별 sentiment slice·테마 탐지, Microsoft 자체 'Employee Signals' 사용, Azure·GPT-4 추정, Entra ID RBAC, Power BI 연동, anonymity threshold, monthly pulse 주기, KR 대기업 직원 수 예시를 제거하고 _미공개_ 처리. default ON 시점은 2026-03 → 2026-04-30(raw 기준)으로 정정.

## Consulting Angle

- **KR 대기업 annual 조직문화 진단의 직접 reference**:
  - 대기업 annual engagement survey의 open-end 코멘트 코딩 부담 — Copilot Highlights·comment summarization으로 매니저 단위 요약 가능 (고객 사례 수치는 미확보)
  - Glint Copilot은 이 ROI 격차 즉시 해소 — 이미 M365 도입사는 추가 도입 부담 적음
- **한국 기업 한국어 요약 품질 검증 필수**: Highlights는 사용자 설정 언어로 생성 [[sources/microsoft-techcommunity-viva-glint-news-to-know-2026-04]] — 한국어 존댓말·업계 용어 처리 POC 필요
- **2026 Q3-Q4 KR consulting deck**: Glint Copilot + Amazon Connections [[amazon-connections-daily-pulse]] + 워크데이 Illuminate Sentiment — 3-vendor sentiment 비교
- **반면교사**:
  - sentiment slice를 부서·재임기간 등 small group으로 자르면 re-identification — 익명성 약화 가능. 한국 노조 sensitivity 큰 영역
  - Glint Copilot 결과를 매니저 평가에 직접 사용 시 한국 AI 기본법 고영향 AI 의무 (인적감독·고지) 트리거 — sentiment 기반 매니저 평가 자동화 회피 권장
