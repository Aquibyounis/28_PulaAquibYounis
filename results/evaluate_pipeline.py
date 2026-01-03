import csv
from pipeline.loader import load_transcript, get_all_call_ids
from pipeline.extractor import extract_insights

OUTPUT_FILE = "results/pipeline_evaluation.csv"

def evaluate_pipeline():
    fieldnames = [
        "call_id",
        "schema_valid",
        "deterministic",
        "has_objection",
        "has_competitor",
        "sentiment"
    ]

    rows = []

    for call_id in get_all_call_ids():
        row = {"call_id": call_id}

        try:
            transcript = load_transcript(call_id)

            # Run twice to test determinism
            out1 = extract_insights(transcript)
            out2 = extract_insights(transcript)

            row["schema_valid"] = True
            row["deterministic"] = out1.model_dump() == out2.model_dump()
            row["has_objection"] = len(out1.objections) > 0
            row["has_competitor"] = len(out1.competitors_mentioned) > 0
            row["sentiment"] = out1.product_sentiment

        except Exception:
            row["schema_valid"] = False
            row["deterministic"] = False
            row["has_objection"] = False
            row["has_competitor"] = False
            row["sentiment"] = "error"

        rows.append(row)

    # Write CSV
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Evaluation saved to {OUTPUT_FILE}")

    # Dataset-level summary
    total = len(rows)
    print("\n--- DATASET SUMMARY ---")
    print("Schema Validity Rate:", sum(r["schema_valid"] for r in rows) / total)
    print("Determinism Rate:", sum(r["deterministic"] for r in rows) / total)
    print("Objection Coverage Rate:", sum(r["has_objection"] for r in rows) / total)
    print("Competitor Coverage Rate:", sum(r["has_competitor"] for r in rows) / total)

if __name__ == "__main__":
    evaluate_pipeline()
