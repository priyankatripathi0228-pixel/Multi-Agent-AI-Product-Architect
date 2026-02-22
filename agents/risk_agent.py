from core.llm import call_llm

def run_risk_agent(prd: str):
    prompt = f"""
You are a Risk Analysis AI.

Identify risks in this product.

PRD:
{prd}

Return ONLY JSON with:
- technical_risks
- security_risks
- scalability_risks
- business_risks
"""
    return call_llm(prompt)
