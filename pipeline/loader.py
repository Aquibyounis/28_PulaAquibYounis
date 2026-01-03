import pandas as pd
from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/raw/call_transcripts.csv")

def get_all_call_ids():
    df = pd.read_csv("data/raw/call_transcripts.csv")
    return sorted(df["call_id"].unique().tolist())


def load_transcript(call_id: int) -> str:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    # 🔒 Strong typing (critical)
    df["call_id"] = df["call_id"].astype(int)
    df["speaker"] = df["speaker"].astype(str)
    df["text"] = df["text"].astype(str)

    required_columns = {"call_id", "speaker", "text", "timestamp"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"Dataset must contain columns: {required_columns}")

    call_df = df[df["call_id"] == call_id]

    if call_df.empty:
        raise ValueError(f"No transcript found for call_id={call_id}")

    call_df = call_df.sort_values("timestamp")

    conversation_lines = []
    for _, row in call_df.iterrows():
        speaker = row["speaker"].strip()
        text = row["text"].strip()
        if text:
            conversation_lines.append(f"{speaker}: {text}")

    return "\n".join(conversation_lines)
