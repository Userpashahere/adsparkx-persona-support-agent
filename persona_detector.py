def detect_persona(query):

    query = query.lower()

    technical_keywords = [
        "api",
        "logs",
        "authentication",
        "endpoint",
        "configuration",
        "debug",
        "token",
        "error"
    ]

    frustrated_keywords = [
        "frustrated",
        "angry",
        "nothing works",
        "terrible",
        "urgent",
        "annoyed",
        "issue"
    ]

    executive_keywords = [
        "business",
        "impact",
        "operations",
        "revenue",
        "timeline",
        "customer",
        "executive"
    ]

    if any(word in query for word in technical_keywords):
        return "Technical Expert"

    elif any(word in query for word in frustrated_keywords):
        return "Frustrated User"

    elif any(word in query for word in executive_keywords):
        return "Business Executive"

    return "Frustrated User"