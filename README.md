# adsparkx-persona-support-agent
Project Overview
Persona Adaptive Customer Support Agent
that customizes responses based on
user personas and performs intelligent escalation.

Features
✔ Persona Detection
✔ Knowledge Base Retrieval
✔ Gemini AI Responses
✔ Escalation Logic
✔ Human Handoff Summary
✔ Streamlit Interface

Tech Stack
Python
Streamlit
Gemini AI
Google Generative AI SDK
Document Knowledge Base

Architecture

User Query
     |
     v
Persona Detector
     |
     v
Knowledge Base
     |
     v
Gemini AI
     |
     +-------> Escalation Engine
     |
     v
Response Generator
     |
     v
User



Example Queries

1. Technical Expert
Input
Can you explain the API authentication failure and provide troubleshooting steps?
Expected Output
Detected Persona:
Technical Expert

Retrieved Sources:
api_authentication.md

AI Response:
The authentication failure is likely caused by an invalid API key,
expired token, or incorrect request headers.

Root Cause:
- Invalid API credentials
- Expired token
- Misconfigured endpoint

Troubleshooting:
1. Verify API key.
2. Check token validity.
3. Validate request headers.
4. Review server logs.

Escalation Status:
Issue Resolved
2. Frustrated User
Input
I am frustrated. Nothing works and I cannot log in.
Expected Output
Detected Persona:
Frustrated User

Retrieved Sources:
login_issues.md
password_reset.md

AI Response:
I understand how frustrating this situation can be.

Please try the following:
1. Verify your username and password.
2. Clear browser cache.
3. Reset your password.
4. Try logging in again.

If the issue continues, our support team can assist further.

Escalation Status:
Issue Resolved
3. Business Executive
Input
What is the impact of login issues on business operations?
Expected Output
Detected Persona:
Business Executive

Retrieved Sources:
login_issues.md

AI Response:
Business Impact:
- Reduced employee productivity
- Customer dissatisfaction
- Delayed operations

Resolution Timeline:
Approximately 15-30 minutes for standard login issues.

Recommended Actions:
- Notify affected users.
- Monitor authentication systems.
- Escalate recurring incidents.

Escalation Status:
Issue Resolved
4. Escalation Example
Input
My account was hacked and I need legal assistance.
Expected Output
Detected Persona:
Frustrated User

Retrieved Sources:
security_policy.md
account_recovery.md

AI Response:
Your account security is important.

Immediately:
1. Change your password.
2. Enable MFA.
3. Review account activity.

Escalation Status:
Escalated to Human Support

Human Handoff Summary:
{
    "persona": "Frustrated User",
    "issue": "My account was hacked and I need legal assistance.",
    "documents_used": [
        "security_policy.md",
        "account_recovery.md"
    ],
    "recommendation": "Escalate to human support team"
}
5. Billing Query
Input
Why was my payment declined?
Expected Output
Detected Persona:
Frustrated User

Retrieved Sources:
billing_faq.md

AI Response:
Common reasons for payment failure include:
- Insufficient funds
- Expired card
- Bank restrictions

Please verify your payment details and try again.

Escalation Status:
Issue Resolved
