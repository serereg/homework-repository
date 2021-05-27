from homework7.hw3 import tic_tac_toe_checker


def test_x_or_o_wins():
    # TODO: is it right way to generate combinations automatically?
    #  also use mark.parametrize

    w, l, u = "x", "o", "-"
    # fmt: off
    board_w_wins_horizontal = [[[u, u, l],
                                [u, l, l],
                                [w, w, w]],

                               [[u, u, l],
                                [w, w, w],
                                [w, w, l]],

                               [[w, w, w],
                                [w, u, l],
                                [w, w, l]]]

    board_w_wins_vertical = [[[w, l, l],
                              [w, u, l],
                              [w, l, w]],

                             [[u, w, l],
                              [w, w, l],
                              [l, w, w]],

                             [[u, u, w],
                              [w, l, w],
                              [l, w, w]]]

    board_w_wins_diagonal = [[[w, u, l],
                              [u, w, l],
                              [u, l, w]],

                             [[l, u, w],
                              [u, w, l],
                              [w, u, u]]]
    # fmt: on
    assert "x wins!" == tic_tac_toe_checker(board_w_wins_horizontal[0])
    assert "x wins!" == tic_tac_toe_checker(board_w_wins_horizontal[1])
    assert "x wins!" == tic_tac_toe_checker(board_w_wins_horizontal[2])
    assert "x wins!" == tic_tac_toe_checker(board_w_wins_vertical[0])
    assert "x wins!" == tic_tac_toe_checker(board_w_wins_vertical[1])
    assert "x wins!" == tic_tac_toe_checker(board_w_wins_vertical[2])
    assert "x wins!" == tic_tac_toe_checker(board_w_wins_diagonal[0])
    assert "x wins!" == tic_tac_toe_checker(board_w_wins_diagonal[1])


def test_draw():
    # fmt: off
    board1 = [["o", "x", "o"],
              ["x", "o", "o"],
              ["x", "o", "x"]]

    # fmt: on
    board2 = [["x", "o", "o"], ["o", "x", "x"], ["x", "o", "o"]]
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
