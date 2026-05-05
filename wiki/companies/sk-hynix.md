---
name: SK하이닉스
type: company
industry: [semiconductor]
region: [kr]
headquarters: 경기 이천
size_employees: 38000
public: true
ticker: 000660.KS
ingested_first: 2026-05-05
last_confirmed: 2026-04-01
---

# SK하이닉스

세계 2위 메모리 반도체 기업. SK 그룹 핵심 멤버사이자 **국가핵심기술 보유사**. **HR AI는 채용 + 그룹 표준 결합**: (1) **A!SK** AI 영상면접 hybrid (AI + 미래 동료 평가) — 2025 신설, (2) SK 그룹 'A.Biz' 표준 사용 with 자체 LLM 'A.X' 격리 환경.

## HR AI 전략 / 핵심 테마

- **국가핵심기술 보유사 격리 LLM**: 자체 LLM 'A.X' + SK AX 산업특화 AI — 산업안보 강화
- **AI single decision 회피 hybrid**: A!SK AI + 미래 동료 peer review — 한국 AI 기본법 인적감독 의무 자동 충족 best practice
- **그룹 표준 활용**: SK 'A.Biz' 표준으로 그룹 차원 거버넌스

## 📊 SK하이닉스 HR AI Use Cases

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  primary_category AS "카테고리",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE contains(company, "SK하이닉스")
SORT confidence DESC
```

## Consulting Angle

- **KR 채용 AI hybrid model 1순위 reference**:
  - 마이다스 inAIR (vendor single AI) + SK C&C 자체 (자체 single AI) + SK하이닉스 (자체 hybrid AI + peer)
  - hybrid 모델이 한국 AI 기본법 + 채용절차법 fit 가장 우수
- **국가핵심기술 격리 LLM 패턴**: 삼성전자·LG에너지솔루션·삼성바이오로직스 등 산업안보 + AI 활용 trade-off solution
- **2026 Q3-Q4 KR 반도체·이차전지·바이오 그룹사 컨설팅 reference**
