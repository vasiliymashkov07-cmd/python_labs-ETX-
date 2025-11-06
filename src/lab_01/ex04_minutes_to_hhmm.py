minutes = input('Введите минуты:')
m = int(minutes)
hours = m // 60
ostatok = m % 60
print(f'{hours}:{ostatok}')