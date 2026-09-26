---
type: research-note
generated_at: 2026-09-27
topic: LLM Wiki 패턴의 2026-04 → 2026-09 진화 — 도구·논문·Claude Code 기능·HR AI 피더 소스
purpose: system-review-2026-09-27 의 §5 근거. 각 항목 끝 [검증됨]=1차 출처 확인, [2차]=요약만 확인, [추정]=해석
tags: [llm-wiki, research, tooling, provenance, claude-code]
---

# LLM Wiki 동향 리서치 (2026-09-27)

> 리서치 서브에이전트 산출을 정리한 참고 노트. 본 wiki의 use case 데이터가 아니므로 export 대상이 아니다.

## 1. Karpathy 원문과 커뮤니티 정제

- 원문 gist(2026-04-04): raw/ → wiki/ → schema 3계층, index.md·log.md, Ingest/Query/Lint 3작업, "bookkeeping이 진짜 비용". 공식 v2는 없음. https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f [검증됨]
- 스키마가 제품이다 — 위키 레이어만 만들고 스키마에 투자 안 한 포크가 실패. https://cozypet.github.io/llm-wiki-schema/ [검증됨]
- rohitg00 "v2" gist(신뢰도 점수·감쇠·4단 메모리) 및 그 코멘트 비판: "숫자 신뢰도는 정밀도가 권위를 가장", float 대신 source-chain, 훅보다 사람 게이트. https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2 [검증됨]
- 취할 것/버릴 것: 3단 신뢰 마커, reconciliation(재작성), pruning, 스케줄 에이전트 O / 벡터 검색(10만 토큰 이하면 grep이 낫다)·계층 메모리 X. "페이지 없음" 거짓 부정 → grep으로 부재 확인 규칙. https://theaioperator.io/p/karpathys-llm-wiki-v2-what-to-keep [검증됨]
- append→rewrite, 모순은 최신성·권위로 해소하고 패자는 사유와 함께 아카이브. https://theaioperator.io/p/i-rebuilt-karpathys-llm-wiki-heres [검증됨]
- 3개월 운영기(Zissa): 결정론적 lint, 인용문 원문 대조, Stop 훅. 10~15 ingest마다 lint, 소스 4개 이상이면 synthesis, ~100 소스에서 lint 필수. https://github.com/MetamusicX/zissa-wiki [검증됨]
- 저널리즘 실사용(Casey Newton): 매일 clipper→ingest, 그래도 원문 열어 환각 확인 필수, 페이지 비대화→compaction. https://www.platformer.news/karpathy-llm-wiki-journalism-productivity/ [검증됨]
- 1개월 회고(R&D World, 760페이지): 유지보수≈절약(손익분기). 스키마 강제·lint 스크립트·인라인 인용·감독형 에이전트·adversarial 검증. https://www.rdworldonline.com/is-karpathys-viral-llm-wiki-helpful-mostly-yes-one-month-in/ [검증됨]
- Cornell 회고: 핵심은 bookkeeping 규율. index가 컨텍스트에 들어가야 하므로 수백 페이지가 실질 상한. https://innovationhub.ai.cornell.edu/articles/teaching-an-ai-to-remember-what-i-learned-building-a-wiki-llm/ [검증됨]
- ETH Zurich(2026-02): LLM이 생성한 긴 CLAUDE.md는 성공률 하락·비용 +20%. 사람이 쓴 간결 파일만 소폭 개선. https://arxiv.org/html/2602.11988v1 [2차]

## 2. 구현·툴링

| 프로젝트 | 가져올 패턴 |
|---|---|
| Astro-Han/karpathy-llm-wiki (2.4k★) | **Grounding Invariant**(load-bearing 사실은 raw 파일에 verbatim 존재), `check_evidence.py`(보고만), triage New/Update/Disputed/No material, Status 블록. https://github.com/Astro-Han/karpathy-llm-wiki [검증됨] |
| atomicstrata/llm-wiki-compiler (2.1k★) | 주장 단위 소스+라인 범위 인용, `fresh/stale/orphaned/unverified`, `refresh --stale`, MCP `serve`. https://github.com/atomicstrata/llm-wiki-compiler [검증됨] |
| lucasastorian/llmwiki (1.6k★) | 폴더 워처 자동 ingest, MCP, 결정론적 lint. https://github.com/lucasastorian/llmwiki [검증됨] |
| Obsidian 플러그인 "Karpathy LLM Wiki" (54k DL) | 3단계 중복 탐지+병합, 5단 검색 캐스케이드, lint Smart Fix. https://community.obsidian.md/plugins/karpathywiki [검증됨] |
| MetamusicX/zissa-wiki | `wiki.py lint`(index drift·thin source·"새 소스가 건드렸어야 할 페이지"), `wiki.py quotes`(글자 대조), `[W]/[P]/[?]` epistemic 마커, Stop 훅·pre-commit·CI. [검증됨] |
| kfchou/wiki-skills | 결정론+LLM 하이브리드 lint, `wiki-audit` 각주 대조, strong mode(타 프로바이더 adversarial), `wiki-merge`. https://github.com/kfchou/wiki-skills [검증됨] |
| praneybehl/llm-wiki-plugin | 150페이지 초과 시 index 샤딩, 페이지 상한 400/800줄. https://github.com/praneybehl/llm-wiki-plugin [검증됨] |
| Obelyth/cortex | 검증 가능한 인용 read path — "인용 검증은 텍스트가 거기 있다는 것만 증명". https://github.com/Obelyth/cortex [검증됨] |
| Google OKF v0.2 (2026-06) | 마크다운+YAML 지식 번들 표준: 주장별 각주, `generated/verified/stale_after`. https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md [검증됨] |
| LangChain OpenWiki / WikiBench | reader agent가 위키만 보고 답하는 점수로 유용성 측정. [2차] |

