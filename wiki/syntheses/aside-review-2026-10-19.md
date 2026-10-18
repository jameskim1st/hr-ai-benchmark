---
type: tool-review
generated_at: 2026-10-19
topic: Aside (aside.com) 에이전트 브라우저 — 우리 리서치 파이프라인과의 접목 검토
sources_checked: [https://aside.com/, https://aside.com/pricing, https://aside.com/policy/terms, https://aside.com/features/browser-agent, https://aside.com/blog/how-we-built-the-sota-browser-agent-that-outperforms-fable, https://aside.com/blog/developers, https://docs.aside.com/help/developers, https://docs.aside.com/changelog/components, https://www.eesel.ai/blog/aside-ai-browser-review, https://runtimewire.com/article/aside-ai-browser-launches-windows-app, https://vibecoding.tech/news/2026/09/27/aside-browser-mcp-agents, https://en.stackfinch.com/2026/09/aside-browser-guide-setup-pricing.html, https://github.com/Yeachan-Heo/gajae-code/blob/main/docs/aside-integration.md]
tags: [review, tooling, browser-agent, source-acquisition]
---

# Aside 검토 — 무엇이고, 우리 시스템에 어떻게 붙이나 (2026-10-19)

## 0. 한 줄 판정

**좁게 쓰면 가치가 있다.** 우리 파이프라인의 가장 큰 구멍인 "로그인·구독이 필요한 페이지의 원문 확보"를 ToS를 지키면서 메울 수 있는 도구이고, Claude Code에 MCP로 바로 붙는다. 다만 출시 4개월 된 제품이라 **본문 추출은 결정론적 REPL로, 에이전트 모드는 리서치 보조로만** 쓰는 것이 맞다. 벤치마크 수치는 전부 자사 보고라 근거로 삼지 않는다.

## 1. Aside가 무엇인가 (확인된 사실)

| 항목 | 내용 | 근거 |
|---|---|---|
| 정체 | Aside Computer Inc.(YC F25)의 **에이전트 내장 Chromium 브라우저**. 창업자 Jun Kim·Chanhee Lee·Sanghun Lee | aside.com, runtimewire 2026-09-14 |
| 출시 | macOS 2026-06-23, **Windows 2026-09-14** (공개 다운로드, Win 10 22H2+/11) | runtimewire, stackfinch, download 페이지 |
| 핵심 방식 | 사용자가 **이미 로그인한 사이트** 안에서 에이전트가 읽고 클릭한다. API 통합 없음. 페이지 인식은 수정된 접근성 트리(ref id), 스크린샷은 폴백. "Asidewright"라는 Playwright 호환 CDP 래퍼로 JS를 써서 조작 | 기술 블로그 2026-06-25 |
| 백그라운드 | Blink 패치로 에이전트 탭이 포커스를 뺏지 않음(1440×900 고정). "Agent Tabs" 사이드바 | 기술 블로그, vibecoding |
| 개발자 인터페이스 | `aside "<task>"`(에이전트 작업), `aside exec -m <model> "<prompt>"`, `aside --session <id>`, **`aside repl "<js>"`**(Playwright식 `page`·탭·locator·스크린샷·다운로드·JS, 결정론적), **`aside mcp`**(MCP 서버, mcp.json에 `command: aside, args: [mcp]`), `aside skills list/show/install`, `aside login` | docs.aside.com/help/developers, changelog |
| Windows CLI | `https://releases.aside.com/install.ps1` 서명 설치 스크립트, Settings > Developers에서도 설치 | docs |
| 자동화 | Routines: **Cron**(새 작업) / **Heartbeat**(기존 대화 계속) / 이벤트 트리거, 월간·복수 시각 지원 | changelog 5~9월 |
| 원격 | Channels(Slack·Telegram 원격 제어, Pro) | changelog 8월 |
| 모델 | 자체 내장 모델(크레딧 소모) 또는 **BYO: ChatGPT/Claude 구독 OAuth, 또는 API 키** | pricing, docs |
| 가격 | Free $0: 500 크레딧/월, routine 3개, BYO, 비밀번호 관리자, 메모리 · Pro $20: 3배, Ultrabrowse(딥리서치), routine 무제한, Channels, 클라우드 핸드오프 · Max $200: 40배 | aside.com/pricing |
| 프라이버시 | 로컬 우선. 작업 기록·메모리(마크다운)·데이터는 기기에. 모델 제공자에는 작업 컨텍스트만, 가능하면 ZDR·no-training 설정 | ToS §5·§6, eesel 리뷰 |
| 자격증명 | Vault가 자동 입력, 모델은 비밀번호를 못 봄. MFA·CAPTCHA·passkey는 사람이. **기본값 "Always allow"** → "While unlocked"로 바꿀 것 | vibecoding 2026-09-27 |
| 약관 | 스크래핑·페이월 조항 없음. §7 "access controls… bypass" 금지, §5·§8 **제3자 약관 준수는 사용자 책임**. 프롬프트 인젝션 경고(§5·§15) | aside.com/policy/terms |
| 벤치마크 | Online-Mind2Web 99.0%(297/300), BU-Bench 93%, Odyssey 1위 — **자사 실행·자사 채점**. 독립 검증 없음 | /sota, eesel |
| 미문서화 | **MCP 툴 이름·반환 형식**(텍스트/마크다운/스크린샷), REPL stdout 형식, 크레딧 소모 기준, Linux | docs에 없음 |

## 2. 우리 파이프라인의 어디에 붙는가

```
                     현재                                      Aside 접목
① 수집   WebSearch(Brave) / Google News RSS          + aside routine: 로그인 필요 소스(HR Brew 뉴스레터, 한경 CHO Insight) 주간 스윕 → raw/inbox
② 스냅샷  requests→trafilatura (→ Jina → Wayback 예정)  + 폴백 #3: `aside repl`로 로그인 세션에서 본문 추출 → raw/*.md (snapshot_quality: browser)
③ source  LLM이 Key Quotes 작성                        변화 없음 (raw가 있으면 동일)
④ usecase /hr-ingest                                    변화 없음
⑤ 검증   hr-verifier: Read/Grep/WebFetch               + `aside mcp`로 원문 페이지를 직접 열어 인용 대조 (WebFetch의 손실 추출 대체)
⑥ 산출물  build_all                                     변화 없음
```

### 2-1. 가장 큰 가치: 막힌 소스 13~20건의 원문 확보 (ToS 준수)

- 2026-10-19 테스트에서 HR Brew·Business Wire는 Jina Reader로, Bloomberg는 Wayback으로 받아진다. 그러나 **Jina는 Bloomberg를 도메인 차단**하고, 게이트 PDF(Gloat 케이스 스터디)·구독 매체(HR Executive 일부, 한경 CHO Insight 뉴스레터)·로그인 커뮤니티(원티드 인살롱 등)는 어떤 프록시로도 안 된다.
- Aside는 **사용자 본인의 로그인 세션**으로 읽으므로 ToS상 가장 깨끗하다(제3자 약관 준수 책임이 사용자에게 있고, 본인 구독 콘텐츠 열람은 그 범위 안). 12ft류·스텔스 브라우저와 성격이 다르다.
- 핵심은 **에이전트가 아니라 REPL**을 쓰는 것: `aside repl "const p = await openTab(url); …document.body.innerText…"`처럼 결정론적으로 본문을 뽑으면 (a) 페이지 안의 프롬프트 인젝션이 모델에 닿지 않고 (b) 크레딧이 거의 들지 않으며 (c) 결과가 재현된다. 에이전트 모드로 "이 기사 요약해 줘"를 시키는 것은 우리 Grounding 원칙(요약 아닌 verbatim)과 맞지 않는다.

### 2-2. MCP로 Claude Code에 연결 — `/hr-research`·`/hr-verify`의 눈

- `.mcp.json`에 `aside` 서버를 추가하면 `/hr-research`가 로그인 필요한 사이트(벤더 고객 포털, 컨퍼런스 온디맨드, 게이트 PDF 폼)를 탐색할 수 있고, `hr-verifier`가 WebFetch 대신 실제 렌더된 페이지에서 인용문을 대조할 수 있다.
- 단 MCP 툴 목록·반환 형식이 문서화돼 있지 않다. 설치 후 `claude mcp add aside -- aside mcp` → 세션에서 툴 스키마를 확인해야 한다. changelog에 "긴 MCP 대화에서 스크린샷 축소"가 있어 **스크린샷 위주 반환**일 가능성이 있다. 텍스트 반환이 안 되면 REPL 경로만 쓴다.

### 2-3. Routines로 주간 피더 — 비용 문제의 우회로

- 사용자가 거부한 `weekly.ps1`의 이유는 무인 `claude -p` 비용이었다. Aside Routine은 **BYO Claude 구독**으로 돌면 추가 API 비용이 없고, Free 플랜에 routine 3개가 포함된다.
- 예: Cron routine "매주 월 09:00 — Google News KR `인사 AI 도입 when:7d`, HR Brew 뉴스레터(로그인), 한경 CHO Insight를 열어 지난 7일 신규 기사 목록(제목·URL·날짜·2줄 요약)을 `C:\AI\AI-HR\Benchmark\raw\inbox\weekly-YYYY-MM-DD.md`로 저장. 파일 쓰기 외 어떤 행동도 하지 말 것."
- 주의: 리뷰어들이 "Registration does not prove execution", "misleading completion messages"를 지적한다 → 첫 4주는 실행 결과를 사람이 확인하고, 이 routine은 **파일 쓰기만** 허용(Guard 모드, 도구 규칙 Deny).

### 2-4. 붙이지 말 것

- **내부 자료(PwC 제안서, `raw/internal`)**를 Aside 작업 컨텍스트에 넣지 않는다. 모델 제공자로 전송된다(ZDR이라도 정책상 금지).
- 에이전트 모드로 소스 **내용을 생성**시키지 않는다(요약·수치 추출). raw는 REPL 추출물만.
- Vault "Always allow" 기본값을 두고 쓰지 않는다. Benchmark 작업용 **별도 브라우저 프로필**(구독 매체 로그인만, 은행·메일 없음)을 만든다.
- 자사 벤치마크(99%)를 선택 근거로 쓰지 않는다. 우리 기준은 "13건이 실제로 받아지는가".

## 3. 대안과 비교

| 필요 | Jina Reader | Wayback | Playwright 지속 프로필(직접 작성) | Claude in Chrome | **Aside** |
|---|---|---|---|---|---|
| 로그인 없는 403 (HR Brew·BW) | ✅ 확인 | HR Brew ✅ | ✅ | ✅ | ✅ |
| 구독 페이월 (Bloomberg 등) | ❌ 도메인 차단 | ✅(스냅샷 있을 때) | ✅ 본인 로그인 | ✅ 본인 로그인 | ✅ 본인 로그인 |
| 게이트 PDF 폼 | ❌ | ❌ | 수동 코딩 | ✅ 승인 후 | ✅ 승인 후 |
| 결정론적 본문 추출 | ✅ | ✅ | ✅ | ❌(에이전트) | ✅ REPL |
| Claude Code 연결 | HTTP | HTTP | Bash | 이 세션엔 없음 | **MCP + CLI** |
| 주간 스케줄 | 외부 cron | — | 외부 cron | — | **내장 Routines** |
| 비용 | 무료~$50 | 무료 | 무료 | 유료 플랜 | Free 500크레딧 / BYO |
| 신규 제품 리스크 | 낮음 | 없음 | 없음 | 중 | **높음(4개월)** |

솔직한 평가: **"받아오기"만 놓고 보면 Playwright 지속 프로필 스크립트가 Aside REPL과 같은 일을 하고 리스크가 없다.** Aside의 고유 가치는 (1) MCP·CLI·Routines가 이미 묶여 있어 우리가 만들 것이 없다는 점, (2) 로그인 사이트의 다단계 탐색(폼 제출·포털 검색)을 에이전트가 해 준다는 점, (3) 한국 창업팀이라 한국 사이트 호환이 기대된다는 점(미검증)이다.

## 4. 접목 절차 (승인 시)

**Step 0 — 사용자가 할 일 (10분)**
1. aside.com/download → Windows 설치 → Benchmark 전용 프로필 생성, HR Brew(무료 계정)·HR Executive·구독 매체 로그인
2. Settings > Models > Providers에서 Claude 구독 연결(BYO). Settings > Passwords > Access policy를 "While unlocked"로
3. PowerShell: `irm https://releases.aside.com/install.ps1 | iex` → `aside login --email ...` → 앱에서 기기 승인 → `aside --version`

**Step 1 — 추출 검증 (내가, 30분)**
- `aside repl`로 막힌 URL 13건을 열어 `document.querySelector('article')?.innerText ?? document.body.innerText`를 stdout으로 받는지 확인. 형식이 확인되면 `scripts/fetch_via_aside.py` 작성: URL → REPL → raw/*.md(frontmatter `snapshot_quality: browser`, `fetched_via: aside-repl`, content_hash). `fetch_raw.py` 폴백 체인에 #3으로 삽입 (requests → Jina → **aside** → Wayback).
- 받은 raw로 `check_quotes.py`가 통과하는지, 해당 source 페이지 `snapshot_quality` 갱신.

**Step 2 — MCP 연결 (30분)**
- `.mcp.json`에 `aside` 추가 → 툴 목록·반환 형식 기록 → `hr-verifier.md`의 tools에 Aside MCP 추가(읽기 전용 툴만 허용 목록에) → `/hr-research` 스킬에 "로그인 필요 소스는 Aside MCP로 열고, 본문은 REPL로 저장" 절차 추가.
- `.claude/rules/protocols.md`에 규칙 추가: "Aside 에이전트 모드는 탐색·폼 제출에만, 저장되는 텍스트는 REPL 추출물만. 내부 자료 금지."

**Step 3 — Routine 1개 시범 (4주)**
- 위 2-3 프롬프트로 Cron routine 등록(Guard 모드, 파일 쓰기만). 매주 `raw/inbox` 산출물을 `/hr-ingest raw/inbox --dry-run`으로 triage. 4주 후 신규 사례 수·오탐·실패 횟수로 지속 여부 결정.

**중단 기준**: Step 1에서 REPL stdout이 텍스트를 못 돌려주거나 13건 중 절반 미만만 받아지면, Aside는 MCP 탐색용으로만 두고 추출은 Playwright 지속 프로필 스크립트로 간다.

## 4-1. 실행 결과 (2026-10-19 당일)

- 설치·로그인 완료 (CLI 1.26.1015.732, 앱 1.26.1019.335). MCP 서버 툴 3개 확인: `repl`(Playwright식 JS, `console.log`로만 반환), `exec`(에이전트), `memory_search`.
- REPL 추출 테스트: HR Brew Cloudflare 챌린지가 사용자 브라우저에서 10초 후 통과, 기사 본문 6,019자 확보.
- 막힌 소스 34건 일괄 재시도 (`fetch_via_aside.py --unavailable`): **24건 복구**(full 19·partial 5). 실패 10건 중 HR Executive 3건과 ServiceNow Siemens PDF는 `fetch_raw.py` 폴백 체인(Jina)으로 추가 복구 → **합계 27/34**. 남은 7건: G2(JS 렌더 실패), GenON 2건(404), Holistic AI(뉴스와이어 로그인), UNLEASH 2건(삭제), WEF(404). Gloat 2건은 게이트 폼 랜딩 요약만(partial).
- 판정 기준 "절반 이상"을 넘었으므로 채택. 폴백 체인 direct → Jina → Aside → Wayback을 `fetch_raw.py`에 내장, `.mcp.json`에 `aside` 등록, `hr-verifier`·`/hr-research`·protocols 규칙 반영. 복구된 27건의 Key Quotes 보강과 use case `미공개` 복구는 별도 에이전트로 진행.

## 5. 검증하지 못한 것
- MCP 툴 이름·반환 형식, REPL stdout 형식, REPL이 크레딧을 소모하는지, Windows CLI의 PowerShell 인용 규칙, 한국 사이트(네이버 로그인·한경) 호환성, 라우틴 실행 신뢰도. 전부 설치 후 30분이면 확인된다.
