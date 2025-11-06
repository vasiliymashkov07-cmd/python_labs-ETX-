First = input("Первое число:")
if ',' in First: First = First.replace(',','.')
Second = input("Второе число:")
if ',' in Second: Second = Second.replace(',','.')
floatfirst = float(First)
floatsecond = float(Second)

Sum = floatfirst + floatsecond
Average = Sum / 2

print(f'Сумма = {Sum:.2f}; Среднее = {Average:.2f}')