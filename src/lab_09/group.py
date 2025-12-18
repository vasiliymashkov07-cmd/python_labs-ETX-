import csv
from pathlib import Path
from typing import List, Dict, Any
from class_Student import Student

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        data_dir = Path("src/data/lab_09")
        self.path = data_dir / storage_path
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        if not self.path.exists():
            with open(self.path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
                writer.writeheader()
    
    def _read_all(self) -> List[Dict[str, Any]]:
        rows = []
        with open(self.path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != ['fio', 'birthdate', 'group', 'gpa']:
                raise ValueError("Неверный формат заголовка CSV файла")
            
            for row in reader:
                row['gpa'] = float(row['gpa'])
                rows.append(row)
        return rows
    
    def _write_all(self, rows: List[Dict[str, Any]]):
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(rows)
    
    def list(self) -> List[Student]:
        rows = self._read_all()
        students = []
        for row in rows:
            try:
                student = Student.from_dict(row)
                students.append(student)
            except ValueError as e:
                print(f"Ошибка валидации: {e}")
        return students
    
    def add(self, student: Student):
        try:
            validated_student = Student(
                fio=student.fio,
                birthdate=student.birthdate,
                group=student.group,
                gpa=student.gpa
            )
        except ValueError as e:
            raise ValueError(f"Некорректные данные: {e}")
        
        with open(self.path, 'a', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writerow(validated_student.to_dict())
    
    def find(self, substr: str) -> List[Student]:
        students = self.list()
        return [student for student in students if substr.lower() in student.fio.lower()]
    
    def remove(self, fio: str):
        rows = self._read_all()
        updated_rows = [row for row in rows if row['fio'] != fio]
        
        if len(updated_rows) == len(rows):
            raise ValueError(f"Студент с ФИО '{fio}' не найден")
        
        self._write_all(updated_rows)
    
    def update(self, fio: str, **fields):
        rows = self._read_all()
        updated = False
        
        for row in rows:
            if row['fio'] == fio:
                for field, value in fields.items():
                    if field in ['fio', 'birthdate', 'group', 'gpa']:
                        row[field] = value
                updated = True
                try:
                    Student.from_dict(row)
                except ValueError as e:
                    raise ValueError(f"Некорректные данные: {e}")
                break
        
        if not updated:
            raise ValueError(f"Студент с ФИО '{fio}' не найден")
        
        self._write_all(rows)


if __name__ == "__main__":
    group = Group("students.csv")
    
    if group.list() == []:
        test_students = [
            Student("Иванов Иван", "2000-05-15", "БИВТ-21-1", 3.5),
            Student("Петрова Анна", "2001-12-03", "БИВТ-21-2", 3.9),
            Student("Сидоров Алексей", "1999-08-22", "БИВТ-21-3", 4.5),
        ]
        
        for student in test_students:
            group.add(student)
    
    print("Все студенты:")
    for student in group.list():
        print(f"  {student}")
    
    print("\nПоиск 'Иванов':")
    for student in group.find("Иванов"):
        print(f"  {student}")
    
    try:
        group.update("Иванов Иван", gpa=5.0)
        print("\nПосле обновления GPA Иванова:")
        for student in group.list():
            if "Иванов" in student.fio:
                print(f"  {student}")
    except ValueError as e:
        print(f"Ошибка обновления: {e}")
    
    try:
        group.remove("Сидоров Алексей")
        print(f"\nПосле удаления Сидорова: {len(group.list())} студентов")
    except ValueError as e:
        print(f"Ошибка удаления: {e}")