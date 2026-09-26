---
title: "LLM Wiki 구조 가이드 — 언제든 다시 볼 수 있는 설명서"
created_at: 2026-04-12
updated_at: 2026-09-27
purpose: 이 wiki가 어떻게 생겼고 어떻게 작동하는지, 한동안 안 보다가 돌아와도 바로 이해할 수 있도록 정리한 문서
---

# 🧭 HR AI Benchmark Wiki — 구조 가이드 (2026-09 개정판)

> 2026-04에 만든 v1 가이드를 2026-09-27 전면 점검([[system-review-2026-09-27]]) 후 다시 썼다. 숫자(건수·분포)는 여기 적지 않는다 — **[[index]]가 스크립트로 생성**하므로 거기서 본다.

## 1. 한마디로

**HR 프로세스에 AI를 적용한 실제 사례를 모아, 근거를 추적 가능하게 검증해 두고, 컨설팅 제안서에 바로 인용할 수 있게 유지하는 살아있는 자료집.**

v1과 달라진 핵심 한 줄: "AI가 요약해서 쌓는다"에서 **"모든 수치가 raw 원문에 있는지 스크립트가 검사한다"**로 바뀌었다.

## 2. 3층 구조 + 2개 강제 장치

```
CLAUDE.md + .claude/rules/     규칙서 (78줄 core + 4개 rules 파일)
        ↓ 따른다
wiki/                          Claude가 쓰고 유지하는 자료 (usecases · sources · companies …)
        ↓ 가리킨다
raw/                           원본 스냅샷 (불변). 모든 수치의 최종 근거
```

강제 장치 2개:
- **hooks** — raw/ 쓰기는 차단, wiki/ 저장 직후 `lint.py --quick` 자동 실행 (critical이면 Claude가 즉시 고침)
- **scripts** — `lint.py`(점검) `grade.py`(등급 계산) `check_quotes.py`(수치가 raw에 있나) `build_index.py`(목차) `build_all.py`(HTML/Excel). 숫자는 사람도 LLM도 손으로 안 쓴다.

## 3. 폴더

| 폴더 | 내용 | 누가 쓰나 |
|---|---|---|
| `raw/articles` `raw/vendors` `raw/reports` | `fetch_raw.py`가 받은 원문 스냅샷 (frontmatter에 url·content_hash·snapshot_quality) | 스크립트만 |
| `raw/inbox` | Obsidian Web Clipper로 캡처한 새 기사 (templates/obsidian-web-clipper) | 사람 → `/hr-ingest`가 이동 |
| `raw/internal` | 클라이언트·제안서 자료 (기밀) | 사람 |
| `wiki/usecases` | ★ HR 프로세스 AI 사례 1건 = 1페이지 | Claude |
| `wiki/enterprise-ai` | 전사 GenAI 플랫폼 사례 — 참고용, use case 카운트에서 제외 | Claude |
| `wiki/reference` | 법령(AI 기본법)·리포트(Deloitte HC Trends)·제도 맥락 | Claude |
| `wiki/sources` | 기사 1건 = 1페이지. `raw:`로 스냅샷 연결, Key Quotes는 원문 verbatim | Claude |
| `wiki/companies` `wiki/vendors` | 홀리스틱 뷰. 목록은 Dataview 자동, 서사만 손으로 | Claude |
| `wiki/categories` | 7개 카테고리 뷰 + [[taxonomy-crosswalk]] (SHRM·Bersin·AIHR 대응표) | Claude |
| `wiki/syntheses` | lint 리포트·digest·compare·research 후보·리뷰 | 스크립트 + Claude |
| `wiki/exports` | HTML·Excel 산출물 (`visibility: internal` 자동 제외) | 스크립트 |
| `wiki/bases` | Obsidian Bases 뷰 (Dataview 대체 준비) | — |
| `evals/` | 골든 Q&A 30문항 + 결과 (`eval_qa.py`) | 스크립트 |

## 4. 페이지 하나를 읽는 법 — frontmatter 핵심 필드

