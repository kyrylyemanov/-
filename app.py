
class Figure:
    """Фігура з однією заданою довжиною."""

    _ANGLES = {
        "квадрат": (90, 90, 90, 90),
        "прямокутник": (90, 90, 90, 90),
        "трикутник": (60, 60, 60),
    }

    def __init__(self, figure_type: str, length: float) -> None:
        if figure_type not in self._ANGLES:
            raise ValueError(f"Невідомий тип фігури: {figure_type}")
        if length <= 0:
            raise ValueError("Довжина має бути більшою за нуль")

        self._figure_type = figure_type
        self._length = length

    @property
    def get_figure_type(self) -> str:
        return self._figure_type

    @property
    def get_figure_length(self) -> float:
        return self._length

    def get_angles(self) -> tuple[int, ...]:
        return self._ANGLES[self._figure_type]


def count_vowels(text: str) -> int:
    """Рахує українські голосні літери незалежно від регістру."""
    vowels = "аеєиіїоуюя"
    return sum(character in vowels for character in text.casefold())


def read_positive_integer() -> int:
    """Зчитує з консолі та перевіряє додатне ціле число."""
    number = int(input("Введіть додатне ціле число: "))
    if number <= 0:
        raise ValueError("Число має бути більшим за нуль")
    return number
