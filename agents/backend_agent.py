from core.llm import call_llm

def run_backend_agent(prd: str):
    prompt = f"""
You are a Backend Engineer AI.

Create REST API design from this PRD.

PRD:
{prd}

Return ONLY JSON with:
- endpoints
- request_models
- response_models
- auth_flow
"""
    return call_llm(prompt)
