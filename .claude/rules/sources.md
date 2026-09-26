# Source Tiers & Confidence

### Source Tiers
모든 소스 페이지(`wiki/sources/<slug>.md`)는 frontmatter에 `tier` 필드를 가진다.

| Tier | 정의 | 예시 | 기본 confidence 기여 |
|---|---|---|---|
| 1 | 분석기관·권위 프레임워크 | Gartner, McKinsey, Deloitte, Bersin, Hackett, MIT SMR, HBR | +0.35 |
| 2 | HR 전문 미디어·리서치 | AIHR, HR Brew, HR Dive, HR Executive, SHRM, CIPD | +0.20 |
| 3 | 벤더 1차 소스 | Workday/SAP/Oracle/Eightfold/Gloat/Paradox 공식 blog·release | +0.10 (주장임을 감안) |
| 4 | 실사례 신호 | 기업 press release, 컨퍼런스 발표, 10-K, 채용공고, 학술(SSRN/arXiv) | +0.15 |

### Use Case Confidence 공식 (가이드)
```
base = Σ(source tier 기여)
recency_modifier = +0.10 if last_confirmed within 6 months
                   0.00 if 6–12 months
                  -0.15 if 12–24 months
                  -0.30 if >24 months
contradiction_penalty = -0.20 per unresolved contradiction
confidence = clamp(base + recency_modifier + contradiction_penalty, 0.0, 1.0)
```

confidence < 0.4 인 use case는 `wiki/log.md`에 경고로 남기고, 다음 `/hr-lint`에서 재확인 대상이 된다.

### Confidence 감쇠 원칙
- 어떤 claim이 last_confirmed로부터 12개월이 지나면 자동으로 `stale` 플래그
- lint가 stale을 찾아 재검증 요청 → autoresearch 또는 수동 확인

---

# Source Whitelist

아래 소스는 새로 발견되면 **무조건 ingest 후보**이며 `scripts/fetch_sources.ps1`의 RSS 피드에도 포함된다.

**Tier 1 (분석기관)**:
- Gartner HR (articles, research notes)
- McKinsey People & Organizational Performance
- Deloitte Human Capital Trends
- Josh Bersin Co. / Bersin Academy
- Hackett Group HR research
- MIT Sloan Management Review (HR/workforce 주제)
- Harvard Business Review (HR/talent 주제)

**Tier 2 (HR 전문 미디어)**:
- AIHR (aihr.com)
- HR Brew (hr-brew.com)
- HR Dive (hrdive.com)
- HR Executive (hrexecutive.com)
- SHRM (shrm.org)
- CIPD People Management (영국)
- TLNT / ERE (채용 중심)
- LinkedIn Talent Blog

**Tier 3 (벤더 primary, 수동 whitelist)**:
- Workday, SAP SuccessFactors, Oracle HCM, ServiceNow HR, Microsoft Viva
- Eightfold, Gloat, Fuel50, Beamery, Phenom, Paradox, HireVue
- Visier, Lattice, 15Five, BetterUp
- 국내: 원티드랩, 잡코리아, 마이다스아이티, 플렉스, 시프티, 아이클라우드

**Tier 4**: 키워드 트리거 기반 (회사명 + "AI" + "HR") — 자동 포착, 수동 승인 후 ingest

---


# 2026-09-27 개정 — Source 페이지 필수 필드와 근거 등급

Karpathy 패턴의 원칙은 "raw가 진실의 원천"이다. 이를 강제하기 위해 모든 source 페이지는 다음 frontmatter를 가진다:

```yaml
title: "<원문 제목>"
url: "<url>"                    # 내부 자료는 internal
publisher: "<매체·기관·회사>"
tier: 1|2|3|4
source_type: analyst|media|vendor|company|academic|government|consulting-document
independent: true|false         # tier 1·2·academic·government = true, vendor·company self-report = false
publication_date: YYYY-MM-DD    # 일 불명이면 YYYY-MM
ingested_at: YYYY-MM-DD
raw: raw/articles/<file>.md     # fetch_raw.py 스냅샷 경로 (필수). 내부 자료는 raw/internal/...
snapshot_quality: full|partial|llm-extracted|unavailable
supports: [<usecase slugs>]
```

본문: `## Summary`(3~5줄) · `## Key Quotes`(raw에서 verbatim 복사한 인용 3~5개, 각각 뒷받침하는 주장 명시) · `## Limitations`.

- **Tier 판정**: 1 분석기관·권위 프레임워크 / 2 독립 매체(HR 전문지 + 일반 경제·IT 매체) / 3 벤더 1차 자료 / 4 도입 기업 발표·보도자료·학술·정부. Tier는 "누가 말했나", `independent`는 "이해관계가 없나"를 뜻한다.
- **Compilation 금지**: 2026-04~05에 만든 4개 compilation source(`kr-conglomerate-2026-q2-research` 등)는 `deprecated: true`로 남겨두고 링크 해석용으로만 유지한다. 새로 만들지 않는다.
- **근거 등급(evidence_grade)**은 `scripts/grade.py`가 use case의 `sources:`를 읽어 계산한다 (A 독립 2+ / B 독립 1 / C 벤더·자사만 / D 없음). 기존 §4 "Confidence 공식"의 tier 가중치 합산은 폐기하고, `confidence`는 등급 파생값으로만 쓴다.
- **Grounding 검사**: `scripts/check_quotes.py`가 use case의 수치 토큰이 인용 source의 raw 텍스트에 있는지 확인한다. 미확인 비율 50% 초과는 lint warning.
