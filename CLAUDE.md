# HR AI Benchmark Wiki — Agent Schema (core)

이 저장소는 **HR 부문 AI 적용 use case**를 축적·검증·갱신하는 LLM Wiki다 (Karpathy 패턴: raw → wiki → schema). 사용자는 컨설턴트 1인이며, 산출물은 "클라이언트 앞에 가져가도 부끄럽지 않은 품질"이 기준이다. 기본 언어 한국어, 인용은 원문 유지, 날짜는 `YYYY-MM-DD`.

상세 규칙은 아래 파일에 있고 이 문서와 함께 로드된다:
@.claude/rules/taxonomy.md
@.claude/rules/usecase-schema.md
@.claude/rules/sources.md
@.claude/rules/protocols.md

---

## 1. 레이아웃

```
raw/            원본 (불변). articles/ vendors/ reports/ feeds/ inbox/(클리퍼 캡처 → ingest 후 이동) internal/(기밀)
wiki/
  index.md      scripts/build_index.py 가 생성 — 손으로 편집 금지
  log.md        append-only 이력
  usecases/     ★ HR 프로세스에 AI를 적용한 사례 1건 = 1페이지 (도입 사례 + 벤더 제품)
  enterprise-ai/ 전사 GenAI 플랫폼 사례 (참고용 — use case 카운트 제외)
  reference/    법령·리포트·맥락 페이지 (규제·시장 데이터, use case 아님)
  sources/      기사 1건 = source 1페이지, 반드시 raw 스냅샷(`raw:`)에 연결
  vendors/ companies/ categories/ syntheses/ exports/
scripts/        lint.py grade.py check_quotes.py fetch_raw.py build_index.py build_all.py (extract_v3 → build_html_v6 → build_excel)
.claude/        rules/ skills/(hr-ingest hr-lint hr-verify hr-research hr-digest hr-compare) agents/hr-verifier.md settings.json(hooks)
```

## 2. 불변 원칙 (위반 시 hooks·lint가 막는다)

1. **raw/ 는 수정·삭제하지 않는다.** 새 스냅샷은 `python scripts/fetch_raw.py <url> <raw path>`로만 만든다. (PreToolUse 훅이 raw/ 쓰기를 차단)
2. **기사 1건 = source 1페이지.** 여러 URL을 묶은 compilation source 금지. source 페이지는 `raw:` 경로와 `independent:` 필드를 가진다.
3. **Grounding Invariant** — use case의 수치·시스템명·모델명·팀 규모·날짜는 인용한 source의 raw 스냅샷에 verbatim으로 존재해야 한다. `python scripts/check_quotes.py <slug>`가 검사한다. 근거가 없으면 `_미공개 (not disclosed)_`.
4. **Hedging 보존** — 소스가 "계획·검토 중·추정·예정"이라 쓴 것을 확정형으로 승격하지 않는다. 벤더 자료는 `⚠️ 벤더 주장:`, 도입 기업 발표는 `⚠️ 자사 보고:` 접두사.
5. **금지어** — 아마도·추정·보통·일반적으로·대개·대체로·통상·likely·probably·typically·generally. 쓰고 싶으면 그 문장을 쓰면 안 된다는 신호.
6. **부재 확인** — "페이지가 없다"고 말하기 전에 반드시 `grep -ril`로 확인한다.
7. **숫자는 스크립트가 계산한다** — `confidence`·`evidence_grade`·`corroborated_by`·`freshness`·`depth`는 `python scripts/grade.py`가 쓴다. 손으로 고치지 않는다. index·카운트도 `build_index.py`.
8. **자동 수정 금지** — lint·verify는 보고만 한다. 수정은 사용자 승인 후 한 건씩.
9. **기밀** — 클라이언트·제안서 자료에서 나온 페이지는 `visibility: internal`. export(HTML/Excel)에서 자동 제외된다.
10. **모든 변경은 `wiki/log.md`에 append** (`## [YYYY-MM-DD] <op> | ...`, op: ingest·lint·verify·research·digest·compare·refactor·manual-edit).

## 3. 근거 등급 (evidence_grade) — 인용 가능 기준

| 등급 | 정의 | 제안서 사용 |
|---|---|---|
| **A** | 서로 다른 독립 소스(Tier 1·2, 학술, 정부) 2개 이상 | ✅ reference case로 인용 |
| **B** | 독립 소스 1개 | ✅ 조건 명시하고 인용 |
| **C** | 벤더·자사 보고(Tier 3·4)만 | ⚠️ "벤더 주장"으로만 |
| **D** | 소스 없음·미확보·stub | ❌ 인용 금지 |

`confidence`는 등급 기반 파생값(A 0.70 / B 0.45 / C 0.25 / D 0.10 + 최신성 ±0.1·0.2 − 미해결 contradiction 0.15)이며 필터용 숫자일 뿐이다. `depth`(full/partial/stub)는 A~E 섹션 실질 내용과 Mermaid 유무로 계산한다.

## 4. 페이지 유형 판정

- **usecases/**: 특정 HR 프로세스(채용·온보딩·L&D·성과·보상·EX/HR Ops·전략/거버넌스)가 AI로 바뀐 사례. `case_type: adoption`(도입 기업 명시) 또는 `vendor-product`(벤더 제품, 고객 다수).
- **enterprise-ai/**: 전사 GenAI 플랫폼·코파일럿 배포(직원 Q&A 포함)로 HR 프로세스 변화가 소스에 명시되지 않은 것.
- **reference/**: 법령(AI 기본법·EU AI Act), 분석 리포트(Deloitte HC Trends), AI가 아닌 제도 개편.
- 채용·평가·승진·해고·이탈 예측·근태 감시에 관여하면 `regulatory_exposure: [kr-high-impact, eu-annex-iii]`.

## 5. 운영 루프

```
raw/inbox (클리퍼) ──/hr-ingest──▶ sources + usecases ──grade.py──▶ lint.py ──▶ build_all.py (HTML/Excel)
      ▲                                   │
 /hr-research (후보+스냅샷만)         /hr-verify (hr-verifier 서브에이전트: 주장↔raw 대조)
                                          ▼
                             /hr-lint (스크립트 결과 + LLM 판단) → /hr-digest (주간) → /hr-compare
```

- 주간 자동: `scripts/weekly.ps1` (grade → lint 리포트 → index → export → inbox triage dry-run → digest → commit). 등록은 `scripts/register_weekly_task.ps1`.
- Hooks: raw/ 쓰기 차단(PreToolUse), wiki/ 저장 직후 `lint.py --quick`(PostToolUse, critical이면 즉시 수정).
- 회귀 평가: `python scripts/eval_qa.py` (evals/golden-qa.json — wiki만 보고 답해야 하는 질문 30개).

## 6. 컨설팅 관점 (모든 use case 필수)

`## Consulting Angle`에 ① 참고 가능한 산업·규모 ② 바로 쓸 제안서/워크숍 용도 ③ 반면교사라면 경고할 리스크 ④ 파생 질문 ⑤ 한국 적용성(법규·노조·언어·국내 벤더 지원 — frontmatter `kr_law/kr_union/kr_language/kr_vendor`)을 쓴다. 비어 있으면 lint가 경고한다.

프로젝트 메모리: `C:\Users\user\.claude\projects\c--AI-AI-HR\memory\` 및 `c--AI-AI-HR-Benchmark\memory\`.
