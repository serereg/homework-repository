import os

from homework2.hw1 import get_longest_diverse_words


test_data = os.path.dirname(__file__) + '/test_data/data.txt'


def test_get_longest_diverse_words():
    """Testing function get_longest_divetse_words
    """
    assert ['Bev\\u00f6lkerungsabschub',
     'unmi\\u00dfverst\\u00e4ndliche', 'Werkst\\u00e4ttenlandschaft', 
     'Werkst\\u00e4ttenlandschaft', 'Selbstverst\\u00e4ndlich', 'vernachl\\u00e4ssigt', 
     'r\\u00e9sistance-Bewegungen', 'au\\u00dfenpolitisch', '\\u00fcberw\\u00e4ltigende', 
     '\\u00fcberw\\u00e4ltigend'] == get_longest_diverse_words(test_data)

