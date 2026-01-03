from sentence_transformers import SentenceTransformer, util
from pathlib import Path

MODEL = SentenceTransformer("all-MiniLM-L6-v2")
KNOWLEDGE_PATH = Path("knowledge/sales_knowledge.txt")


def retrieve_context(query: str, top_k: int = 2) -> str:
    
    if not KNOWLEDGE_PATH.exists():
        return ""

    knowledge_text = KNOWLEDGE_PATH.read_text(encoding="utf-8").split("\n")
    knowledge_text = [k for k in knowledge_text if k.strip()]

    query_embedding = MODEL.encode(query, convert_to_tensor=True)
    knowledge_embeddings = MODEL.encode(knowledge_text, convert_to_tensor=True)

    scores = util.cos_sim(query_embedding, knowledge_embeddings)[0]
    top_indices = scores.topk(top_k).indices

    retrieved = [knowledge_text[i] for i in top_indices]
    return "\n".join(retrieved)
