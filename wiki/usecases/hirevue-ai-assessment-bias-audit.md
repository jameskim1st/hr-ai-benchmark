---
title: "HireVue — AI 비디오 면접 + 게임 기반 평가"
slug: hirevue-ai-assessment-bias-audit
primary_category: Talent Acquisition
subcategory: Interview & Selection
tags: [video-interview, game-based-assessment, bias-audit, nyc-ll144, compliance, forrester]
company: _다수 (major financial institution 등)_
industry: [all]
region: [global]
employee_class: [all]
vendor: [HireVue]
vendor_type: [point-solution]
output: "후보자 비디오 면접·게임 평가의 competency 점수 (시각 단서 미사용) + 알고리즘 disparate impact 분석 보고서 (인종·성별·교차 ~300건, DCI Consulting 외부 감사) + AI Explainability Statement"
ai_tech_type: [predictive]
ai_tech_subtype: [clustering-classification, prediction]
stage: production
frequency: daily
first_seen: 2025
last_confirmed: 2025
confidence: 0.35               # Tier 1 Forrester TEI(+0.35) + Tier 3 vendor(+0.10) - 구체 고객명 1곳만 = 0.35
consulting_angle_status: filled
sources:
  - "HireVue official https://www.hirevue.com/"
  - "HireVue bias audit press release https://www.hirevue.com/press-release/hirevue-leads-industry-in-fair-and-ethical-hiring-practice-engaging-external-auditor-dci-consulting-group-for-external-bias-audit-of-algorithms"
  - "Forrester TEI study (referenced in reviews)"
related_usecases:
  - midas-inair-ai-assessment-korea
  - chipotle-paradox-olivia
  - eightfold-ai-talent-intelligence
related_vendors: []
---

# HireVue — AI 비디오 면접 + 게임 기반 평가

> **이 use case의 핵심 가치**: 제품 기능이 아니라 **bias audit와 compliance 대응**. HireVue는 AI 채용 업계에서 **가장 먼저·가장 투명하게** 편향 감사를 공개한 벤더이며, **NYC Local Law 144 준수를 위한 DCI Consulting 외부 감사**를 받은 사실이 wiki의 Governance 관점에서 가장 가�� 있는 Fact.

## Summary

HireVue는 **AI 비디오 면접 + 게임 기반 역량 평가** 플랫폼. 주요 성과: ⚠️ 벤더 주장 — time-to-hire **60~89% 단축**, 만족도 **17~25% 향상**. **Forrester TEI** 연구에서 major financial institution 대상 **134% ROI** 보고. ★ **2020년 facial analysis 제거** (AI 윤리 논란 후 자발적 결정). **DCI Consulting, ORCAA, Landers Workforce Science** 등 외부 독��� 감사 기관에 알고리즘 bias audit 의뢰.

## Solution Architecture

### A. Process (프로세스)

- **Before**: AI 채용 알고리즘이 inference time에 학습되거나 bias 점검 없이 운영
- **After**:
  1. HireVue의 competency·game-based 알고리즘은 lab에서 학습·테스트 후 lock (static·deterministic)
  2. 외부 감사기관(DCI Consulting Group)이 인종·성별·교차 카테고리별 disparate impact 분석
  3. NYC Local Law 144 등 규제 요건에 맞춰 bias audit table 생성 (~300건)
  4. 결과 공개·AI Explainability Statement 게시
  5. 알고리즘 업데이트는 명시적 재학습·재감사 절차 거쳐야만 가능
  6. 고객사는 자사 사용 결과로 추가 fairness monitoring 수행
- **HITL**: 외부 감사인이 알고리즘 결과 검증, HR/legal team이 사용 가능 여부 결정
- **Frequency**: annual + 알고리즘 변경 시
- **Source**: HireVue press release on DCI bias audit


## Impact / Metrics (기대효과)

### 기대효과 요약
Before: _미공개 (major financial institution의 기존 채용 비용·기간)_ → After: Forrester TEI 분석 기준 134% ROI(Fact). ⚠️ 벤더 주장 time-to-hire 60~89% 단축, 후보자 만족도 17~25% 향상 (Before 절대값 미공개).

| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| ROI | **134%** (major financial institution) | Forrester TEI | ✅ Fact (Tier 1 독립 분석) |
| Time-to-hire 단축 | **60~89%** | HireVue 공식 | ⚠️ 벤더 주장 |
| 후보자 만족도 향상 | **17~25%** | HireVue 공식 | ⚠️ 벤더 주장 |

## ★ Governance & Bias Audit (이 페이지의 핵심)

### Facial Analysis 제거 (2020)
- HireVue는 **2020년에 AI 면접의 facial analysis(표정 분석) 기능을 자발적으로 제거**
- 배경: AI 편향 논란·학계 비판·언론 보도 후 결정
- **이것이 중요한 이유**: "문제가 밝혀진 후 벤더가 스스로 기능을 제거한" 거의 유일한 사례. 다른 벤더(Paradox·마이다스아이티 등)는 아직 이런 수준의 투명성을 보이지 않음.

### NYC Local Law 144 bias audit
- **DCI Consulting Group** (외부 독립 감사 기관)에 의뢰
- NYC LL144 규정에 따라 algorithm bias audit 실시
- 감사 대상: **역량 기반(competency-based) + 게임 기반(game-based)** 알고리즘
- 감사 축: **인종(race), 성별(gender), 인종×성별 교차** — 복수 직급·use case별로 실시
- **ORCAA, Landers Workforce Science LLC**도 별도 감사

### AI 작동 방식 (편향 완화 관점)
- 현재 HireVue AI는 **구조화된 면접 답변 + 게임 기반 input**에서 데이터 수집
- **시각적 단서(visual cues) 분석 안 함** (2020년 제거 이후)
- 직무 관련 역량(competencies)에 대한 예측 정확도를 최대화하면서 인구통계적 차이를 최소화하도록 설계

## Consulting Angle

### ★ Governance 관점에서 wiki 최고 가치 사례

1. **"AI 채용의 편향 감사를 어떻게 하나?"에 대한 가장 구체적 reference**: DCI Consulting + NYC LL144 기반
2. **"facial analysis 제거" 결정**: 벤더의 **자발적 AI 윤리 결정**의 선례 — 클라이언트에 "벤더에게 요구해야 할 것" 체크리스트
3. **Forrester TEI 134% ROI**: Tier 1 독립 분석이므로 다른 벤더의 자체 주장 ROI보다 신뢰도 높음

### vs 마이다스아이티 inAIR

| | HireVue | 마이다스아이티 inAIR |
|---|---|---|
| **검증 유형** | **Bias audit** (편향 감사) | **성과 예측 ���확도** (Nature 논문) |
| **핵심 질문** | "AI가 공정한가?" | "AI가 정확한가?" |
| **감사 기관** | DCI Consulting (외부 독립) | KAIST (학술 독립) |
| **제거한 기능** | facial analysis (2020) | 없음 |
| **NYC LL144 대응** | ✅ 명시적 | ❓ 미공개 |
| **한국 적용** | 한국어 대응 미확인 | ✅ 한국 특화 |

**두 벤더를 함께 제시하면**: "정확도(마이다스아이티) + 공정성(HireVue)"이라는 **채용 AI의 두 축**을 클라이언트에게 설명할 수 있음.

### EU AI Act 관점
- HireVue의 bias audit approach는 **EU AI Act의 high-risk 시스템 요구사항** (Article 9: Risk Management, Article 10: Data Governance, Article 14: Human Oversight)에 가장 가까운 현존 실무
- 2026-08 의무화 전에 "이미 이렇게 하는 벤더가 있다"는 증거
