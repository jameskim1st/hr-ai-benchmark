---
type: system-review
generated_at: 2026-09-27
scope: Benchmark wiki 전체 (CLAUDE.md · commands · wiki/ 262 pages · scripts · exports)
method: 결정론적 스크립트 전수 점검 + 대표 페이지 정독 + 외부 리서치
tags: [review, lint, roadmap, llm-wiki]
---

# Benchmark 시스템 전면 점검 (2026-09-27)

> 마지막 커밋 2026-05-06 이후 약 4.7개월 만의 점검. 스크립트로 262개 페이지를 전수 검사한 결과와 대표 페이지 정독 결과를 합쳐 정리했다.

## 0. 한 줄 결론

**설계(CLAUDE.md)는 좋은데 운영이 설계를 따르지 않았다.** raw→sources→usecases 근거 사슬이 절반 이상 끊겨 있고, lint가 LLM 수작업이라 문제를 못 잡았으며, 5월 이후 ingest·lint가 한 번도 돌지 않아 "살아있는 wiki"가 멈춰 있다. 콘텐츠 자체는 상위 30~40건이 충분히 쓸 만하지만, 나머지는 confidence 숫자를 믿고 인용하기 어렵다.

## 1. 자동 점검 수치 (2026-09-27 기준)

| 항목 | 값 | 비고 |
|---|---|---|
| use case / source / company / vendor / synthesis | 140 / 62 / 20 / 15 / 13 | index.md는 110, guide.md는 81, memory는 126이라고 기록 — 셋 다 불일치 |
| raw/ 원본 파일 | 19 (md 13 + jpg 6) | source 62건 중 **49건은 raw 원본 없음** |
| use case frontmatter `sources` 항목 중 실제 source 페이지로 안 이어지는 것 | **187건** | URL·기사명을 문자열로 적어둔 것 + 만들지 않은 `sources/xxx.md` |
| Solution Architecture에 `[[sources/…]]` 인용이 0개인 use case | **110 / 140** | §3 "노드 1개마다 citation" 규칙 사실상 미적용 |
| confidence가 §4 공식과 0.15 이상 어긋나는 use case | **101 / 140** | 공식이 아니라 감으로 매겨짐 |
| 깨진 wikilink | 299개 (35 페이지) | 4월 lint 리포트는 "broken 0건"으로 기록 |
| orphan 페이지 (inbound 0) | 29 | companies 8, usecases 16, syntheses 4, vendors 2 |
| 금지어(아마도·추정·보통·통상 등) 포함 use case | 62 | |
| `## Contradictions` 섹션 없음 | 95 | 템플릿 필수 섹션 |
| A~E 하위 섹션 누락 | B 24 · C 39 · D 40 · E 48 | 누락인데 `stage: stub`은 1건뿐 |
| `## Problem` 없음 / `## Summary` 없음 | 20 / 8 | |
| `last_confirmed`가 `2025`처럼 연도만 | 23 | 날짜 연산 불가 → stale 판정 누락 |
| stale (12개월 초과) | 32 | 2026-05 이후 갱신이 없어 연말이면 80건+로 급증 |
| Tier 1·2 독립 소스 0건 | 77 | 절반 이상이 벤더·자사 보고에만 의존 |
| Mermaid 0개 | 68 | |
| use case당 평균 source 수 / 평균 `미공개` 표기 수 | 2.1 / 7.7 | |
| confidence ≥0.7 / ≥0.5 / <0.4 | 15 / 56 / 55 | 평균 0.44 |

## 2. 발견된 문제 (심각도 순)

### A. 구조적 문제 — 설계와 운영의 괴리

**A-1. 근거 사슬(raw → source → use case)이 끊겨 있다.**
- Karpathy 패턴의 핵심은 "raw가 진실의 원천, wiki는 파생물"인데, 실제로는 대부분의 use case가 WebSearch 결과를 바로 wiki에 쓴 것이다. raw/에는 13개 md만 있고 raw/feeds·raw/reports는 비어 있다.
- `sources/kr-conglomerate-2026-q2-research`, `us-large-enterprise-hr-ai-2025-2026`, `korea-conglomerate-hr-ai-2025-2026`, `ibm-hr-ai-portfolio-2025-2026` 네 개는 "multi-source compilation"으로, **에이전트 리서치 메모를 source로 등록한 것**이다. 이 4개가 35개 use case의 유일한 근거이고, Tier 2로 매겨져 confidence를 +0.20씩 올린다. 원문 인용도 없어 나중에 검증할 방법이 없다.
- 187개 dangling reference는 나중에 "이 수치 어디서 나왔지?"를 답할 수 없게 만든다. 컨설팅 자산으로서 가장 치명적인 결함이다.

