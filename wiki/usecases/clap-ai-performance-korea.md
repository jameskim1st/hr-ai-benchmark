---
title: "CLAP — AI 기반 성과관리 SaaS"
slug: clap-ai-performance-korea
primary_category: Performance & Talent Management
subcategory: Goal & Performance
tags: [performance-management, ai-feedback, ai-summary, one-on-one, korea, saas, mid-enterprise]
company: 디웨일 (CLAP)
industry: [tech]
region: [kr]
employee_class: [기술사무직, 전임직]
vendor: []
vendor_type: [point-solution]
output: "주관식 평가 코멘트 자동 요약·정제 + AI 피드백 텍스트 + 원온원 미팅 요약 + 서술형 리뷰 초안 + 직원별 AI 성장 리포트 (한국 중견기업용 SaaS)"
ai_tech_type: [generative]
ai_tech_subtype: [summarization-qa, text-generation]
stage: production
frequency: monthly
first_seen: 2024-01-01
last_confirmed: 2025-10-01
confidence: 0.30
sources:
  - sources/clap-blog-hr-ai-trend-2026.md
  - sources/sisajournal-clap-2025.md
  - sources/thebell-diwhale-2025-10.md
related_usecases:
  - moderna-self-review-gpt
  - workday-illuminate-employee-sentiment
related_vendors: []
---

## Summary

디웨일이 운영하는 CLAP(클랩)는 중견·대기업 특화 AI 기반 성과관리 SaaS로, 주요 AI 기능은 주관식 평가 코멘트 AI 자동 요약, AI 피드백 생성, AI 원온원 미팅 내용 요약, AI 평가(서술형 리뷰 초안 작성), AI 성장 리포트 등이다. ⚠️ **자사 보고**: 인지그룹 등 중견기업에 공급 사례를 확보했으며 2025년 시장 확대 중. [[sources/clap-blog-hr-ai-trend-2026.md]] [[sources/sisajournal-clap-2025.md]]

## Problem / Why (도입 배경)

- **Before (baseline)**: 국내 중견·대기업의 성과 평가 시즌(월별·분기·연간)마다 관리자가 **수동으로 주관식 평가 코멘트 작성** + HR이 수백~수천 건의 평가 내용을 **수동 취합·정리**. 원온원 미팅 노트도 수기 기록. ❓ **구체 시간/비용 baseline 미공개** (관리자당 평가 작성 시간, HR 취합 소요 시간 등)
- **Pain point**: (1) **형식적·부정확한 평가 코멘트** — 관리자가 시간 압박으로 "복붙"하거나 피상적으로 작성 → 직원 개발에 도움 안 됨. (2) **HR 행정 부담** — 평가 시즌에 HR 인력이 취합·정리에 과도 투입. (3) 원온원 미팅 내용이 **기록되지 않거나 비체계적** → 지속적 성과 관리 연결 부족
- **Trigger**: 국내 중견기업(인지그룹 등)이 SaaS 기반 성과관리 도구를 탐색하면서 "AI가 코멘트를 자동 요약·초안 작성해준다면" 수요 발생 → CLAP의 AI 기능 확장
- **⚠️ 주의**: 위 pain point는 CLAP이 타겟하는 **국내 중견·대기업 성과관리의 일반적 문제**이며, 특정 도입 기업의 공식 문제 진술은 미공개

## Solution Architecture

> **최우선 원칙**: 이 섹션은 **공개된 사실만** 기록한다.

### A. Process (프로세스)

