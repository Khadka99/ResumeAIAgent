"""
Central logging configuration for Resume AI Agent.
"""

import logging
from pathlib import Path

# ------------------------------------------------------------------
# Create logs directory if it doesn't exist
# ------------------------------------------------------------------

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "resume_ai.log"

# ------------------------------------------------------------------
# Configure logger
# ------------------------------------------------------------------

logger = logging.getLogger("ResumeAIAgent")

if not logger.handlers:
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File Handler
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)