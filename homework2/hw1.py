"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount
    of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from typing import Dict, List

# TODO: make analise unicode, using ord etc


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Find 10 longest words consisting from largest amount of
    unique symbols
    """
    words_with_info = {}
    with open(file_path, encoding="unicode_escape") as fi:
        for line in fi:
            new_line = line.lower()
            for subs in ["# ", ".", ",", "% ", "; ", "- "]:
                new_line = new_line.replace(subs, " ")
            for word in new_line.split():
                words_with_info[len(set(word))] = word
    sorted_words_by_info = sorted(list(words_with_info.items()), reverse=True)

    return [item[1] for item in sorted_words_by_info[:10]]


def get_rarest_char(file_path: str) -> str:
    """Find the rarest char"""
    counts_of_chars: Dict[str, int] = dict()
    with open(file_path, encoding="unicode_escape") as fi:
        for line in fi:
            for char in line:
                counts_of_chars[char] = counts_of_chars.get(char, 0) + 1

    li = [(item, counts_of_chars[item]) for item in counts_of_chars.keys()]
    li.sort(key=lambda el: el[1])
    rarest_char = li[0][0]

    # rarest_char = min(counts_of_chars, key=counts_of_chars.get)

    return rarest_char


def count_punctuation_chars(file_path: str) -> int:
    """Count every punctuation char"""
    counter_of_punctuation = 0
    punctuations = set(string.punctuation)
    with open(file_path, encoding="unicode_escape") as fi:
        for line in fi:
            for char in line:
                if char in punctuations:
                    counter_of_punctuation += 1
    return counter_of_punctuation


def count_non_ascii_chars(file_path: str) -> int:
    """Count every non ascii char"""
    counter_of_non_ascii = 0
    with open(file_path, encoding="unicode_escape") as fi:
        for line in fi:
            # a = len(line)
            # b = len(line.encode("ascii", "ignore"))
            # counter_of_non_ascii += a - b
            for char in line:
                if ord(char) > 127:
                    counter_of_non_ascii += 1
    return counter_of_non_ascii


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Find most common non ascii char for document"""
    counters_of_symbols: Dict[str, int] = {}
    with open(file_path, encoding="unicode_escape") as fi:
        for line in fi:
            for symbol in line:
                counters_of_symbols[symbol] = counters_of_symbols.get(symbol, 1) + 1
        non_ascii_chars: Dict[str, int] = {}
        # non_ascii_chars = {key: value for key, value in
        # counters_of_symbols if key
        # not in string.ascii_letters}
        for key in counters_of_symbols.keys():
            if key not in string.printable:
                non_ascii_chars[key] = counters_of_symbols[key]
        print(non_ascii_chars)
        # most_common = max(non_ascii_chars, key=non_ascii_chars.get)
        sorted_non_ascii_chars = sorted(
            non_ascii_chars.items(), key=lambda kv: kv[1], reverse=True
        )
        most_common = sorted_non_ascii_chars[0][0]
    return most_common
