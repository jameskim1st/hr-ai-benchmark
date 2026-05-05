---
title: "Interactive HTML 산출물 생성 가이드"
created_at: 2026-04-13
purpose: wiki의 81건 use case를 클라이언트 CHRO/임원에게 공유할 수 있는 단일 HTML 파일로 변환하는 방법
---

# Interactive HTML 산출물 생성 가이드

## 1. 이 산출물이 뭔가

wiki에 축적된 HR AI use case 81건을 **단일 HTML 파일**(~250KB)로 변환해서, 클라이언트 CHRO나 임원이 **브라우저에서 바로 열어볼 수 있는 인터랙티브 자료**를 만드는 것입니다.

- 별도 서버 불필요 (file:// 프로토콜로 작동)
- 이메일 첨부·USB 전달 가능
- 검색·필터·다크모드 지원
- 카테고리별 / 기업별 / 매트릭스 3가지 뷰

## 2. 파일 구조

```
scripts/
  extract_v3.py          ← wiki/*.md → JSON 추출 (Step 1)
  build_html_v6.py       ← JSON → HTML 변환 (Step 2)

wiki/exports/
  usecases.json          ← 81건 use case 데이터 (Step 1 산출)
  companies.json         ← 14개 기업 데이터 (Step 1 산출)
  hr-ai-usecase-collection.html  ← 최종 산출물 (Step 2 산출)
```

## 3. 생성 방법 (2단계)

### Step 1: 데이터 추출

wiki의 markdown 파일에서 frontmatter + 본문 핵심 섹션을 JSON으로 추출합니다.

```bash
cd c:\AI\AI-HR\Benchmark
python scripts/extract_v3.py
```

**추출되는 것:**
- `usecases.json` — 81건 use case별:
  - frontmatter (title, category, company, vendor, confidence, tags 등)
  - headline (Summary 첫 문장 — 카드 소제목용)
  - problem (Pain Point, HTML 변환됨)
  - impact_summary (기대효과 요약, HTML 변환됨)
  - consulting (Consulting Angle, HTML 변환됨)
  - system {} (Core HRIS, AI 배치, 배포 환경, 연동 등)
  - data {} (입력 소스, 규모, 전처리, RAG 여부, 거버넌스 등)
  - model {} (Foundation model, 유형, 제공 방식, 가드레일 등)
  - process_before (As-is 상태)
  - process_steps [] (To-be 프로세스 단계들)
- `companies.json` — 14개 기업별:
  - description (기업 설명 2~3줄)
  - strategy (HR AI 전략·테마)
  - consulting (Consulting Angle)

**마크다운→HTML 변환 포함:**
- `**bold**` → `<strong>bold</strong>`
- `- bullet` → `<ul><li>bullet</li></ul>`
- `[[wikilink]]` → 텍스트만 추출
- `\n` → `<br>`

### Step 2: HTML 생성

JSON 데이터를 HTML 파일 안에 JavaScript 변수로 임베딩하고, 인터랙티브 UI를 생성합니다.

```bash
python scripts/build_html_v6.py
```

**생성되는 HTML 구조:**
- Pretendard 한국어 폰트 (CDN)
- Mermaid.js 없음 — 모든 도식은 HTML/CSS로 직접 렌더
- 다크/라이트 모드
- 3개 탭 뷰 (Category / Company / Matrix)

## 4. 업데이트 방법

wiki에 use case를 추가·수정한 후 HTML을 재생성하려면:

```bash
# 1) JSON 재추출 (wiki 변경사항 반영)
python scripts/extract_v3.py

# 2) HTML 재생성
python scripts/build_html_v6.py
```

이 2줄이면 끝. 새 use case가 추가됐거나 기존 페이지가 수정됐으면 자동으로 반영됩니다.

## 5. HTML 산출물의 3가지 뷰

### Category View (기본)
- 7개 HR 카테고리별로 use case 카드 나열
- 각 카드: company + **headline (1문장 요약)** + tags + impact 요약
- 카드 클릭 → 펼침:
  - Pain Point
  - Process Flow (HTML/CSS 박스 → 화살표 → 박스)
  - System | Data | Model (3열 정보 블록)
  - Impact Before → After
  - Consulting Angle

### Company View
- 14개 주요 기업별 holistic 뷰
- 각 기업: 설명 + **HR AI 전략/테마** + 카테고리 커버리지 바
- 소속 use case별 상세 (프로세스·시스템·데이터·Impact)
- 기업 수준 Consulting Angle

### Matrix View
- 기업 × 카테고리 교차 테이블
- 셀에 confidence 점수 색상 표시 (녹/노/빨)

## 6. 필터 기능

| 필터 | 설명 |
|---|---|
| **검색** | 기업명·벤더·제목·태그로 실시간 필터 |
| **Industry** | 산업별 (finance, tech, pharma 등) |
| **Region** | 지역별 (Korea, N. America, Europe, APAC) |
| **Confidence** | 신뢰도 threshold (≥0.50 / ≥0.40 / ≥0.30) |
| **🇰🇷 한국만** | 한국 사례 11건만 표시 |
| **다크 모드** | ☽ 버튼으로 전환 |

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

그런 다음 `build_html_v6.py`에서 JSON 경로를 변경하고 실행하면 금융 특화 버전이 생성됩니다.

### 색상·폰트 변경

`build_html_v6.py` 내 CSS의 `:root` 변수를 수정:

```css
:root {
  --accent: #2563eb;   /* 메인 accent 색상 */
  --cat-ta: #2563eb;   /* Talent Acquisition 색상 */
  /* ... */
}
```

## 8. 주의사항

- **Mermaid.js를 사용하지 않습니다** — 브라우저 렌더링 불안정 문제로 모든 도식은 HTML/CSS로 직접 구현
- **CDN 의존**: Pretendard 폰트만 CDN에서 로드. 완전 오프라인이 필요하면 폰트를 base64로 인라인 가능
- **파일 크기**: ~250KB. 이메일 첨부 제한(보통 10~25MB)보다 훨씬 작음
- **마크다운 잔존 주의**: 새 use case 작성 시 `**`, `[[]]` 등이 있으면 extract_v3.py가 HTML로 변환하지만, 복잡한 마크다운(테이블, 코드블록 등)은 깨질 수 있음 → Summary/Problem/Impact 섹션은 **단순 텍스트 + bullet 정도만** 사용 권장

## 9. 전체 흐름

```
wiki/usecases/*.md (81건)  ──┐
                              ├──→ extract_v3.py ──→ usecases.json ──┐
wiki/companies/*.md (14건) ──┘                      companies.json ──┤
                                                                     ├──→ build_html_v6.py ──→ hr-ai-usecase-collection.html
                                                                     │
                                                        CSS + JS 템플릿 (스크립트 내장)
```

wiki를 수정할 때마다 `python scripts/extract_v3.py && python scripts/build_html_v6.py` 2줄만 실행하면 HTML이 최신 상태로 재생성됩니다.