**A-2. Lint가 결정론적이지 않아 문제를 못 잡는다.**
- `/hr-lint`는 LLM이 읽고 판단하는 방식이다. 4월 12일 4라운드 모두 "broken link 0건"이라 기록했지만 실제로는 수백 건이다. 링크·frontmatter·날짜·금지어·공식 검산은 스크립트가 해야 할 일이다.
- 5월 6일 이후 lint 0회, ingest 0회, digest 0회. 설계상 "정기 점검"이 있지만 트리거가 없다.

**A-3. 슬래시 커맨드와 실제 워크플로가 다르다.**
- `/hr-digest`, `/hr-compare`는 한 번도 실행된 적이 없다(산출물 0건). 실제 성장은 전부 "라운드 N — background agent 3개 병렬 리서치" 방식이었는데, 이 방식은 CLAUDE.md 어디에도 프로토콜이 없다. 그래서 A-1의 편법(compilation source)이 생겼다.
- CLAUDE.md·commands가 참조하는 `/hr-autoresearch`, `scripts/fetch_sources.ps1`, `/hr-query`는 존재하지 않는다.

**A-4. confidence 숫자가 의미를 잃었다.**
- 101/140이 공식과 어긋난다. 예: `accenture-mass-genai-reskilling` 0.75인데 공식 계산은 0.20(Tier 2 한 건), `anaplan-workforce-analyst-ai-agents` 0.70인데 Tier 3 한 건. 반대로 Moderna Ask HR은 4개 소스에 공식대로 0.70.
- 소수점 둘째 자리 수치가 붙어 있으니 사용자는 "정밀하게 계산된 값"으로 오해한다. 계산을 스크립트로 옮기든지, 3단계 서열(검증됨/참고/미검증)로 바꾸든지 해야 한다.

**A-5. 스코프가 "HR AI use case"에서 "기업 GenAI 도입 뉴스"로 번졌다.**
- LG ChatEXAONE, 현대모비스 MoAI, GS칼텍스 AIU, 삼성화재 RAG 챗봇, JPMorgan LLM Suite, Goldman GS AI Assistant, CBA, 한국가스공사, Deloitte Claude 등은 전사 GenAI 플랫폼 사례로 HR 기능 AI가 아니다. 대부분 `Employee Self-service`(18건, 최다 subcategory)에 억지로 들어가 있다.
- `korea-ai-basic-act-hr-compliance`(법령), `deloitte-2026-human-capital-trends-meta`(리포트), `lotte-job-based-hr-reform`(AI 아님, 인사제도 개편)은 use case가 아니다. 별도 페이지 유형(regulations/, reports/)이 필요하다.
- 우리은행 175 에이전트는 5대 영역이 고객관계·자산·내부통제·고객상담·업무자동화로 **HR이 하나도 없는데** "HR Tech Governance"로 분류되어 있다.

**A-6. 기밀성 구분이 없다 — PwC 제안 자료가 클라이언트 공유용 export에 그대로 들어간다.**
- `sk-hynix-pwc-5agent-retention`, `verified-pwc-doc-2026-05`, `pwc-er-ai-deck-2026-05`, raw/etc/ 슬라이드 사진 6장은 컨설팅 제안·내부 자료다. HTML export에 "PwC Korea가 SK하이닉스에 제안한 5-Agent…" 문장이 그대로 실려 있다. 다른 클라이언트에게 이 파일을 보내면 사고다.
- frontmatter에 `visibility: public | internal | client-confidential` 같은 축이 없고, extract 스크립트도 필터하지 않는다.

### B. 콘텐츠 품질

