"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    cnt: int = 0

    def search(subtree: dict):
        nonlocal cnt
        for key, values in subtree.items():
            if isinstance(values, dict):
                search(values)
            for value in values:
                if isinstance(value, dict):
                    search(value)
            if element in values:
                print(key, values)
                cnt += 1

    search(tree)
    return cnt


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
