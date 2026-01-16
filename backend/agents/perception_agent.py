import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

def perception_agent(complaint_text: str):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not loaded")

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=api_key
    )

    prompt = PromptTemplate(
    input_variables=["complaint"],
    template="""
You are a municipal AI perception agent.

Your job is to analyze citizen complaints and identify issues.

Valid issue types:
- water_leak
- electric_hazard
- road_damage
- sanitation_issue

Rules:
1. If the complaint is clear, identify one or more issues.
2. If the complaint is ambiguous, return an empty list or the most likely issue.
3. Do NOT guess aggressively.
4. Always include a confidence_score between 0 and 1.

Return STRICT JSON in this format ONLY:

{{
  "issues_detected": ["water_leak", "electric_hazard"],
  "confidence_score": 0.85,
  "priority": "HIGH",
  "reason": "short explanation"
}}

If unclear:

{{
  "issues_detected": [],
  "confidence_score": 0.25,
  "priority": "LOW",
  "reason": "Insufficient information, clarification required"
}}

Complaint:
{complaint}
"""
)


    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(complaint=complaint_text)

    return json.loads(response)