**B-1. Fact-only 규칙 위반이 "잘 쓴 것처럼 보이는" 페이지에 숨어 있다.**
- 우리은행 페이지 B/C/D: "Core HRIS: Workday 또는 자체", "Brity 추정", "금융 도메인 fine-tuning + RAG (사내 정책)", "우리은행 SSO + 금융정보보호 강화" — 소스에 없는 내용을 항목마다 채웠다. `미공개`로 비워야 할 곳이다. 이런 페이지는 HTML 카드에서 System/Data/Model이 꽉 차 보여서 오히려 더 신뢰받는다.
- SK하이닉스 5-agent 페이지 "B/C/D. System — 추정 architecture", `2026-12 1차 → 2026 초 2차` 같은 날짜 논리 오류.
- 금지어 62건은 lint 리라이트가 4월 5곳에서 멈춘 뒤 계속 늘었다.

**B-2. 템플릿 준수율이 낮다.**
- Contradictions 95건 누락, E 48건, D 40건, C 39건, B 24건 누락. Cathay Pacific 페이지는 Summary·Problem·B~E 전부 없고 벤더 case study 한 줄이 근거인데 `stage: production`, confidence 0.20이다. 이런 페이지 30~40건은 `stub`으로 강등하는 것이 정직하다.
- `last_confirmed: 2025` 23건은 Dataview·lint 모두에서 날짜 연산이 안 된다.

**B-3. 중복·분할 오류.**
- `textio-tmobile-inclusive-jd` vs `t-mobile-textio-dei-hiring` (같은 사례), `hitachi-ema-agentic-hr-onboarding` vs `hitachi-skye-hr-ai-assistant` (둘 다 Skye), `jpmorgan-goldman-sachs-hr-ai`(합본) vs `goldman-sachs-gs-ai-assistant`·`jpmorgan-llm-suite-*`(개별). 합본 페이지는 삭제하고 redirect 남기는 것이 맞다.
- `company: 다수 (LinkedIn, Lyft, …)` 형태가 26건 — 벤더 제품 페이지와 도입 기업 페이지가 한 유형에 섞여 있다. 벤더 제품은 `vendors/` 아래 product 페이지로, 도입 사례만 `usecases/`로 두는 편이 Dataview 집계에 맞다.

**B-4. 문서·메타가 서로 다른 숫자를 말한다.**
- index.md "110건", guide.md §12 "81건", memory "126건", 실제 140. guide §14 "다음 라운드" 표는 5월 이전 상태.
- Moderna company 페이지: "현재는 1개 use case만 수집" + "다음 ingest 후보: self-review GPT·benefits GPT" — 둘 다 이미 ingest돼 있다. Workday vendor 페이지 Related 2건(실제 6건+), "Confirmed Customers 미공개"(Lloyds 페이지 존재). 손으로 쓴 요약은 반드시 stale해진다. 카운트·목록은 Dataview 또는 스크립트 생성으로 바꿔야 한다.

### C. 코드·산출물

**C-1. scripts/ 16개 중 10개가 죽은 코드.**
- `build_html.py`, `_v4`, `_v5`, `extract_to_json.py`, `_v2`, `apply_round8_*`, `apply_round9_sdm.py`, `batch_inject_process.py`, `apply_outputs.py`, `apply_ai_tech_classification.py`는 일회성 마이그레이션이다. `scripts/archive/`로 옮기거나 지워야 다음 세션의 에이전트가 헷갈리지 않는다. `wiki/exports/_data.js`도 4월 13일 잔재.
- 정작 필요한 `lint.py`(결정론적 검사), `fetch_sources`(수집), `build_all`(3-step 원커맨드)은 없다.

**C-2. export가 wiki와 따로 논다.**
- HTML·Excel은 5월 6일 빌드. 섹션이 없는 40여 페이지는 카드의 System/Data/Model이 빈칸이고, 우리은행처럼 추정으로 채운 페이지는 꽉 차 보인다 — 산출물이 품질을 거꾸로 보여준다.
- extract는 `**Before**`·`### 기대효과 요약` 같은 서식에 정규식으로 의존한다. 서식이 조금만 달라도 조용히 빈칸이 된다. frontmatter에 구조화 필드(`impact_summary`, `process_steps`)를 두거나, 최소한 extract 결과의 결측률을 빌드 로그에 찍어야 한다.

