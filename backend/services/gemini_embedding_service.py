import google.generativeai as genai
from config import GEMINI_API_KEY
from typing import List
from utils.logging import get_logger

logger = get_logger(__name__)

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

async def generate_embedding_gemini(text: str) -> List[float]:
    """
    Generate embedding for a given text using Google's Gemini embedding model
    """
    try:
        result = genai.embed_content(
            model="models/embedding-001",
            content=text,
            task_type="retrieval_document"
        )
        return result['embedding']
    except Exception as e:
        logger.error(f"Error generating Gemini embedding: {e}")
        raise

async def generate_embeddings_gemini(texts: List[str]) -> List[List[float]]:
    """
    Generate embeddings for a list of texts using Gemini
    """
    embeddings = []
    for text in texts:
        embedding = await generate_embedding_gemini(text)
        embeddings.append(embedding)
    return embeddings
