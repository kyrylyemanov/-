"""Фігури для демонстрації покриття коду та розгалужень."""


class Figure:
    FIGURES = ("квадрат", "прямокутник", "трикутник")

    def __init__(self, figure_type: str) -> None:
        if figure_type not in self.FIGURES:
            raise ValueError(f"Невідомий тип фігури: {figure_type}")

        self.type = figure_type

    @property
    def get_angles(self) -> tuple[int, ...]:
        if self.type == "квадрат":
            return (90, 90, 90, 90)
        if self.type == "прямокутник":
            return (90, 90, 90, 90)
        return (60, 60, 60)
