# Instruction
## Preparation
 - Install Python 3.9 >(https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository >`https://github.com/serereg/homework-repository`
 - Checkout branch >`homework4`
 - Open terminal
 - Change folder to clonned repository
 - Read docs to the testing module i.e. 'cat homework-repository/homework4/task_4_doctest.py`
 Doctests are placed in the docstring to the testing function fizzbuzz.
 For help on using doctest read https://docs.python.org/3/library/doctest.html
## Running doctest
 - Run doctest: `pytest --doctest-modules homework4/task_4_doctest.py
 - Output should repeat results in the docstring, like
 >>> fizzbuzz(1)
    ['1']

    >>> fizzbuzz(3)
    ['1', '2', 'fizz']

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']

    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz',\
 'buzz', '11', 'fizz', '13', '14', 'fizz buzz']

    >>> fizzbuzz(16)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz',\
 'buzz', '11', 'fizz', '13', '14', 'fizz buzz', '16']

    >>> fizzbuzz(0)
    []

    >>> fizzbuzz(-1)
    []

    >>> fizzbuzz(-10)
    []
## Contact information
 - In case of any issues, please, send the description to author name@example.com
