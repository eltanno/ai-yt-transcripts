"""Configuration for the RAG pipeline."""

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import AzureOpenAI, OpenAI

# Load .env from project root
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_PROJECT_ROOT / ".env")

# OpenAI
OPENAI_API_KEY: str = os.environ.get("OPENAI_API_KEY", "")
EMBEDDING_MODEL: str = os.environ.get("EMBEDDING_MODEL", "text-embedding-3-large")
EMBEDDING_DIMS: int = int(os.environ.get("EMBEDDING_DIMS", "1536"))

# Azure OpenAI
AZURE_OPENAI_API_KEY: str = os.environ.get("AZURE_OPENAI_API_KEY", "")
AZURE_OPENAI_ENDPOINT: str = os.environ.get("AZURE_OPENAI_ENDPOINT", "")
AZURE_OPENAI_API_VERSION: str = os.environ.get("AZURE_OPENAI_API_VERSION", "2024-06-01")
AZURE_OPENAI_DEPLOYMENT: str = os.environ.get("AZURE_OPENAI_DEPLOYMENT", "")


def _use_azure() -> bool:
    """Return True if Azure OpenAI credentials are configured."""
    return bool(AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT)


def get_embedding_client() -> OpenAI:
    """Create the appropriate OpenAI client based on environment variables.

    Uses Azure OpenAI if AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT are set,
    otherwise falls back to regular OpenAI.
    """
    if _use_azure():
        return AzureOpenAI(
            api_key=AZURE_OPENAI_API_KEY,
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_version=AZURE_OPENAI_API_VERSION,
        )
    return OpenAI(api_key=OPENAI_API_KEY)


def get_embedding_model() -> str:
    """Return the model/deployment name to use for embeddings.

    For Azure, this is the deployment name. For OpenAI, it's the model name.
    """
    if _use_azure() and AZURE_OPENAI_DEPLOYMENT:
        return AZURE_OPENAI_DEPLOYMENT
    return EMBEDDING_MODEL


def has_embedding_credentials() -> bool:
    """Return True if any embedding credentials are configured."""
    return _use_azure() or bool(OPENAI_API_KEY)

# LanceDB
DB_PATH: str = os.environ.get("DB_PATH", str(_PROJECT_ROOT / "db"))
TABLE_NAME: str = "transcripts"

# Chunking
CHUNK_SIZE: int = int(os.environ.get("CHUNK_SIZE", "500"))  # tokens
CHUNK_OVERLAP: int = int(os.environ.get("CHUNK_OVERLAP", "100"))  # tokens

# Paths
TRANSCRIPTS_DIR: Path = _PROJECT_ROOT / "transcripts"

# Query defaults
DEFAULT_TOP_K: int = 5

# Time decay
DECAY_HALF_LIFE_DAYS: int = 60
DECAY_FLOOR: float = 0.1