**C-3. 잡동사니.** 루트의 `무제.canvas`(빈 파일, untracked), `wikilink.md`(빈 파일), `raw/etc/`(CLAUDE.md 레이아웃에 없는 폴더), `scripts/__pycache__`.

## 3. 잘 된 것 (유지할 것)

- **스키마 설계**: A~F Solution Architecture, 5단계 Fact 표기(✅/⚠️ 벤더/⚠️ 자사/❓/🚫), 벤더 주장 vs 자사 보고 구분, Consulting Angle 필수화는 HR 컨설팅 자산으로서 차별점이다. 그대로 두고 **강제 수단**만 붙이면 된다.
- **상위 페이지 품질**: Moderna Ask HR, HR Acuity olivER, Workday paradox synthesis 같은 페이지는 미공개를 미공개라 쓰고, 컨설팅 활용법·파생 질문·인용 가이드까지 있다. 이 수준을 "기준 페이지(golden example)"로 지정해 lint가 비교하게 하면 된다.
- **Fact-check가 실제로 가치를 냈다**: PwC 자료의 Mastercard 벤더 오귀속(Eightfold→Gloat), Legion·Nayya 펀딩 오기 정정은 이 시스템만 할 수 있는 일이다. 이 "검증 루프"를 핵심 기능으로 승격시켜야 한다.
- **AI 기술 유형 축(5×13)**, 한국 특유 taxonomy(연말정산·PS/PI·전임직 등), Excel long-format 시트는 다른 곳에 없는 자산이다.

## 4. 개선 방향 — 효용·효과·효율

(리서치 결과와 함께 §5에서 우선순위를 매김. 여기서는 방향만.)

**효용(가치)을 높이는 것 — "무엇을 담을까"**
1. 스코프를 "HR 기능에 AI를 적용해 프로세스가 바뀐 사례"로 다시 조이고, 전사 GenAI 플랫폼은 `enterprise-ai-context`라는 별도 유형으로 분리해 use case 카운트에서 뺀다.
2. 페이지 유형 추가: `regulations/`(AI 기본법·EU AI Act·NYC LL144), `reports/`(Deloitte HC Trends 등 Tier 1 리포트), `products/`(벤더 제품 — 도입 사례와 분리). 지금은 전부 usecases에 섞여 있다.
3. **claim 단위 근거**: 수치·시스템명 하나마다 `[[sources/x]] "원문 인용"` 을 붙이는 규칙을 extract가 검사한다. 근거가 없는 수치는 export에서 자동으로 `⚠️ 근거 미확인` 표시.
4. **검증 루프 상품화**: "이 벤더 주장 사실인가?"를 답하는 `/hr-verify <claim>` 커맨드. PwC 자료 fact-check가 보여준 가치가 이것이다.
5. **한국 적용성 축** 추가: `kr_applicability: {법규, 노조, 언어, 벤더 국내 지원}` 4개 필드. Consulting Angle에 산문으로 흩어진 내용을 필터 가능한 필드로.

**효과(정확성·신뢰)를 높이는 것 — "얼마나 믿을 수 있나"**
6. `scripts/lint.py`(이 리포트의 점검 스크립트를 정식화) + Claude Code hook으로 **wiki/ 쓰기 후 자동 실행**. 깨진 링크·frontmatter·날짜·금지어·confidence 공식은 LLM이 아니라 코드가 검사한다.
7. confidence를 스크립트가 계산해 frontmatter에 써 넣는다(사람·LLM은 못 고침). 또는 `evidence_grade: A/B/C`로 단순화.
8. raw 스냅샷 의무화: WebSearch로 찾은 기사도 본문을 `raw/articles/`에 저장하고 source 페이지가 그 파일을 가리키게. compilation source 4개는 개별 source로 분해.
9. 기밀 축(`visibility`) 추가 + export 필터 + PwC 자료 페이지를 `internal`로 마킹.
10. 템플릿 미달 페이지 30~40건을 `stage: stub`으로 정직하게 강등하고, HTML에서 stub은 별도 섹션으로.

