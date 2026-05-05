---
description: raw/ 아래 소스 1건 또는 디렉토리를 wiki로 ingest (요약·엔티티 추출·use case 갱신·cross-link·contradiction 체크·log 업데이트)
argument-hint: <raw path — 예: raw/articles/xxx.md 또는 raw/feeds/2026-04-12.md>
---

# /hr-ingest

다음 소스(들)을 [CLAUDE.md](../../CLAUDE.md) **§6 Ingest Protocol**에 따라 wiki로 ingest하세요.

**대상**: `$ARGUMENTS`

## 실행 절차

1. **대상 검증**
   - `$ARGUMENTS` 경로가 `raw/` 아래인지 확인. 아니면 중단.
   - 디렉토리면 내부의 ingest되지 않은 파일(= `wiki/sources/`에 대응 페이지가 없는 것)만 처리.
   - 이미 ingest된 파일은 skip하되 사용자에게 알림.

2. **소스 페이지 생성** (`wiki/sources/<slug>.md`)
   - Frontmatter: `title, url (있으면), tier (1~4), source_type (analyst/media/vendor/case-signal), ingested_at, publication_date, authors`
   - Tier 판정 기준: CLAUDE.md §4 참조
   - 본문: 3~7줄 요약 + 핵심 인용 3~5개 (원문 언어 유지) + takeaway 2~3개

3. **엔티티·use case 추출**
   - 등장하는 회사·벤더·use case·개념을 모두 식별
   - 각 use case에 대해:
     - `wiki/usecases/` 검색 → 기존 페이지가 있으면 **업데이트** (sources 리스트 append, last_confirmed 갱신, confidence 재계산, 새 정보 병합)
     - 없으면 **신규 생성** (frontmatter 전체 + Summary/Problem/Solution Architecture(A~F)/Impact/Governance/Contradictions/Consulting Angle 섹션)
   - 회사·벤더 페이지도 동일하게 업데이트 또는 생성 (stub이라도 OK)

4. **Solution Architecture 작성 — Fact-only 모드** (★ 가장 중요한 단계)
   - CLAUDE.md §3 템플릿의 A~F 하위 섹션 (Process / System & Infra / Data / Model / Org & Team / Diagrams) 작성
   - **작성 규칙**:
     - 각 항목은 소스에 **명시적으로** 쓰여 있을 때만 채운다
     - 없으면 `_미공개 (not disclosed)_`로 표시 — 빈 섹션 금지, 공백 금지
     - 벤더·자사 주장은 `⚠️ 벤더 주장:` 접두사 + 독립검증 여부 병기
     - **금지어**: 아마도, 추정, 보통, 일반적으로, 대개, 대체로, 통상, likely, typically, generally — 이 단어를 쓰고 싶으면 해당 문장을 쓰면 안 된다는 신호
     - **추측으로 빈칸 채우기 금지**: "이런 시스템은 보통 Azure AD와 연동되므로..." 같은 일반론 절대 금지
   - **Mermaid 도식 필수**: A~E 중 3개 이상이 Fact로 채워졌다면 최소 1개 이상 생성 (process / system / data flow)
     - 실선 = 소스 확인됨, 점선 + `(미확인)` = 확인 안 됨
     - 모든 노드·엣지는 sources 리스트의 어느 페이지에 근거가 있어야 함
   - **Hallucination self-check**: 작성 후 본문의 모든 구체 주장(시스템·모델·수치·팀 역할)이 어느 소스에서 왔는지 하나씩 짚어본다. 짚어지지 않는 문장은 삭제 또는 `_미공개_`로 대체.
   - 정보가 크게 부족하면 `stage: stub`으로 표시하고 confidence 낮게 유지. 억지로 채우지 말 것.

5. **카테고리 분류**
   - CLAUDE.md §2의 taxonomy로 `primary_category`, `subcategory`, `tags` 확정
   - 여러 카테고리에 걸치면 primary는 1개만, 나머지는 tags에 반영
   - 축 태그(industry, region, employee_class, frequency, stage, vendor_type)도 반드시 기입

6. **Cross-link**
   - 본문의 회사·벤더·주요 concept는 `[[wikilink]]`로 연결
   - 새 엔티티는 stub 페이지라도 생성해서 broken link 방지

7. **Contradiction check**
   - 새 소스의 claim이 기존 wiki와 충돌하면 `[!contradiction]` 콜아웃 추가 (silent overwrite 금지)
   - 양쪽 출처 명시, 상태는 `unresolved`로

8. **Index·log 갱신**
   - `wiki/index.md`에 신규 엔트리 추가
   - `wiki/log.md`에 append: `## [YYYY-MM-DD] ingest | <소스 제목> | touched: N pages | new: X usecases, Y vendors, Z companies | contradictions: K`

9. **Report**
   - 사용자에게 요약 보고:
     - 신규/업데이트 건수
     - 발견된 contradiction (있으면 각각 1줄)
     - confidence가 0.4 미만인 신규 use case (재확인 필요)
     - 애매했던 카테고리 분류 (사용자 확인 요청)
     - **Solution Architecture 품질 리포트**: 각 신규 use case에 대해 "fact X개 / 미공개 Y개 / 도식 Z개"를 표로 요약. stub 상태도 표시.

## 중요 원칙

- **추측 금지**: 소스에 없는 정보는 만들지 않는다. 불확실하면 confidence를 낮추고 "insufficient data"로 표시.
- **품질 > 분량**: 엉성한 use case 5개보다 탄탄한 1개가 낫다. 소스가 부족하면 stub으로만 만들고 다음 소스를 기다린다.
- **컨설팅 관점 필수**: 모든 신규 use case에 `## Consulting Angle` 섹션 작성. 못 쓰겠으면 이유를 frontmatter `consulting_angle_status: pending`으로 남기고 다음 lint에 걸리게 한다.
- **1건의 소스는 보통 5~15 페이지를 touch한다**. 이 범위 크게 벗어나면 스키마 해석을 다시 확인.
