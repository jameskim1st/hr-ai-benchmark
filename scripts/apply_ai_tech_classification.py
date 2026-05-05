#!/usr/bin/env python3
"""
One-shot script: inject ai_tech_type and ai_tech_subtype frontmatter fields
into all 110 use case pages, based on LLM classification results from the
3 background agents (Tier A 37 + B 48 + C 25 = 110).

Inserts both fields immediately AFTER the `vendor_type:` line. Idempotent —
if the fields already exist, replaces them.
"""
import re
from pathlib import Path

BASE = Path(__file__).parent.parent
UC = BASE / "wiki" / "usecases"

# Combined classifications from agents A/B/C
# Format: slug -> (ai_tech_type list, ai_tech_subtype list)
CLASSIFICATIONS = {
    # ===== Tier A (37) =====
    "accenture-mass-genai-reskilling": (["generative"], ["summarization-qa"]),
    "cisco-ai-workforce-consortium-skills-evolution": (["predictive"], ["clustering-classification"]),
    "jpmorgan-llm-suite-redeployment": (["generative"], ["summarization-qa"]),
    "moderna-ask-hr-routing": (["generative", "predictive"], ["summarization-qa", "clustering-classification"]),
    "cisco-ai-assistant-hr-agentic": (["generative"], ["summarization-qa"]),
    "deloitte-zora-ai-hc-suite": (["generative", "predictive"], ["summarization-qa", "clustering-classification"]),
    "ibm-charlie-learning-ops-agent": (["generative", "predictive", "automation"], ["summarization-qa", "clustering-classification", "rpa"]),
    "ibm-hr-workforce-reduction-agentic": (["generative", "predictive", "automation"], ["summarization-qa", "prediction", "clustering-classification", "rpa"]),
    "korea-ai-basic-act-hr-compliance": ([], []),
    "microsoft-people-skills-inferred-ontology": (["generative", "predictive"], ["information-extraction", "clustering-classification", "recommendation-ranking"]),
    "walmart-openai-certification": (["generative"], ["summarization-qa"]),
    "amazon-connections-daily-pulse": (["predictive"], ["prediction", "clustering-classification"]),
    "jnj-digital-talent-platform-skills-ai": (["generative", "predictive"], ["information-extraction", "clustering-classification", "recommendation-ranking"]),
    "jpmorgan-ai-made-easy-upskilling": (["generative"], ["summarization-qa"]),
    "chipotle-paradox-olivia": (["generative", "predictive"], ["summarization-qa", "clustering-classification"]),
    "commonwealth-bank-ai-workforce": (["generative"], ["summarization-qa"]),
    "deloitte-2026-human-capital-trends-meta": ([], []),
    "ibm-blue-match-internal-mobility": (["generative", "predictive"], ["information-extraction", "recommendation-ranking", "clustering-classification"]),
    "jpmorgan-llm-suite-employee-productivity": (["generative"], ["summarization-qa"]),
    "kb-bank-ai-hr-deep-change": (["decision-optimization", "predictive"], ["optimization", "clustering-classification"]),
    "lloyds-banking-workday-genai-hr": (["generative"], ["summarization-qa"]),
    "mercy-health-ai-nursing-workforce": (["generative", "predictive", "recognition", "decision-optimization"], ["summarization-qa", "prediction", "speech-recognition", "optimization"]),
    "microsoft-viva-glint-copilot-sentiment": (["generative", "predictive"], ["summarization-qa", "clustering-classification"]),
    "siemens-servicenow-hr-gbs": (["generative", "predictive", "automation"], ["summarization-qa", "clustering-classification", "rpa"]),
    "walmart-ai-frontline-workforce": (["generative", "predictive"], ["summarization-qa", "clustering-classification"]),
    "walmart-ask-sam-workforce-ai": (["generative", "predictive", "recognition"], ["summarization-qa", "clustering-classification", "speech-recognition"]),
    "bosch-rob-hr-ai-assistant": (["generative", "predictive"], ["summarization-qa", "clustering-classification"]),
    "dbs-bank-hr-ai-talent-analytics": (["generative", "predictive"], ["information-extraction", "prediction", "recommendation-ranking", "clustering-classification"]),
    "goldman-sachs-gs-ai-assistant": (["generative"], ["summarization-qa"]),
    "ibm-predictive-attrition-comp-ai": (["predictive"], ["prediction", "recommendation-ranking"]),
    "midas-inair-ai-assessment-korea": (["predictive", "recognition", "generative"], ["prediction", "speech-recognition", "multimodal"]),
    "sap-successfactors-1h-2026-joule-agents": (["generative", "predictive"], ["summarization-qa", "recommendation-ranking", "clustering-classification"]),
    "schneider-electric-gloat-talent-marketplace": (["predictive"], ["recommendation-ranking"]),
    "shinhan-bank-ai-one-platform": (["generative", "recognition"], ["summarization-qa", "ocr", "speech-recognition"]),
    "sk-cc-adot-biz-hr-recruitment": (["generative", "predictive"], ["information-extraction", "summarization-qa", "clustering-classification"]),
    "sk-group-aibiz-25-companies": (["generative", "automation"], ["summarization-qa", "rpa"]),
    "workday-agent-system-of-record-asor": ([], []),

    # ===== Tier B (48) =====
    "amazon-hr-ai-restructuring": (["generative", "predictive", "automation"], ["summarization-qa", "clustering-classification", "rpa"]),
    "betterup-ai-coaching-twilio": (["generative", "predictive"], ["summarization-qa", "recommendation-ranking"]),
    "deloitte-claude-470k-employees": (["generative"], ["text-generation", "summarization-qa"]),
    "ibm-askhr-watsonx": (["generative", "predictive", "automation"], ["summarization-qa", "text-generation", "clustering-classification", "rpa"]),
    "ibm-watsonx-orchestrate-ta-agent": (["generative", "predictive"], ["summarization-qa", "recommendation-ranking", "clustering-classification"]),
    "jobkorea-hiring-center-talent-agent": (["generative", "predictive"], ["summarization-qa", "recommendation-ranking"]),
    "korea-electric-power-hr-bot": (["generative", "predictive"], ["summarization-qa", "recommendation-ranking"]),
    "mirae-asset-ai-assistant-platform": (["generative"], ["summarization-qa"]),
    "novartis-gloat-skills-marketplace": (["predictive", "generative"], ["recommendation-ranking", "information-extraction"]),
    "sap-joule-performance-goals-agent": (["generative", "predictive"], ["summarization-qa", "recommendation-ranking"]),
    "siemens-reskilling-internal-mobility": (["predictive"], ["recommendation-ranking"]),
    "sk-hynix-ask-ai-interview": (["generative", "predictive"], ["text-generation", "clustering-classification"]),
    "tcs-infosys-ai-reskilling-india": (["generative"], ["summarization-qa"]),
    "workday-sana-for-workday-lms": (["generative", "predictive"], ["text-generation", "multimodal", "summarization-qa", "recommendation-ranking"]),
    "docebo-ai-learning-lazboy": (["generative", "predictive"], ["text-generation", "summarization-qa", "recommendation-ranking"]),
    "fujitsu-hr-ai-skills-career": (["generative", "predictive"], ["summarization-qa", "recommendation-ranking"]),
    "hitachi-skye-hr-ai-assistant": (["generative", "automation"], ["summarization-qa", "rpa"]),
    "ibm-watson-recruitment": (["predictive"], ["clustering-classification", "recommendation-ranking", "prediction"]),
    "jpmorgan-goldman-sachs-hr-ai": (["generative", "predictive"], ["summarization-qa", "text-generation", "prediction", "recommendation-ranking"]),
    "meta-ai-performance-review-mandate": (["generative"], ["text-generation", "summarization-qa"]),
    "moderna-benefits-equity-gpts": (["generative"], ["summarization-qa"]),
    "moderna-self-review-gpt": (["generative"], ["summarization-qa"]),
    "sk-group-aict-ai-recruitment": (["generative", "predictive"], ["summarization-qa", "clustering-classification", "text-generation"]),
    "tampa-general-visier-people-analytics": (["predictive", "generative"], ["prediction", "summarization-qa"]),
    "workday-illuminate-performance-review-agent": (["generative", "predictive"], ["summarization-qa", "text-generation"]),
    "beamery-atkins-realis-skills-architecture": (["generative", "predictive"], ["information-extraction", "clustering-classification", "recommendation-ranking"]),
    "coca-cola-southwest-perceptyx-activate": (["generative", "predictive"], ["summarization-qa", "recommendation-ranking"]),
    "deloitte-workforce-analyzer-salesforce": (["generative", "predictive"], ["summarization-qa", "clustering-classification", "prediction"]),
    "hirevue-ai-assessment-bias-audit": (["predictive"], ["clustering-classification", "prediction"]),
    "hitachi-ema-agentic-hr-onboarding": (["generative", "automation"], ["summarization-qa", "rpa"]),
    "korea-gov-ai-hr-public-sector": (["generative"], ["summarization-qa", "text-generation"]),
    "lotte-job-based-hr-reform": ([], []),
    "microsoft-employee-self-service-agent": (["generative", "automation"], ["summarization-qa", "rpa"]),
    "pwc-ai-upskilling-65k": (["generative"], ["summarization-qa", "text-generation"]),
    "t-mobile-textio-dei-hiring": (["generative", "predictive"], ["summarization-qa", "clustering-classification"]),
    "textio-tmobile-inclusive-jd": (["generative", "predictive"], ["summarization-qa", "clustering-classification"]),
    "toshiba-microsoft-copilot-viva": (["generative", "predictive"], ["summarization-qa", "text-generation", "recommendation-ranking"]),
    "accenture-ai-learning-workforce": (["generative", "predictive"], ["summarization-qa", "recommendation-ranking"]),
    "adp-assist-payroll-ai": (["generative", "predictive"], ["summarization-qa", "clustering-classification", "prediction"]),
    "clap-ai-performance-korea": (["generative"], ["summarization-qa", "text-generation"]),
    "cultureamp-ai-coach-asana": (["generative", "predictive"], ["summarization-qa", "recommendation-ranking"]),
    "greetinghr-ats-ai-korea": (["predictive", "automation"], ["recommendation-ranking", "clustering-classification"]),
    "hsbc-eightfold-gloat-multi-vendor": (["predictive", "generative"], ["recommendation-ranking", "information-extraction", "clustering-classification"]),
    "phenom-merck-kgaa-talent-marketplace": (["predictive", "generative"], ["recommendation-ranking", "information-extraction"]),
    "qualtrics-adidas-employee-experience-ai": (["generative", "predictive"], ["summarization-qa", "clustering-classification", "prediction", "recommendation-ranking"]),
    "spring-health-general-mills-ai-eap": (["predictive"], ["recommendation-ranking", "prediction", "clustering-classification"]),
    "ukg-ai-workforce-scheduling-healthcare": (["decision-optimization", "predictive", "generative"], ["optimization", "recommendation-ranking", "summarization-qa"]),
    "zapier-enboarder-ai-onboarding": (["generative", "automation"], ["summarization-qa", "rpa"]),

    # ===== Tier C (25) =====
    "15five-kona-reup-ai-manager-coaching": (["generative", "recognition"], ["summarization-qa", "speech-recognition"]),
    "allegis-group-holistic-ai-governance": (["predictive"], ["clustering-classification"]),
    "bersin-galileo-learn-ai-native-lms": (["generative"], ["text-generation", "summarization-qa", "multimodal"]),
    "betterworks-nextgen-ai-performance": (["generative", "predictive"], ["summarization-qa", "clustering-classification"]),
    "ericsson-degreed-ai-skills-upskilling": (["generative", "predictive"], ["summarization-qa", "recommendation-ranking"]),
    "flex-korea-hr-ai-saas": (["generative", "recognition"], ["summarization-qa", "ocr"]),
    "lattice-ai-performance-summarization": (["generative", "predictive"], ["summarization-qa", "prediction"]),
    "lgcns-agentic-ai-hr": (["generative", "predictive"], ["summarization-qa", "information-extraction", "recommendation-ranking"]),
    "nestle-paradox-recruiting": (["generative", "predictive"], ["summarization-qa", "clustering-classification"]),
    "salesforce-orgvue-org-design-ai": (["predictive"], ["clustering-classification"]),
    "servicenow-now-assist-hr": (["generative", "predictive"], ["summarization-qa", "clustering-classification"]),
    "unilever-flex-gloat-talent-marketplace": (["predictive"], ["recommendation-ranking"]),
    "visier-vee-people-analytics": (["generative"], ["summarization-qa"]),
    "workday-illuminate-job-architecture": (["generative", "predictive"], ["summarization-qa", "clustering-classification"]),
    "cathay-pacific-hirevue": (["generative", "predictive", "recognition"], ["summarization-qa", "clustering-classification", "speech-recognition"]),
    "douzone-one-ai-year-end-tax": (["generative", "predictive", "automation"], ["summarization-qa", "information-extraction", "clustering-classification", "rpa"]),
    "eightfold-ai-talent-intelligence": (["generative", "predictive"], ["summarization-qa", "recommendation-ranking"]),
    "emirates-hirevue-volume-hiring": (["predictive", "recognition"], ["clustering-classification", "speech-recognition"]),
    "fuel50-lennox-internal-mobility": (["predictive"], ["recommendation-ranking"]),
    "mcdonalds-paradox-recruiting": (["generative", "predictive"], ["summarization-qa", "clustering-classification"]),
    "paychex-flex-agentic-workforce": (["predictive"], ["prediction", "clustering-classification"]),
    "samsung-multicampus-ai-learning": (["predictive"], ["recommendation-ranking"]),
    "syndio-pay-equity-ai": (["generative", "predictive"], ["summarization-qa", "recommendation-ranking"]),
    "wantedlab-ai-recruiting-agent": (["generative", "predictive"], ["summarization-qa", "information-extraction", "recommendation-ranking"]),
    "workday-illuminate-employee-sentiment": (["predictive"], ["clustering-classification"]),
}


