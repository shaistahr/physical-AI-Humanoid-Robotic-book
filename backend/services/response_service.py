from config import OPENAI_API_KEY, GEMINI_API_KEY, get_ai_service
from typing import List, Dict
from utils.logging import get_logger
import asyncio

logger = get_logger(__name__)

# Determine which service to use
AI_SERVICE = get_ai_service()

if AI_SERVICE == "openai":
    import openai
    client = openai.AsyncClient(api_key=OPENAI_API_KEY)
elif AI_SERVICE == "gemini":
    import google.generativeai as genai
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')

async def generate_response(user_query: str, context_chunks: List[Dict], out_of_context_message: str = "I cannot answer that question based on the available content.") -> str:
    """
    Generate a response using OpenAI's GPT model with the provided context
    """
    # Construct the context from relevant chunks
    context_text = ""
    sources = []

    for chunk in context_chunks:
        context_text += f"Source: {chunk.get('source_url', 'Unknown')}\n"
        context_text += f"Content: {chunk.get('content', '')}\n\n"
        if chunk.get('source_url') not in sources:
            sources.append(chunk.get('source_url'))

    # If no context chunks were found, return out-of-context message
    if not context_chunks or not context_text.strip():
        return out_of_context_message

    # Create the prompt for the AI model
    prompt = f"""
    You are a helpful assistant that answers questions based on the provided context.
    Only use the information from the context provided below to answer the user's question.
    If the question cannot be answered based on the provided context, respond with: "{out_of_context_message}"

    Context:
    {context_text}

    User question: {user_query}

    Answer:
    """

    try:
        if AI_SERVICE == "openai":
            # Generate response using OpenAI
            response = await client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that answers questions based only on the provided context. If the question cannot be answered with the provided context, say that you don't know based on the available information. When providing information from the context, mention the source URL if relevant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )
            generated_text = response.choices[0].message.content.strip()

        elif AI_SERVICE == "gemini":
            # Generate response using Gemini
            response = model.generate_content(prompt)
            generated_text = response.text.strip()

        else:
            return "AI service not configured properly."

        logger.info(f"Generated response for query: {user_query[:50]}...")
        return generated_text

    except Exception as e:
        logger.error(f"Error generating response: {str(e)}")
        return f"Sorry, there was an error processing your request: {str(e)}"