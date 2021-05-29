"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
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


def find_occurrences(tree, element) -> int:
    """Take element and finds the number of occurrences in a tree.

    Args:
        tree: can only contains basic structures like:
            str, list, tuple, dict, set, int, bool.
        element: element for search and counting.

    Returns:
        int: number of occurrences of element in the given tree.

    Links:
        https://www.youtube.com/watch?v=Uwuv05aZ6ug
    """
    if tree == element:
        return 1
    if isinstance(tree, list):
        return sum(find_occurrences(subtree, element) for subtree in tree)
    if isinstance(tree, dict):
        return sum(find_occurrences(subtree, element) for subtree in tree.values())
    return 0
