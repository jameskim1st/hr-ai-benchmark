# Obsidian Web Clipper 템플릿 (raw/inbox 캡처용)

브라우저에서 기사·보도자료·리포트를 `raw/inbox/`에 frontmatter 포함 마크다운으로 저장한다. 이후 `/hr-ingest raw/inbox`가 triage → 스냅샷 → source 페이지 → use case 순으로 처리한다.

## 설치
1. Obsidian Web Clipper 확장 → Settings → Templates → Import → 아래 JSON 파일 선택
2. Vault: `Benchmark`, 저장 폴더는 템플릿에 `raw/inbox`로 고정돼 있음
3. 소스 유형별 템플릿 3개: `article.json`(독립 매체 기사), `vendor.json`(벤더·기업 보도자료/케이스 스터디), `report.json`(분석기관 리포트)

## 파일명 규칙
`YYYY-MM-DD-<publisher>-<slug>.md` — 클리퍼가 `{{date}}-{{domain}}-{{title|slug}}` 로 생성. ingest 시 `raw/articles/` 또는 `raw/vendors/`로 이동(수정 없음).

## frontmatter 필드
| 필드 | 의미 | ingest에서의 용도 |
|---|---|---|
| `url`, `title`, `publisher`, `published` | 원문 메타 | source 페이지 frontmatter |
| `source_kind` | article / vendor / report | tier 초기값 (2 / 3 / 1) |
| `clipped_at` | 캡처일 | `ingested_at` |
| `hr_hint` | 캡처 시 사람이 적는 한 줄 메모 (예: "채용 AI, Paradox 고객") | triage 힌트 |
| `content_hash` | 비어 있음 — `fetch_raw.py`가 아닌 클리퍼 캡처이므로 ingest 시 계산 | 변경 감지 |

캡처 본문은 클리퍼의 readability 추출 결과이며, 원문과 다를 수 있으므로 ingest 단계에서 `scripts/fetch_raw.py`로 서버 스냅샷을 한 번 더 받아 `raw:`에는 그 파일을 연결한다 (클리퍼 파일은 보조 사본).
