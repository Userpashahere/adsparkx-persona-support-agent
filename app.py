import os
import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv
from persona_detector import detect_persona
from escalation import should_escalate
from handoff import generate_handoff
from rag_pipeline import get_documents

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit UI
st.set_page_config(page_title="Adsparkx Support Agent")

st.title("🤖 Persona Adaptive Customer Support Agent")

query = st.text_area("Enter your support issue")

if st.button("Submit"):

    if not query.strip():
        st.warning("Please enter a query.")
        st.stop()

    # Detect persona
    persona = detect_persona(query)

    # Load documents
    docs = get_documents()

    # Build context
    context = ""

    for doc in docs[:5]:
        context += doc["content"] + "\n\n"

    # Persona-based prompt
    if persona == "Technical Expert":

        prompt = f"""
You are a senior technical support engineer.

Knowledge Base:
{context}

User Query:
{query}

Provide:
1. Technical explanation
2. Root cause
3. Troubleshooting steps
"""

    elif persona == "Business Executive":

        prompt = f"""
You are an executive support advisor.

Knowledge Base:
{context}

User Query:
{query}

Provide:
1. Business impact
2. Resolution timeline
3. Recommended actions
"""

    else:

        prompt = f"""
You are an empathetic customer support specialist.

Knowledge Base:
{context}

User Query:
{query}

Provide:
1. Friendly response
2. Solution steps
3. Reassurance
"""

    # Generate response
    try:
        response = model.generate_content(prompt)
        answer = response.text

    except Exception as e:
        answer = f"Error generating response: {str(e)}"

    # Escalation check
    escalation = should_escalate(query, len(docs))

    # Display results
    st.subheader("Detected Persona")
    st.write(persona)

    st.subheader("Retrieved Sources")

    for doc in docs[:5]:
        st.write(doc["name"])

    st.subheader("AI Response")
    st.write(answer)

    st.subheader("Escalation Status")

    if escalation:

        st.error("Escalated to Human Support")

        summary = generate_handoff(
            persona,
            query,
            [doc["name"] for doc in docs[:5]]
        )

        st.subheader("Human Handoff Summary")
        st.code(summary, language="json")

    else:
        st.success("Issue Resolved")