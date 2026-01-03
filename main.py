from pipeline.loader import load_transcript
from pipeline.extractor import extract_insights
import json

if __name__ == "__main__":
    transcript = load_transcript(call_id=1)

    insights = extract_insights(transcript)

    print("\n--- AI INSIGHTS ---\n")
    print(json.dumps(insights.dict(), indent=2))
