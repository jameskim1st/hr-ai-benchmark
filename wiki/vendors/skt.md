---
name: SK Telecom (SKT)
type: vendor
page_type: vendor
vendor_type: foundation-model
category: [telecom, llm, korean-vendor]
headquarters: Seoul, South Korea
founded: 1984
public: true
ticker: "017670.KS"
parent: SK Holdings
products:
  - A.X (자체 한국어 LLM 제품군)
  - SKT Enterprise AI
ingested_first: 2026-04-12
last_confirmed: 2024
stub: true
---

# SK Telecom (SKT)

> ⚠ **Stub**: 이 페이지는 [[sk-ax]]·[[sk-group-aict-ai-recruitment]]의 "SKT 합작 파트너" 언급을 해소하기 위해 생성된 stub. SKT HR AI 관점의 단독 리서치는 다음 ingest 라운드 보강 필요.

한국 최대 통신사. SK 그룹 계열사. **자체 한국어 LLM 'A.X' 시리즈**를 개발·운영. HR AI 영역에서는 [[sk-ax]](SK 그룹 IT 서비스 계열사)와 **합작 솔루션**으로 SK 그룹 자사 공채에 생성형 AI 채용 서비스를 제공.

## wiki 상의 역할

SKT는 본 wiki에서 **SK 그룹 HR AI 인프라의 기술 파트너**로 등장:

- [[sk-ax]] 와의 합작 솔루션 (HR AI 채용 서비스)
- [[sk-group-aict-ai-recruitment]] — SK Group 2024 하반기 신입 공채 생성형 AI 채용 (SKT의 구체 역할은 소스에 미공개)
- [[sk-group-aibiz-25-companies]] — SKT–SK AX 합작 'A.Biz'의 그룹 25개 멤버사 확산; 국가핵심기술 보유사에는 자체 LLM **'A.X'** 적용 명시
- [[sk-cc-adot-biz-hr-recruitment]] — A.Biz 첫 제품 '에이닷 비즈 HR'의 SK C&C 채용 적용

## 관련 제품

### A.X LLM (한국어 특화)
SKT가 자체 개발한 한국어 LLM 시리즈. 본 wiki의 SK 그룹 AICT 채용 서비스가 **A.X를 foundation model로 사용하는지 여부는 공개되지 않음** — [[sk-ax-ai-recruitment-service-2024]] 소스에 명시 없음. 추측 금지. 단, A.Biz 그룹 확산에서는 **국가핵심기술 보유사(SK하이닉스·SK온·SK실트론)에 A.X 적용**이 소스에 명시됨 ([[sk-group-aibiz-25-companies]]).

## 미공개 / 보강 필요 (stub)

- ❓ SKT 자체 HR AI 도입 (사내 HR 시스템)
- ❓ SK 그룹 AICT·A.Biz에서 SKT의 구체 역할 (foundation model 제공? 인프라? 알고리즘?)
- ❓ A.X LLM의 HR 도메인 특화 여부
- ❓ SKT Enterprise AI 제품군의 HR 용도

## 관련 use cases

```dataview
TABLE WITHOUT ID file.link AS "Use Case", company AS "고객", primary_category AS "대그룹", evidence_grade AS "등급", depth AS "depth"
FROM "wiki/usecases" OR "wiki/enterprise-ai"
WHERE contains(vendor, "SKT")
SORT evidence_grade ASC
```
> 목록은 Dataview 자동 생성 — 손으로 갱신하지 않음

## Related
- Partner vendor: [[sk-ax]]
- Company: [[sk-group]] · [[sk-hynix]]
- Use cases: 상단 Dataview 표 (자동 생성 — 손으로 갱신하지 않음)
- Sources: [[sk-ax-ai-recruitment-service-2024]] · [[korea-conglomerate-hr-ai-2025-2026]]
