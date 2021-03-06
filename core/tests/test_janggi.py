# coding: utf-8
import janggi
from data import Piece, A_INITIAL_STATE, B_INITIAL_STATE


def test_initial_board():
    j = janggi.Janggi()
    assert len(j.board) == 10
    assert all(row == [0] * 9 for row in j.board)
    assert j.on_changed is None


def test_initial_board_with_change_callback():
    def change_callback(board):
        assert True
    j = janggi.Janggi(change_callback)
    j.reset(A_INITIAL_STATE, B_INITIAL_STATE)
    assert len(j.board) == 10
    assert j.on_changed == change_callback


def test_turn():
    j = janggi.Janggi()
    assert j.turn == 'b'  # 楚
    assert not j.can_move(Piece.Cha_a)
    assert j.can_move(Piece.Cha_b)

    j.change_turn()
    assert j.turn == 'a'  # 漢
    assert j.can_move(Piece.Cha_a)
    assert not j.can_move(Piece.Cha_b)


def test_score():
    j = janggi.Janggi()
    j.reset(A_INITIAL_STATE, B_INITIAL_STATE)
    assert j.score('a') == 72 + 1.5
    assert j.score('b') == 72
