---
title: "Workday Peakon Employee Voice — Illuminate AI"
slug: workday-peakon-illuminate-employee-voice
primary_category: Employee Experience & HR Ops
subcategory: Listening & Engagement
tags: [workday, peakon, illuminate, employee-voice, sentiment-analysis, continuous-listening, multilingual, theme-extraction, engagement]
company: _다수 (Workday Peakon 고객, Workday 자사 도입 포함)_
industry: [all]
region: [global]
employee_class: [all]
vendor: [Workday]
vendor_type: [hrms, point-solution]
output: "60+ 언어 pulse 서베이의 자동 테마·sentiment·driver 추출 + 부서별 매니저 dashboard (강점·기회·이슈 highlight) + 이탈/번아웃 risk 선제 alert"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [summarization-qa, clustering-classification]
stage: production
visibility: public
case_type: vendor-product
regulatory_exposure: []
kr_law: sentiment 결과를 매니저 평가에 쓰면 AI 기본법 고영향 가능 + 소집단 재식별 위험
kr_union: 단체교섭/근로자대표 협의 필요 (이탈·번아웃 risk alert, 평가 연계 시)
kr_language: 60+ 언어 지원 (벤더 주장); 한국어 정확도 POC 4주 검증 권고 (페이지)
kr_vendor: 미확인 (국내 파트너 확인 필요)
frequency: monthly
first_seen: 2021-02-01
last_confirmed: 2026-04-01
confidence: 0.55
evidence_grade: B
corroborated_by: 1
freshness: fresh
depth: partial
graded_at: 2026-09-27
consulting_angle_status: filled
sources: [sources/verified-pwc-doc-2026-05.md, sources/constellation-workday-rising-2024-illuminate-2024-09.md]
related_usecases:
  - workday-illuminate-employee-sentiment
  - microsoft-viva-glint-copilot-sentiment
  - amazon-connections-daily-pulse
  - qualtrics-adidas-employee-experience-ai
related_vendors:
  - workday
---

## Summary

Workday가 2021-02 인수한 **Peakon Employee Voice** (인수 금액 _미공개_ — 인용 소스에 없음, 2026-09-27 grounding 점검) — 지속적 pulse 서베이 + AI 감정·테마 분석. 2024-12-11에 **Illuminate AI** 기능 발표 ([[sources/verified-pwc-doc-2026-05]] — Workday Newsroom 2024-12-11 확인). ⚠️ 벤더 주장: 1B+ 응답 + 200M+ 텍스트 피드백, 60+ 언어, 160개국 (공식 보도자료) ([[sources/verified-pwc-doc-2026-05]]). ⚠️ 자사 보고: Workday 사내 활용 결과 직원 성장·커리어 만족도 **+35%** ([[sources/verified-pwc-doc-2026-05]]). Illuminate 플랫폼 배경: Workday 플랫폼의 800 billion 트랜잭션 기반 모델 ([[sources/constellation-workday-rising-2024-illuminate-2024-09]] — Peakon 자체 내용은 없음).

## Problem / Why (도입 배경)

- **Before**: 5만~10만 직원 KR 대기업 annual 조직문화 진단의 open-end 코멘트 코딩에 HRBP 팀 수주 투입 — insight 도출 지연
- **Pain point**: 글로벌 organization은 60+ 언어 응답 통합 분석 어려움 + theme·sentiment를 매니저별 actionable insight로 변환 어려움
- **Trigger**: Workday 2021-02 Peakon 인수 → 2024-12 Illuminate AI 통합 (Workday Illuminate 시리즈 일환)

## Solution Architecture

### A. Process (프로세스)

- **Before**: annual 서베이 → 외부 vendor 또는 manual 분석 → 수주~수개월 후 PPT 보고
- **After**:
  1. 직원이 정기·수시 pulse 서베이 응답 (closed-end + open-end)
  2. Peakon Illuminate가 60+ 언어로 자연어 처리
  3. 자동 테마·sentiment·driver 추출 (1B+ 응답 학습 모델 기반)
  4. 매니저·HRBP에게 부서별 dashboard 제공 — 강점·기회·이슈 자동 highlight
  5. 매니저가 추천 action 실행, 다음 cycle에서 효과 측정
  6. 이상 신호 (이탈 risk·번아웃·문화 이슈) 선제적 alert
- **HITL**: HRBP·매니저가 insight 검토·action 결정
- **Frequency**: continuous (정기 pulse) + ad-hoc

### B. System & Infrastructure (시스템·인프라)

- **Core HRIS**: ✅ Workday 제품군 (Peakon은 Workday 인수 후 활성 제품) ([[sources/verified-pwc-doc-2026-05]]); HCM 통합 형태 _미공개_
- **AI 시스템**: ✅ Illuminate AI 기능 (2024-12-11 발표) ([[sources/verified-pwc-doc-2026-05]]); Illuminate 플랫폼은 Workday Rising 2024 발표 ([[sources/constellation-workday-rising-2024-illuminate-2024-09]])
- **배포 환경**: _미공개 (not disclosed)_
- **연동·통합**: _미공개 (not disclosed)_
- **사용자 접점**: _미공개 (not disclosed)_
- **인증·권한**: _미공개 (not disclosed)_

