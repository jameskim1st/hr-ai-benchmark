# Ingest Protocol

새 소스가 `raw/` 아래에 도착하면 아래 순서로 처리한다.

1. **Read & classify**
   - 소스 유형(article/report/vendor/feed) 판별
   - Tier 판정 → `wiki/sources/<slug>.md` 생성 (frontmatter: title, url, tier, source_type, ingested_at)
   - 요약 3~7줄 + 원문 주요 인용 (3~5개)

2. **Extract entities & use cases**
   - 등장하는 회사·벤더·use case 식별
   - 각 use case에 대해:
     - 기존 `wiki/usecases/` 검색 → 존재하면 **업데이트**, 없으면 **신규 생성**
     - `sources` 리스트에 이번 소스 추가
     - `last_confirmed` 갱신, confidence 재계산
   - 기존 vendor/company 페이지 업데이트 (언급, 제품 변경사항, case list 추가)

3. **Solution Architecture 작성 — Fact-only 모드**
   - §3 템플릿의 A~F 하위 섹션(Process / System / Data / Model / Org / Diagrams)을 채운다.
   - **작성 규칙**:
     1. 각 항목은 원본 소스에서 인용 가능한 문장 또는 수치가 있을 때만 채운다.
     2. 없으면 반드시 `_미공개 (not disclosed)_`로 표시. 빈 섹션은 허용하되 공백으로 두지 말 것.
     3. 벤더·자사 주장은 `⚠️ 벤더 주장:` 접두사로 격리하고, Tier 1·2 독립 검증 여부를 병기.
     4. "일반적으로", "보통", "아마도", "추정컨대", "이런 시스템은 대개…" 등 **일반론으로 빈칸 채우기 전면 금지**.
     5. 도식(Mermaid)은 최소 1개 이상 생성하되, 모든 노드·엣지에 대응하는 소스 근거가 있어야 한다. 근거 없는 연결은 점선 + `(미확인)` 라벨로 표시하거나 아예 그리지 말 것.
   - **Hallucination self-check**: 작성 후 본문의 모든 구체적 주장(시스템명·모델명·수치·팀 역할 등)이 `sources` 리스트 중 어느 페이지에서 온 것인지 마음속으로 짚어본다. 짚어지지 않으면 해당 문장을 삭제하거나 `_미공개_`로 대체한다.
   - 이 단계에서 정보가 크게 부족하면 페이지를 `stage: stub`으로 표시하고 `confidence`를 낮게 유지한다. 억지로 채우지 말 것.

4. **Cross-link**
   - 본문의 회사·벤더·concept는 `[[wikilink]]` 형태로 연결
   - 새로 등장한 엔티티는 stub 페이지라도 생성

5. **Contradiction check**
   - 새 소스의 claim이 기존 wiki의 claim과 충돌하면 해당 페이지에 다음 블록 추가:
     ```
     > [!contradiction] <날짜> — <요약>
     > - 기존 주장: ... (출처: [[sources/old]])
     > - 새 주장: ... (출처: [[sources/new]])
     > - 상태: unresolved
     ```
   - 충돌은 silent overwrite 금지. 반드시 콜아웃으로 표면화.

6. **Update index & log**
   - `wiki/index.md`: 신규 use case·vendor·company 엔트리 추가
   - `wiki/log.md`: `## [YYYY-MM-DD] ingest | <소스 제목> | touched: N pages | new: X usecases`

7. **Report back**
   - 사용자에게 요약: 신규 N건, 업데이트 M건, 충돌 K건, 확인 요청 사항
   - **Solution Architecture 품질 리포트**: 각 신규 use case의 A~E 항목 중 몇 개가 Fact로 채워졌는지, 몇 개가 `_미공개_`인지 명시 (예: "fact 3/5, 미공개 2/5 — stub 상태")

**1건의 소스는 보통 5~15개 wiki 페이지를 touch한다.** 이 범위를 크게 벗어나면 스키마 해석이 잘못된 것.

---

# Lint Protocol

`/hr-lint` 실행 시 아래를 점검한다.

1. **Stale claims**: `last_confirmed`가 12개월 경과한 use case
2. **Low confidence**: `confidence < 0.4` 페이지
3. **Orphan pages**: 어떤 다른 페이지에서도 `[[wikilink]]`되지 않은 페이지
4. **Broken links**: 존재하지 않는 페이지로의 `[[wikilink]]`
5. **Missing entities**: 언급되었지만 페이지가 없는 회사·벤더
6. **Unresolved contradictions**: 상태가 unresolved인 contradiction 콜아웃 전수
7. **Category coverage gaps**: 대/중/소 카테고리 중 use case가 0건인 곳
8. **Tier imbalance**: Tier 3·4에만 의존하는(= Tier 1·2 출처 0건인) use case
9. **Solution Architecture 품질 점검** (★ 가장 중요)
   - A~E(Process / System / Data / Model / Org) 중 3개 이상이 `_미공개_`이거나 빈 페이지는 `stage: stub` 또는 경고
   - **추측성 표현 탐지**: "아마도", "추정", "보통", "일반적으로", "대개", "대체로", "통상" 등 금지어가 본문에 있으면 즉시 critical로 플래그 (의도적 불확실성 표시여도 다른 표현으로 리라이트)
   - **Unverified 벤더 주장 / 자사 보고**: `⚠️ 벤더 주장:` 또는 `⚠️ 자사 보고:` 접두사 없이 벤더·도입 기업 출처에서 나온 수치·단언이 그대로 단언형으로 쓰여 있으면 경고. 벤더 주장과 자사 보고의 구분이 올바른지도 확인 (§3 표 참조)
   - **Citation 커버리지**: Solution Architecture 섹션의 구체적 주장(시스템명·모델명·수치) 중 인접한 `[[sources/xxx]]` citation이 없는 문장 탐지
   - **Mermaid 다이어그램 누락**: Solution Architecture에 도식이 0개이고 공개 정보가 충분한(A~E 중 3개 이상 Fact) 페이지는 경고
