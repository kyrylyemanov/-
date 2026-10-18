import unittest
from unittest.mock import patch

from app import Figure, count_vowels, read_positive_integer


class TestFigure(unittest.TestCase):
    def test_figure_properties(self):
        for figure_type in ("квадрат", "прямокутник", "трикутник"):
            with self.subTest(figure_type=figure_type):
                figure = Figure(figure_type, 5)
                self.assertEqual(figure_type, figure.get_figure_type)
                self.assertEqual(5, figure.get_figure_length)

    def test_figure_angles(self):
        expected_angles = {
            "квадрат": (90, 90, 90, 90),
            "прямокутник": (90, 90, 90, 90),
            "трикутник": (60, 60, 60),
        }
        for figure_type, angles in expected_angles.items():
            with self.subTest(figure_type=figure_type):
                self.assertEqual(angles, Figure(figure_type, 5).get_angles())

    def test_invalid_figure_data(self):
        for length in (0, -1):
            with self.subTest(length=length):
                with self.assertRaises(ValueError):
                    Figure("квадрат", length)
        with self.assertRaises(ValueError):
            Figure("коло", 5)


class TestCountVowels(unittest.TestCase):
    def test_ukrainian_word(self):
        self.assertEqual(6, count_vowels("Привіт, Україно"))

    def test_empty_string(self):
        self.assertEqual(0, count_vowels(""))

    def test_digits_and_punctuation(self):
        self.assertEqual(0, count_vowels("12345!?"))

    def test_ukrainian_letters_and_case(self):
        self.assertEqual(10, count_vowels("АЕЄИІЇОУЮЯ"))


class TestReadPositiveInteger(unittest.TestCase):
    @patch("builtins.input", return_value="5")
    def test_reads_positive_integer(self, mock_input):
        self.assertEqual(5, read_positive_integer())
        mock_input.assert_called_once_with("Введіть додатне ціле число: ")

    @patch("builtins.input", return_value="0")
    def test_rejects_zero(self, _mock_input):
        with self.assertRaises(ValueError):
            read_positive_integer()

    @patch("builtins.input", return_value="не число")
    def test_rejects_non_integer(self, _mock_input):
        with self.assertRaises(ValueError):
            read_positive_integer()


if __name__ == "__main__":
    unittest.main()
