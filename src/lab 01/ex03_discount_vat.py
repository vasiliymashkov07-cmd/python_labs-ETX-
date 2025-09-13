price = input('Цена:')
discount = input('Скидка%:')
vat = input('vat%:')

base = int(price) * (1 - int(discount)/100)
vat_amount = base * int(vat)/100
total = base + vat_amount
print(f'Итого к оплате: {total:.2f}.')