| 필드 | 뜻 | 누가 정하나 |
|---|---|---|
| `evidence_grade` A/B/C/D | A 독립 소스 2+ · B 독립 1 · C 벤더·자사만 · D 미검증 | grade.py |
| `corroborated_by` | 서로 다른 독립 소스 수 | grade.py |
| `depth` full/partial/stub | B·C·D·E 섹션 실질 내용 + Mermaid 유무 | grade.py |
| `freshness` fresh/stale/unverified | 12개월 기준 | grade.py |
| `confidence` | 등급 파생 숫자 (필터용) | grade.py |
| `visibility` public/internal | internal = export 제외 | 사람/ingest |
| `case_type` adoption/vendor-product | 도입 기업 사례 vs 벤더 제품 페이지 | ingest |
| `regulatory_exposure` | `kr-high-impact` `eu-annex-iii` (채용·평가·승진·해고·이탈예측) | ingest (규칙) |
| `kr_law` `kr_union` `kr_language` `kr_vendor` | 한국 적용성 4축 한 줄씩 | ingest |
| `stage` | 배포 단계 (announced/pilot/production/sunset) — 정보 부족은 depth로 | ingest |
| `sources` / `sources_unresolved` | `sources/<slug>.md` 만 허용 / 원문 못 찾은 옛 참조 | ingest |

**제안서 인용 기준**: `evidence_grade` A·B **and** `depth` full. C는 "벤더 주장"으로만, D는 인용 금지. Dashboard의 "제안서 즉시 투입 가능" 표가 이 조건이다.

본문 표기 5단계는 그대로다: ✅ Fact · ⚠️ 벤더 주장 · ⚠️ 자사 보고 · ❓/`_미공개_` · 🚫 금지(일반론). 2026-09 추가: **hedging 보존** (소스가 "계획·검토 중"이면 wiki도 그렇게) · **선택지 나열식 추정 금지** ("Workday 또는 자체" ✗ → `_미공개_`).

## 5. 운영 — 6개 스킬과 1개 서브에이전트

| 하고 싶은 것 | 명령 | 산출 |
|---|---|---|
| 새 기사 넣기 | 클리퍼로 `raw/inbox`에 저장 → `/hr-ingest raw/inbox` | triage → 스냅샷 → source → use case → grade → lint |
| 건강 점검 | `/hr-lint` (`--report`로 파일 저장, `--strong`으로 검증 에이전트 투입) | 스크립트 결과 + LLM 판단, 승인 필요 수정 목록 |
| 주장 검증 | `/hr-verify <slug 또는 "주장">` | ✅/⚠️/❌/🔁 판정표 (hr-verifier 서브에이전트) |
| 갭 리서치 | `/hr-research <topic>` | 후보 목록 + 스냅샷 + source까지만. use case는 승인 후 ingest |
| 주간 요약 | `/hr-digest weekly` | syntheses/digest-… |
| 비교 | `/hr-compare A vs B` | syntheses/compare-… |
| 산출물 | `python scripts/build_all.py` | HTML + Excel (internal 제외) |
| 목차·등급 갱신 | `python scripts/grade.py && python scripts/build_index.py` | index.md, frontmatter |

주간 자동: `scripts/weekly.ps1` (등록 `scripts/register_weekly_task.ps1`, 월 08:00). grade → lint 리포트 → index → export → inbox triage(dry-run) → digest → commit. push는 사람이.

다른 프로젝트에서 이 wiki를 쓰려면: `.mcp.json`의 `hr-wiki` MCP 서버 (`wiki_search` `wiki_read` `wiki_sources` `wiki_verify_quote`).

## 6. 하지 않는 것

- raw/ 수정, compilation source, 손글씨 카운트, LLM lint의 자동 수정, "라운드 N 대량 생성" 리서치.
- 벡터 검색·감쇠 곡선 같은 v2 기능 (수백 페이지 이하에서 효과 미입증 — [[llm-wiki-landscape-2026-09]]).

## 7. 문제가 생기면

| 증상 | 확인 |
|---|---|
| Dataview 표가 코드로 보임 | 커뮤니티 플러그인 Dataview 설치 (dashboard.md 하단) |
| lint critical `unresolved-source` | `sources:`에 `sources/<slug>.md` 형식이 아닌 항목 → source 페이지 생성 또는 `_미공개_` |
| `not-graded` | `python scripts/grade.py` |
| `internal-in-export` | `python scripts/build_all.py` 재실행 (extract가 internal 제외) |
| check_quotes ⚠️ | 수치가 raw에 없음 → 소스 확인 후 인용 추가 또는 `_미공개_` |
| hook이 raw/ 쓰기를 막음 | 의도된 동작. `fetch_raw.py`로 새 파일 생성 |

이 문서는 규칙이 바뀔 때만 갱신한다. 현황 숫자는 [[index]]·[[dashboard]].
