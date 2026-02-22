from core.llm import call_llm

def run_pm_agent(idea: str):
    prompt = f"""
You are a Product Manager AI.

Convert this idea into a structured PRD.

IDEA:
{idea}

Return ONLY valid JSON with:
- product_name
- target_users
- personas
- problem_statement
- features
- user_stories
- success_metrics
"""
    return call_llm(prompt)
