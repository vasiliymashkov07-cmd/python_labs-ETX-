from serialize import students_to_json, students_from_json
import json
import os


class Config:
    BASE_DIR = "src/data/lab_08"
    INPUT_FILE = os.path.join(BASE_DIR, "students_input.json")
    OUTPUT_FILE = os.path.join(BASE_DIR, "students_output.json")


def create_input_file():
    if not os.path.exists(Config.INPUT_FILE):  # создает students_input.json
        sample_data = [
            {
                "fio": "Машков Василий Сергеевич",
                "birthdate": "2007-08-28",
                "group": "BIVT-03",
                "gpa": 4.4,
            },
            {
                "fio": "Тарасов Михаил Ярославович",
                "birthdate": "2006-05-12",
                "group": "BIVT-02",
                "gpa": 4.8,
            },
            {
                "fio": "Большакова Камила Никитична",
                "birthdate": "1992-01-11",
                "group": "BIVT-10",
                "gpa": 2.3,
            },
            {
                "fio": "Кузнецов Роман Адамович",
                "birthdate": "2010-09-14",
                "group": "BIVT-12",
                "gpa": 3.2,
            },
        ]
        with open(Config.INPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(sample_data, f, ensure_ascii=False, indent=2)

        print(f"Создан файл {Config.INPUT_FILE} с тестовыми данными")
    return Config.INPUT_FILE


def main():
    print("Думаем")

    # Создаем файл students_input.json
    create_input_file()

    # Загружаем студентов
    try:
        students = students_from_json(Config.INPUT_FILE)  # Используем Config
        print(f"Загружено: {len(students)} студентов")
        for s in students:
            print(f"  - {s}")
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
        return

    # Сохраняем студентов
    try:
        students_to_json(students, Config.OUTPUT_FILE)  # Используем Config
        print(f"Сохранено в {Config.OUTPUT_FILE}")
    except Exception as e:
        print(f"Ошибка сохранения: {e}")
        return


if __name__ == "__main__":
    main()
