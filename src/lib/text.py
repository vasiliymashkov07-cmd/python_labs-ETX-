import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    result = text
    result = result.replace("\t", " ").replace("\n", " ").replace("\r", " ")
    if casefold == True:
        result = result.casefold()

    if yo2e == True:
        result = result.replace("Ё", "Е").replace("ё", "е")

    result = result.strip()

    if "  " in result:
        result = result.replace("  ", "")

    return result


def tokenize(text: str) -> list[str]:
    symbols = r"\w+(?:-\w+)*\b"  # /w+ (ищет слова) ?:-\w+ (ищет слова с дефисами)
    # * (ноль и более раз дефис) \b (граница слова)
    tokens = re.findall(symbols, text)

    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq_dict = {}
    for tok in tokens:
        if tok in freq_dict:
            freq_dict[tok] += 1
        else:
            freq_dict[tok] = 1
    return freq_dict


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

    items = list(freq.items())

    items.sort(key=lambda x: x[0])
    items.sort(key=lambda x: x[1], reverse=True)

    return items[:n]


if __name__ == "__main__":
    print(normalize("ПрИвЕт\nМИр\t"))
    print(normalize("ёжик, Ёлка"))
    print(normalize("Hello\r\nWorld"))
    print(normalize("   двойные   пробелы  "))
    print(tokenize("привет мир"))
    print(tokenize("hello,world!!!"))
    print(tokenize("по-настоящему круто"))
    print(tokenize("2025 год"))
    print(tokenize("emoji 😀 не слово"))
    words = ["a", "b", "a", "c", "b", "a"]
    c_words = count_freq(words)
    print(c_words)
    frame = ["bb", "aa", "bb", "aa", "cc"]
    c_frame = count_freq(frame)
    print(c_frame)
    print(top_n(c_words, 2))
    print(top_n(c_frame, 2))
