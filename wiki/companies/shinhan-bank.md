---
name: 신한은행
type: company
industry: [finance, banking]
region: [kr]
headquarters: 서울 중구
size_employees: 14000
public: true
ticker: 신한지주
ingested_first: 2026-05-05
last_confirmed: 2026-04-01
---

# 신한은행

한국 4대 시중은행 (KB·신한·우리·하나) 중 하나. **HR AI 사례 가장 풍부**: (1) 'AI ONE' 직원 업무비서 플랫폼 (40+ AI 통합), (2) 'AI 정기인사 알고리즘' (2,414명 시뮬레이션), (3) 신한카드 'AINa' 플랫폼 (그룹사). 자체 LLM·자체 알고리즘 선호 — 데이터 주권·금융 규제 대응이 driver.

## HR AI 전략 / 핵심 테마

- **자체 통합 platform 'AI ONE'**: 40+ AI를 단일 인터페이스 + Speech-to-AI 모바일/태블릿
- **AI 인사이동 알고리즘**: 2020~ 운영, 신한·KB 한국 large-scale 인사 AI 양대 reference
- **그룹사 확산**: 신한카드 'AINa' (AI 5025 프로젝트) — 그룹 차원 LLM 활용
- **자체 GenAI**: 외부 모델 의존 축소 — 데이터 주권 강조

## 📊 신한은행 HR AI Use Cases

```dataview
TABLE WITHOUT ID
  file.link AS "Use Case",
  primary_category AS "카테고리",
  confidence AS "신뢰도"
FROM "wiki/usecases"
WHERE contains(company, "신한")
SORT confidence DESC
```

## Consulting Angle

- **KR 금융권 사내 AI 플랫폼 Top 3 reference**: KB AI HR Deep Change·하나 지식챗봇·미래에셋 AI Assistant와 비교덱
- **자체 LLM·통합 platform 모델**: KR 대기업 산발 AI 통합 솔루션 — JPMorgan LLM Suite와 양 방향
- **2026 Q3-Q4 KR 금융 컨설팅 deck 핵심 reference**
- **반면교사**: 자사 발표 metric (30분 절감·80% 자동화 목표)는 외부 인용 시 출처 명시 필수
