import json

def generate_handoff(
    persona,
    issue,
    docs_used
):

    summary = {
        "persona": persona,
        "issue": issue,
        "documents_used": docs_used,
        "recommendation":
        "Escalate to human support agent"
    }

    return json.dumps(
        summary,
        indent=4
    )