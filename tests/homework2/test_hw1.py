import os

from homework2.hw1 import get_longest_diverse_words


test_data = os.path.dirname(__file__) + '/test_data/data.txt'


def test_get_longest_diverse_words():
    """Testing function get_longest_divetse_words
    """
    assert ['unmißverständliche', 'Kollektivschuldiger', 'Bevölkerungsabschub',
            'résistance-Bewegungen', 'politisch-strategischen', 'Werkstättenlandschaft',
            'Werkstättenlandschaft', 'Selbstverständlich', 'Schicksalsfiguren',
            'zoologisch-politischen'] == get_longest_diverse_words(test_data)
