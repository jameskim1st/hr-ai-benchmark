---
title: "포스코DX — 인사·구매·경영분석 110 AI 에이전트 + 그룹 AI 거버넌스 (2026 조직개편)"
slug: posco-dx-110-agents-hr
primary_category: Strategic Workforce & Governance
subcategory: HR Tech Governance
tags: [posco-dx, posco-group, 110-agents, hr-procurement-analytics, ai-robot-fusion, organizational-redesign, korea, manufacturing]
company: 포스코DX (포스코 그룹)
industry: [it-services, manufacturing, steel]
region: [kr]
employee_class: [기술사무직, 전임직]
vendor: [POSCO DX internal]
vendor_type: [internal-build]
ai_tech_type: [generative, automation, predictive]
ai_tech_subtype: [summarization-qa, rpa, clustering-classification]
stage: announced
frequency: daily
first_seen: 2026-01-01
last_confirmed: 2026-04-01
confidence: 0.40
consulting_angle_status: filled
sources:
  - sources/kr-conglomerate-2026-q2-research.md
related_usecases:
  - woori-bank-175-ai-agents
  - hyundai-mobis-moai-platform
  - sk-group-aibiz-25-companies
related_vendors: []
---

## Summary

포스코DX가 2026 그룹 조직개편과 함께 **인사·구매·경영분석 사무 업무 영역 ~110개 AI 에이전트** 개발 중. 2026 그룹DX전략실장(임치현 UNIST 교수 영입), AI·로봇 융합 연구소장(윤일용) 신설로 그룹 차원 AI 거버넌스 강화. 우리은행 175 에이전트 [[woori-bank-175-ai-agents]]와 함께 KR 기업 **AI 에이전트 portfolio 규모** 트렌드의 제조업 reference.

## Problem / Why

- **Before**: 포스코 그룹 ~30K 직원 사무 영역 (인사·구매·경영분석)에 단순 반복 업무 다수
- **Pain point**: 철강 산업 DX 전환 + 그룹 차원 AI 통합 부재 (계열사별 분산)
- **Trigger**: 2026 그룹 조직개편 — 그룹DX전략실 + AI·로봇 융합 연구소 신설로 거버넌스 강화

## Solution Architecture

### A. Process

- **Before**: 인사·구매·경영분석 업무가 각 계열사별 산발 처리
- **After (개발 중, 2026 launch 예정)**:
  1. 110개 AI 에이전트가 인사·구매·경영분석 사무 업무 자동화
  2. 그룹DX전략실 (임치현 실장)이 portfolio 거버넌스
  3. AI·로봇 융합 연구소 (윤일용 소장)이 R&D 연계
  4. 계열사 (포스코·포스코홀딩스·포스코이앤씨 등) 공통 활용
- **HITL**: 그룹DX전략실 + 계열사 사업부장 cross-functional
- **Frequency**: 개별 에이전트 daily, portfolio review annual

### B/C/D. System

- 포스코DX 자체 구축 (구체 platform _미공개_)
- 데이터: 인사·구매·경영분석 도메인
- 모델: _미공개_ (자체·외부 혼합 추정)

### E. Organization

- 포스코DX (개발) + 그룹DX전략실 + AI·로봇 융합 연구소
- 임치현 (UNIST 영입) + 윤일용 (AI·로봇 융합 연구소장)

### B. System & Infrastructure (R9 research)

- **Core HRIS**: 포스코 그룹 사내 HRIS (구체 _미공개_)
- **AI 시스템 배치**: ✅ 포스코DX 자체 — ~110개 AI 에이전트 portfolio
- **배포 환경**: _미공개_ — 포스코 그룹 자체 클라우드 추정
- **연동·통합**: ✅ 계열사 (포스코·홀딩스·이앤씨 등) 공통 활용 설계, 그룹DX전략실 portfolio 거버넌스
- **사용자 접점**: _미공개_ (계열사 사업부 web/desktop 추정)
- **인증·권한**: 그룹 SSO 추정

### C. Data (R9 research)

- **입력 데이터 소스**: ✅ 인사·구매·경영분석 도메인 데이터
- **데이터 규모**: ✅ 포스코 그룹 ~30K 직원 사무 영역
- **전처리·정제**: _미공개_
- **학습 vs RAG vs In-context**: _미공개_
- **데이터 거버넌스**: ✅ 그룹DX전략실 + AI·로봇 융합 연구소 cross-functional (2026 조직개편)
- **민감정보 처리**: ⚠️ 인사 영역 KR AI 기본법 고영향 AI 분류 가능

### D. Model (R9 research)

- **Foundation model**: _미공개_ — 자체·외부 혼합 추정
- **모델 유형**: generative + automation (RPA) + classifier
- **제공 방식**: ✅ 포스코DX internal build
- **커스터마이징 기법**: _미공개_
- **Orchestration 프레임워크**: _미공개_ — 110개 quality·일관성 governance framework 미공개
- **평가·가드레일**: ⚠️ "개발 중" (announced) — production 후 검증 필요


## Impact / Metrics

### 기대효과 요약
한국 제조 그룹의 AI 에이전트 portfolio 첫 사례 + 그룹 차원 거버넌스 — 우리은행 금융권 사례와 paired reference.

- ✅ 110개 에이전트 개발 중 (2026 launch 예정)
- ✅ 인사·구매·경영분석 사무 영역 cover
- ✅ 그룹 AI 거버넌스 신설 (조직개편)

## Governance & Risk

- ⚠️ 110개 에이전트 quality·일관성 governance — 우리은행 175와 동일 risk
- ⚠️ 인사 영역은 한국 AI 기본법 고영향 AI 분류 가능
- ⚠️ "개발 중" — production launch 후 효과 검증 필요

## Consulting Angle

- **KR 제조 그룹 AI 에이전트 portfolio reference**:
  - 우리은행 175 [[woori-bank-175-ai-agents]] (금융, portfolio framework)
  - 포스코DX 110 (제조, 그룹 거버넌스 강화)
  - SK A.Biz 25개사 [[sk-group-aibiz-25-companies]] (단일 표준 platform)
  - 3가지 KR 그룹사 AI 에이전트 운영 모델 비교
- **그룹 거버넌스 reference**: UNIST 교수 영입 + 신규 연구소장 임명 = 외부 인재 + 내부 R&D 통합 패턴
- **반면교사**:
  - "개발 중" → production 효과 검증 _미공개_
  - 110개 에이전트 동시 운영 governance 복잡도 (우리은행 동일 risk)
- **Watch list**: 2026 production launch 시 본 page 갱신
