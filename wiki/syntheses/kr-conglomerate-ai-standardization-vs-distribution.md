---
title: "KR 그룹 AI HR 표준화 vs 분산 패턴 (SK·LG·삼성·현대·금융 비교)"
type: synthesis
created_at: 2026-05-05
slug: kr-conglomerate-ai-standardization-vs-distribution
---

# KR 그룹 AI HR 표준화 vs 분산 패턴

## 요약

한국 5대 conglomerate (SK·LG·삼성·현대·금융 4사)의 AI HR 도입 패턴을 cross-entity 분석. **SK는 그룹 단일 표준화, LG·삼성·현대는 계열사별 분산, 금융은 단독 platform** 패턴 명확. KR 컨설팅 RFP에서 "그룹 차원 AI 표준 vs 계열사 자율" 의사결정의 reference framework.

## 그룹별 비교

### SK 그룹 — ★ 그룹 단일 표준 (유일)

| Use case | Confidence | 패턴 |
|---|---|---|
| [[sk-group-aibiz-25-companies]] | 0.50 | **A.Biz 단일 platform → 25개사 8만 명** |
| [[sk-cc-adot-biz-hr-recruitment]] | 0.50 | 그룹 표준 활용 (SK C&C 채용) |
| [[sk-hynix-ask-ai-interview]] | 0.45 | 자체 hybrid (peer review) — 표준 위 customization |
| [[sk-hynix-pwc-5agent-retention]] | 0.20 | PwC 제안 추진 계획 |
| [[sk-group-aict-ai-recruitment]] | 0.40 | AICT 그룹 표준 채용 |

**핵심 패턴**:
- SKT-SK AX 합작 'A.Biz'를 그룹 표준 platform으로 25개사 일괄 배포
- 국가핵심기술 보유사 (SK하이닉스·SK온·SK실트론) 격리 LLM 'A.X'
- 사업 영역(채용·HR Q&A·자동화)별 표준 모듈 + 계열사 customization

**KR 컨설팅 시사점**: 한국에서 **유일하게 그룹 단일 표준화** 사례. 다른 그룹 RFP 시 "SK 표준화 모델"로 reference 가능. 단 다른 그룹 cultural fit 검증 필수.

### LG 그룹 — 계열사별 분산 (LG AI연구원이 LLM은 표준)

| Use case | Confidence | 패턴 |
|---|---|---|
| [[lg-chatexaone-group-rollout]] | 0.55 | LG AI연구원 EXAONE → LG전자·이노텍·디스플레이 5만+ |
| [[lg-uplus-jihye-employee-agent]] | 0.30 | LG U+ 자체 '지혜' (별도) |
| [[lgcns-agentic-ai-hr]] | 0.25 | LG CNS 자체 agentic |

**핵심 패턴**:
- **LLM은 표준화 (EXAONE)** → 모델 차원 그룹 자산
- **Application은 계열사별 분산** — 전자·이노텍·디스플레이는 ChatEXAONE 공통, U+·CNS는 자체
- 그룹사별 자율성 + AI연구원 R&D 통합

**KR 컨설팅 시사점**: "자체 LLM은 그룹 표준 + 응용은 계열사 자율" — 한국 대기업의 가장 합리적 절충 모델. 글로벌 commercial LLM (GPT·Claude) 의존 회피하면서 계열사 다양성 유지.

### 삼성 그룹 — 분산 + 그룹 AI센터 별도

| Use case | Confidence | 패턴 |
|---|---|---|
| [[samsung-multicampus-ai-learning]] | 0.20 | 멀티캠퍼스 (HRD 자회사) |
| [[samsung-fire-employee-rag-chatbot]] | 0.30 | 삼성화재 자체 추진 |
| (예정) 삼성SDS Brity Copilot | — | HCM 통합 계획 (별건) |

**핵심 패턴**:
- **그룹 표준화 미공개** — SK 같은 단일 platform 부재
- 삼성생명 중심 그룹 AI센터 (126명) 인접 인프라 — 화재·생명 등 금융 계열사 활용
- 삼성SDS Brity Copilot은 외부 판매 위주, 그룹 내 HCM 통합 진행 중
- 공식 발표 매우 sparse (보안·노조 sensitivity)

**KR 컨설팅 시사점**: 한국 1위 그룹이지만 외부 reference 가장 약함 — "선두주자 기회"로 framing 가능. 단 보안 정책상 외부 reference 못 만들 가능성도 고려.

### 현대차 그룹 — 분산 (제조 위주)

