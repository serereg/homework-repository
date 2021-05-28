from typing import List, Tuple

from homework7.hw3 import wins_combinations, tic_tac_toe_checker


def test_wins_combinations():
    ((a, b, c), (d, e, f), (g, h, i)) = (
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
    )
    combinations = wins_combinations(3)

    assert [
        [a, b, c],
        [a, d, g],
        [d, e, f],
        [b, e, h],
        [g, h, i],
        [c, f, i],
        [a, e, i],
        [c, e, g],
    ] == list(combinations)


def generate_boards(
    win: str, los: str, unf: str
) -> Tuple[List[List[List[str]]], List[List[List[str]]], List[List[List[str]]]]:
    # fmt: off
    board_w_wins_horizontal = [[[unf, unf, los],
                                [unf, los, los],
                                [win, win, win]],

                               [[unf, unf, los],
                                [win, win, win],
                                [win, win, los]],

                               [[win, win, win],
                                [win, unf, los],
                                [win, win, los]]]
    board_w_wins_vertical = [[[win, los, los],
                              [win, unf, los],
                              [win, los, win]],

                             [[unf, win, los],
                              [win, win, los],
                              [los, win, win]],

                             [[unf, unf, win],
                              [win, los, win],
                              [los, win, win]]]
    board_w_wins_diagonal = [[[win, unf, los],
                              [unf, win, los],
                              [unf, los, win]],

                             [[los, unf, win],
                              [unf, win, los],
                              [win, unf, unf]]]
    # fmt: on
    return (board_w_wins_diagonal, board_w_wins_horizontal, board_w_wins_vertical)


def test_x_or_o_wins():
    # TODO: is it right way to generate combinations automatically?
    #  also use mark.parametrize

    (
        board_w_wins_diagonal,
        board_w_wins_horizontal,
        board_w_wins_vertical,
    ) = generate_boards("x", "o", "-")

    assert "x wins!" == tic_tac_toe_checker(board_w_wins_horizontal[0])
    assert "x wins!" == tic_tac_toe_checker(board_w_wins_horizontal[1])
    assert "x wins!" == tic_tac_toe_checker(board_w_wins_horizontal[2])
    assert "x wins!" == tic_tac_toe_checker(board_w_wins_vertical[0])
    assert "x wins!" == tic_tac_toe_checker(board_w_wins_vertical[1])
    assert "x wins!" == tic_tac_toe_checker(board_w_wins_vertical[2])
    assert "x wins!" == tic_tac_toe_checker(board_w_wins_diagonal[0])
    assert "x wins!" == tic_tac_toe_checker(board_w_wins_diagonal[1])

    (
        board_w_wins_diagonal,
        board_w_wins_horizontal,
        board_w_wins_vertical,
    ) = generate_boards("o", "x", "-")

    assert "o wins!" == tic_tac_toe_checker(board_w_wins_horizontal[0])
    assert "o wins!" == tic_tac_toe_checker(board_w_wins_horizontal[1])
    assert "o wins!" == tic_tac_toe_checker(board_w_wins_horizontal[2])
    assert "o wins!" == tic_tac_toe_checker(board_w_wins_vertical[0])
    assert "o wins!" == tic_tac_toe_checker(board_w_wins_vertical[1])
    assert "o wins!" == tic_tac_toe_checker(board_w_wins_vertical[2])
    assert "o wins!" == tic_tac_toe_checker(board_w_wins_diagonal[0])
    assert "o wins!" == tic_tac_toe_checker(board_w_wins_diagonal[1])

    smallest_board = [["x"]]
    assert "x wins!" == tic_tac_toe_checker(smallest_board)

    smallest_board = [["o"]]
    assert "o wins!" == tic_tac_toe_checker(smallest_board)


def test_draw():
    # fmt: off
    board1 = [["o", "x", "o"],
              ["x", "o", "o"],
              ["x", "o", "x"]]

    board2 = [["x", "o", "o"],
              ["o", "x", "x"],
              ["x", "o", "o"]]
    # fmt: on
    assert "draw!" == tic_tac_toe_checker(board1)
    assert "draw!" == tic_tac_toe_checker(board2)


def test_unfinished():
    # fmt: off
    board1 = [["-", "x", "o"],
              ["-", "o", "o"],
              ["-", "o", "x"]]

    board2 = [["-", "-", "o"],
              ["o", "-", "o"],
              ["x", "-", "x"]]
    # fmt: on
    assert "unfinished" == tic_tac_toe_checker(board1)
    assert "unfinished" == tic_tac_toe_checker(board2)
