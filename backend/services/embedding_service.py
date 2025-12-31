from config import OPENAI_API_KEY, GEMINI_API_KEY, get_ai_service
from typing import List
from utils.logging import get_logger

logger = get_logger(__name__)

# Determine which service to use
AI_SERVICE = get_ai_service()

if AI_SERVICE == "openai":
    import openai
    client = openai.AsyncClient(api_key=OPENAI_API_KEY)
elif AI_SERVICE == "gemini":
    import google.generativeai as genai
    genai.configure(api_key=GEMINI_API_KEY)

async def generate_embedding(text: str) -> List[float]:
    """
    Generate embedding for a given text using the configured AI service
    """
    try:
        if AI_SERVICE == "openai":
            response = await client.embeddings.create(
                input=text,
                model="text-embedding-3-small"
            )
            return response.data[0].embedding
        elif AI_SERVICE == "gemini":
            result = genai.embed_content(
                model="models/embedding-001",
                content=text,
                task_type="retrieval_document"
            )
            return result['embedding']
        else:
            raise ValueError(f"Unsupported AI service: {AI_SERVICE}")
    except Exception as e:
        logger.error(f"Error generating embedding: {e}")
        raise

async def generate_embeddings(texts: List[str]) -> List[List[float]]:
    """
    Generate embeddings for a list of texts
    """
    embeddings = []
    for text in texts:
        embedding = await generate_embedding(text)
        embeddings.append(embedding)
    return embeddings