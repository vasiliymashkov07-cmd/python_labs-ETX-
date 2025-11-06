from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:

    try:
       p = Path(path)
       return p.read_text(encoding=encoding)
    except FileNotFoundError: 
       return 'Файл не найден'
    except UnicodeDecodeError: 
       return 'Не та кодировка'

import csv
from pathlib import Path
from typing import Iterable, Sequence

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        if rows:
            equal = len(rows[0])
            for r in rows:
                if len(r) != equal:
                    raise ValueError('Строка не имеет одинаковое длинну')
            for r in rows:
                w.writerow(r)

txt01 = read_text("src/data/lab_04/input.txt")  
print(txt01)
write_csv([("world","count"),("test",3)], r'C:\GitHub_Misis\python_labs-ETX-\src\data\lab_04\check.csv', header=('a','b'))
   