- **Before (As-is)**: 관리자가 수동으로 주관식 평가 작성. 원온원 노트 수동 기록.
- **After (To-be)**:
  1. ✅ **Fact** 주관식 평가 코멘트 AI 자동 요약·정제 + 비속어·불필요 표현 필터링. [[sources/clap-blog-hr-ai-trend-2026.md]]
  2. ✅ **Fact** AI 피드백 생성. [[sources/clap-blog-hr-ai-trend-2026.md]]
  3. ✅ **Fact** AI 원온원 — 미팅 내용 자동 요약. [[sources/clap-blog-hr-ai-trend-2026.md]]
  4. ✅ **Fact** AI 평가 — 서술형 리뷰 초안 작성. [[sources/clap-blog-hr-ai-trend-2026.md]]
  5. ✅ **Fact** AI 성장 리포트 — 구성원 성장 현황 요약. [[sources/clap-blog-hr-ai-trend-2026.md]]
- **Human-in-the-loop**: AI가 초안·요약을 생성하고 관리자/HR이 최종 검토·확정.
- **Trigger & Frequency**: 성과 평가 주기(월별·분기·연간) + 원온원 발생 시 수시.
- **Scope of autonomy**: Recommend 수준.

### B. System & Infrastructure (시스템·인프라)

- **배포 환경**: 클라우드 SaaS. 세부 _미공개 (not disclosed)_.
- **연동·통합**: ✅ **Fact** 모듈형 설계 — 성과관리, 근무관리, 인사관리, 워크플로 결합 가능. [[sources/sisajournal-clap-2025.md]]
- **사용자 접점**: 웹 포털. _미공개 (not disclosed)_.

### C. Data (데이터)

- **입력 데이터 소스**: 주관식 평가 텍스트, 원온원 노트, 직원 성과 데이터.
- **학습 vs RAG vs In-context**: _미공개 (not disclosed)_
- **데이터 거버넌스**: _미공개 (not disclosed)_ — 개인정보보호법 적용 환경.

### D. Model (모델)

- **Foundation model**: _미공개 (not disclosed)_
- **커스터마이징**: _미공개 (not disclosed)_

### E. Organization & Team (조직·팀 구조)

- **오너십**: 디웨일 (대표이사 구자욱). "글로벌 HR SaaS 리더" 목표 공개. [[sources/thebell-diwhale-2025-10.md]]
- **고객 현황**: ✅ **Fact** 인지그룹에 공급. [[sources/startupn-clap-2025.md]] 중견기업 위주 확대 중.
- **팀 규모**: _미공개 (not disclosed)_

## Impact / Metrics (기대효과)

### 기대효과 요약
⚠️ 기대효과 수치 미공개. 아래 표 참조.

- _미공개 (not disclosed)_ — 구체 성과 수치 공개된 것 없음. Tier 1·2 독립 검증 미확인.

## Governance & Risk

- 평가 AI 생성 내용의 편향·공정성 감사 체계 _미공개 (not disclosed)_.
- 개인정보보호법 적용. 평가 데이터는 민감 개인정보.
- 비속어 필터링은 공개됐으나 전반적 콘텐츠 가드레일 _미공개 (not disclosed)_.

## Contradictions

없음 (현재 기준).

## Consulting Angle

- **국내 성과관리 AI SaaS 대표 사례**: 모더나의 자체 GPT 기반 성과 리뷰 (→ [[moderna-self-review-gpt]]) 와 비교하면, CLAP은 내재화 역량이 없는 국내 중견기업을 위한 "성과관리 AI SaaS" 패턴.
- **평가 코멘트 AI 요약**: 국내 기업 성과 평가 시즌(보통 연 1~2회) 직전 도입 수요가 높음. HR tech 제안 시 "평가 시즌 생산성" 개선 사례로 활용.
- **한계**: 소스가 벤더 자사 블로그·언론 보도 수준(Tier 3~4). 독립 검증 없음. confidence 0.30 — 벤처 단계 스타트업으로 시장 검증 아직 진행 중. 추가 고객 케이스 스터디 필요.
- **파생 질문**: "CLAP 같은 국내 성과관리 SaaS가 Workday Performance·SAP SuccessFactors Performance 대비 가격·현지화 측면에서 어떤 경쟁 우위를 갖는가?"
