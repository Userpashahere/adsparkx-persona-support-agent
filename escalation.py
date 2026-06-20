def should_escalate(query, docs_found):

    sensitive_keywords = [
        "legal",
        "lawsuit",
        "billing dispute",
        "fraud",
        "hacked",
        "account hacked"
    ]

    query = query.lower()

    if docs_found == 0:
        return True

    if any(word in query for word in sensitive_keywords):
        return True

    return False