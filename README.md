# python_labs-ETX-

# Задание 1
# Простая программа: Привет/Возраст/Возраст через год
```python
Name = input('Имя:')
Age = input('Возраст:')
print(f"Привет, {Name}! Через год тебе будет {int(Age) + 1}.")
```
![](/images/lab%2001/img01.png)


# Задание 2
# Программа подсчёта суммы,среднее значение( Программа написана для вещественных чисел, без разницы на <,> и <.>)
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


