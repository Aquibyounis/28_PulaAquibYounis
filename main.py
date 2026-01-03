from pipeline.loader import load_transcript, get_all_call_ids
from pipeline.extractor import extract_insights
import json

if __name__ == "__main__":
    all_call_ids = get_all_call_ids()

    all_results = []

    for call_id in all_call_ids:
        transcript = load_transcript(call_id=call_id)
        insights = extract_insights(transcript)

        all_results.append({
            "call_id": call_id,
            "insights": insights.model_dump()  # Pydantic v2
        })

    print("\n--- AI INSIGHTS (ALL CALLS) ---\n")
    print(json.dumps(all_results, indent=2))
