"""Фігури для прикладів із pytest."""


class Figure:
    FIGURES = ("квадрат", "прямокутник", "трикутник")

    def __init__(self, figure_type: str, length: int) -> None:
        if figure_type not in self.FIGURES:
            raise ValueError(f"Невідомий тип фігури: {figure_type}")
        if length <= 0:
            raise ValueError("Довжина має бути більшою за нуль")

        self.type = figure_type
        self._length = length

    @property
    def get_figure_length(self) -> int:
        return self._length
