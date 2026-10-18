import pytest

from app import Figure


@pytest.fixture

def square():
    return Figure("квадрат", 10)


@pytest.fixture(scope="module")
def allowed_figures():
    return Figure.FIGURES


@pytest.mark.unit
@pytest.mark.parametrize("figure_type", Figure.FIGURES)
def test_allowed_figure(figure_type):
    figure = Figure(figure_type, 1)
    assert figure.type == figure_type


@pytest.mark.parametrize("figure_type", ["коло", "", "п'ятикутник"])
def test_rejects_unknown_figure(figure_type):
    with pytest.raises(ValueError):
        Figure(figure_type, 1)


@pytest.mark.parametrize("length", [0, -1, -10])
def test_rejects_invalid_length(length):
    with pytest.raises(ValueError):
        Figure("квадрат", length)


def test_square_properties(square):
    assert square.type == "квадрат"
    assert square.get_figure_length == 10


@pytest.mark.unit
def test_allowed_figures_are_available(allowed_figures):
    assert allowed_figures == ("квадрат", "прямокутник", "трикутник")


def test_allowed_figures_are_unique(allowed_figures):
    assert len(allowed_figures) == len(set(allowed_figures))
