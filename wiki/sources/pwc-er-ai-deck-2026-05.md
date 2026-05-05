---
title: "PwC Korea — ER (Employee Relations · 노무) AI 적용 컨설팅 자료"
url: internal
tier: 3
source_type: vendor
ingested_at: 2026-05-06
date_published: 2026
---

# PwC Korea ER AI 적용 컨설팅 자료

## 개요

PwC Strategy& Korea가 작성한 6 슬라이드 deck — ER (Employee Relations / 노무) 영역 AI 적용 현황 + To-Be 프로세스 재설계 권장. raw/etc/ 내부 자료 (외부 공개 X).

## ER 영역 정의 (PwC)

> ER 영역에서는 핵심적 판단 및 대면 교섭 영역을 제외한 **사실관계 정리·이슈 모니터링·내부 규정 해석·문서화** 등 지원 업무를 중심으로 AI가 도입되고 있음

## ER Value Chain (4단계)

1. **이슈 식별 및 접수**
2. **사실관계 확인 및 기준 검토**
3. **대응 및 협의 실행**
4. **후속 조치 및 리스크 관리**

## ER Player 별 AI 도입 현황

### 집단노사 영역
> "신속한 노사 이슈 대응을 위한 준비·지원"

| 단계 | 적용 AI | 벤더 |
|---|---|---|
| 이슈 식별 및 접수 | 노사 이슈 상시 모니터링 및 잠재 이슈 탐지 (관계 데이터로 위험 사례 기반 패턴 도출) | spire (Spire Energy + SAP SuccessFactors) |
| 사실관계 확인 및 기준 검토 | 노사 이슈 사실관계 정리 및 조사 (사건 관련 정보 자동 분류, 단계별 시점 관련 구조화) | spire |
| 대응 및 협의 실행 | 노사 대응 전략 수립 지원 (교섭 전략 수립 데이터·다양한 채널 텍스트 자동 분석) | Cisco Webex / Saakaroon |
| 후속 조치 및 리스크 관리 | 단협·노조규칙 기반 후속 운영 자동화 (단협·규칙을 시스템 rule로 입력, 후속 운영 자동화) | Adept Solid Solutions |

### 준법지원 영역
> "이슈 대응의 체계화와 일관된 처리 기준 확립"

| 단계 | 적용 AI | 벤더 |
|---|---|---|
| 이슈 식별 및 접수 | 고충 접수·내용 자동 분류 (제기 사유, 신고, 조사 의뢰 데이터 분석 기반으로 분류) | Waymo (HR Acuity 활용) |
| 사실관계 확인 및 기준 검토 | Compliance Assistant 챗봇 (시간 위험 자동 감별, 규정 변경 사항·자동 영향 분석) | Yelp (HR Acuity 활용) |
| 대응 및 협의 실행 | 처리 내역 자동 문서화 (사건 조사·처리 과정 데이터 기반으로 일관된 Resolution Note 자동 생성) | Anonymous Company |
| 후속 조치 및 리스크 관리 | 준법지원 통합 DB 구축 (최신 법령·규정 정보, 사건 관련 ER 데이터 통합 활용·후속 조치 전략 수립에 활용) | Hitachi (Pilot — Skye Companion) |

## 통합 시사점 (PwC)

### Player 별 벤치마킹 Summary

- **이슈 식별 및 접수**: AI 기반 이슈 조기 탐지·초기 분류 고도화
- **사실관계 확인 및 기준 검토**: 사실·기준 검토의 신속성 및 정합성 강화
- **대응 및 협의 실행**: 대면 협상 실행을 위한 자료 준비
- **후속 조치 및 리스크 관리**: 처리 결과 및 조치 이력의 체계적 축적

### 핵심 원칙
> AI가 데이터와 프로세스 흐름을 연결하되, **협상·대응·의사결정 등 핵심 Action은 사람이 수행**

### 업무 흐름 시사점
- 이슈 식별부터 후속 관리까지 전 단계가 끊김 없이 연결되는 업무 흐름 설계 필요
- 사전 예방 → 이슈 대응 → 후속 관리에 이르기까지 단계적 AI 개입

### AI 역할 배치
- AI 4단계 전반에 AI Agent를 배치하되, **핵심 판단·교섭·의사결정은 사람**이 수행하는 구조 설계
- AI가 담당하는 영역 범위: 데이터 수집·정리·분석, 문서화·생성, 노사·법률, 인사이트, 통합·관리·구조화·정형 활용 가능한 구조 확보 필요

## To-Be Process Structure 재설계

### As-Is 구조 한계
- 집단노사·준법지원 업무를 영역별로 분리 설계 → Case 처리 일관성 부재

### To-Be 재설계 기준
- Case별 완결성과 통합 연계성을 고려한 Workflow 구조
- **L2: Value Chain** (Case 처리 전반 Lifecycle): 이슈 식별·접수 → 사실관계·기준 검토 → 대응·협의 실행 → 후속 조치·리스크 관리
- **L3: Workflow Step** (공통 프로세스): 모니터링·접수 → 분석·계획 → 사실 조사 → 기준 검토 → 협상·대응 → 분석·검토·보고
- **L4: Case 유형별 분화** (집단노사·준법지원·개별노무 등 각 공통 Workflow Step에 fine-tuning)
- **L5: 실행 Task** (접수·조사·검토·승인·확장·결정·공유)

## ER 선도사 AI 적용 사례 종합

ER 4단계별로:
- **이슈 식별 및 접수**: 노사 이슈 조기 경보 / 고충 접수 및 담당자 자동 연계 / 법령 개정 모니터링 및 영향분석
- **사실관계 확인 및 기준 검토**: AI Compliance Assistant 챗봇
- **대응 실행 및 협의**: 교섭 전략 지원 Agent
- **후속 조치 및 리스크 관리**: 사건 처리 내역 자동 문서화 / 이행·실적 모니터링 / 처리 결과 공유

## Source 출처 (PwC slide 하단 인용)

- Soliday Solutions — AI for Employee & Labor Relations
- PSE Customer Case Study
- Spire Energy Customer Case Study
- SAP SuccessConnect 2018
- HR Acuity (다수 인용)
- Waymo Customer Story
- HR Acuity AI & Compliance Guide for HR Teams
- LiKHR AI Companion
- HR Executive
- Hitachi AI HR Companion "Skye" Case (2022)

## Note

⚠️ 본 source는 PwC Korea 내부 자료 (raw/etc/1000023757-762.jpg, 2026-05-06 ingest). 외부 공개 X.
PwC 인용 vendor 명칭 일부 OCR 신뢰도 낮음 (예: "Saakaroon", "Adept Solid Solutions") — 외부 검증 결과는 [[2026-05-06] ingest log]] 참조.