# Validation: subtype must have its parent type
SUBTYPE_TO_TYPE = {
    "text-generation": "generative",
    "summarization-qa": "generative",
    "multimodal": "generative",
    "information-extraction": "generative",
    "prediction": "predictive",
    "clustering-classification": "predictive",
    "recommendation-ranking": "predictive",
    "ocr": "recognition",
    "speech-recognition": "recognition",
    "optimization": "decision-optimization",
    "rpa": "automation",
}


def yaml_list(items):
    """Format Python list as YAML inline list with brackets."""
    if not items:
        return "[]"
    return "[" + ", ".join(items) + "]"


def validate(slug, types, subtypes):
    """Each subtype must have its parent type included."""
    for st in subtypes:
        parent = SUBTYPE_TO_TYPE.get(st)
        if not parent:
            print(f"  WARN {slug}: unknown subtype '{st}'")
        elif parent not in types:
            print(f"  WARN {slug}: subtype '{st}' requires parent '{parent}' but type list = {types}")


def update_page(slug, types, subtypes):
    fp = UC / f"{slug}.md"
    if not fp.exists():
        print(f"SKIP {slug}: file not found")
        return False
    text = fp.read_text(encoding="utf-8")

    # Build new lines
    new_lines = (
        f"ai_tech_type: {yaml_list(types)}\n"
        f"ai_tech_subtype: {yaml_list(subtypes)}\n"
    )

    # Pattern A: fields already exist — replace both lines
    pat_existing = re.compile(
        r"^ai_tech_type:\s*\[[^\]]*\]\s*\n^ai_tech_subtype:\s*\[[^\]]*\]\s*\n",
        re.MULTILINE,
    )
    if pat_existing.search(text):
        new_text = pat_existing.sub(new_lines, text, count=1)
        fp.write_text(new_text, encoding="utf-8")
        return True

    # Pattern B: fields don't exist — insert after vendor_type line
    pat_vendor = re.compile(r"^(vendor_type:.*\n)", re.MULTILINE)
    m = pat_vendor.search(text)
    if not m:
        print(f"FAIL {slug}: no vendor_type line found")
        return False
    new_text = pat_vendor.sub(m.group(1) + new_lines, text, count=1)
    fp.write_text(new_text, encoding="utf-8")
    return True


def main():
    ok, fail = 0, 0
    print(f"Applying {len(CLASSIFICATIONS)} classifications...")
    for slug, (types, subtypes) in CLASSIFICATIONS.items():
        validate(slug, types, subtypes)
        if update_page(slug, types, subtypes):
            ok += 1
        else:
            fail += 1
    print(f"\nDone: {ok} updated, {fail} failed (of {len(CLASSIFICATIONS)} total)")


if __name__ == "__main__":
    main()
