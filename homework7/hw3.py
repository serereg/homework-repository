"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def wins_combinations(n: int = 1):
    """Generate wins combinations from a board with size NxN.

    Example of board and wins combinations:
    ((a, b, c),
     (d, e, f),
     (g, h, i)) = (
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
    )

    wins_combinations = [
        [a, b, c], [d, e, f], [g, h, i],
        [a, d, g], [b, e, h], [c, f, i],
        [a, e, i],
        [c, e, g],
    ]
    """
    if n <= 1:
        yield [(0, 0)]
        return

    for i in range(n):
        line_horizontal = []
        line_vertical = []
        # TODO: change to tuple comprehension
        for j in range(n):
            line_horizontal.append((i, j))
            line_vertical.append((j, i))
        yield line_horizontal
        yield line_vertical

    yield [(i, i) for i in range(n)]  # diagonal left-right
    yield [(i, n - 1 - i) for i in range(n)]  # diagonal right-left


def tic_tac_toe_checker(board: List[List]) -> str:
    """Check a Tic-Tac-Toe NxN board for the winner.

    Args:
        board: a board size NxN. The smallest size is N = 1.
        For 3x3:
            [[-, -, o],
             [-, x, o],
             [x, o, x]]

    Returns:
        If there is "x" winner, function should return "x wins!"
        If there is "o" winner, function should return "o wins!"
        If there is a draw, function should return "draw!"
        If board is unfinished, function should return "unfinished!"
    """

    def check_winner(letter: str):
        def check_line(line: list):
            return all(sym == letter for sym in line)

        return any(
            check_line([board[pos[0]][pos[1]] for pos in combination])
            for combination in wins_combinations(len(board))
        )

    x_pretend = check_winner("x")
    o_pretend = check_winner("o")
    if (x_pretend, o_pretend) == (True, False):
        return "x wins!"
    if (x_pretend, o_pretend) == (False, True):
        return "o wins!"
    if any("-" in row for row in board):
        return "unfinished"
    return "draw!"
