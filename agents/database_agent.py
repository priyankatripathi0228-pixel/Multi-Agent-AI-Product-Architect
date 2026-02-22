from core.llm import call_llm

def run_database_agent(prd: str):
    prompt = f"""
You are a Database Architect AI.

Design database schema.

PRD:
{prd}

Return ONLY JSON with:
- tables
- fields
- relationships
- indexing_strategy
"""
    return call_llm(prompt)
