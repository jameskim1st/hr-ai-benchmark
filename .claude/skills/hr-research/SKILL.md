---
name: hr-research
description: 주제·기업·카테고리 갭에 대한 웹 리서치 라운드. 산출은 "후보 목록 + raw 스냅샷 + source 페이지"까지만. use case 생성은 반드시 /hr-ingest 경로를 탄다 (compilation source 금지).
argument-hint: "<topic | company | category gap> [--max N]"
---

# /hr-research

주제: `$ARGUMENTS` (예: `Total Rewards 갭`, `현대자동차 HR AI`, `SHRM 2026 top use cases`)

현재 카테고리 커버리지 (lint info의 gap 항목):

!`python scripts/lint.py --json | python -c "import json,sys; d=json.load(sys.stdin); print('\n'.join(f['page']+' '+f['detail'] for f in d['findings'] if f['code'] in ('category-gap','subcategory-gap')))"`

## 절차
1. **부재 확인** — `grep -ril "<키워드>" wiki/usecases wiki/enterprise-ai wiki/sources`로 이미 있는 페이지를 먼저 확인한다. 있으면 "갱신 후보"로 분류한다.
2. **검색** — WebSearch로 후보 기사·보도자료·리포트를 찾는다. Tier 1·2(분석기관·독립 매체)를 우선하고, 벤더 자료는 보조로만. `--max N`(기본 10)건까지.
3. **스냅샷 + source 페이지** — 후보마다 `python scripts/fetch_raw.py`로 raw 스냅샷을 만들고 `wiki/sources/<slug>.md`를 작성한다 (`/hr-ingest` 3단계와 동일 형식, `supports: []`로 비워둠). 스냅샷이 `unavailable`이면 후보 목록에 그 사실을 적는다.
4. **후보 목록** — `wiki/syntheses/research-<topic>-YYYY-MM-DD.md`에 표로 저장: 회사 | 제품/벤더 | HR 카테고리 | 핵심 주장(수치) | source 슬러그 | tier | 권고(New/Update/Skip)와 이유. frontmatter `type: research-candidates`.
5. **보고** — 사용자에게 표를 보여주고 "어느 것을 ingest할지" 묻는다. 승인된 항목만 `/hr-ingest`로 이어진다. `wiki/log.md`에 `## [YYYY-MM-DD] research | <topic> | candidates: N | sources: M` append.

## 금지
- 이 스킬에서 use case 페이지를 만들지 않는다. 여러 URL을 한 source 페이지에 묶지 않는다.
- 검색 결과 요약을 근거로 수치를 쓰지 않는다 — 수치는 raw 스냅샷에서 verbatim으로만.
