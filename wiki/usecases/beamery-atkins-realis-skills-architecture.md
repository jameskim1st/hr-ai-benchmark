---
title: "AtkinsRéalis — Beamery 기반 Skills Architecture (89% 스킬매핑 시간↓, Forrester 467% ROI)"
slug: beamery-atkins-realis-skills-architecture
primary_category: Strategic Workforce & Governance
subcategory: Workforce Planning
tags: [skills-mapping, job-architecture, beamery, forrester-roi, engineering]
company: AtkinsRéalis
industry: [engineering, construction]
region: [global]
employee_class: [기술사무직]
vendor: [Beamery]
vendor_type: [talent-marketplace]
output: "Skills Inference 엔진의 role별 핵심 skill 추출 (90% 적합도) + Dynamic Job Architecture (role/family/proficiency) + Workday/SAP 동기화용 skills taxonomy (1,200 JD → 40 역할 통합)"
ai_tech_type: [generative, predictive]
ai_tech_subtype: [information-extraction, clustering-classification, recommendation-ranking]
stage: production
frequency: monthly
first_seen: 2025
last_confirmed: 2025
confidence: 0.35               # Tier 1 Forrester TEI(+0.35) + Tier 3 vendor(+0.10) - platform-wide TEI not AtkinsRéalis specific = 0.35
consulting_angle_status: filled
sources:
  - "Beamery case study https://beamery.com/resources/case-studies/case-study-atkins-realis"
  - "Beamery Flex case study https://beamery.com/resources/case-studies/job-architecture-case-study-flex-skills-based-hiring-ai"
  - "Forrester TEI (referenced by Beamery)"
related_usecases:
  - jnj-digital-talent-platform-skills-ai
  - visier-vee-people-analytics
related_vendors: []
---

# AtkinsRéalis + Flex — Beamery Skills Architecture

## Summary

**AtkinsRéalis** ($8.6B 엔지니어링)가 Beamery로 skills-based 채용 전환. ⚠️ 벤더 주장: 신규 채용자가 **25% 빨리 성과 마일스톤** 도달, best-fit 후보 식별 **30% 시간↓**, 후보 engagement **40%↑**. **Flex** (전자 제조)는 skills mapping을 **89% 단축** (4~6개월→17일), **1,200+ JD를 40개 역할 아키텍처로** 통합, 스킬 추론 **90% 적합도**. **Forrester TEI**: Beamery 플랫폼 전체 **467% ROI**.

## Solution Architecture

### A. Process

- **Before**: 정적 직무 기술서·수동 skills 매핑 (4~6개월 소요), 부서별 분절된 skills 데이터
- **After**:
  1. 기존 직무 기술서·HRIS·프로젝트 이력 등 fragmented data 업로드
  2. Beamery Skills Inference 엔진이 role별 핵심 skill 추출 (⚠️ 벤더 주장 90% 정확도)
  3. Dynamic Job Architecture 자동 생성 — role/family/proficiency level 매핑
  4. HRBP·HR tech 팀이 taxonomy 검토·승인
  5. Workday/SAP SuccessFactors로 동기화하여 채용·내부이동·L&D에 활용
  6. 시장·내부 시그널 변화 시 skills blueprint 자동 갱신
- **HITL**: HR/COE가 inferred skills taxonomy의 role mapping 승인
- **Frequency**: 초기 17일 구축 후 continuous refresh
- **Source**: Beamery Job Architecture product page


## Impact / Metrics (기대효과)

### 기대효과 요약
Skills-based 채용으로 성과 마일스톤 도달 25% 가속, 후보 식별 시간 30% 단축, Flex는 skills mapping 89% 단축 (벤더 주장 기반).

### AtkinsRéalis ($8.6B 엔지니어링)
| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| 성과 마일스톤 도��� 속도 | **25% 빠름** (Beamery 채용자) | Beamery case study | ⚠️ 벤더 주장 |
| Best-fit 후보 식별 시간 | **30%↓** | Beamery case study | ⚠️ 벤더 주장 |
| 후보 engagement | **40%↑** | Beamery case study | ⚠️ 벤더 주장 |

### Flex (전자 제조)
| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| Skills mapping 시간 | **89%���** (4~6개월→17일) | Beamery case study | ⚠️ 벤더 주장 |
| JD 통합 | **1,200+ JD → 40개 역할** | Beamery case study | ⚠️ 벤더 주장 |
| 스킬 추론 적합도 | **90%** (첫 ���뷰) | Beamery case study | ⚠️ 벤더 주장 |

### Platform-wide
| 지표 | 값 | 출처 | 성격 |
|---|---|---|---|
| ROI | **467%** | Forrester TEI | ✅ Fact (Tier 1) |

## Consulting Angle

- **Job Architecture AI의 대표 사례**: Flex의 "1,200 JD→40역할" 통합은 [[workday-illuminate-job-architecture]]와 같은 도메인이지만 **실제 deployment + metric**이 있음
- **Forrester 467% ROI**: HireVue의 134%를 크게 상회, Tier 1 독립 검증
- **J&J(MIT CISR, 스킬 추론)과의 비교**: J&J는 학술 검증(정확도), Beamery는 Forrester(ROI) — 검증 축이 다름