### C. Data (데이터)

- **입력 데이터 소스**: ✅ 직원 서베이 응답·텍스트 피드백 ([[sources/verified-pwc-doc-2026-05]])
- **데이터 규모**: ⚠️ 벤더 주장: 1B+ 응답 + 200M+ 텍스트 피드백, 60+ 언어, 160개국 ([[sources/verified-pwc-doc-2026-05]])
- **전처리·정제**: _미공개 (not disclosed)_
- **학습 vs RAG vs In-context 구분**: _미공개 (not disclosed)_
- **데이터 거버넌스**: _미공개 (not disclosed)_
- **민감정보 처리**: _미공개 (not disclosed)_

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_ — ⚠️ 벤더 주장: Illuminate 모델은 Workday 플랫폼 800 billion 트랜잭션 기반 ([[sources/constellation-workday-rising-2024-illuminate-2024-09]]); Peakon 적용 모델 세부 _미공개_
- **Model 유형**: ✅ 텍스트 피드백 요약·테마 추출 (GenAI) ([[sources/verified-pwc-doc-2026-05]])
- **제공 방식**: _미공개 (not disclosed)_
- **커스터마이징 기법**: _미공개 (not disclosed)_
- **Orchestration 프레임워크**: _미공개 (not disclosed)_
- **평가·가드레일**: _미공개 (not disclosed)_

### E. Organization & Team (조직·팀 구조)

- **오너십**: 벤더 제품 — 고객별 상이. _미공개 (not disclosed)_
- **참여 역할·팀 규모·거버넌스·변화관리·파트너**: _미공개 (not disclosed)_

## Impact / Metrics (기대효과)

### 기대효과 요약
글로벌 60+ 언어 통합 sentiment 분석 + Workday HCM native — KR 대기업 annual 조직문화 진단의 cycle time을 수주 → 즉시로 단축 가능.

- ⚠️ 벤더 주장 (Workday newsroom 2024-12-11, [[sources/verified-pwc-doc-2026-05]] 확인): 1B+ 응답·200M+ 텍스트·60+ 언어·160개국
- ⚠️ 자사 보고 (Workday 사내): 직원 성장·커리어 만족도 +35% (Illuminate 활용 결과) ([[sources/verified-pwc-doc-2026-05]])
- GA 일정: _미공개_ (인용 소스 미확인)

## Governance & Risk

- ✅ Workday IAM·tenant 격리 — 금융권·공공 보안 reference
- ⚠️ 35% 수치는 Workday 자사 보고 — 독립 검증 부재
- ⚠️ open-end 코멘트의 anonymization 보장 — small group re-identification risk
- ⚠️ sentiment 분석 결과를 매니저 평가에 사용 시 한국 AI 기본법 고영향 AI 분류 가능성

## Contradictions

_없음._

> [!note] 2026-09-27 grounding — Peakon 인수 금액은 인용 소스에 없어 `_미공개_`. [[sources/constellation-workday-rising-2024-illuminate-2024-09]]는 Peakon 내용이 없는 Illuminate 배경 자료. PwC 자료의 Qualtrics 수치(채택률·MAU)는 Peakon과 무관하여 미반영 ([[sources/verified-pwc-doc-2026-05]]). B/C/D의 tenant 격리·GDPR·자체 호스팅 서술은 소스에 없어 `_미공개_`.

## Consulting Angle

- **KR engagement survey vendor 비교 reference (Top 3)**:
  - Workday Peakon (Workday HCM 도입사 우선) vs Microsoft Glint Copilot [[microsoft-viva-glint-copilot-sentiment]] (M365 도입사) vs Qualtrics [[qualtrics-adidas-employee-experience-ai]] (standalone EX)
  - Amazon Connections [[amazon-connections-daily-pulse]] (frontline daily pulse)와 cadence 비교
- **2026 Q3-Q4 KR 컨설팅 deck**:
  - 60+ 언어 지원은 글로벌 KR 대기업 (삼성·LG·현대·SK 글로벌 자회사) 직접 reference
  - Workday Illuminate 시리즈 종합 (Sentiment + Job Architecture + Performance + ASOR) — vendor lock-in 검토 슬라이드
- **반면교사**:
  - 1B+·200M+·35% 모두 ⚠️ 벤더 주장 또는 ⚠️ 자사 보고 — 독립 분석가(Bersin·Gartner) 검증 별도 필요
  - 한국어 sentiment 정확도 POC 4주 검증 필수 (존댓말·dialect·industry-specific term)
  - Workday HCM 미사용 KR 대기업에는 fit 안 맞음 — Peakon 단독 도입은 Workday 의존성 동반
- **양 방향 비교**: Workday Illuminate Employee Sentiment Agent [[workday-illuminate-employee-sentiment]] (continuous monitoring) vs Peakon (cycle-based pulse) — 같은 Workday 우산 안에서 cadence 차별화
