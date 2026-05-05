---
title: "SK하이닉스 — One Resume + AI 구성원 검색"
slug: sk-hynix-one-resume-employee-search
primary_category: Employee Experience & HR Ops
subcategory: Core HR & Employee Records
tags: [sk-hynix, one-resume, employee-search, talent-profile, korean-conglomerate, korea, semiconductor, internal-build]
company: SK하이닉스
industry: [semiconductor]
region: [kr]
employee_class: [기술사무직, 전임직]
vendor: [SK하이닉스 internal]
vendor_type: [internal-build]
output: "직원 1인당 단일 통합 프로필 (One Resume — 인사·평가·교육·프로젝트·자격·관심사·skill 통합) + 매니저용 자연어 talent search (예: '머신러닝 + 양산공정 경험 5년+ 한국어/영어 가능' 검색) + 직원 본인의 career path 시각화"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [summarization-qa, information-extraction, recommendation-ranking]
stage: production
frequency: monthly
first_seen: 2026-05-01
last_confirmed: 2026-05-06
confidence: 0.22
consulting_angle_status: filled
sources:
  - sources/verified-pwc-doc-2026-05.md
related_usecases:
  - sk-hynix-pwc-5agent-retention
  - sk-hynix-ask-ai-interview
  - mastercard-unlocked-gloat-talent-marketplace
  - schneider-electric-gloat-talent-marketplace
related_vendors: []
---

> 📌 **중요 caveat**: 본 사례는 SK하이닉스 **내부 운영 시스템**으로 **공개 1차 출처 0건** (한국어/영문 검색 모두 zero hits, 2026-05-06 검증). 시장 일반 reference로 사용 시 출처 명시 필수. SK하이닉스 외부 공개 HR AI 사례는 채용 영역의 [[sk-hynix-ask-ai-interview|A!SK]]뿐 — 본 페이지를 외부 인용 시 "SK하이닉스 내부 운영 시스템, 외부 공개 자료 부재" 명시 권장.

## Summary

SK하이닉스 **One Resume + AI 구성원 검색** 시스템. 직원 1인당 분산된 데이터 (HRMS·평가·교육·프로젝트·자격·관심사·skill)를 **단일 통합 프로필 (One Resume)**로 구성하고, 매니저가 자연어로 사내 talent를 검색·추천 받는 **AI talent search** 기능을 결합. 직원 self-service career path 시각화·내부 기회 추천 포함. **2026-05 시점: 내부 운영 중, 외부 공개 metric 미공개**.

## Problem / Why

- **Before**: SK하이닉스 38K 직원의 인사 데이터가 **HRMS·평가·교육·프로젝트·자격증·외부 교육 등 다수 시스템에 분산**. 매니저가 internal mobility·project staffing·후계자 후보 검색 시 여러 시스템 + 인적 네트워크 의존
- **Pain point**:
  - 사내 talent visibility 부족 — 매니저가 "양산공정 + 머신러닝 경험 5년+ 영어 가능자"를 사내에서 찾기 어려움
  - 직원 본인도 자기 career path·내부 기회 잘 모름
  - 핵심 인재 retention·project staffing·후계자 풀 식별 모두 동일한 root cause (skill·경력 visibility 부재)
- **Trigger**: 2024-25 SK 그룹 차원 AI 적극 도입 흐름

## Solution Architecture

### A. Process

- **Before**: HR이 인사·평가·교육·프로젝트 데이터를 매번 수작업으로 조합해 매니저에 talent list 제공. 직원 본인 정보도 부서·기능별 시스템 분산
- **After**:
  1. **데이터 통합 layer**: HRMS·평가·교육 LMS·프로젝트 시스템·자격 DB·외부 교육 이력 등에서 직원별 데이터 자동 수집 → ETL → 단일 직원 프로필
  2. **One Resume 생성**:
     - 정형 데이터 (인사 기본·역할·근속·평가·교육) + 비정형 데이터 (프로젝트 기여·자격·관심사) 결합
     - LLM 기반 자기소개 자동 생성 + 직원 본인 review/edit
     - skill 자동 추출 (프로젝트·교육에서 skill inference)
  3. **AI 구성원 검색 (talent search)**:
     - 매니저가 자연어 query 입력 (예: "머신러닝 + 양산공정 경험 5년+ 한국어/영어 가능")
     - 검색 엔진이 의미 기반 (semantic search) + skill ontology 매칭 → 후보자 ranking
     - 매니저가 후보자 프로필 review → contact (HR 승인 후)
  4. **직원 self-service**: 본인 One Resume 검토·수정·career path 시각화·내부 기회 추천 받기
  5. HR·리더 분석 dashboard: skill gap·talent inventory·후계자 풀 분석
- **HITL**: 직원 본인이 One Resume 최종 승인. 매니저 검색 결과 → HR 승인 후 contact
- **Frequency**: monthly profile 갱신 + 수시 검색
- **Scope of autonomy**: recommend (검색·추천만, contact·이동은 사람 결정)

