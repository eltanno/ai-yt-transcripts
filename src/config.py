"""Configuration for the RAG pipeline."""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env from project root
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_PROJECT_ROOT / ".env")

# OpenAI
OPENAI_API_KEY: str = os.environ.get("OPENAI_API_KEY", "")
EMBEDDING_MODEL: str = os.environ.get("EMBEDDING_MODEL", "text-embedding-3-large")
EMBEDDING_DIMS: int = int(os.environ.get("EMBEDDING_DIMS", "1536"))

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
