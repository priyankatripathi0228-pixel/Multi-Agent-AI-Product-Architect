from core.llm import call_llm

def run_testing_agent(prd: str):
    prompt = f"""
You are a QA Testing AI.

Generate test cases.

PRD:
{prd}

Return ONLY JSON list with:
- unit_tests
- integration_tests
- edge_cases
- api_tests
"""
    return call_llm(prompt)
