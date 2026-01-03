from flask import Flask, request, jsonify
from pipeline.extractor import extract_insights
import csv
import io

app = Flask(__name__)

# ---------------------------
# Health check
# ---------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


# ---------------------------
# Helper: Normalize CSV-style conversation
# ---------------------------
def normalize_csv_conversation(raw_text: str) -> str:
    """
    Converts CSV-style call logs into clean conversational text
    suitable for LLM inference.
    """

    lines = raw_text.strip().splitlines()

    # Remove header if present
    if lines and lines[0].lower().startswith("call_id"):
        lines = lines[1:]

    reader = csv.reader(lines)
    conversation = []

    for row in reader:
        if len(row) < 4:
            continue

        _, speaker, text, _ = row
        conversation.append(f"{speaker.strip()}: {text.strip()}")

    return "\n".join(conversation)


# ---------------------------
# Analyze text endpoint
# ---------------------------
@app.route("/analyze/text", methods=["POST"])
def analyze_text():
    try:
        # Read raw text (NOT JSON)
        raw_text = request.get_data(as_text=True)

        if not raw_text or not raw_text.strip():
            return jsonify({"error": "Empty request body"}), 400

        normalized_text = normalize_csv_conversation(raw_text)
        insights = extract_insights(normalized_text)

        return jsonify({
            "status": "success",
            "normalized_conversation": normalized_text,
            "insights": insights.model_dump()
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500



# ---------------------------
# Run server
# ---------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
