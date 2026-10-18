---
type: method-review
generated_at: 2026-10-19
scope: 현재 리서치·검증 파이프라인이 2026-10 기준 최선인지 재검토 (딥리서치 에이전트 · 인용 추출 API · 소스 수집 도구 · 검색 API · KB 컨테이너 · 출처 모델 · 검증/eval · 신선도 · 소싱 피드)
method: 리서치 서브에이전트 9개 (1차 출처 fetch + 라이브 테스트) + 자체 테스트 (Jina Reader·Wayback)
tags: [review, method, research-pipeline, llm-wiki]
---

# 리서치 방법 재검토 (2026-10-19)

## 0. 결론

**골격은 최선에 가깝다. 바꿀 것은 골격이 아니라 다섯 가지 부품이다.**

| 판정 | 항목 |
|---|---|
| **유지** | 마크다운 위키 + raw 스냅샷 + 결정론적 lint·grade·grounding, 근거 등급 A~D, skills/hooks, MCP, "LLM은 판단만·스크립트가 숫자" 원칙 |
| **바꿀 것** | ① 소스 획득 체인(Jina Reader·Wayback 폴백, HR Executive 추출기), ② 한국 소싱(Naver API + Google News KR RSS), ③ 인용 저장 방식(문장 단위 오프셋·raw 해시), ④ 회귀 평가(30문항 regex → 사실 목록 150문항 + 기권·한정어 계층), ⑤ 신선도 모델(bitemporal 필드 + stale_after) |
| **추가** | 주 1회 피더 파이프라인(15 피드 → 프리필터 → LLM 점수 → inbox), 파생 SQLite 인덱스, 클레임 stance(supports/disputes) |
| **하지 말 것** | 딥리서치 에이전트 결과를 source로 ingest, GraphRAG/지식그래프 이전, Notion/Airtable 이전, 12ft류 우회 도구·스텔스 브라우저, 벡터 검색 도입 |

## 1. 딥리서치 에이전트 (Claude Research · OpenAI Deep Research · Gemini DR · Perplexity)

- **소스가 아니라 검색 보조로만 쓴다.** 어느 제품도 "원문의 verbatim 인용"을 돌려주지 않는다. OpenAI·Gemini·Vertex의 `start/end_index`는 **생성된 답변 텍스트** 안의 위치이고, Perplexity는 검색 스니펫, Anthropic `web_search`의 `cited_text`는 150자 조각이다. [검증됨: 각 API 레퍼런스]
- 인용 신뢰도: Penn 2026(arXiv 2604.03173, 53,090 URL) — 인용 URL의 3~13%가 **Wayback에도 없는 허위**, 5~18%가 비해석. DeepResearch Bench(ICLR 2026) 인용 정확도 78~94%. Tow Center 2025: 8개 도구 60%+ 오답. [검증됨]
- OpenAI `o3/o4-mini-deep-research`는 2026-07-23 종료, `gpt-5.6-sol`로 대체. Gemini DR은 작업당 $1~7. Perplexity Sonar chat은 2026-09-27 종료(Agent API로). [검증됨]
- **우리 규칙("모든 수치는 우리가 받은 raw에 verbatim")과 양립하는 유일한 사용법**: 에이전트 → URL 수확 → 생존 확인 → 우리가 fetch → 우리가 인용. 에이전트 보고서는 리드로만 저장. 이것이 바로 `/hr-research`의 설계이므로 유지.

## 2. 인용 추출 API

- **Anthropic Citations API만 원문 측 오프셋**(`char_location` start/end, `cited_text` 서버 추출·토큰 무과금)을 준다. 단 최소 단위가 **문장**(숫자 하나만 인용 불가), structured outputs와 병용 불가(400), 한국어 인덱스 단위(코드포인트 vs UTF-16) 미문서화. [검증됨]
- OpenAI는 원문 오프셋 없음, Gemini는 출력 측 바이트 오프셋만. [검증됨]
- 오픈소스: Google **LangExtract**(Apache-2.0, 추출마다 `char_interval`), **llmground**(추출값↔원문 grounded/weak/ungrounded 판정, 숫자·통화·날짜 정규화). [검증됨 페이지]
- **적용**: ingest 단계에서 raw를 Citations API에 `document`로 넘겨 claim마다 `cited_text`+오프셋을 받고, `check_quotes.py`가 `raw[start:end]==cited_text and 숫자 in cited_text`를 검사하도록 바꾸면 현재의 "숫자 토큰 존재" 검사보다 **문맥 일치**까지 확인된다. 비용은 입력 토큰만.

## 3. 소스 획득 (현재 unavailable 35건의 원인별 해법)

라이브 테스트(2026-10-19, 한국에서):

