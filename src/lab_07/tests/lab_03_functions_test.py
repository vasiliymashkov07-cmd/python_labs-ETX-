import pytest
from functions import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет\nмир\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("hello\r\nworld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("", []),  # пустая строка
        ("   ", []),  # только пробелы
        ("!!!@@@###", []),  # только спецсимволы
        ("раз два.три,четыре!пять?", ["раз", "два", "три", "четыре", "пять"]),
        ("цифры123 и символы!", ["цифры123", "и", "символы"]),
    ],
)
def test_tokenize(source, expected):
    assert tokenize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        (["apple", "apple", "banana"], {"apple": 2, "banana": 1}),
        (["a", "b", "a", "c", "c"], {"a": 2, "b": 1, "c": 2}),
        ([], {}),  # пустой список
        (["x"], {"x": 1}),  # один элемент
        (["lol", "lol", "lol"], {"lol": 3}),  # все одинаковые
        (["4", "6", "8"], {"4": 1, "6": 1, "8": 1}),  # все разные
    ],
)
def test_count_freq(source, expected):
    assert count_freq(source) == expected


@pytest.mark.parametrize(
    "freq, n, expected",
    [
        ({"pineapple": 2, "apple": 1}, 1, [("pineapple", 2)]),
        ({"a": 5, "b": 5, "c": 3}, 2, [("a", 5), ("b", 5)]),  # ничья
        ({"x": 1}, 1, [("x", 1)]),  # один элемент
        ({}, 5, []),  # пустой словарь
        ({"a": 10, "b": 10, "c": 10}, 2, [("a", 10), ("b", 10)]),  # все одинаковые
        ({"z": 1, "y": 2, "x": 3}, 2, [("x", 3), ("y", 2)]),  # проверка порядка
    ],
)
def test_top_n(freq, n, expected):
    assert top_n(freq, n) == expected
