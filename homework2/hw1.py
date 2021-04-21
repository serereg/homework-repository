"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List, Set


# TODO: make analise unicode, using ord etc 

def get_longest_diverse_words(file_path: str) -> List[str]:
    """Find 10 longest words consisting from largest amount of unique symbols
    """
    words_with_info = list()
    with open(file_path, encoding="unicode_escape") as fi:
        for line in fi:
            line.lower()
            line = (line.replace("# ", " ").replace(".", " ").replace(",", " ")
                    .replace("% ", " ").replace("; ", " ").replace("- ", " "))
            for word in line.split():
                words_with_info.append((len(set(word)), word))
    words_with_info.sort(reverse=True)

    result = [item[1] for item in words_with_info[:10]]
    return result


def get_rarest_char(file_path: str) -> str:
    """Find the rarest char
    """
    counts_of_chars = dict() 
    with open(file_path, encoding='unicode_escape') as fi:
        for line in fi:
            for char in line:
                if char in counts_of_chars:
                    counts_of_chars[char] += 1
                else:
                    counts_of_chars[char] = 1
                    
    li = [(item, counts_of_chars[item]) for item in counts_of_chars.keys()] 
    li.sort(key= lambda el: el[1])
    rarest_char = li[0][0]
    return rarest_char


def count_punctuation_chars(file_path: str) -> int:
    """Count every punctuation char
    """
    ...


def count_non_ascii_chars(file_path: str) -> int:
    ...


def get_most_common_non_ascii_char(file_path: str) -> str:
    ...


if __name__ == "__main__":
    res = get_longest_diverse_words('data.txt')
    print(res)
    res = get_rarest_char('data.txt')
    print(res)