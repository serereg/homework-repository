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
    """Take element and finds the number of occurrences in a tree.

    Args:
        tree: can only contains basic structures like:
            str, list, tuple, dict, set, int, bool.
        element: element for search and counting.

    Returns:
        int: number of occurrences of element in the given tree.
    """
    cnt: int = 0

    def search_in(subtree: dict):
        nonlocal cnt
        for key, values in subtree.items():
            if element == values:
                cnt += 1
                continue
            if isinstance(values, dict):
                search_in(values)
                continue
            for value in values:
                if element == value:
                    cnt += 1
                elif isinstance(value, dict):
                    search_in(value)

    search_in(tree)
    return cnt


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
