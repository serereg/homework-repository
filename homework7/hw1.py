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


def find_occurrences(node, target):
    """Take element and finds the number of occurrences in a tree.

    Args:
        node: can only contains basic structures like:
            str, list, tuple, dict, set, int, bool.
        target: element for search and counting.

    Returns:
        int: number of occurrences of element in the given tree.

    Links:
        https://www.youtube.com/watch?v=Uwuv05aZ6ug
    """
    if node == target:
        return 1
    if isinstance(node, list):
        return sum(find_occurrences(subnode, target) for subnode in node)
    if isinstance(node, dict):
        return sum(find_occurrences(subnode, target) for subnode in node.values())
    return 0
