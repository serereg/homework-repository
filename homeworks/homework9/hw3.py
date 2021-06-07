"""
Write a function that takes directory path, a file extension and an
optional tokenizer. It will count lines in all files with that extension
if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
from pathlib import Path
from typing import Optional, Callable


def tokenizer_lines(path: Path):
    with path.open() as fi:
        for line in fi:
            yield line


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """Count lines in all files with extension if there are no
    tokenizer, or use tokenizer.

    If a the tokenizer is not none, it will count tokens.

    Args:
        dir_path: directory.
        file_extension: type of file for operating.
        tokenizer: if None, function counts lines of files.

    Example:
        >>> universal_file_counter(test_dir, "txt")
        ...6
        >>> universal_file_counter(test_dir, "txt", str.split)
        ...6

    """
    if not dir_path.is_dir():
        raise IOError(f"{dir_path} is not a directory")
    files = dir_path.glob(f"*.{file_extension}")
    count_of_occurance = 0
    for file in files:
        for i, token in enumerate(tokenizer_lines(file), 1):
            print(i, token)
        count_of_occurance += i
    return count_of_occurance
