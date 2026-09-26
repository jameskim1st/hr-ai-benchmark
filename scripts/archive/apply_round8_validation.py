#!/usr/bin/env python3
"""
Round 8 — Agent B (Validation) 결과 적용:
  - 15건 use case에 독립 2nd source 추가 (frontmatter sources list)
  - confidence boost (+0.05 ~ +0.10)

각 entry: (slug, new_confidence, [(source_label, url), ...])
"""
import re
from pathlib import Path

BASE = Path(__file__).parent.parent
UC = BASE / "wiki" / "usecases"

UPDATES = {
    "accenture-mass-genai-reskilling": (0.75, [
        ("Accenture Reinvention Report (Gartner methodology)", "https://www.accenture.com/content/dam/accenture/final/accenture-com/document-2/Accenture-Reinvention-in-the-age-of-generative-AI-Report.pdf"),
    ]),
    "cisco-ai-workforce-consortium-skills-evolution": (0.75, [
        ("Cisco AI Workforce Consortium Full Report 2025", "https://www.cisco.com/content/dam/cisco-cdc/site/m/ai-workforce-consortium/documents/2025-ai-workforce-consortium-full-report.pdf"),
    ]),
    "jpmorgan-llm-suite-redeployment": (0.80, [
        ("McKinsey: JPM Derek Waldron AI-first bank culture interview", "https://www.mckinsey.com/industries/financial-services/our-insights/jpmorgan-chases-derek-waldron-on-building-an-ai-first-bank-culture"),
    ]),
    "workday-peakon-illuminate-employee-voice": (0.80, [
        ("Constellation Research: Workday Rising 2024 — AI Illuminate analysis", "https://www.constellationr.com/insights/news/workday-rising-2024-ai-illuminate-ai-agents-evisort-acquisition"),
    ]),
    "anaplan-workforce-analyst-ai-agents": (0.70, [
        ("Anaplan press 2025-12-09 (GlobeNewswire) + Gartner MQ Financial Planning Software 9X Leader", "https://www.globenewswire.com/news-release/2025/12/09/3202449/0/en/Anaplan-Introduces-Role-Based-AI-Agents-to-Advance-Industry-Leading-Enterprise-Scenario-Planning-and-Analysis-Platform.html"),
    ]),
    "cisco-ai-assistant-hr-agentic": (0.70, [
        ("Cisco engineering blog — Internal AI assistant 45M+ interactions", "https://blogs.cisco.com/cisco-on-cisco/cisco-secure-internal-ai-assistant"),
    ]),
    "ibm-charlie-learning-ops-agent": (0.70, [
        ("IBM official case study: HR ELOA cHaRlie", "https://www.ibm.com/case-studies/ibm-hr-eloa"),
        ("IntelligentHQ — IBM cHaRlie watsonx Orchestrate award-winning analysis", "https://www.intelligenthq.com/hr-transformation-ibm-leverages-watsonx-orchestrate-to-create-award-winning-ai-assistant-charlie/"),
    ]),
    "ibm-hr-workforce-reduction-agentic": (0.75, [
        ("WSJ Krishna interview via HR Asia: 8K layoff + AskHR + rehire nuance", "https://hr.asia/asia-pacific/ibm-lays-off-8000-to-embrace-ai-only-to-rehire-just-as-many/"),
    ]),
    "korea-ai-basic-act-hr-compliance": (0.75, [
        ("Littler Mendelson: Understanding South Korea's New AI Law (multinational employers)", "https://www.littler.com/news-analysis/asap/understanding-south-koreas-new-ai-law-key-considerations-multinational-employers"),
        ("Cooley LLP: South Korea AI Basic Act overview", "https://www.cooley.com/news/insight/2026/2026-01-27-south-koreas-ai-basic-act-overview-and-key-takeaways"),
    ]),
    "microsoft-people-skills-inferred-ontology": (0.70, [
        ("Forrester: Microsoft Viva Disrupts EX Operating System", "https://www.forrester.com/blogs/microsoft-viva-disrupts-todays-ex-operating-system/"),
    ]),
    "walmart-openai-certification": (0.75, [
        ("Retail Dive: Walmart taps OpenAI for employee training", "https://www.retaildive.com/news/walmart-openai-chatgpt-employee-training-certification/759317/"),
        ("HR Dive: Walmart OpenAI training certification", "https://www.hrdive.com/news/walmart-openai-chatgpt-employee-training-certification/759398/"),
    ]),
    "amazon-connections-daily-pulse": (0.65, [
        ("CNBC 2018: Amazon employee reaction to Connections + Forte (anonymity skepticism)", "https://www.cnbc.com/2018/03/30/amazon-employee-reaction-to-hr-programs-connections-forte.html"),
    ]),
    "jpmorgan-ai-made-easy-upskilling": (0.70, [
        ("McKinsey: JPM Derek Waldron interview — 'AI Made Easy' program direct mention", "https://www.mckinsey.com/industries/financial-services/our-insights/jpmorgan-chases-derek-waldron-on-building-an-ai-first-bank-culture"),
    ]),
    "ibm-blue-match-internal-mobility": (0.65, [
        ("Bersin (Tier 1, 2020-12): The Evolving Role of IBM in HR Marketplace — Blue Matching analysis (stale caveat)", "https://joshbersin.com/2020/12/the-evolving-role-of-ibm-in-the-hr-marketplace/"),
    ]),
    "kb-bank-ai-hr-deep-change": (0.65, [
        ("서울경제: AI에 인사 맡겼더니…'3시간 출퇴근 지옥' 탈출한 구 과장", "https://www.sedaily.com/NewsVIew/1Z5BAFO2IP"),
        ("전자신문 2022 단독: KB국민은행 AI 인사 시스템", "https://www.etnews.com/20221221000210"),
    ]),
}


def update_page(slug, new_conf, new_sources):
    fp = UC / f"{slug}.md"
    if not fp.exists():
        print(f"SKIP {slug}: not found")
        return False
    text = fp.read_text(encoding="utf-8")

    # 1. Update confidence in frontmatter
    # Match `confidence: <number>` (with possible inline comment)
    pat_conf = re.compile(r"^(confidence:\s*)([\d.]+)(\s*(?:#.*)?)$", re.MULTILINE)
    m = pat_conf.search(text)
    if not m:
        print(f"FAIL {slug}: no confidence field")
        return False
    text = pat_conf.sub(f"\\g<1>{new_conf:.2f}\\g<3>", text, count=1)

    # 2. Append new sources to frontmatter `sources:` list
    # Find sources block: starts with `sources:` and ends at next top-level key or `---`
    pat_sources = re.compile(
        r"^(sources:\s*\n(?:  -.*\n)*)",
        re.MULTILINE,
    )
    m = pat_sources.search(text)
    if not m:
        print(f"FAIL {slug}: no sources field")
        return False
    existing_sources = m.group(1)
    new_lines = ""
    for label, url in new_sources:
        # Use quoted form: '<label> <url>' (mimic existing inline citation pattern)
        new_lines += f'  - "{label} {url}"\n'
    new_sources_block = existing_sources + new_lines
    text = pat_sources.sub(new_sources_block, text, count=1)

    fp.write_text(text, encoding="utf-8")
    return True


def main():
    ok, fail = 0, 0
    for slug, (new_conf, new_sources) in UPDATES.items():
        if update_page(slug, new_conf, new_sources):
            ok += 1
            print(f"  +{new_conf:.2f} | {slug} (+{len(new_sources)} src)")
        else:
            fail += 1
    print(f"\nR8-B applied: {ok}/{len(UPDATES)} pages updated")


if __name__ == "__main__":
    main()
