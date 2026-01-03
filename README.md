# Sales Rep Call Intelligence Analyzer (P10)

## Domain
Healthcare / Pharmaceutical Sales Intelligence

---

## Problem Statement
Medical sales representatives conduct frequent calls with healthcare professionals (HCPs) to promote pharmaceutical products. These conversations contain valuable insights such as objections, competitor mentions, sentiment, and follow-up opportunities. However, manual analysis of call transcripts is time-consuming, inconsistent, and not scalable.

The objective of this project is to build an AI-powered backend system that analyzes medical sales call transcripts and extracts structured, actionable insights to support sales effectiveness and decision-making.

---

## Proposed Solution
This project implements a backend-first AI pipeline that processes text-based call transcripts and produces structured intelligence in JSON format.

The system leverages Large Language Models (LLMs) and NLP techniques to extract:
- Key topics discussed during the call
- Objections raised by the healthcare professional
- Competitor products or brands mentioned
- Overall sentiment toward the promoted product
- Recommended Next Best Action (NBA) for the sales representative

The output is deterministic, schema-validated JSON suitable for downstream analytics, CRM integration, or reporting tools.

---

## Data Source

The dataset used in this project is a **synthetic, AI-generated sales call transcript dataset** created specifically for this assignment.

The conversations were generated to simulate realistic medical sales calls between pharmaceutical representatives and healthcare professionals (HCPs). Each call consists of multiple speaker turns with timestamps, objections, competitor mentions, and sales outcomes.

Synthetic data was intentionally used to:
- Avoid privacy and compliance issues associated with real medical conversations
- Ensure reproducibility and controlled evaluation
- Cover positive, neutral, and negative sales scenarios

The dataset is stored as a CSV file with the following schema:
- call_id
- speaker (Rep / Doctor / HCP)
- text
- timestamp

---

## System Design
1. Load and normalize call transcripts
2. Pass transcript text to an LLM-based insight extraction module
3. Enforce structured JSON output using a predefined schema
4. Validate and return insights for evaluation or storage
---

## Guardrails & Reliability

To ensure reliability and production-aligned behavior, multiple guardrails are applied:

- Prompt-level constraints to enforce structured JSON output
- Deterministic inference (temperature = 0) for consistent results
- Pydantic schema validation to prevent hallucinated or malformed fields
- If the model output deviates from the expected structure, the pipeline fails fast.
---

## Assumptions
- Input data consists of clean, text-based call transcripts
- Speaker roles (Rep / HCP / Doctor) are identifiable
- Audio processing (ASR) is out of scope for the MVP

---

## Tech Stack
- Python
- LangChain
- Large Language Models (Mistral/ Sentence-Transformers)
- Pydantic (for schema validation)
- Pandas (data handling)

---

## How to Run (MVP)
```bash
pip install -r requirements.txt
python main.py
```

---
## Architecture & Pipeline Flow

The system follows a modular, backend-first design:

1. Call transcripts are loaded from a CSV dataset containing speaker-level logs.
2. Conversations are grouped by call_id and reconstructed into chronological transcripts according to time stamps.
3. External domain knowledge is retrieved and injected using a lightweight RAG mechanism.
4. A deterministic LLM is prompted to extract structured insights.
5. The output is validated using a strict Pydantic schema.
6. Insights are returned as JSON for downstream use.

This design prioritizes correctness, explainability, and extensibility.

---

## Evaluation & Validation

The system was evaluated qualitatively on synthetic sales conversations covering:

- Positive adoption scenarios
- Competitive objections
- Pricing concerns
- Safety/efficacy discussions
- Negative or rejected sales outcomes

Correctness was verified by inspecting:
- Extracted topics
- Identified objections
- Sentiment polarity
- Recommended next best actions

Schema validation ensures structural correctness of all outputs.

---

# PULA AQUIB YOUNIS