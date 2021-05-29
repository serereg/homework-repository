from homework7.hw1 import find_occurrences


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