| 대상 | requests | Jina Reader(r.jina.ai, 키 없음) | Wayback | 비고 |
|---|---|---|---|---|
| HR Brew | 403 Cloudflare | **200 전문** | 저장 가능(SPN) | 피드 `/feed.xml`도 Jina 경유 가능 |
| HR Executive | **200** (본문 HTML에 있음) | 200 전문 | 빈 셸 | **차단 아님 — trafilatura 추출 실패**. `<article>`/JSON-LD 파싱으로 해결 |
| Business Wire | 403 Akamai | **200 전문**(최신 URL) / 구 URL은 "Page Unavailable" | 없음 | `feed.businesswire.com` RSS 생존, Yahoo Finance 미러에 전문 |
| Bloomberg | 403 | 403 (Jina가 도메인 차단) | **`id_` 원문 스냅샷 전문**, archive.ph도 전문 | 유료 구독 + Claude in Chrome이 ToS상 깨끗한 경로 |

- 추천 체인: `requests` → **Jina Reader(키 발급, 500 RPM)** → Firecrawl `auto`(무료 1,000) → Wayback `id_` / SPN → archive.ph(수동). Jina ToS: "방어 수단을 적극 우회하지 않음, 사이트 약관 준수는 사용자 책임". [검증됨]
- 12ft.io는 2025-07 폐쇄(News/Media Alliance), Google·Bing 캐시 폐지. 스텔스 브라우저(nodriver 등)는 명백한 우회 도구 → 쓰지 않는다.
- 게이트 PDF(Gloat 케이스 스터디 등)는 실명으로 폼 제출이 유일한 깨끗한 경로.
- **기대 효과**: 35건 중 HR Brew 3·HR Executive 3·Business Wire 6·Bloomberg 1 = **13건 즉시 복구 가능**, 게이트 4건은 폼 제출, 삭제 페이지 5건은 Wayback 시도.

## 4. 검색 API

- Claude Code `WebSearch`는 Brave 백엔드 추정(서브프로세서 공개, 인용 79% 일치)이며 **한국어 리콜은 Brave 수준**. 한국어 자연어 질의는 리콜이 나쁘고 키워드+`site:`가 낫다는 2026 개발 로그 존재. [2차]
- **한국 언론은 Naver 검색 API**(뉴스 `display 100`·`start 1000`·`sort=date`, 일 25,000건, 무료)가 모든 서양 인덱스를 이긴다. 날짜 필터가 없어 `pubDate`로 페이징 중단. [검증됨 파라미터]
- 벤더 사례연구: Exa `category:"company"` + `includeDomains`($7/1k), Perplexity Search API($5/1k, fast $1/1k). 벤치마크(Artificial Analysis 2026-09, BrowseComp)에서 Perplexity ≥ Parallel ≥ Exa ≥ Brave > Tavily. 전부 벤더 주도 평가라 B2B 니치 리콜 증거는 없음. [검증됨/2차]
- Google CSE JSON API는 신규 고객 종료(기존 2027-01-01까지), Bing Search API 2025-08 종료 → Google SERP는 Serper/SerpApi(SerpApi는 Naver 엔진도 제공).
- 월 2,000쿼리 예산: Anthropic $20 · Exa $14 · Brave $10 · Perplexity $10 · Naver $0.

## 5. 지식베이스 컨테이너

- Karpathy 원문이 "~100 소스, 수백 페이지" 규모를 명시; 커뮤니티 비판의 처방(결정적 도구 분리, 모순/신선도 검사, index 샤딩)은 이미 반영돼 있음.
- **GraphRAG는 maintenance mode**(MS), LightRAG는 "프로덕션 비권장" 기본 저장소, Kuzu는 2025-10 아카이브(LadybugDB 포크). 2026-10 비용 분석: 인덱싱 벡터 $1.4 vs LightRAG $330 vs GraphRAG $430(10M 토큰). arXiv 2609.18099: 그래프는 위치 찾기에만 쓰고 원문으로 답하는 편이 57% 저렴. **→ 500페이지·단일 유지자에는 비권장.** [검증됨]
- Notion/Airtable: raw 스냅샷·링크 그래프가 속성으로 환원되지 않고 API 버전 종속, PwC 자료 클라우드 저장 리스크 → 비권장.
- **Obsidian Bases**: 1.14(2026-09) Kanban·그룹 접기, **CLI `base:query --format json|csv`**(1.12.7+)로 에이전트가 질의 가능. Dataview 대체 공식 언급 없음, Datacore는 beta. → 보조 뷰로 채택(이미 `wiki/bases/usecases.base` 있음).
- **추가 권장**: frontmatter+링크를 **파생 SQLite(FTS5) 인덱스**로 빌드해 산업×카테고리×등급 교차집계·Excel 생성·MCP `query_sql`에 쓴다. 진실 공급원은 마크다운+raw 유지.

