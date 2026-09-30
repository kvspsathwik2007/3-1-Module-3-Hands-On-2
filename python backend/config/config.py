import os
from dotenv import load_dotenv

# Load .env from python_backend folder
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(ENV_PATH)


# -----------------------------
# API CONFIGURATION
# -----------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-20b"
)


# -----------------------------
# RETRIEVAL CONFIGURATION
# -----------------------------

TOP_K = int(os.getenv("TOP_K", "3"))


# -----------------------------
# FILE PATHS
# -----------------------------

DATA_DIR = os.path.join(BASE_DIR, "data")

DOCUMENTS_FILE = os.path.join(
    DATA_DIR,
    "documents.json"
)

EMBEDDINGS_FILE = os.path.join(
    DATA_DIR,
    "document_embeddings.npy"
)


# -----------------------------
# EMBEDDING MODEL
# -----------------------------

EMBEDDING_MODEL = "all-MiniLM-L6-v2"


def is_groq_configured():
    """
    Check whether Groq API key is available.
    """
    return bool(
        GROQ_API_KEY
        and GROQ_API_KEY != "YOUR_ACTUAL_GROQ_API_KEY"
        and GROQ_API_KEY != "your_groq_api_key_here"
    )