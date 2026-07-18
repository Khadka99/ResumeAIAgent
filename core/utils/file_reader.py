"""
Utility functions for reading input files.
"""

from pathlib import Path


SUPPORTED_EXTENSIONS = {
    ".txt",
}


def read_text_file(file_path: str | Path) -> str:
    """
    Read a UTF-8 text file.

    Args:
        file_path:
            Path to the text file.

    Returns:
        File contents as a string.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {path}"
        )

    if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {path.suffix}"
        )

    return path.read_text(
        encoding="utf-8"
    )