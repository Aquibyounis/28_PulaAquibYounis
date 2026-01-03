from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from schemas.insight_schema import CallInsights
from pipeline.retriever import retrieve_context

import json
import re


def extract_insights(transcript: str) -> CallInsights:
    """
    Extract structured sales intelligence from a call transcript
    using Mistral (Ollama) with lightweight RAG grounding.
    """

    # 1️⃣ LLM (local, deterministic)
    llm = OllamaLLM(
        model="mistral",
        temperature=0
    )

    # 2️⃣ Load prompt template
    with open("prompts/insight_extraction.txt", "r", encoding="utf-8") as f:
        template_text = f.read()

    prompt = PromptTemplate(
        input_variables=["transcript"],
        template=template_text
    )

    # 3️⃣ Retrieve external domain context (RAG)
    context = retrieve_context(transcript)

    augmented_transcript = f"""
Conversation:
{transcript}

Relevant domain knowledge:
{context}
""".strip()

    # 4️⃣ Invoke LLM
    response = llm.invoke(
        prompt.format(transcript=augmented_transcript)
    )

    raw_output = response.strip()

    # 5️⃣ JSON guardrail (critical for demos & interviews)
    match = re.search(r"\{.*\}", raw_output, re.DOTALL)
    if not match:
        raise ValueError("Model did not return valid JSON")

    parsed = json.loads(match.group())

    # 6️⃣ Schema validation (guardrail)
    return CallInsights(**parsed)