| Use case | Confidence | 패턴 |
|---|---|---|
| [[hyundai-mobis-moai-platform]] | 0.45 | 현대모비스 자체 'MoAI' (자동차 부품) |
| [[hyundai-steel-hip-platform]] | 0.40 | 현대제철 자체 'HIP' (철강) |

**핵심 패턴**:
- **계열사별 자체 구축** — 그룹 표준화 0
- 제조업 특성: 온프레미스 + 매뉴얼·도면 RAG 중심 (보안 민감)
- 본사 (현대자동차·기아) 자체 HR-AI 공식 발표 0건 — 공급망 부품사·소재사가 주도

**KR 컨설팅 시사점**: "제조 그룹사 분산 패턴" 표본. 그룹 표준화 의사결정 시 reference 부재 (SK 패턴 적용 vs LG 절충 적용 검토).

### 금융 4사 — 단독 platform (그룹 차원 X)

| Use case | Confidence | 패턴 |
|---|---|---|
| [[woori-bank-175-ai-agents]] | 0.50 | 우리은행 175 에이전트 (삼성SDS 구축) |
| [[kb-bank-ai-hr-deep-change]] | 0.65 | KB 인사이동 ML (5년+) |
| [[shinhan-bank-ai-one-platform]] | 0.50 | 신한 AI ONE (40+ AI 통합) |
| [[mirae-asset-ai-assistant-platform]] | 0.45 | 미래에셋증권 (No-code 빌더) |

**핵심 패턴**:
- **각 은행이 단독 platform** — 그룹 (지주사) 차원 통합 0
- **vendor 다양성**: 우리=삼성SDS·KB=내부·신한=내부·미래에셋=네이버클라우드
- 금융정보보호법 + 전자금융감독규정 → strict private deployment
- 각 은행이 best-in-class 추구 (KB 5년 stability·우리 175 portfolio·신한 40+ 통합·미래 No-code)

**KR 컨설팅 시사점**: 금융 그룹사 합병·통합 시 "기존 platform 통합 vs 신규 표준화" 의사결정 reference. 우리은행 175 portfolio framework가 가장 진보된 reference.

## 4가지 표준화 패턴 framework

| 패턴 | 사례 | 장점 | 단점 |
|---|---|---|---|
| **1. 그룹 단일 표준화** | SK A.Biz | 비용 효율·거버넌스 일관성·교육 단일 | 계열사 specific need 미충족·vendor lock-in |
| **2. LLM 표준화 + 응용 분산** | LG (EXAONE) | 데이터 주권 + 계열사 자율 절충 | 응용 quality 격차·cross-entity 학습 어려움 |
| **3. 계열사별 분산 (R&D 표준 부재)** | 삼성·현대 | 계열사 자율·실험 다양성 | 중복 투자·표준 부재·governance 어려움 |
| **4. 단독 platform (그룹 통합 X)** | 금융 4사 | regulatory fit·best-in-class 추구 | 그룹 시너지 부재·통합 시 cost |

## KR 컨설팅 의사결정 framework

```mermaid
flowchart TB
    Start[KR 그룹사 AI HR 도입 검토] -->|평가| Q1{그룹 차원 거버넌스 의지?}
    Q1 -->|강함| Q2{자체 LLM 보유?}
    Q1 -->|약함 → 계열사 자율| Pat3[패턴 3 — 분산]
    Q2 -->|예 (LG·SK 계열)| Pat2[패턴 2 — LLM 표준 + 응용 분산]
    Q2 -->|아니오| Q3{단일 vendor 채택?}
    Q3 -->|예 (SK A.Biz)| Pat1[패턴 1 — 그룹 단일 표준]
    Q3 -->|아니오 → 산업별 specific| Pat4[패턴 4 — 단독 platform]
    Pat1 --> SKRef[SK 모델 reference]
    Pat2 --> LGRef[LG 모델 reference]
    Pat3 --> NoStd[표준화 부재 — 향후 통합 cost]
    Pat4 --> FinRef[금융권 모델 reference]
```

## 데이터 source

본 synthesis는 다음 wiki source 기반:
- KR 21건 use case (R8 + R8-C 결과)
- 각 그룹 company page (SK Group·LG·신한은행·KB국민은행·SK하이닉스 등)
- KR consulting reference doc (`기타/ai_technology_categories.md`)

## 다음 라운드 갱신

- 신규 KR group case 추가 시 본 분석 재실행
- 삼성·현대 zero-find 그룹 신규 announcement 시 패턴 재분류
- 그룹사별 actual ROI metric publication 시 비교 update
