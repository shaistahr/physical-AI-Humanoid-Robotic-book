import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./rag_chatbot.db")

# AI Service Configuration (support both Gemini and OpenAI)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# JWT Authentication
JWT_SECRET = os.getenv("JWT_SECRET", "dev-secret-change-in-production")
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_DAYS = 7

# Vector Database (Qdrant)
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION", "textbook_chunks")

# Content Configuration
CONTENT_URL = os.getenv("CONTENT_URL")

# CORS Configuration
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")

# Application Settings
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# Validate required environment variables
def validate_config():
    """Validate that required environment variables are set"""
    # At least one AI service key must be provided
    if not GEMINI_API_KEY and not OPENAI_API_KEY:
        raise ValueError("Either GEMINI_API_KEY or OPENAI_API_KEY must be set")
    
    if not JWT_SECRET or JWT_SECRET == "dev-secret-change-in-production":
        if not DEBUG:
            raise ValueError("JWT_SECRET must be set in production")
    
    return True

def get_content_url():
    """Retrieve the pre-stored URL from environment variables"""
    return CONTENT_URL

def get_ai_service():
    """Determine which AI service to use (Gemini preferred)"""
    if GEMINI_API_KEY:
        return "gemini"
    elif OPENAI_API_KEY:
        return "openai"
    else:
        raise ValueError("No AI service configured")