### B/C/D. System

- 추정 architecture (실제 구현 detail _미공개_):
  - 통합 데이터 layer (ETL or data lake)
  - LLM (자기소개 생성·자연어 검색 query 이해·skill inference)
  - Vector DB (semantic search)
  - Skill ontology (한국어·기술 도메인)
  - 매니저용 검색 UI + 직원용 self-service portal
- 데이터 source: HRMS·평가·LMS·프로젝트·자격·외부 교육 이력
- 모델: LLM (GPT 계열 또는 자체 fine-tune _미공개_) + embedding 모델 + classification (skill 추출)

### E. Organization

- SK하이닉스 인사·디지털혁신·R&D HR 주도 (구체 조직 구성 _미공개_)
- 함께 운영되는 [[sk-hynix-pwc-5agent-retention|retention 시스템]]의 input data layer 역할 가능 (One Resume이 통합 직원 프로필 base)

## Impact / Metrics (기대효과)

### 기대효과 요약
직원 데이터를 **분산 → 통합** + 매니저 검색을 **수동 → AI 자연어**로 전환. **외부 공개 production metric 0건** — 내부 운영 효과 _미공개_.

- ⚠️ 모든 production metric ⚠️ **외부 공개 미실시**
- 비교 reference (글로벌 talent profile/search 검증 사례):
  - Mastercard Unlocked [[mastercard-unlocked-gloat-talent-marketplace]] (Gloat): 93% 등록률·1M project hours 누적
  - Schneider Electric [[schneider-electric-gloat-talent-marketplace]] (Gloat): 360,000+ unlocked hours
  - Eightfold [[eightfold-ai-talent-intelligence]]: skill ontology 기반 talent intelligence

## Governance & Risk

- ⚠️ **공개 1차 출처 0건** — 한국어 ("SK하이닉스 One Resume" / "AI 구성원 검색") + 영문 검색 모두 zero hits (2026-05-06 검증). 외부 시장 reference로 인용 시 신뢰도 손상 risk
- ⚠️ SK하이닉스 외부 공개 HR AI는 [[sk-hynix-ask-ai-interview|A!SK 비디오 면접]]뿐 — 내부 employee profile/검색 시스템은 무공개
- ⚠️ 한국 AI 기본법 (2026-01-22) — talent search·career 추천이 인사 의사결정에 영향 시 **고영향 AI** 분류 가능 → 영향평가 필요
- ⚠️ **노조 사전 합의 필수** (SK하이닉스 노조 강성) — 직원 통합 프로필·skill inference·매니저 검색은 노조 강한 우려 영역 (개인정보·차별 가능성)
- ⚠️ skill inference (프로젝트·교육에서 자동 추출)는 **부정확 risk** — 잘못된 skill tag가 매니저 검색에서 직원에게 불리하게 작용 가능
- ⚠️ One Resume 데이터 동의 범위 (HRMS·평가·외부 교육 결합)는 한국 개인정보보호법상 별도 동의 필요 가능

## Consulting Angle

- **KR talent profile/search 컨설팅에서의 위치 — "한국형 자체 구축 reference"**:
  - SK하이닉스가 글로벌 SaaS 벤더 (Gloat·Eightfold) 대신 **자체 구축**으로 talent profile/search를 운영 — 한국 반도체·이차전지·바이오 그룹사 talent profile 컨설팅의 자체 구축 reference
  - 단 외부 공개 metric 0건 → "SK하이닉스 사례"로 인용 시 출처 한계 명시 필수
- **글로벌 비교**:
  - Mastercard Unlocked (Gloat): talent marketplace 패턴, 30K+ 직원 production
  - Schneider Electric (Gloat): manufacturing·engineering talent marketplace
  - Eightfold: skill ontology + talent intelligence
  - SK하이닉스: **자체 구축 (internal-build) 패턴** — 글로벌 SaaS 벤더 대신 자체 architecture
- **Trade-off (vendor SaaS vs 자체 구축)**:
  - SaaS (Gloat·Eightfold): 검증된 글로벌 reference + skill ontology + 빠른 배포 / 단 한국어·한국 직무체계 fit·data sovereignty 한계
  - 자체 구축 (SK하이닉스): 한국어·도메인·노조 합의·data sovereignty 통제 / 단 외부 검증 reference 부재·구현 risk·시간
- **2026 Q3-Q4 KR talent management 컨설팅 deck**:
  - "한국 대기업 talent profile/search의 진화" — 분산 시스템 → 통합 프로필 → AI 자연어 검색 → talent marketplace
  - SK하이닉스 self-build 패턴 vs 글로벌 SaaS 벤더 트레이드오프 비교 reference
- **반면교사 / 위험 시그널**:
  - 외부 1차 reference 0건 — 클라이언트에게 "SK하이닉스 사례"로 인용 시 정량 metric 부재 한계 솔직 공개 필수
- **Watch list**: SK하이닉스 외부 publication·발표·컨퍼런스 사례 발표 시 (예상 2026~2027) 본 page 갱신
