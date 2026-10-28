import pytest

from app import Figure


def test_square_angles():
    assert Figure("квадрат").get_angles == (90, 90, 90, 90)


def test_rectangle_angles():
    assert Figure("прямокутник").get_angles == (90, 90, 90, 90)


def test_triangle_angles():
    assert Figure("трикутник").get_angles == (60, 60, 60)


def test_unknown_figure_is_rejected():
    with pytest.raises(ValueError, match="Невідомий тип фігури"):
        Figure("коло")