**효율(운영 비용)을 낮추는 것 — "얼마나 싸게 굴러가나"**
11. 주간 자동 사이클: 수집(RSS/뉴스 → raw/feeds) → ingest 후보 리스트 → 사용자 승인 → ingest → lint → export 재빌드 → digest. Claude Code 스케줄 루틴 또는 Windows 작업 스케줄러 + `claude -p`.
12. 손으로 쓰는 카운트·목록(index·guide·company Related·vendor Customers)을 전부 Dataview/스크립트 생성으로 교체.
13. 죽은 스크립트 정리, `build_all.py` 하나로 3-step 통합, 빌드 로그에 결측률 출력.
14. 라운드형 대량 리서치를 정식 프로토콜(`/hr-research <topic>`)로 만들되, 산출은 "후보 목록 + raw 저장"까지만 하고 use case 생성은 ingest 프로토콜을 타게 한다.

## 5. 외부 동향 (2026-04 → 09) — 이 시스템에 직접 관련된 것만

리서치 결과 중 1차 출처가 확인된 것 위주. 전체는 별첨 [[llm-wiki-landscape-2026-09]] 참조.

### 5-1. 커뮤니티가 5개월 만에 합의한 것

| 합의 | 우리 상태 | 근거 |
|---|---|---|
| **결정론적 lint와 LLM lint를 분리**한다. 링크·frontmatter·index drift·페이지 크기는 스크립트, 모순·낡음 판단만 LLM | 전부 LLM. 4월 "broken 0" 오판 | Zissa Wiki `wiki.py lint`, kfchou `lint-mechanical.py`, Astro-Han `check_evidence.py` |
| **Grounding Invariant**: 수치·날짜·직접 인용은 raw/ 파일에 verbatim으로 존재해야 하고 스크립트가 글자 단위로 대조 | raw 19개, 근거 사슬 187건 단절 | Astro-Han karpathy-llm-wiki(2.4k★), Zissa `quotes`, CAMS 논문(arXiv 2606.23989) |
| **숫자 confidence는 "정밀도가 권위를 가장한다"** → 3단 범주(`stated/inferred/speculative`) + 독립 소스 수 + supersession 링크 | 소수점 둘째 자리 float, 101건 공식 불일치 | rohitg00 v2 gist 코멘트, Manufactured Confidence 논문(2606.29279), Google OKF v0.2 |
| **hedging 보존**: 소스가 "검토 중·추정"이라 쓴 것은 wiki에서 확정형으로 승격 금지. 에이전트는 출처보다 문장의 확신도에 반응한다 | 우리은행 B/C/D가 정확히 이 실패 | Manufactured Confidence 논문 |
| **append 대신 rewrite + 명시적 supersession**: 모순은 두 버전 누적이 아니라 재작성하고 패자는 사유와 함께 아카이브 | `[!contradiction]` 누적 방식. Workday 800B/70B 5개월째 unresolved | theaioperator "I rebuilt Karpathy's wiki", MemStrata 논문 |
| **페이지 freshness 상태** `fresh/stale/unverified` + "새 소스가 건드렸어야 할 페이지" 검사 | `last_confirmed` 날짜만, 23건은 연도만 | llm-wiki-compiler(2.1k★), OKF `stale_after` |
| **슬러그 기반 dedup/merge** 툴 | Textio·Hitachi 중복 방치 | Obsidian "Karpathy LLM Wiki" 플러그인(3단계 중복 탐지), kfchou `wiki-merge` |
| **자동 수정 금지, 보고만** — 운영 회고 3건 모두 사람 승인 권고 | 4월 lint `--fix` 설계는 자동 수정 포함 | R&D World 1개월 회고, Cornell 회고 |
| **150~200페이지부터 index 샤딩**, 페이지 상한(400/800줄), CLAUDE.md 200줄 이하 | 262페이지, index 단일, CLAUDE.md 548줄 | praneybehl 플러그인, ETH Zurich 논문(2602.11988), Claude Code memory 문서 |
| **임베딩·벡터 검색은 10만 토큰 전까지 불필요** | 없음 (맞는 선택) | theaioperator, Astro-Han |
| **손익분기 경고**: 760페이지 운영자 "유지보수 시간 ≈ 절약 시간" | 5월 이후 유지보수 0 → 감가상각 중 | R&D World |

### 5-2. Claude Code 기능 중 바로 쓸 것

