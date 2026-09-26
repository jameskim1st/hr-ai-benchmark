---
title: "산출물 생성 가이드 (HTML + Excel)"
created_at: 2026-04-13
updated_at: 2026-09-27
purpose: wiki의 use case를 클라이언트 CHRO/임원에게 공유할 수 있는 단일 HTML + Excel 파일로 변환하는 방법
---

# 산출물 생성 가이드 (HTML + Excel)

## 1. 이 산출물이 뭔가

wiki에 축적된 HR AI use case(공개분)와 전사 AI 플랫폼 참고 사례를 **두 종류의 단일 파일**로 변환:

| 산출물 | 크기 | 용도 |
|---|---|---|
| **HTML** (`hr-ai-usecase-collection.html`) | ~780KB | 클라이언트 CHRO·임원의 **열람·발표** (브라우저에서 검색·필터·다크모드, 인터랙티브) |
| **Excel** (`hr-ai-usecase-collection.xlsx`) | ~245KB | 컨설턴트·실무진의 **작업·분석** (필터·정렬·피벗·셀 copy/paste·보고서 가공) |

- 별도 서버 불필요 (file:// 프로토콜·로컬 Excel)
- 이메일 첨부·USB 전달 가능
- HTML: 검색·필터·다크모드 + Category/Company/Matrix 3개 뷰 + 하단 "전사 AI 플랫폼 사례 (참고)" 접힘 섹션
- Excel: 5 sheet (개요 / Use Cases / AI 기술 분포 / Companies / 전사 AI 참고) + AutoFilter + Pivot 가능
- **`visibility: internal` 페이지는 JSON·HTML·Excel 어디에도 포함되지 않음** (extract 단계에서 제외, HTML·Excel 단계에서 한 번 더 방어)

## 2. 파일 구조

```
scripts/
  build_all.py           ← lint 게이트 → extract → HTML → Excel 일괄 실행 (권장)
  extract_v3.py          ← wiki/*.md → JSON 추출 (Step 1)
  build_html_v6.py       ← JSON → HTML 변환 (Step 2a)
  build_excel.py         ← JSON → Excel 변환 (Step 2b)

wiki/exports/
  usecases.json          ← use case 데이터 (Step 1 산출, internal 제외)
  enterprise_ai.json     ← 전사 AI 플랫폼 사례 (Step 1 산출, wiki/enterprise-ai/)
  companies.json         ← 기업 데이터 (Step 1 산출)
  hr-ai-usecase-collection.html  ← HTML 산출물 (Step 2a)
  hr-ai-usecase-collection.xlsx  ← Excel 산출물 (Step 2b)
```

**입력 디렉토리:**

| 디렉토리 | frontmatter `page_type` | export |
|---|---|---|
| `wiki/usecases/` | (없음 = usecase) | `usecases.json` → HTML 본문 + Excel "Use Cases" |
| `wiki/enterprise-ai/` | `enterprise-ai` | `enterprise_ai.json` → HTML 하단 참고 섹션 + Excel "전사 AI 참고" |
| `wiki/reference/` | `reference` | **export 안 함** (규제·리포트) |
| `wiki/sources/` | — | 직접 export 안 함. use case의 `sources:` 항목을 해석해 title·publisher·tier·url 제공 |
| `wiki/companies/` | — | `companies.json` |

## 3. 생성 방법

### 한 줄 실행 (권장)

```bash
cd c:\AI\AI-HR\Benchmark
PYTHONIOENCODING=utf-8 python scripts/build_all.py
```

`build_all.py`가 하는 일:

0. `python scripts/lint.py --json` 실행 → finding code `internal-in-export`가 하나라도 있으면 **중단** (방어). 이 경우 현재 `wiki/exports/usecases.json`에 internal 페이지가 남아 있다는 뜻이므로 `python scripts/extract_v3.py`를 먼저 단독 실행해 깨끗한 JSON을 만든 뒤 재실행.
1. `extract_v3.py` → JSON 3종
2. `build_html_v6.py` → HTML
3. `build_excel.py` → Excel

각 단계의 요약을 출력하고, 어느 단계든 실패하면 이후 단계를 실행하지 않고 non-zero로 종료한다.

### 개별 실행

```bash
# 1) JSON 추출
python scripts/extract_v3.py

# 2a) HTML 생성
python scripts/build_html_v6.py

# 2b) Excel 생성 (openpyxl 필요)
python scripts/build_excel.py
```

### Step 1: 데이터 추출 (`extract_v3.py`)

wiki의 markdown 파일에서 frontmatter + 본문 핵심 섹션을 JSON으로 추출합니다.

**추출되는 것 (`usecases.json` / `enterprise_ai.json` 동일 레코드 형태):**
- frontmatter (title, category, company, vendor, confidence, tags 등)
- **신규 필드** (없으면 default):

  | 필드 | 값 | default | 용도 |
  |---|---|---|---|
  | `visibility` | `public` / `internal` | `public` | internal은 export 전체에서 제외 |
  | `page_type` | `usecase` / `enterprise-ai` / `reference` | 디렉토리 기준 | reference는 export 안 함 |
  | `case_type` | `adoption` / `vendor-product` | `''` | HTML 칩 "도입 사례"/"벤더 제품", Excel 사례유형 |
  | `evidence_grade` | `A`/`B`/`C`/`D` | `''` (미산정) | HTML 배지·필터, Excel 근거등급 + 조건부 서식 |
  | `corroborated_by` | 정수 | `0` | 독립 소스 수 (배지 tooltip, Excel 독립소스수) |
  | `freshness` | `fresh`/`stale`/`unverified` | `''` | stale → HTML "⏳ 12개월+" 마커, Excel 신선도 |
  | `depth` | `full`/`partial`/`stub` | `''` | stub → 점선 테두리 + "정보 부족(stub)" 라벨, "stub 숨기기" 토글(기본 on) |
  | `regulatory_exposure` | 리스트 (`kr-high-impact`, `eu-annex-iii`) | `[]` | HTML 칩 "⚖️ KR 고영향"/"⚖️ EU Annex III", Excel 규제노출 |
  | `kr_law` `kr_union` `kr_language` `kr_vendor` | 짧은 문자열 (또는 nested `kr_applicability: {law, union, language, vendor}`) | `''` | 있을 때만 HTML 펼침 카드 "한국 적용성" 섹션, Excel KR 4컬럼 |
  | `sources` | `sources/<slug>.md` 참조 리스트 | `[]` | `sources_resolved`로 해석 (아래) |

- `sources_resolved` [] — `sources/<slug>.md`를 `wiki/sources/`에서 찾아 `{title, publisher, tier, url, resolved}`로 해석. source 페이지가 없으면 `resolved: false` (slug만), 구형 자유 텍스트 항목은 `legacy: true` + URL 추출
- headline (Summary 첫 문장 — 카드 소제목용) · summary_clean (Excel 개요용 2~3문장)
- problem / impact_summary / consulting (HTML 변환됨)
- system {} / data {} / model {} / process_before / process_steps []
- `companies.json` — 기업별 description / strategy / consulting

`evidence_grade`·`corroborated_by`·`freshness`·`depth`·`confidence`는 `python scripts/grade.py`가 계산해 frontmatter에 쓴다. 미실행 페이지는 HTML에서 점선 "–" 배지(미산정)로 표시되고 Evidence 필터 "전체"에서만 보인다.

**빌드 로그:** 추출 끝에 커버리지 표(process_steps / system / data / model / impact_summary / consulting / sources resolved / evidence_grade / case_type 보유 건수)와 `summary_clean` 또는 `process_steps`가 빈 slug 목록, internal 제외 건수, 추출 실패 페이지를 출력한다.

**마크다운→HTML 변환 포함:** `**bold**` → `<strong>`, `- bullet` → `<ul><li>`, `[[wikilink]]` → 텍스트, `\n` → `<br>`

### Step 2a: HTML 생성 (`build_html_v6.py`)

JSON 데이터를 HTML 파일 안에 JavaScript 변수(`D` use cases, `EA` 전사 AI, `CO` companies)로 임베딩하고, 인터랙티브 UI를 생성합니다.

- Pretendard 한국어 폰트 (CDN)
- Mermaid.js 없음 — 모든 도식은 HTML/CSS로 직접 렌더
- 다크/라이트 모드
- 3개 탭 뷰 (Category / Company / Matrix)
- AI 기술 5색 칩 (생성형·판별예측·인식·의사결정최적화·자동화)
- 카드 상단: 회사명 + 칩(도입 사례/벤더 제품, ⚖️ 규제, ⏳ stale, stub) + **Evidence 배지** (A 녹 / B 파랑 / C 노랑 / D 회색, tooltip "A=독립 소스 2+ / B=독립 1 / C=벤더·자사 보고만 / D=미검증"). confidence 숫자는 **펼친 카드에서만** 표시
- 펼친 카드: Pain Point · Process Flow · System|Data|Model · Output · Impact · AI 기술 분류 · **한국 적용성**(있을 때만) · Consulting · **Sources**(source 페이지 title 링크 + Tier 칩 + publisher)
- **전사 AI 플랫폼 사례 (참고 — HR 전용 use case 아님)**: Category 뷰 맨 아래 접힌 섹션. 같은 카드 컴포넌트를 쓰되 헤더 use case 수·Matrix 뷰에서 제외. 검색·필터는 동일하게 적용

### Step 2b: Excel 생성 (`build_excel.py`)

동일한 JSON 데이터로 Excel 워크북을 생성합니다 (openpyxl 필요).

**5개 시트 구조:**

| 시트 | 행 | 컬럼 | 용도 |
|---|---|---|---|
| **개요** | ~75 | 2 | README + schema reference + 근거등급 설명 + 사용법 |
| **Use Cases** | use case 수 | 52 | 메인 데이터 — AutoFilter, Freeze D2, **근거등급 conditional formatting** |
| **AI 기술 분포** | ~240 | 7 | long-format (use_case × subtype) — Pivot Table 즉시 가능 |
| **Companies** | 20 | 9 | 기업별 holistic view + use case 수·평균 신뢰도 자동 계산 |
| **전사 AI 참고** | enterprise-ai 수 | 52 | `wiki/enterprise-ai/` 사례 — Use Cases와 동일 컬럼 |

**Use Cases 신규 컬럼** (신뢰도 뒤): 근거등급 · 독립소스수 · 신선도 · 깊이 · 사례유형 · 규제노출 · KR 법규 · KR 노조 · KR 언어 · KR 국내벤더. 출처1~3은 `sources_resolved`의 title(`[T1] 제목 (publisher)`)을 표시하고 url을 하이퍼링크로 연결 (source 페이지 없는 항목은 `(미해석) slug`).

**Excel 활용법:**
- **필터**: Use Cases 시트 → 헤더 dropdown (산업·지역·AI 기술·근거등급·사례유형 등)
- **정렬**: 헤더 우클릭 → 정렬 (근거등급 → 신뢰도 순 권장)
- **피벗 heatmap**: AI 기술 분포 시트 → Insert → PivotTable → 행=AI 기술 (소), 열=HR 대분류, 값=COUNT
- **근거등급 색상**: 자동 (A 녹 / B 파랑 / C 노랑 / D 회색). 신선도 stale은 옅은 주황, 깊이 stub은 회색 기울임
- **한국 사례**: 지역 컬럼에 🇰🇷 KR + 옅은 노란 배경 자동 highlight

## 4. 업데이트 방법

wiki에 use case를 추가·수정한 후:

```bash
PYTHONIOENCODING=utf-8 python scripts/build_all.py
```

이 한 줄이면 끝. 새 use case가 추가됐거나 기존 페이지가 수정됐으면 자동으로 반영됩니다. (근거 등급까지 갱신하려면 그 전에 `python scripts/grade.py` 실행.)

## 5. HTML 산출물의 3가지 뷰

### Category View (기본)
- 7개 HR 카테고리별로 use case 카드 나열
- 각 카드: company + 칩 + Evidence 배지 + **headline (1문장 요약)** + tags + impact 요약
- 카드 클릭 → 펼침: 제목·Confidence · Pain Point · Process Flow (HTML/CSS 박스 → 화살표 → 박스) · System | Data | Model · Output · Impact Before → After · AI 기술 분류 · 한국 적용성 · Consulting Angle · Sources
- 맨 아래: **전사 AI 플랫폼 사례 (참고)** 접힘 섹션

### Company View
- 주요 기업별 holistic 뷰: 설명 + **HR AI 전략/테마** + 카테고리 커버리지 바
- 소속 use case별 상세 (칩·배지·confidence · 프로세스·시스템·데이터·Impact · 한국 적용성 · Sources)
- 기업 수준 Consulting Angle

### Matrix View
- 기업 × 카테고리 교차 테이블 (use case만, 전사 AI 참고 제외)
- 셀에 confidence 점수 색상 표시 (녹/노/빨)

## 6. 필터 기능

| 필터 | 설명 |
|---|---|
| **검색** | 기업명·벤더·제목·태그로 실시간 필터 |
| **Industry** | 산업별 (finance, tech, pharma 등) |
| **Region** | 지역별 (Korea, N. America, Europe, APAC) |
| **AI 기술** | 5 대분류 |
| **Evidence** | 근거 등급 (A만 / A+B / 전체). 미산정 페이지는 "전체"에서만 표시 |
| **stub 숨기기** | `depth: stub` 카드 숨김 (기본 on) |
| **🇰🇷 한국만** | 한국 사례만 표시 |
| **다크 모드** | ☽ 버튼으로 전환 |

필터는 use case와 전사 AI 참고 섹션에 함께 적용되고, 카운트(`n / N`)는 use case 기준이다.

## 7. 커스터마이징

### 특정 클라이언트에 맞춰 필터링된 버전을 만들려면

`extract_v3.py`의 출력 JSON을 수정하면 됩니다:

```python
# 예: 금융 산업 클라이언트에게만 보여줄 버전
import json
with open('wiki/exports/usecases.json') as f:
    data = json.load(f)
filtered = [uc for uc in data if 'finance' in uc.get('industry', []) or 'banking' in uc.get('industry', [])]
with open('wiki/exports/usecases_finance.json', 'w') as f:
    json.dump(filtered, f, ensure_ascii=False)
```

그런 다음 `build_html_v6.py`에서 JSON 경로를 변경하고 실행하면 금융 특화 버전이 생성됩니다. (전사 AI 참고 섹션을 빼려면 `enterprise_ai.json`을 빈 배열 `[]`로 두면 섹션 자체가 사라짐.)

### 색상·폰트 변경

`build_html_v6.py` 내 CSS의 `:root` 변수를 수정:

```css
:root {
  --accent: #2563eb;   /* 메인 accent 색상 */
  --cat-ta: #2563eb;   /* Talent Acquisition 색상 */
  /* ... */
}
```

Evidence 배지 색은 `.gb-A` ~ `.gb-D`, 칩 색은 `.tg.ct` / `.tg.vp` / `.tg.reg` / `.tg.stale` / `.tg.stub`.

## 8. 주의사항

- **Mermaid.js를 사용하지 않습니다** — 브라우저 렌더링 불안정 문제로 모든 도식은 HTML/CSS로 직접 구현
- **CDN 의존**: Pretendard 폰트만 CDN에서 로드. 완전 오프라인이 필요하면 폰트를 base64로 인라인 가능
- **파일 크기**: HTML ~780KB. 이메일 첨부 제한(보통 10~25MB)보다 훨씬 작음
- **internal 페이지**: `visibility: internal`은 세 스크립트 모두에서 걸러지며 `build_all.py`가 lint의 `internal-in-export`로 한 번 더 확인. 그래도 산출물을 외부에 보내기 전에 `lint.py`가 깨끗한지 확인 권장
- **sources 해석 실패**: `sources/<slug>.md`가 `wiki/sources/`에 없으면 HTML에는 slug가 회색 모노스페이스로, Excel에는 `(미해석) slug`로 표시됨. 빌드 로그의 "sources resolved" 수치로 확인
- **마크다운 잔존 주의**: 새 use case 작성 시 `**`, `[[]]` 등이 있으면 extract_v3.py가 HTML로 변환하지만, 복잡한 마크다운(테이블, 코드블록 등)은 깨질 수 있음 → Summary/Problem/Impact 섹션은 **단순 텍스트 + bullet 정도만** 사용 권장

## 9. 전체 흐름

```
scripts/lint.py --json ──→ internal-in-export 있으면 중단
                                                            (build_all.py)
wiki/usecases/*.md       ──┐
wiki/enterprise-ai/*.md  ──┤                     usecases.json ──────┐
wiki/sources/*.md (해석) ──┼──→ extract_v3.py ──→ enterprise_ai.json ─┼──→ build_html_v6.py ──→ hr-ai-usecase-collection.html
wiki/companies/*.md      ──┘                     companies.json ─────┤
                                                                     └──→ build_excel.py ────→ hr-ai-usecase-collection.xlsx
wiki/reference/*.md  ──→ (export 안 함)
```

wiki를 수정할 때마다 `PYTHONIOENCODING=utf-8 python scripts/build_all.py` 한 줄만 실행하면 HTML·Excel이 최신 상태로 재생성됩니다.
