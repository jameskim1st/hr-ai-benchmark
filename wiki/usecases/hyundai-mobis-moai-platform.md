---
title: "현대모비스 — 'MoAI' 사내 전용 GenAI"
slug: hyundai-mobis-moai-platform
primary_category: Employee Experience & HR Ops
subcategory: Employee Self-service
tags: [hyundai-mobis, moai, on-premise, rag, 10m-documents, automotive-supplier, prompt-template, korea, change-management]
company: 현대모비스
industry: [automotive, manufacturing]
region: [kr]
employee_class: [기술사무직, 전임직]
vendor: [현대모비스 internal]
vendor_type: [internal-build]
output: "사내 1,000만 건 매뉴얼·도면·기술문서 RAG 검색 답변 + 출처 표시 (R&D·IT·품질·영업·생산 영역, HR Q&A는 2025+ 확장 예정)"
ai_tech_type: [generative]
ai_tech_subtype: [summarization-qa, information-extraction]
stage: production
frequency: daily
first_seen: 2025-10-21
last_confirmed: 2026-04-01
confidence: 0.45
consulting_angle_status: filled
sources:
  - sources/kr-conglomerate-2026-q2-research.md
related_usecases:
  - lg-chatexaone-group-rollout
  - sk-group-aibiz-25-companies
  - hyundai-steel-hip-platform
related_vendors: []
---

## Summary

현대모비스가 2025-10-21 본격 운영하는 사내 전용 GenAI 플랫폼 **'MoAI(Mobis one AI)'**. 온프레미스 배포로 **1,000만 건 사내문서 RAG** 기반 검색·요약. R&D·IT·품질·영업·생산 등 **7개 업무**에 적용. 2025년 내 **법무·경영지원(HR 포함)으로 확장 계획**. 변화관리로 프롬프트 템플릿 사전 탑재. 한국 제조 대기업의 **"온프레미스 + 변화관리"** 정석 사례.

## Problem / Why

- **Before**: 자동차 부품사 33K 직원 — 매뉴얼·도면·기술 문서 fragmented. 보안 민감 (R&D 영업비밀)
- **Pain point**: 글로벌 commercial LLM 사용은 영업비밀·도면 leakage risk → 사내 LLM 필요
- **Trigger**: 2025 현대차 그룹 AI 가속 + 모비스 R&D 효율 압박

## Solution Architecture

### A. Process

- **Before**: R&D·IT·품질·영업·생산 직원이 매뉴얼·도면·기술 문서를 sharepoint·서버 search → 시간 소요
- **After**:
  1. 직원이 MoAI 자연어 query (사전 탑재 프롬프트 템플릿 활용)
  2. MoAI가 1,000만 건 사내문서 RAG 검색
  3. 답변 + 출처 표시
  4. 7개 업무 영역 (R&D·IT·품질·영업·생산 + 2개)
  5. 2025+ 법무·경영지원(HR) 확장 계획
- **HITL**: 직원 자율, IT/HR governance 모니터링
- **Frequency**: daily
- **Scope**: assistive — Q&A·요약·추출

### B. System

- **Core HRIS**: 현대모비스 자체 HR (그룹 표준 추정)
- **AI 시스템 배치**: 사내 온프레미스 (보안 민감 — 영업비밀 보호)
- **배포 환경**: on-prem (구체 hyperscaler 미사용)
- **연동·통합**: 사내 sharepoint·문서 server·도면 DB
- **사용자 접점**: web (PC), 모바일 _미공개_
- **인증·권한**: 모비스 SSO

### C/D. Data & Model

- **데이터**: 1,000만 건 사내문서 (매뉴얼·도면·기술·정책)
- **Foundation model**: 자체 운영 (구체 base LLM _미공개_, 한국 vendor 추정)
- **커스터마이징**: RAG (1,000만 건) + 프롬프트 템플릿 사전 탑재 (변화관리)

### E. Organization

- 현대모비스 IT + R&D + HR (확장 계획)

## Impact / Metrics

### 기대효과 요약
온프레미스 사내 GenAI로 1,000만 건 문서 검색·요약 — 한국 제조 대기업 보안 민감 환경의 표준 패턴.

- ✅ 1,000만 건 사내문서 RAG (한국경제·로봇신문 보도)
- ✅ 7개 업무 영역 적용 (R&D·IT·품질·영업·생산 등)
- ✅ 프롬프트 템플릿 사전 탑재 (변화관리 design)
- 2025+ 법무·HR 확장 (예정)

## Governance & Risk

- ✅ 온프레미스 — 영업비밀·도면 보호 강력
- ⚠️ HR 적용 비중·구체 시점 _미공개_ ("예정" 단계)
- ⚠️ 1,000만 건 RAG quality·노이즈 통제 governance _미공개_

## Consulting Angle

- **KR 제조 대기업 ★ reference**:
  - 보안 민감 + 매뉴얼·도면 많은 클라이언트 (중공업·반도체 장비) 제안 시 1순위 벤치마크
  - 포스코·현대제철 [[hyundai-steel-hip-platform]]·한화 등 같은 제조 그룹사 reference
- **온프레미스 vs cloud trade-off**:
  - 모비스 = 온프레미스 (보안 우위, 비용·확장 disadvantage)
  - LG ChatEXAONE [[lg-chatexaone-group-rollout]] = cloud (확장성 우위)
  - SK A.Biz [[sk-group-aibiz-25-companies]] = SK cloud (그룹 표준)
- **변화관리 (프롬프트 템플릿)**: KR client adoption 격차 해소 핵심 — POC + 템플릿 라이브러리 동반 권장
- **반면교사**:
  - HR 확장 "예정" — 실제 적용 시 본 page 갱신 필요
  - 1,000만 건 RAG의 quality monitoring 부담 — index 갱신·노이즈 제거 process 명시 필요
