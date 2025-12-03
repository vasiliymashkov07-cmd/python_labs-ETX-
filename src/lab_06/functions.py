import re
import csv
from openpyxl import Workbook
import json, csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:

    json_file = Path("src/data/lab_05/samples/people.json")

    if not json_file.exists():
        raise FileNotFoundError("Файл не найден")
    if json_file.suffix.lower() != ".json":
        raise ValueError("Не json")

    with open(json_path, "r", encoding="utf-8") as f:
        data_json = json.load(f)

    with open(csv_path, "w", encoding="utf-8") as f:
        write = csv.DictWriter(f, fieldnames=data_json[0])
        write.writeheader()
        write.writerows(data_json)


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_file = Path("src/data/lab_05/samples/people.csv")

    if not csv_file.exists():
        raise FileNotFoundError("Файл не найден")
    if csv_file.suffix.lower() != ".csv":
        raise ValueError("Не csv")

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    with open(json_path, "w", newline="", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    with open(csv_path, "r", encoding="utf-8") as f:
        read = csv.reader(f)
        for row in read:
            ws.append(row)

    for column in ws.columns:
        column_letter = column[0].column_letter  # Получаем букву колонки (A, B, C...)
        max_length = 8  # Минимальная ширина

        for cell in column:
            if cell.value:
                # Ищем самую длинную строку в колонке
                max_length = max(max_length, len(str(cell.value)))

        # Устанавливаем ширину колонки
        ws.column_dimensions[column_letter].width = max_length + 2

    wb.save(xlsx_path)


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