- **Hooks**: `PreToolUse`로 `raw/**` 편집을 deny(bypass 모드에서도 강제), `PostToolUse(Edit|Write)`로 `wiki/**` 저장 직후 lint 실행, `Stop` 훅으로 lint 실패 시 세션 종료 차단. agent 타입 훅(서브에이전트가 파일을 읽고 판정)으로 "이 ingest가 raw 인용을 실제로 갖췄는가" 게이트 가능.
- **Skills**: `.claude/commands`는 계속 동작하지만 skills만 스크립트 동봉·`context: fork`·`allowed-tools`·`` !`cmd` `` 주입이 된다. `/hr-lint`가 `!python scripts/lint.py`로 결정론적 결과를 프롬프트에 넣고 LLM은 해석만 하게 만들 수 있다.
- **서브에이전트**: `.claude/agents/hr-verifier.md`에 `tools: Read, Grep, Glob, WebFetch`, 다른 `model`, `memory: project`로 fact-checker 정의. 5월 PwC fact-check가 했던 일을 정식 역할로.
- **스케줄**: 로컬 vault라 Cloud Routine(GitHub clone 기반)은 repo를 GitHub에서 직접 운영할 때만 가능. 현실적으로는 Desktop scheduled task(1분 간격 가능, PC 켜져 있어야, worktree 격리) 또는 Windows 작업 스케줄러 + `claude -p`. GitHub private repo가 이미 있으니 Cloud Routine으로 주간 lint+digest를 `claude/` 브랜치에 push하는 방식도 가능.
- **`claude plugin eval`**(9월): 골든 Q&A 30~50개로 CLAUDE.md·모델 변경 시 회귀 평가. 무료 grader(`regex`, `file_exists`, `tool_used`) 위주.
- **`.claude/rules/*.md` + `paths:`**: 548줄 CLAUDE.md를 200줄 이하 핵심 규칙 + `rules/usecases.md`(paths: wiki/usecases/**) + `rules/sources.md`로 분할.

### 5-3. HR AI 벤치마크 피더·택소노미

- **SHRM State of AI in HR 2026**(2026-04, n≈1,908): 6 practice area × top 20 use case, 채택률 수치 공개. 우리 taxonomy와 crosswalk 만들면 "시장 대비 우리 커버리지"를 말할 수 있는 유일한 공개 기준선.
- **Josh Bersin HR 2030 / Superagent 6 family**(2026-01·04): 카테고리 수준만 공개, 100+ use case 목록은 Galileo 유료. 자동 피더 불가, 분류 축 정렬용.
- **Gartner Hype Cycle for AI in HR 2026**(doc 8074065): 유료. 보도자료만.
- **AIHR 2026 가이드**: AI 유형 7종(Generative/Conversational/Voice/ML/NLP/Automation/Agents) × 라이프사이클 9영역 — 우리 5×13 축과 crosswalk 가능.
- **규제 축**: 한국 AI기본법 시행령 2026-07-21 개정, 고영향 AI 판단 가이드라인(2026-04-29)이 "인사권자 개입 없는 채용 AI"를 예시로 명시. EU AI Act Annex III(고용) 의무는 Digital Omnibus로 **2027-12-02**로 연기. `regulatory_exposure: [kr-high-impact, eu-annex-iii]` 필드로 넣을 가치가 있다.
- **Google Open Knowledge Format v0.2**(2026-06): 마크다운+YAML 지식 번들 표준. `sources`·주장별 각주·`generated/verified/stale_after` 필드 관례를 그대로 차용하면 이식성 확보.

## 6. 우선순위 로드맵

"효과(신뢰) → 효율(자동화) → 효용(범위 확장)" 순서. 신뢰가 회복되기 전에 범위를 늘리면 A-1이 반복된다.

### Phase 0 — 지금 당장 (반나절, 파괴적 변경 없음)
| # | 작업 | 해결하는 문제 |
|---|---|---|
| 0-1 | `visibility: internal` frontmatter를 PwC 관련 4개 페이지에 붙이고 extract_v3에서 제외. raw/etc jpg는 `raw/internal/`로 이동 | A-6 기밀 노출 |
| 0-2 | 점검 스크립트를 `scripts/lint.py`로 정식화(이 리포트 §1 표를 그대로 출력) + `--json` | A-2 |
| 0-3 | `last_confirmed: 2025` 23건을 실제 날짜로 정정(소스 발행일 기준), 중복 3쌍 병합 | B-2, B-3 |
| 0-4 | 죽은 스크립트 10개 `scripts/archive/`로, `무제.canvas`·`wikilink.md`·`_data.js` 삭제 | C-1, C-3 |
| 0-5 | index·guide·company·vendor의 손글씨 카운트를 Dataview/스크립트 생성으로 교체 | B-4 |

### Phase 1 — 신뢰 회복 (1~2주, 스키마 변경)
| # | 작업 | 해결하는 문제 |
|---|---|---|
| 1-1 | **Grounding Invariant** 도입: use case의 수치·시스템명·인용은 `[[sources/x]]` + 원문 verbatim 인용을 같이 적는다. `scripts/check_quotes.py`가 raw 파일과 글자 대조 | A-1, B-1 |
| 1-2 | compilation source 4개를 개별 source 페이지(기사 1건 = 1페이지)로 분해하고, 각 기사 본문을 `raw/articles/`에 스냅샷 + 콘텐츠 해시 | A-1 |
| 1-3 | dangling `sources` 187건: URL 문자열 → source 페이지 생성 또는 삭제. 생성 불가하면 해당 주장을 `미공개`로 강등 | A-1 |
| 1-4 | confidence 재설계: `evidence_grade: A(독립 2+)/B(독립 1)/C(벤더·자사만)/D(미검증)` + `corroborated_by: N` + `superseded_by`. 기존 float는 스크립트가 계산해 `confidence_calc`로만 유지 | A-4 |
| 1-5 | hedging 보존 규칙과 "부재 주장 전 grep 필수" 규칙을 CLAUDE.md에 추가. 우리은행형 위반 페이지를 lint가 "B/C/D에 인용 0개인데 미공개 표기도 0개"로 탐지 | B-1 |
| 1-6 | 템플릿 미달 30~40건 `stage: stub` 강등 (자동 판정, 사람 승인) | B-2 |
| 1-7 | hooks: `PreToolUse` raw/ 쓰기 deny, `PostToolUse` wiki/ 쓰기 후 `lint.py --quick`, `Stop` 훅 게이트 | A-2 |

### Phase 2 — 자동 운영 (2~4주)
| # | 작업 |
|---|---|
| 2-1 | `raw/inbox/` + Obsidian Web Clipper 템플릿(소스 유형별 frontmatter) → `/hr-ingest raw/inbox` 가 triage(New/Update/Disputed/No material) 결과를 log에 기록 |
| 2-2 | 주간 cadence: Desktop scheduled task 또는 Cloud Routine(GitHub repo 기준)으로 `lint → digest → export 재빌드`. 자동 수정은 하지 않고 PR/리포트만 |
| 2-3 | `.claude/agents/hr-verifier.md` fact-checker 서브에이전트 + `/hr-verify <claim>` 스킬 (PwC 자료 검증에서 증명된 가치를 상품화) |
| 2-4 | `/hr-research <topic>` 정식 프로토콜: 산출은 후보 목록 + raw 스냅샷까지. use case 생성은 반드시 ingest 경로 |
| 2-5 | 골든 Q&A 30개 + `claude plugin eval` 회귀 세트. CLAUDE.md를 200줄 이하로 다이어트하고 `.claude/rules/`로 분할한 뒤 eval로 회귀 확인 |
| 2-6 | 스킬 이전: commands → skills (`!python scripts/lint.py` 주입, `context: fork`) |

### Phase 3 — 가치 확장 (그 이후)
| # | 작업 |
|---|---|
| 3-1 | 페이지 유형 분리: `products/`(벤더 제품), `regulations/`, `reports/`, `enterprise-ai-context/`(전사 GenAI). use case 카운트는 "HR 프로세스가 바뀐 도입 사례"만 |
| 3-2 | taxonomy crosswalk 페이지: 우리 7×26 ↔ SHRM 6 ↔ Bersin 6 ↔ AIHR 9, AI 유형 5×13 ↔ AIHR 7. "시장 대비 커버리지" 대시보드 |
| 3-3 | `kr_applicability`(법규·노조·언어·국내 벤더 지원 4필드) + `regulatory_exposure` 축 → Excel 필터·HTML 칩 |
| 3-4 | index 샤딩(카테고리별 index) + 페이지 상한 규칙 + compaction |
| 3-5 | MCP로 wiki 노출(검증된 인용 read path) — 다른 프로젝트 세션·제안서 작성 세션에서 재사용. 임베딩은 10만 토큰 넘기 전까지 보류 |
| 3-6 | Dataview → Obsidian Bases 이전 검토(Dataview는 Datacore로 대체 예정) |

### 하지 말 것
- 감쇠 곡선·4단 메모리·벡터 DB 같은 "v2" 기능: 수백 페이지 이하에서 효과 미입증.
- LLM lint 자동 수정: 모든 운영 회고가 반대. 보고 → 사람 승인 → 적용.
- 신뢰가 회복되기 전 대량 리서치 라운드 재개: 지금 방식으론 use case 1건당 근거 없는 주장이 같이 늘어난다.

## 7. 실행 결과 (2026-09-27 당일, Phase 0~3 일괄 실행)

사용자 승인 후 로드맵 전체를 실행했다. 커밋: `4e6a8d3`(Phase 0~1 스키마·스크립트), `4ed9bba`(소스 재구축), 이후 grounding 정리 커밋.

| 지표 | 점검 시 (§1) | 실행 후 |
|---|---|---|
| use case (HR 사례) | 140 | **118** (enterprise-ai 15 · reference 4 분리, 중복 3 병합) |
| source 페이지 / raw 스냅샷 연결 | 62 / 13 | **300 / 300** (unavailable ~30건은 헤더만) |
| `sources` 항목 중 source 페이지로 안 이어지는 것 | 187 | **0** (8건은 `sources_unresolved`에 보존) |
| Solution Architecture 인용 0개 페이지 | 110 | 0 (B·C·D 미인용 bullet은 `_미공개_`로) |
| 본문 수치 중 raw에서 미확인 | 측정 불가 | **0 / 463** (check_quotes) |
| confidence 공식 불일치 | 101 | 0 (grade.py가 계산) |
| 깨진 wikilink / orphan | 299 / 29 | **0 / 0** |
| 금지어 페이지 | 62 | 0 |
| 필수 섹션 누락 | Contradictions 95 등 | 0 |
| lint critical / warning / info | 960 / 522 / 171 | **0 / 101 / 77** (warning = stale 50 + 추정 날짜 50 + contradiction 1) |
| evidence_grade | 없음 | A 49 · B 34 · C 45 · D 5 |
| depth | 없음 | full 18 · partial 86 · stub 29 |
| 골든 Q&A (오프라인) | 없음 | 30/30 |
| 기밀 페이지 export 노출 | 3 | 0 (`visibility: internal` 2건 제외, 이중 가드) |

**정직하게 짚을 것 — 겉보기 정보량은 줄었다.** Grounding 규칙을 적용하자 120여 페이지에서 소스에 없던 수치·시스템명이 `_미공개_`로 내려갔고, 근거 없는 노드를 뺀 Mermaid 도식이 줄어 `depth: full`이 42→18로 감소했다. 특히 원문이 초록·마케팅 페이지뿐인 사례(J&J MIT CISR, flex, Fuel50 Lennox, Diligent, HireVue, Emirates, Docebo, 삼성 멀티캠퍼스, IBM Watson Recruitment)는 사실상 stub이 됐다. 이것이 5월 상태의 실제 근거 수준이며, 복구 경로는 `/hr-research`로 1차 소스(케이스 스터디 원문·논문 본문)를 확보하는 것이다.

**미완·사용자 판단 필요**
- 주간 자동 작업(`scripts/register_weekly_task.ps1`) 등록 — 무인 `claude -p` 호출 비용이 발생하므로 사용자 확인 후.
- `sk-hynix-ask-ai-interview` 등에 PwC 제안 프로세스 서술이 `미인용` 표기로 남아 있음 — `visibility: internal`로 돌릴지 결정.
- snapshot_quality `unavailable` 소스 ~30건(Cloudflare 403·paywall·gated) — 대체 URL·Wayback 확보 시 재점검.
- `sources_unresolved` 8건, `date-estimated` 50건 — 소스 발행일 확인 후 정정.
- 미해결 contradiction 1건(삼성 멀티캠퍼스 — 단일 소스가 사례와 무관).
