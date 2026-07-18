from pathlib import Path

from core.utils.file_reader import read_text_file


def test_read_text_file(tmp_path: Path):

    file = tmp_path / "job.txt"

    file.write_text(
        "Accounting Clerk",
        encoding="utf-8",
    )

    text = read_text_file(file)

    assert text == "Accounting Clerk"