## 6. 클레임 출처 모델 — 우리 체인에 없는 것

Elicit·Scite·ClaimReview·PROV-O·Nanopub·Wikidata·KeyCite 비교 결과, 우리 use case → source → raw 체인에 부족한 10가지:
1. raw 내 **문자 오프셋** (Anthropic `start_char_index`, Scite 섹션 위치) — 현재는 숫자 존재만 확인
2. **인용문·raw 해시** (Nanopub Trusty URI, C2PA 하드 바인딩) — `content_hash`는 있으나 인용문별 바인딩 없음
3. **stance** (CiTO supports/disputes, Scite contrasting) — 반박·수정 출처 구분 없음
4. 안정적 **클레임 ID** — 등급 재계산 이력 추적 불가
5. 검증자·검증 시각 (PROV `wasAttributedTo`/`generatedAtTime`)
6. 랭크/폐기 상태+사유 (Wikidata deprecated + P2241, SNOMED REPLACED_BY) — `superseded_by` 필드 없음
7. 시효 (ClaimReview `expires`, Wikipedia `{{As of}}`) — `stale_after` 없음
8. "분석 전" 플래그 (KeyCite 노랑) — 자동 추출·미검토 상태 구분 없음
9. 정정 이력 불변성 — 덮어쓰기 대신 별도 정정 레코드(Crossmark `updated_by`)
10. 추출 비결정성 기록 — Elicit 독립 평가에서 값 일치 90%지만 **인용문 일치 46%** → 추출 모델·프롬프트·날짜 저장 필요
→ 1·2·6·7은 frontmatter 필드 추가로 해결, 3·5·8·9는 운영 규칙, 4·10은 선택.

## 7. 검증·eval

- **다른 계열 모델로 채점**: DeepMind FACTS Grounding이 Gemini·GPT·Claude 3판정자를 쓴 이유 = 자기선호 편향(+3.23%, 2차). Anthropic docs도 "생성 모델과 다른 모델로 평가" 권고. 단 GPT/Claude/Gemini 상호검토가 자기검토보다 낫다는 **독립 2026 연구는 없음**. [검증됨/추정]
- **한정어 소실은 실측됨**: Peters & Chin-Yee 2025 — LLM 요약 26~73%가 원문보다 넓게 일반화, OR 4.85, 신형 모델이 더 나쁨, "정확히 하라" 프롬프트는 무효. → 우리 hedging 보존 규칙은 맞지만 **검사 계층이 없다**.
- **30문항 regex의 검출력**: 변경이 사실의 5%를 깨면 78% 탐지, 2%면 45%, 1%면 26%. Anthropic "Adding Error Bars"(arXiv 2411.00640): 3%p 차이 검출에 ~969문항. → 30문항은 스모크 테스트로만.
- **권장 계층**: L0 lint/grounding(커밋마다) · L1 30문항 완화(contains-any) · **L2 120~150문항, WikiBench식 JSON 사실 목록(2~4개)+`source_page`, 다른 계열 모델 이진 채점+Unknown 허용, 2회 시행** · L3 기권 20~25문항(UAEval4RAG식 "위키에 없는 것"→"자료 없음") · L4 한정어 보존 15~20문항 · L5 인용 링크 실재 · L6 분기 변이 테스트(수치·한정어 훼손 후 L2~L4가 잡는지). 판정자 검증용 Pass 30/Fail 30 수동 라벨. 예상 비용 월 수 달러.
- OpenAI Evals 플랫폼 2026-11-30 종료 → 의존 금지. promptfoo/Inspect AI는 결정적+LLM 혼합 가능.

## 8. 신선도·변경 탐지

- **Bitemporal**(Graphiti `valid_at/invalid_at/created_at/expired_at`, MemStrata): 사실의 세계 시간과 시스템 인지 시간 분리, 모순 시 삭제 대신 `expired_at`. MemStrata: 일반 RAG는 구버전 사실을 15~40% 서빙, 코사인 유사도는 모순·중복 구분 AUROC 0.59 → 결정적 (주어,속성) 키 대체 규칙 필요. [검증됨]
- 권장 필드: `claim_type`, `valid_from`, `valid_to`, `observed_at`, `last_verified`, `stale_after`, `superseded_by`, `status: current|superseded|retracted|unreachable`, `source_hash`, `wayback_url`.
- 재검증 주기(제안): 벤더 가격 분기 · 벤더 기능 릴리스 직후(Workday 3/9월, SAP 5/11월, ServiceNow 반기) · 사례 메트릭 반기+뉴스 트리거(Klarna 반전형) · 규제 이벤트 · 조직 사실 연 1회.
- 변경 탐지: **changedetection.io 셀프호스트**(CSS/XPath 본문만, Ignore text, RSS 출력) 또는 Firecrawl Change Tracking(`changeStatus`·`visibility: hidden`으로 조용한 삭제 탐지, 5크레딧/페이지). sitemap `lastmod`는 신뢰 불가(Google도). Google Alerts 누락 다수. Wayback Availability API로 과거 증거 보강.

