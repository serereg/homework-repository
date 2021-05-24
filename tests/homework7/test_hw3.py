from homework7.hw3 import tic_tac_toe_checker


def test_x_wins():
    board1 = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]
    assert "x wins!" == tic_tac_toe_checker(board1)

    board2 = [["x", "-", "o"], ["x", "o", "o"], ["x", "o", "x"]]

    assert "x wins!" == tic_tac_toe_checker(board2)


def test_o_wins():
    board1 = [["-", "-", "o"], ["-", "o", "x"], ["o", "o", "o"]]
    assert "o wins!" == tic_tac_toe_checker(board1)

    board2 = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "o"]]
    assert "o wins!" == tic_tac_toe_checker(board2)

    assert "o wins!" == tic_tac_toe_checker(board2)


def test_draw():
    board1 = [["o", "x", "o"], ["x", "o", "o"], ["x", "o", "x"]]
    assert "draw!" == tic_tac_toe_checker(board1)

    board2 = [["x", "o", "o"], ["o", "x", "x"], ["x", "o", "o"]]

    assert "draw!" == tic_tac_toe_checker(board2)


def test_unfinished():
    board1 = [["-", "x", "o"], ["-", "o", "o"], ["-", "o", "x"]]
    assert "unfinished" == tic_tac_toe_checker(board1)

    board2 = [["-", "-", "o"], ["o", "-", "o"], ["x", "-", "x"]]

    assert "unfinished" == tic_tac_toe_checker(board2)
