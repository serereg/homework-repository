"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount
    of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import operator
import string
from typing import Dict, List
import unicodedata

from collections import namedtuple
from unicodedata import category


Token = namedtuple("Token", ["type", "value"])


def tokenize(file_input):
    buffer = ""
    symbol = file_input.read(1)
    while symbol:
        if category(symbol).startswith("L"):
            buffer += symbol
            symbol = file_input.read(1)
            continue
        if buffer:
            yield Token("word", buffer)
            buffer = ""
        if category(symbol) == "Po":
            yield Token("punctuation", symbol)
        yield Token("symbol", symbol)

        symbol = file_input.read(1)
    yield Token("word", buffer)


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

    sorted_counts_of_chars = [
        k for k, v in sorted(counts_of_chars.items(), key=operator.itemgetter(1))
    ]
    return sorted_counts_of_chars[0]


def count_punctuation_chars(file_path: str) -> int:
    """Count every punctuation char"""
    counter_of_punctuation = 0
    with open(file_path, encoding="unicode_escape") as fi:
        counters_of_symbols: Dict[str, int] = {}
        for line in fi:
            for symbol in line:
                counters_of_symbols[symbol] = counters_of_symbols.get(symbol, 0) + 1
        for symbol, number in counters_of_symbols.items():
            if unicodedata.category(symbol) == "Po":
                counter_of_punctuation += number
    return counter_of_punctuation


def count_punctuation_chars_with_tokenize(file_path: str) -> int:
    """Count every punctuation char"""
    counter_of_punctuation = 0
    with open(file_path, encoding="unicode_escape") as fi:
        for token in tokenize(fi):
            if token.type == "punctuation":
                counter_of_punctuation += 1
    return counter_of_punctuation


def count_non_ascii_chars(file_path: str) -> int:
    """Count every non ascii char"""
    counter_of_non_ascii = 0
    with open(file_path, encoding="unicode_escape") as fi:
        for line in fi:
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
        for key in counters_of_symbols.keys():
            if key not in string.printable:
                non_ascii_chars[key] = counters_of_symbols[key]
        print(non_ascii_chars)
        sorted_non_ascii_chars = [
            k for k, v in sorted(non_ascii_chars.items(), key=operator.itemgetter(1))
        ]
        sorted_non_ascii_chars.reverse()
    return sorted_non_ascii_chars[0]


if __name__ == "__main__":
    with open("data.txt") as fi:
        for token in tokenize(fi):
            print(token)
