from core.llm import call_llm

def run_architecture_agent(prd: str):
    prompt = f"""
You are a System Architect AI.

Design system architecture from this PRD.

PRD:
{prd}

Return ONLY JSON with:
- system_components
- architecture_style
- tech_stack
- data_flow
- scalability_notes
"""
    return call_llm(prompt)