10. **Consulting Angle 누락**: `## Consulting Angle` 섹션이 비어 있거나 `consulting_angle_status: pending`인 use case
11. **Frontmatter 불일치**: 필수 필드 누락, 태그 오탈자, primary_category가 taxonomy에 없는 값

산출물: `wiki/syntheses/lint-YYYY-MM-DD.md` 생성 및 사용자에게 액션 리스트 보고.

---

# Query Protocol

사용자 질문은 우선 wiki 내부만 검색·합성해 답한다.

1. 관련 페이지 검색 (카테고리·태그·frontmatter)
2. 페이지 내용 읽고 citation과 함께 답변 (`[[wikilink]]` 포함)
3. 답변이 "재사용 가치 있음"이면 `wiki/syntheses/<topic>-YYYY-MM-DD.md`로 승격
4. wiki 내에 답이 부족하면 사용자에게 **명시적으로** 알리고 `/hr-autoresearch` 제안 (wiki 내 데이터로는 답할 수 없다고 솔직하게 말한다 — 추측 금지)

---

# Log Convention

`wiki/log.md`는 append-only. 모든 엔트리는 아래 prefix로 시작:

```
## [YYYY-MM-DD] <operation> | <one-line description>
```

operation 값: `ingest` | `query` | `lint` | `digest` | `refactor` | `manual-edit`

오래된 엔트리 삭제·수정 금지. grep 가능하도록 포맷 엄수.

---


# 2026-09-27 개정 — Research · Verify 프로토콜과 자동화

## Research Protocol (`/hr-research`)
리서치 라운드의 산출물은 **후보 목록(`wiki/syntheses/research-<topic>-<date>.md`) + raw 스냅샷 + source 페이지**까지다. use case 생성은 사용자가 후보를 승인한 뒤 `/hr-ingest`로만 한다. 2026-04~05의 "라운드 N — background agent 대량 생성" 방식은 근거 사슬을 끊었으므로 금지.

## Verify Protocol (`/hr-verify`, `hr-verifier` 서브에이전트)
- 판정 4종: ✅ 확인 / ⚠️ 표기 오류(접두사·hedging 누락) / ❌ 근거 없음 / 🔁 supersede(최신 소스가 다른 값).
- 검증은 "텍스트가 raw에 있다"만 증명한다. 결과 표에 이 문장을 항상 남긴다.
- 클라이언트 자료(제안서·벤더 deck) 검증 결과는 `visibility: internal` synthesis로 저장.

## Supersession (contradiction 처리 개정)
- 두 소스가 다른 값을 말하면 `[!contradiction]` 콜아웃을 남기되, 최신성·권위(Tier)·독립성이 명확히 우세한 쪽이 있으면 본문을 그 값으로 **재작성**하고 콜아웃에 `상태: superseded — <근거>`를 적는다. 두 값을 나란히 누적만 하는 것은 금지.
- 판단이 안 서면 `상태: unresolved`로 두고 lint가 매주 표면화한다.

## Lint 개정
- 결정론 항목(링크·frontmatter·날짜·근거 등급·금지어·섹션·grounding·index drift·export 기밀 누출)은 `scripts/lint.py`가 판정한다. LLM은 모순·낡음·품질 판단만 한다. LLM lint가 "broken link 0"처럼 스크립트 영역을 스스로 세지 않는다.
- 자동 수정 없음. `--fix`는 폐기.

## 자동화
- PreToolUse 훅 `scripts/hooks/guard_raw.py`: raw/ 쓰기 차단.
- PostToolUse 훅 `scripts/hooks/post_write_lint.py`: wiki/*.md 저장 직후 `lint.py --quick` (critical → exit 2, 즉시 수정).
- 주간 `scripts/weekly.ps1`: grade → lint 리포트 → index → export → inbox triage(dry-run) → digest → commit(push 없음).
- 회귀 평가 `scripts/eval_qa.py`: `evals/golden-qa.json`의 질문을 wiki만 보고 답하게 하고 정규식으로 채점. CLAUDE.md·rules·모델 변경 시 실행.
