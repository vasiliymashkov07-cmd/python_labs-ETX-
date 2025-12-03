FIO = input("Введите ФИО:").strip()
FIO_clean = " ".join(FIO.split())
initials = "".join([w[0].upper() for w in FIO_clean.split()])

print(f"Инициалы: {initials}.")
print(f"Длина: {len(FIO_clean)}")
