def errorcheckandformat(fio: str, group: str, gpa: float) -> tuple:
    if not isinstance(fio, str):
        raise TypeError("Строки нету")
    if not isinstance(group, str):
        raise TypeError("Строки нету")
    if not isinstance(gpa, (float, int)):
        raise TypeError("Тип float или int не найден")

    nameandsurname = fio.strip().split()  # Удаляем пробелы и разбиваем
    nameandsurname = [
        x.capitalize() for x in nameandsurname
    ]  # 1-буква с заглавной, остальные с маленькой

    def format(parts):
        username = parts[0]
        first_initial = parts[1][0].upper() + "."
        if len(parts) > 2:
            secondinitial = parts[2][0].upper() + "."
        else:
            secondinitial = ""
        return f"{username} {first_initial}{secondinitial}"

    new_fio = format(nameandsurname)
    new_gpa = f"{gpa:.2f}"  # Округляем до 2 знаков после запятой

    return (new_fio, group, new_gpa)


print(errorcheckandformat("Иванов Иван Иванович", " гр. BIVT-25", 4.6))
print(errorcheckandformat("Петров Пётр", " гр. IKBO-12", 5.0))
print(errorcheckandformat("Петров Пётр Петрович", " гр. IKBO-12", 5.0))
print(errorcheckandformat("  сидорова  анна   сергеевна ", " гр. ABB-01", 3.999))
