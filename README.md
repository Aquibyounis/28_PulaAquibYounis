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
Synthetic Call Center Transcript Dataset (Kaggle):  
https://www.kaggle.com/datasets/willirath/synthetic-call-center-data

The dataset contains simulated call conversations with speaker turns, making it suitable for rapid prototyping and evaluation.

---

## System Design (High Level)
1. Load and normalize call transcripts
2. Pass transcript text to an LLM-based insight extraction module
3. Enforce structured JSON output using a predefined schema
4. Validate and return insights for evaluation or storage

No frontend/UI is implemented, as the focus is on backend correctness and AI utilization.

---

## Assumptions
- Input data consists of clean, text-based call transcripts
- Speaker roles (Rep / HCP / Doctor) are identifiable
- Audio processing (ASR) is out of scope for the MVP
- The system prioritizes correctness and clarity over UI features

---

## Tech Stack
- Python
- LangChain
- Large Language Models (OpenAI / Sentence-Transformers)
- Pydantic (for schema validation)
- Pandas (data handling)

---

## How to Run (MVP)
```bash
pip install -r requirements.txt
python main.py
