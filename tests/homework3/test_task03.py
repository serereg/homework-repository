from homework3.task03 import Filter, make_filter


def testing_with_dictionaries_with_filter_by_properties():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]

    assert [sample_data[1]] == (
        make_filter(name="polly", type="bird").apply(sample_data)
    )


def testing_with_dictionaries_with_filter_with_non_existing_properties():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]

    assert (make_filter(name="Bill", type="bird").apply(sample_data)) == []


def test_with_list_of_integers_with_positive_evens_filter():
    positive_even = Filter(
        [lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)]
    )
    assert [2, 4, 6, 8] == positive_even.apply(range(10))


def test_with_zero_list_for_filtering():
    positive_even = Filter(
        [lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)]
    )
    assert [] == positive_even.apply(range(0))


def test_with_always_false_functions():
    zero = Filter([lambda a: a > 0, lambda a: a < 0])
    assert [] == zero.apply(range(100))


def test_with_no_data_for_selected_criteria():
    zero = Filter([lambda a: a % 2 == 0, lambda a: a > 0])
    assert [] == zero.apply([-1, -2, -3])
