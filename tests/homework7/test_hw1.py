from homeworks.homework7.hw1 import find_occurrences


def test_usual_tree():
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
    cnt = find_occurrences(example_tree, "RED")
    assert cnt == 6

    example_tree = {
        "first": ["RED", "BLUE"],
        "second": {
            "simple_key": ["RED", "list", "of", "RED", "valued"],
        },
        "third": {
            "abc": "RED",
            "jhl": "RED",
            "complex_key": {
                "key1": "value1",
                "key2": "RED",
                "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
            },
        },
        "fourth": "RED",
    }
    cnt = find_occurrences(example_tree, "RED")
    assert cnt == 8

    example_tree = {
        "first": ["RED", "BLUE"],
        "second": {
            "simple_key": ["RED", "list", "of", "RED", "valued"],
        },
        "third": {
            "abc": "RED",
            "jhl": "RED",
            "complex_key": {
                "key1": "value1",
                "key2": "RED",
                "key3": [
                    "a",
                    "RED",
                    "of",
                    "values",
                    {"nested_key": "RED", "abd": "xyz", "qwe": ["a", "RED"]},
                ],
            },
        },
        "fourth": "RED",
    }
    cnt = find_occurrences(example_tree, "RED")
    assert cnt == 10


def test_empty_tree():
    tree = {}
    cnt = find_occurrences(tree, "RED")
    assert cnt == 0
    cnt = find_occurrences(tree, "")
    assert cnt == 0


def test_with_one_node():
    tree = {"first": "RED"}
    cnt = find_occurrences(tree, "RED")
    assert cnt == 1
    tree = {"first": ""}
    cnt = find_occurrences(tree, "")
    assert cnt == 1
    tree = {False: False}
    cnt = find_occurrences(tree, False)
    assert cnt == 1


def test_tree_with_different_types_and_nesting():
    tree = {
        bool(False): False,
        True: 0,
        1: False,
        int(0): 2.0,
        float(0.0): 0,
        frozenset({1, 2, 3}): {1, 2, 3},
        frozenset({4, 5, 6}): {frozenset({1, 2, 3}): {1, 2, 3}, False: {7, 8, 9}},
        (0, 0): [(0, 0), (0, 1), (0, 1)],
    }

    cnt = find_occurrences(tree, False)
    assert cnt == 2
    cnt = find_occurrences(tree, {1, 2, 3})
    assert cnt == 2
    cnt = find_occurrences(tree, (7, 8, 9))
    assert cnt == 0
    cnt = find_occurrences(tree, {7, 8, 9})
    assert cnt == 1
    cnt = find_occurrences(tree, 0)
    assert cnt == 2  # could be 5
    cnt = find_occurrences(tree, (0, 0))
    assert cnt == 1
    cnt = find_occurrences(tree, (0, 1))
    assert cnt == 2


def test_with_float():
    tree = {"first": 2.0, "second": 2, "third": 0.5}
    cnt = find_occurrences(tree, 2.0)
    assert cnt == 2
    cnt = find_occurrences(tree, 0.5)
    assert cnt == 1


# TODO: ask mentor about this test
# def test_fails_with_float():
#     tree = {
#         1: bool(False),
#     }
#     cnt = find_occurrences(tree, float(0.0))
#     assert cnt == 0


def test_tree_with_invalid_data():
    tree = {"first": 1, "second": 2, "fourth": 4}
    cnt = find_occurrences(tree, 3)
    assert cnt == 0
