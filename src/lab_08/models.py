from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        # Валидация формата даты
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                f"Неверный формат: {self.birthdate}. Ожидается формат: YYYY-MM-DD"
            )

        # Валидация диапазона GPA
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"Gpa должен быть от 0 до 5 {self.gpa}")

    def age(self) -> int:
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()

        # Вычисляем возраст
        age = today.year - birth_date.year

        # Если день рождения в этом году еще не наступил, вычитаем 1 год
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age = age - 1

        return age

    def to_dict(self) -> dict:
        # Проверяем, что все поля корректны
        if not all([self.fio, self.birthdate, self.group]):
            raise ValueError("Все поля должны быть заполнены")

        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        # Десереализация из словаря
        return cls(
            fio=d["fio"], birthdate=d["birthdate"], group=d["group"], gpa=d["gpa"]
        )

    def __str__(self):
        # Вывод
        return f"{self.fio}, группа {self.group}, возраст {self.age()}, GPA: {self.gpa}"
