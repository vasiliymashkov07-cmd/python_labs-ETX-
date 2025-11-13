# python_labs-ETX-

# Лабораторная работа 1
# Задание 1
# Простая программа: Привет/Возраст/Возраст через год
```python
Name = input('Имя:')
Age = input('Возраст:')
print(f"Привет, {Name}! Через год тебе будет {int(Age) + 1}.")
```
![](/images/lab_01/img01.png)


# Задание 2
# Программа подсчёта суммы,среднее значение( Написана для вещественных чисел, без разницы на <,> и <.>)
```python
First = input("Первое число:")
if ',' in First: First = First.replace(',','.')
Second = input("Второе число:")
if ',' in Second: Second = Second.replace(',','.')
floatfirst = float(First)
floatsecond = float(Second)

Sum = floatfirst + floatsecond
Average = Sum / 2

print(f'Сумма = {Sum:.2f}; Среднее = {Average:.2f}')
```
![](/images/lab_01/img02.png)


# Задание 3
# Думаю все ходили в магазин, так что вот простая программа подсчета итоговой суммы, которая учитывает ценник, скидку и НДС
```python
price = input('Цена:')
discount = input('Скидка%:')
vat = input('vat%:')

base = int(price) * (1 - int(discount)/100)
vat_amount = base * int(vat)/100
total = base + vat_amount
print(f'Итого к оплате: {total:.2f}.')
``` 
![](/images/lab_01/img03.png)


# Задание 4
# Перевод минут в Часы/Минуты (ЧЧ:ММ)
```python
minutes = input('Введите минуты:')
m = int(minutes)
hours = m // 60
ostatok = m % 60
print(f'{hours}:{ostatok}')
```
![](/images/lab_01/img04.png)

# Задание 5
# Программа вводит ФИО, делает инициалы, не учитывая пробелы начала/конца/других лишних пробелов, считает длинну символов ФИО
```python
FIO = input('Введите ФИО:').strip()
FIO_clean = ' '.join(FIO.split())
initials = ''.join([w[0].upper() for w in FIO_clean.split()])

print(f'Инициалы: {initials}.')
print(f'Длина: {len(FIO_clean)}')
```
![](/images/lab_01/img05.png)


# Лабораторная работа 2
# Задание 1 - arrays.py
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
     return ValueError('Список пуст')
    return tuple([min(nums), max(nums)])

print(min_max([3,-1,5,5,0]))
print(min_max([42]))
print(min_max([-5,-2,-9]))
print(min_max([]))
print(min_max([1.5,2,2.0,-3.1]))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return list(set(nums))

print(unique_sorted([3,1,2,1,3]))
print(unique_sorted([]))
print(unique_sorted([-1,-1,0,2,2]))
print(unique_sorted([1.0, 1, 2.5,2.5,0]))


def flatten(mat: list[list | tuple]) -> list:
    I = list()
    for i in range(len(mat)):
        if isinstance(mat[i], list) or isinstance(mat[i], tuple):
            for j in mat[i]:
                I.append(j)
        else:
            return TypeError('Строка не строка строк матрицы')
    return I

print(flatten([[1,2],[3,4]]))
print(flatten([[1,2],(3,4,5)]))
print(flatten([[1],[],[2,3]]))
print(flatten([[1,2],"ab"]))
```
![](/images/lab_02/arrays.png)


# Задание 2 - matrix.py
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if mat == []:
        return []

    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            return ValueError("Матрица рваная - строки разной длины")

    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

print(transpose([[1,2,3]]))
print(transpose([[1],[2],[3]]))
print(transpose([[1,2],[3,4]]))
print(transpose([]))
print(transpose([[1,2] ,[3]]))


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []

    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            return ValueError("Матрица рваная - строки разной длины")

    return [sum(row) for row in mat]

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            return ValueError("Матрица рваная - строки разной длины")
    
    mat = transpose(mat)
        
    return [sum(row) for row in mat]

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```
![](/images/lab_02/matrix.png)


# Задание 3 - tuples.py
```python
def errorcheckandformat(fio: str, group: str, gpa: float) -> tuple:
    if not isinstance(fio, str):
        raise TypeError("Строки нету")
    if not isinstance(group, str):
        raise TypeError("Строки нету")
    if not isinstance(gpa, (float, int)):
        raise TypeError("Тип float или int не найден")
    
    nameandsurname = fio.strip().split() #Удаляем пробелы и разбиваем
    nameandsurname = [x.capitalize() for x in  nameandsurname] #1-буква с заглавной, остальные с маленькой


    def format(parts):
        username = parts[0]
        first_initial = parts[1][0].upper() + '.'
        if len(parts) > 2:
            secondinitial = parts[2][0].upper() + '.'
        else: secondinitial = ''
        return f'{username} {first_initial}{secondinitial}'
    
    new_fio = format(nameandsurname)
    new_gpa = f'{gpa:.2f}' #Округляем до 2 знаков после запятой

    return (new_fio,group,new_gpa)

print(errorcheckandformat("Иванов Иван Иванович", " гр. BIVT-25", 4.6))
print(errorcheckandformat("Петров Пётр", " гр. IKBO-12", 5.0))
print(errorcheckandformat("Петров Пётр Петрович", " гр. IKBO-12", 5.0))
print(errorcheckandformat("  сидорова  анна   сергеевна ", " гр. ABB-01", 3.999))
```
![](/images/lab_02/tuples.png)


