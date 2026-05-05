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
frequency: monthly
first_seen: 2021-02-01
last_confirmed: 2026-04-01
confidence: 0.80
consulting_angle_status: filled
sources:
  - sources/verified-pwc-doc-2026-05.md
  - "Constellation Research: Workday Rising 2024 — AI Illuminate analysis https://www.constellationr.com/insights/news/workday-rising-2024-ai-illuminate-ai-agents-evisort-acquisition"
related_usecases:
  - workday-illuminate-employee-sentiment
  - microsoft-viva-glint-copilot-sentiment
  - amazon-connections-daily-pulse
  - qualtrics-adidas-employee-experience-ai
related_vendors:
  - workday
---

## Summary

Workday가 2021-02 인수 (~$700M)한 **Peakon Employee Voice** — 지속적 pulse 서베이 + AI 감정·테마 분석. 2024-12-11에 **Illuminate AI** 기능 발표 — open-end comment 자동 요약·테마 추출·driver 식별. ⚠️ 벤더 주장: 1B+ 응답 + 200M+ 텍스트 피드백 학습, 60+ 언어, 160개국 운영. ⚠️ 자사 보고: Workday 사내 활용 결과 직원 성장·커리어 만족도 **+35%**.

## Problem / Why (도입 배경)

- **Before**: 5만~10만 직원 KR 대기업 annual 조직문화 진단의 open-end 코멘트 코딩에 HRBP 팀 수주 투입 — insight 도출 지연
- **Pain point**: 글로벌 organization은 60+ 언어 응답 통합 분석 어려움 + theme·sentiment를 매니저별 actionable insight로 변환 어려움
- **Trigger**: Workday 2021-02 Peakon 인수 → 2024-12 Illuminate AI 통합 (Workday Illuminate 시리즈 일환)

## Solution Architecture

### A. Process

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

### B. System & Infrastructure

- **Core HRIS**: Workday HCM (Peakon은 Workday 통합 모듈)
- **AI 시스템**: Workday Illuminate 통합 (2024-12 발표 시 기존 Peakon 모델 + Illuminate LLM 결합)
- **배포 환경**: Workday cloud
- **연동·통합**: Workday HCM 마스터 + 매니저 dashboard

### C/D. Data & Model

- **데이터**: 1B+ 응답 + 200M+ 텍스트 피드백 (글로벌 누적, ⚠️ 벤더 주장)
- **언어**: 60+ 지원
- **모델**: Workday Illuminate (자체 호스팅) + 기존 Peakon NLP 모델
- **거버넌스**: Workday tenant 격리, GDPR 준수

### E. Organization

- Workday HR Tech + 고객사 HRBP·People Science 팀

## Impact / Metrics (기대효과)

### 기대효과 요약
글로벌 60+ 언어 통합 sentiment 분석 + Workday HCM native — KR 대기업 annual 조직문화 진단의 cycle time을 수주 → 즉시로 단축 가능.

- ✅ Tier 3 공식 (Workday newsroom): 1B+ 응답·200M+ 텍스트·60+ 언어·160개국
- ⚠️ 자사 보고 (Workday 사내): 직원 성장·커리어 만족도 +35% (Illuminate 활용 결과)
- 2025년 상반기 GA 일정 명시

## Governance & Risk

- ✅ Workday IAM·tenant 격리 — 금융권·공공 보안 reference
- ⚠️ 35% 수치는 Workday 자사 보고 — 독립 검증 부재
- ⚠️ open-end 코멘트의 anonymization 보장 — small group re-identification risk
- ⚠️ sentiment 분석 결과를 매니저 평가에 사용 시 한국 AI 기본법 고영향 AI 분류 가능성

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