## 9. 소싱 피드 (주 1회 라이트 파이프라인)

- 피드 가용성 라이브 확인: **있음** — HR Dive, HR Grapevine, Personnel Today, HR Tech Feed, Josh Bersin(카테고리 피드), AIHR, Recruiting Brainfood, McKinsey Insights, SAP News, Workday Newsroom, ADP, UKG, Eightfold, Visier, Gloat(blog/feed), Docebo, 고용노동부(정책·공지). **없음** — HR Executive(Google News `site:` RSS로 대체), HR Brew(이메일만), Unleash(사례 sitemap 감시), SHRM(이메일), People Matters(깨짐), Oracle(사망), ServiceNow(차단), HireVue·Phenom·Paradox·Lattice·Culture Amp·Qualtrics·Beamery·Degreed·Paychex(없음), 한경 CHO Insight(수요일 뉴스레터), HR Insight(월간 목차 수동), korea.kr RSS 2026-07 중단.
- **한국 핵심**: Google News KR RSS `인사 AI 도입 when:7d`(주 69건), 그룹사 쿼리(주 50~70건, 중복 많음), Naver 뉴스 API. 반복 매체: 연합·매경·한경 CHO Insight·월간노동법률·헬로티·지디넷·바이라인·디지털투데이.
- 15피드 원시 볼륨 ~400건/주 → 키워드 프리필터 60~80 → Haiku급 점수 8~12 후보 → **등재급 신규 사례 주 2~4건**(추정). 구축 1일, 운영 월 $3~5, 검토 주 30분. 실무 근거: r/claudexplorers 파이프라인("The filter is the product"), arXiv 2509.25491(편집 판단은 사람 하이브리드).
- 분기 수동: Brandon Hall winners, Lighthouse, HR Executive Top Products, Forrester TEI(`tei.forrester.com/go/<vendor>`), Unleash sitemap, Workday Rising 온디맨드, HR Insight 목차, 흐레카·하이파이브 후기, 인사혁신처 보도자료, 미 연방 AI 인벤토리 CSV(1회).
- 건너뛸 것: EU AI Act Art.71 DB(2027-12-02까지 데이터 없음), SSRN, HBS, "Josh Bersin Best Of"(미존재), 삼성SDS·LG CNS·SK AX 뉴스룸(HR 사례 희소).

## 10. 실행 순서 제안 (승인 시)

| 순서 | 작업 | 효과 | 비용 |
|---|---|---|---|
| 1 | `fetch_raw.py` 폴백 체인(Jina 키 → Firecrawl → Wayback `id_`), HR Executive 전용 추출(`<article>`/JSON-LD) | unavailable 35 → ~20 | 반나절, Jina 무료~$50 |
| 2 | Naver 뉴스 API + Google News KR RSS를 `/hr-research` 기본 검색원으로 | 한국 사례 리콜 | 반나절, $0 |
| 3 | 주 1회 피더(feedparser → SQLite dedupe → 키워드 → Haiku 점수 → `raw/inbox`) | 월 1,500건을 주 10건으로 | 1일, 월 $5 |
| 4 | 신선도 필드(`valid_from/valid_to/last_verified/stale_after/superseded_by/status/source_hash`) + grade.py 반영 + changedetection.io | 조용한 메트릭 부패 탐지 | 1일 |
| 5 | Citations API 기반 인용 오프셋 저장 + check_quotes 문맥 일치 검사 | 숫자 존재 → 문장 일치 | 1일, 입력 토큰만 |
| 6 | eval 계층 L2~L5(150문항 사실 목록, 기권, 한정어, 다른 계열 채점) | 1~2% 국소 회귀 탐지 | 2일, 월 수 달러 |
| 7 | 파생 SQLite 인덱스 + MCP `query_sql` + Bases CLI | 교차집계·납품 자동화 | 1일 |

## 11. 검증하지 못한 것
- Bloomberg를 Jina 유료 키로 받을 수 있는지(익명만 차단 확인), Gartner Newsroom RSS가 리더기에서 작동하는지, Bases ~1k 노트 실측 성능, FACTS +3.23%·UAEval4RAG 수치의 논문 본문, 원티드 인살롱·더플랩 접속, Casey Newton 2026-08 운영 수치.
