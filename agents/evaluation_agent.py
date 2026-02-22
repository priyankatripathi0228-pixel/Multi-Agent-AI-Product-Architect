from core.llm import call_llm

def run_evaluation_agent(all_outputs: str):
    prompt = f"""
You are an Evaluation AI.

Score the outputs from 1–10 on:
- completeness
- clarity
- technical_quality
- consistency

DATA:
{all_outputs}

Return ONLY JSON with:
- scores
- overall_score
- improvement_suggestions
"""
    return call_llm(prompt)
