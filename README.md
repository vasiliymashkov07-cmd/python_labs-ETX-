# python_labs-ETX-

# Лабораторная работа 1
# Задание 1
# Простая программа: Привет/Возраст/Возраст через год
```python
Name = input('Имя:')
Age = input('Возраст:')
print(f"Привет, {Name}! Через год тебе будет {int(Age) + 1}.")
```
![](/images/lab%2001/img01.png)


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
![](/images/lab%2001/img02.png)


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
![](/images/lab%2001/img03.png)


# Задание 4
# Перевод минут в Часы/Минуты (ЧЧ:ММ)
```python
minutes = input('Введите минуты:')
m = int(minutes)
hours = m // 60
ostatok = m % 60
print(f'{hours}:{ostatok}')
```
![](/images/lab%2001/img04.png)

# Задание 5
# Программа вводит ФИО, делает инициалы, не учитывая пробелы начала/конца/других лишних пробелов, считает длинну символов ФИО
```python
FIO = input('Введите ФИО:').strip()
FIO_clean = ' '.join(FIO.split())
initials = ''.join([w[0].upper() for w in FIO_clean.split()])

print(f'Инициалы: {initials}.')
print(f'Длина: {len(FIO_clean)}')
```
![](/images/lab%2001/img05.png)


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
![](/images/lab%2002/arrays.png)


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
![](/images/lab%2002/matrix.png)


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
![](/images/lab%2002/tuples.png)


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
    
   
    items.sort(key=lambda x: (-x[1], x[0]))
    
    
    return items[:2]

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
print(top_n(c_words))  
print(top_n(c_frame))
```
![](/images/lab%2003/text_py.png)


# Задание 2 - text_stats.py и defsfromtext.py
```python
import sys
from defsfromtext import normalize, tokenize, count_freq, top_n
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
![](/images/lab%2003/text_stats_py.png)