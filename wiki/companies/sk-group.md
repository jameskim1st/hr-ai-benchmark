---
name: SK Group
type: company
page_type: company
industry: [conglomerate, telecom, semiconductor, energy, it-services]
region: [kr]
headquarters: Seoul, South Korea
size_employees: 100000+         # SK 그룹 전체 근사치
public: true                    # 다수 상장 계열사
ingested_first: 2026-04-12
last_confirmed: 2024             # SK AX 페이지의 2024 하반기 도입 기재 기준
---

# SK Group

한국 3대 재벌 그룹 중 하나. SK Hynix(반도체)·SKT(통신)·SK Innovation(에너지)·SK AX(IT 서비스) 등 주요 계열사 보유. **국내 대기업 중 HR AI 도입 가장 가시적 레퍼런스 중 하나** — 자체 계열사 SK AX + SKT 합작 솔루션을 그룹 공채에 적용.

## HR AI 주요 사례

### SK Group 신입 공채 AI 채용 (2024~)
- **파트너**: [[sk-ax]] (자사 IT 서비스 계열사, SKT 합작)
- **도입 시점**: 2024년 하반기 신입사원 공채
- **주장**: 국내 최초 채용 전 과정 생성형 AI 자동화
- ⚠️ 벤더 주장 (SK AX = SK 그룹 자체): 시간당 1,000명 처리, 사람 대비 100배 빠름
- 핵심 차별점: **AICT (AI Competency Test)** — 기존 코딩 테스트 폐지, 생성형 AI 활용 능력 평가로 전환
- 상세: [[sk-group-aict-ai-recruitment]]

### 'A.Biz' 그룹 단일 표준 확산 (2025 하반기~)
- SKT–SK AX 합작 'A.Biz'를 **25개 멤버사·약 8만 명**에 배포, HR 정책·절차 문의 응대 에이전트를 HR 담당자가 agent builder로 자체 구축 — [[sk-group-aibiz-25-companies]]
- 첫 제품 '에이닷 비즈 HR'을 SK C&C 신입·주니어 채용에 전면 적용 (⚠️ 자사 보고: 지원서 분석 약 1주 → 4시간) — [[sk-cc-adot-biz-hr-recruitment]]
- 국가핵심기술 보유사(SK하이닉스 등)는 자체 LLM 'A.X' 격리 적용 — [[sk-hynix]]

## HR 대그룹 커버리지 (Live)

```dataview
TABLE WITHOUT ID
  primary_category AS "HR 대그룹",
  length(rows) AS "Use Case 수",
  rows.file.link AS "페이지들"
FROM "wiki/usecases" OR "wiki/enterprise-ai"
WHERE contains(company, "SK")
GROUP BY primary_category
```

## 📊 SK Group HR AI Use Cases (Live)

```dataview
TABLE WITHOUT ID file.link AS "Use Case", primary_category AS "대그룹", evidence_grade AS "등급", depth AS "depth", stage AS "단계", last_confirmed AS "확인"
FROM "wiki/usecases" OR "wiki/enterprise-ai"
WHERE contains(company, "SK") OR contains(tags, "sk-group")
SORT evidence_grade ASC, last_confirmed DESC
```
> 목록은 Dataview 자동 생성 — 손으로 갱신하지 않음

## Consulting Angle

- **한국 대기업 HR AI 도입의 flagship reference** — 국내 컨설팅 프로젝트에서 Moderna에 해당하는 위치
- 특히 **AICT 도입 → 기존 코딩 테스트 폐지**는 "AI 시대의 채용 역량 재정의" 워크숍의 앵커 사례
- **주의점**:
  - SK AX가 자사 계열사이므로 **self-deployment** — 외부 고객사 확장 가능성은 별도 검증 필요
  - Tier 2 국내 경제지 보도(서울경제 2025-02 [[sedaily-sk-cc-adot-biz-hr-2025-02]], [[korea-conglomerate-hr-ai-2025-2026]])는 확보됐으나, AICT·처리 속도 등 **성능 수치는 여전히 SK AX 자체 주장** — 독립 효과 분석은 없음
  - AICT 출제·평가의 구체 설계·bias·재현성은 공개 없음
- **활용처**:
  - 국내 대기업 CHRO 대상 "2025 HR AI 트렌드" 브리핑의 대표 케이스
  - "AI competency 평가"라는 새로운 채용 기준에 대한 토론의 촉매
  - 노사관계·개인정보 대응 **체크리스트** 설계 시 출발점

## 반면교사 질문
- SK의 AICT가 정말로 **채용 품질을 개선**했는가? 이직률·성과 data로 검증 가능한가?
- 기존 코딩 테스트와 **상관성**은? AI 활용 능력이 실제 업무 성과와 연결되는가?
- 탈락자에 대한 공정성·이의제기 절차는 어떻게 운영되는가?

## Related
- Vendor: [[sk-ax]] · [[skt]]
- Companies: [[sk-hynix]]
- Use cases: 상단 Dataview 표 (자동 생성 — 손으로 갱신하지 않음)
- Sources: [[sk-ax-ai-recruitment-service-2024]] · [[sk-ax-insight-ai-recruitment-2024]] · [[sedaily-sk-cc-adot-biz-hr-2025-02]] · [[korea-conglomerate-hr-ai-2025-2026]]