합의된 추가 패턴: 결정론/LLM lint 분리, 인용문 원문 검증, freshness 상태, 명시적 supersession, 슬러그 dedup, Stop/pre-commit/CI 게이트, MCP 노출, 임베딩은 보류.

## 3. Claude Code (2026-09)

- Skills가 commands를 대체(보조 파일·`context: fork`·`allowed-tools`·`` !`cmd` `` 주입). `/skill-doctor`, `claude plugin eval`(9월). https://code.claude.com/docs/en/skills [검증됨]
- Hooks 30개 이벤트: `PreToolUse` deny(bypass 모드에서도 강제), `PostToolUse` matcher `Edit|Write` + `if: "Edit(wiki/**)"`, `Stop` 게이트, prompt/agent 타입 훅. https://code.claude.com/docs/en/hooks [검증됨]
- 스케줄: Cloud Routines(GitHub clone, 1시간 단위, 로컬 파일 없음) / Desktop scheduled task(로컬, 1분, PC 켜짐) / `/loop`. https://code.claude.com/docs/en/routines [검증됨]
- 서브에이전트 frontmatter: `tools`, `model`, `memory: project`, `isolation: worktree`. https://code.claude.com/docs/en/sub-agents [검증됨]
- Memory: CLAUDE.md 200줄 이하 권장, `.claude/rules/*.md` + `paths:`. https://code.claude.com/docs/en/memory [검증됨]

### PostToolUse 훅 예시 (settings.json) — 가이드 에이전트 제안, 적용 전 실제 테스트 필요
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "if": "Edit(wiki/**)|Write(wiki/**)",
        "hooks": [
          { "type": "command", "command": "python \"${CLAUDE_PROJECT_DIR}/scripts/lint.py\" --quick", "timeout": 30 }
        ]
      }
    ]
  }
}
```
- 종료 코드 2 = 차단(stderr가 사유). `--bare`, `--permission-prompts none` 같은 headless 플래그는 버전 의존이므로 `claude --help`로 확인 후 사용. [2차]

## 4. 환각 통제 연구

- CAMS(arXiv 2606.23989): 주장마다 verbatim 인용+문서 ID, 오프셋은 결정론적 해석. 귀속 정확도 38→64%. [검증됨 초록]
- Manufactured Confidence(2606.29279): 통합 과정에서 hedging이 확정으로 승격, 에이전트는 출처보다 확신도에 반응, 경고 태그는 무시됨 → hedging 보존 + 복수 독립 소스. [검증됨 초록]
- MemStrata(2606.26511): 임베딩 유사도로는 모순·중복 50%만 탐지, (주어·관계·목적어) 규칙으로 supersession. [검증됨 초록]
- SSGM(2603.11768): 저장 전 일관성 게이트, staged consolidation(검토 기간). [검증됨 초록]

## 5. HR AI 피더·택소노미

- SHRM State of AI in HR 2026(2026-04, n≈1,908): 6 practice area × top 20 use case, 채택률 공개. https://www.shrm.org/executive-network/insights/state-of-ai-hr-2026-5-critical-insights-chros [검증됨]
- Josh Bersin HR 2030(2026-04) / Superagent 6 family(2026-01): 카테고리만 공개, 목록은 Galileo 유료. https://joshbersin.com/2026/04/introducing-hr-2030-a-vision-for-agentic-human-resources/ [검증됨]
- Gartner Hype Cycle for AI in HR 2026(doc 8074065): 유료. [검증됨 URL]
- AIHR 2026: AI 유형 7종 × 라이프사이클 9영역. https://www.aihr.com/blog/ai-in-hr/ [검증됨]
- RedThread 2026 People Analytics Tech(22 theme × 163 벤더) [2차], Deloitte AI Dossier 80+ [검증됨], 미국 연방 AI Use Case Inventory 2,000+ [2차]
- 규제: 한국 AI기본법 시행령 2026-07-21 개정, 고영향 AI 가이드라인(2026-04-29) 채용 AI 예시 명시. https://www.bkl.co.kr/law/insight/newsletter/6245 [검증됨]. EU AI Act Annex III(고용) 의무 Digital Omnibus로 2027-12-02 연기, Art.71 공개 DB 미운영. [검증됨/2차]
- 택소노미 권고: 단일 통일 대신 crosswalk(기능 축 SHRM×Bersin×AIHR, AI 유형 축, 자율성 축 copilot→agent→superagent, 규제 축, 성숙도 축). [추정]

## 회의적으로 볼 것
- v2류 기능(감쇠·4단 메모리·벡터)은 수백 페이지 이하에서 미입증.
- LLM lint 자동 수정은 모든 운영 회고가 반대.
- Bersin·Gartner 목록은 유료 벽 → 자동 피더 불가. 공개 수치가 있는 SHRM이 기준선으로 실용적.
- Cloud Routines·Channels·agent 훅은 research preview.
