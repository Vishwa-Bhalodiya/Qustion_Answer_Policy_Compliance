import json
from mistral_service import call_mistral


def calculate_overall_risk(comparisons):
    if not comparisons:
        return "High"

    high_risk_critical = False
    medium_count = 0
    total = len(comparisons)

    for item in comparisons:
        risk = item.get("risk_level", "Low")
        criticality = item.get("criticality", "Informational")

        if risk == "High" and criticality == "Critical":
            high_risk_critical = True

        if risk == "Medium":
            medium_count += 1

    if high_risk_critical:
        return "High"

    if medium_count / total > 0.3:
        return "Medium"

    return "Low"


def calculate_average(field, comparisons):
    if not comparisons:
        return 0.0
    return round(
        sum(item.get(field, 0) for item in comparisons) / len(comparisons),
        2
    )


def split_matched_unmatched(comparisons):
    matched = []
    unmatched = []

    for item in comparisons:
        alignment = item.get("alignment_type")

        if alignment in ["Fully Aligned", "Vendor Exceeds"]:
            matched.append(item)
        else:
            unmatched.append(item)

    return matched, unmatched


def compare_documents(client_text: str, vendor_text: str):

    prompt = f"""
    You are an enterprise compliance comparison engine.

    Compare the following two policy documents.

    TASK:
    1. Generate important compliance verification questions.
    2. Answer each question using BOTH documents.
    3. Determine alignment_type:
       - Fully Aligned
       - Partially Aligned
       - Not Aligned
       - Vendor Exceeds
       - Not Applicable
    4. Assign criticality:
       - Critical
       - Important
       - Informational
    5. Provide similarity_score (0 to 1).
    6. Provide confidence_score (0 to 1).
    7. If alignment_type is NOT Fully Aligned,
       suggest a minimal improvement statement
       the vendor can add without rewriting the full policy.

    RISK RULES:
    - Fully Aligned → Low
    - Vendor Exceeds → Low
    - Partially Aligned → Medium
    - Not Aligned + Critical → High
    - Not Aligned + Important → Medium
    - Not Aligned + Informational → Low
    - Not Applicable → Low

    IMPORTANT:
    - Return ONLY valid JSON
    - No markdown
    - No extra text

    FORMAT:
    {{
        "comparisons": [
            {{
                "question": "",
                "client_answer": "",
                "vendor_answer": "",
                "alignment_type": "",
                "criticality": "",
                "similarity_score": 0.0,
                "risk_level": "",
                "confidence_score": 0.0,
                "reason": "",
                "improvement_suggestion": ""
            }}
        ]
    }}

    CLIENT POLICY:
    {client_text}

    VENDOR POLICY:
    {vendor_text}
    """

    response = call_mistral(prompt)

    if not response:
        return {
            "error": "Mistral API returned empty response."
        }

    response = response.replace("```json", "").replace("```", "").strip()

    try:
        data = json.loads(response)
        comparisons = data.get("comparisons", [])

        matched, unmatched = split_matched_unmatched(comparisons)

        total = len(comparisons)
        matched_count = len(matched)
        unmatched_count = len(unmatched)

        overall_similarity = calculate_average("similarity_score", comparisons)
        overall_confidence = calculate_average("confidence_score", comparisons)
        overall_risk = calculate_overall_risk(comparisons)

        return {
            "summary": {
                "total_clauses": total,
                "matched_clauses": matched_count,
                "unmatched_clauses": unmatched_count
            },
            "matched": matched,
            "unmatched": unmatched,
            "overall_similarity_score": overall_similarity,
            "overall_risk_level": overall_risk,
            "overall_confidence_score": overall_confidence
        }

    except Exception as e:
        return {
            "error": f"Invalid JSON from Mistral: {str(e)}"
        }