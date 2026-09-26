---
name: hr-ingest
description: raw/ 아래 소스(파일·디렉토리·raw/inbox)를 wiki로 ingest. triage → source 페이지(raw 스냅샷 연결) → use case 생성/갱신(Fact-only) → grade → lint. 컴파일레이션 source 금지.
argument-hint: "<raw path | raw/inbox> [--dry-run]"
---

# /hr-ingest

대상: `$ARGUMENTS` (기본값 `raw/inbox`). 규칙: `.claude/rules/protocols.md` Ingest Protocol, `.claude/rules/usecase-schema.md`, `.claude/rules/sources.md`.

현재 inbox 상태:

!`ls raw/inbox 2>/dev/null | head -30`

## 절차 (소스 1건마다)

1. **Triage** — 소스를 읽고 4개 중 하나로 판정해 log에 남긴다: `New`(새 use case) / `Update`(기존 use case 갱신) / `Disputed`(기존 주장과 충돌) / `No material`(HR AI use case 없음 → source 페이지만 만들고 종료). `--dry-run`이면 여기서 triage 표만 보고하고 멈춘다.
2. **Raw 스냅샷** — 대상이 URL이나 클리퍼 파일이면 `python scripts/fetch_raw.py "<url>" "raw/articles/<YYYY-MM-DD>-<publisher>-<topic>.md" --publisher "<name>"` (벤더 자료는 `raw/vendors/`, 분석기관 리포트는 `raw/reports/`). inbox 파일은 처리 후 `raw/articles/`로 **이동**(`git mv`), 수정 금지.
3. **Source 페이지** — `wiki/sources/<publisher>-<topic>-<yyyy-mm>.md`. frontmatter: title, url, publisher, tier, source_type, independent, publication_date, ingested_at, raw, snapshot_quality, supports. 본문: Summary(3~5줄) / Key Quotes(원문 verbatim 3~5개, 각 인용이 뒷받침하는 주장 명시) / Limitations. **기사 1건 = source 1건.** 여러 기사를 묶은 compilation source는 만들지 않는다.
4. **Use case 생성/갱신** — `wiki/usecases/<slug>.md`. 기존 페이지는 `grep -ril "<회사>" wiki/usecases`로 **부재를 확인한 뒤** 생성한다. 스키마의 모든 섹션을 만들되, 소스에 없는 항목은 `_미공개 (not disclosed)_`. 수치·시스템명·모델명 옆에는 `[[sources/<slug>]]`를 붙인다. 소스가 "검토 중·계획·추정"이라 쓴 것은 확정형으로 바꾸지 않는다(hedging 보존). 벤더 자료 수치는 `⚠️ 벤더 주장:`, 도입 기업 발표는 `⚠️ 자사 보고:`.
   - HR 프로세스가 아닌 전사 GenAI 플랫폼 사례는 `wiki/enterprise-ai/`에, 법령·리포트는 `wiki/reference/`에 만든다.
   - frontmatter 필수: `visibility: public`(내부 자료면 internal), `case_type: adoption|vendor-product`, `regulatory_exposure`(채용·평가·승진·해고·이탈예측 관련이면 `[kr-high-impact, eu-annex-iii]`).
5. **Contradiction** — 기존 주장과 충돌하면 `[!contradiction]` 콜아웃 + `상태: unresolved`. 최신·권위 소스가 명확히 우세하면 본문을 재작성하고 콜아웃에 `상태: superseded (근거)`를 남긴다. 조용히 덮어쓰지 않는다.
6. **Cross-link** — 회사·벤더 페이지 갱신 또는 stub 생성. 손으로 쓰는 목록은 만들지 말고 Dataview 블록에 맡긴다.
7. **계산·점검** — `python scripts/grade.py` → `python scripts/lint.py --quick wiki/usecases/<slug>.md` → critical 0이 될 때까지 수정 → `python scripts/check_quotes.py <slug>`로 수치 근거 확인.
8. **검증(선택, 권장)** — 신규 use case가 evidence_grade A/B이면 `hr-verifier` 서브에이전트에 넘겨 주장 대조 결과를 받고 ❌ 항목을 `_미공개_`로 고친다.
9. **Index·log** — `python scripts/build_index.py`; `wiki/log.md`에 `## [YYYY-MM-DD] ingest | <소스 제목> | triage: New/Update/... | touched: N pages | new: X usecases | contradictions: K` append.
10. **보고** — 신규/갱신 건수, triage 표, 근거 등급(A/B/C/D)과 depth, contradiction, 사용자 확인 필요 항목, `python scripts/build_all.py` 실행 여부.

## 금지
- 소스에 없는 내용 채우기, 일반론("보통 이런 시스템은…"), 금지어(아마도·추정·보통·일반적으로·대개·통상·likely·typically).
- raw/ 파일 수정. compilation source. 손글씨 카운트(index 숫자 등).