# Лабораторная работа 3
# Задание 1 - text.py
```python
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str: 
    result = text
    result = result.replace('\t' , ' ').replace('\n', ' ').replace('\r',' ')
    if casefold == True:
        result = result.casefold()

    if yo2e == True:
        result = result.replace('Ё','Е').replace('ё','е')

    result = result.strip()
    
    if '  ' in result:
        result = result.replace('  ', '')
    
    return result


def tokenize(text: str) -> list[str]: 
    symbols = r'\w+(?:-\w+)*\b'         # /w+ (ищет слова) ?:-\w+ (ищет слова с дефисами) 
                                        # * (ноль и более раз дефис) \b (граница слова)
    tokens = re.findall(symbols,text)

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
    print(tokenize('привет мир'))
    print(tokenize('hello,world!!!'))
    print(tokenize('по-настоящему круто'))
    print(tokenize('2025 год'))
    print(tokenize('emoji 😀 не слово'))
    words = ["a", "b", "a", "c", "b", "a"]
    c_words = count_freq(words)
    print(c_words)
    frame = ["bb","aa","bb","aa","cc"] 
    c_frame = count_freq(frame)
    print(c_frame)
    print(top_n(c_words,2))  
    print(top_n(c_frame,2))
```
![](/images/lab_03/text_py.png)


# Задание 2 - text_stats.py и defsfromtext.py
```python
import sys
sys.path.append(r'C:\GitHub_Misis\python_labs-ETX-\src\lib')
from text import normalize,tokenize,top_n,count_freq

def main():

    
    text = "Привет, мир! Привет!!!"
    

    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    total_words = len(tokens)
    freq_dict = count_freq(tokens)
    unique_words = len(freq_dict)
    top_words = top_n(freq_dict, 5)
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
   
    for word, count in top_words:
        print(f"{word}:{count}")

main()  
```
![](/images/lab_03/text_stats_py.png)


# Лабораторная работа 4
# Задание 1 - io_txt_csv.py
```python
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
```
# Код читает и выводит текст из src/data/lab_04/input.txt а также создает тестовый файл check.csv в src/data/lab_04
![](/images/lab_04/data_input_text.png)
![](/images/lab_04/io_txt_csv.png) 
![](/images/lab_04/check_creatingfile.png)


# Задание 2 - text_report.py
```python
import sys
sys.path.append(r'C:\GitHub_Misis\python_labs-ETX-\src\lib')
from text import normalize,tokenize,top_n,count_freq

from io_txt_csv import read_text,write_csv

def text_stats(text_optimisation):
    text_optimisation01 = normalize(text_optimisation) 
    text_optimisation02 = tokenize(text_optimisation01) 
    words_sum = len(text_optimisation02)
    count_freqtext = count_freq(text_optimisation02)
    uni_words = len(count_freqtext)
    top5 = top_n(count_freqtext)

    print(f"Всего слов: {words_sum}")
    print(f"Уникальных слов: {uni_words}")
    print("Топ-5:")
   
    for word, count in top5:
        print(f"{word}:{count}")



txt01 = read_text("src/data/lab_04/input.txt")
text_stats(txt01)

write_csv(top_n(count_freq(tokenize(normalize(txt01))), 100)\
          , path = r'C:\GitHub_Misis\python_labs-ETX-\src\data\lab_04\check2.csv', header= ['Слова', 'Подсчёт'])
```
# Код читает текст, выводит работу из 3 Лабы (Как в файле src/lab_03/text_stats.py) и создает файл check2.csv в src/data/lab_04
# В check2.csv написано каждое слово текста из src/data/lab_04/input.txt и то, сколько раз оно встречается
![](/images/lab_04/data_input_text.png)
![](/images/lab_04/text_report.png)
![](/images/lab_04/check2_creatingfile.png)


# Лабораторная работа 5
# Задание 1 - json_csv.py
```python
import json, csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:

    json_file = Path("src/data/lab_05/samples/people.json")

    if not json_file.exists():
        raise FileNotFoundError('Файл не найден')
    if json_file.suffix.lower() != '.json':
        raise ValueError('Не json')
    
    with open(json_path,'r', encoding='utf-8') as f:
        data_json = json.load(f)

    with open(csv_path,'w', encoding ='utf-8') as f:
        write = csv.DictWriter(f,fieldnames=data_json[0])
        write.writeheader()
        write.writerows(data_json)


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_file = Path("src/data/lab_05/samples/people.csv")

    if not csv_file.exists():
        raise FileNotFoundError('Файл не найден')
    if csv_file.suffix.lower() != '.csv':
        raise ValueError('Не csv')
    
    with open(csv_path,'r',encoding ='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    with open(json_path,'w',newline="",encoding = 'utf-8') as f:
        json.dump(data,f, ensure_ascii=False, indent=2)


csv_to_json("src/data/lab_05/samples/people.csv","src/data/lab_05/out/people_from_csv.json") 
json_to_csv("src/data/lab_05/samples/people.json", "src/data/lab_05/out/people_from_json.csv")
```
# Было до :
![](/images/lab_05/people_json.png)
![](/images/lab_05/people_csv.png)


# Стало после :
![](/images/lab_05/people_from_json_to_csv.png)
![](/images/lab_05/people_from_csv_to_json.png)


# Задание 2 - csv_xlsx.py
# В файле lib/requirements.txt написано, что нужно написать в терминале чтобы установить openpyxl
```python
import csv

from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    with open(csv_path,'r',encoding="utf-8") as f:
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
          
csv_to_xlsx('src\data\lab_05\samples\people.csv','src\data\lab_05\out\people.xlsx')
```
# Результат преобразования файла people.csv в people.xlsx (Эксель)  
![](/images/lab_05/people.xlsx.png)

