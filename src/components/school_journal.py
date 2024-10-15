from src.components.person import Person
from typing import List, Optional, Dict
from datetime import datetime
from src.components.date_analysis import get_zodiac_sign, days_since_birth


class Grade:
    """Класс для хранения оценок по определенному предмету."""

    def __init__(self, subject: str, grades: List[int]) -> None:
        self.subject = subject
        self.grades = grades

    def get_average(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0.0


class Student(Person):
    """Класс для представления студента."""

    def __init__(self, name: str, birthdate: str) -> None:
        super().__init__(name, birthdate)
        self.birthdate = datetime.strptime(birthdate, "%d.%m.%Y")
        self.grades: Dict[str, Grade] = {}

    def add_grades(self, subject: str, grades: List[int]) -> None:
        MIN_GRADES = 2
        MAX_GRADES = 16
        if MIN_GRADES <= len(grades) <= MAX_GRADES:
            self.grades[subject] = Grade(subject=subject, grades=grades)
        else:
            print(f"Количество оценок по предмету '{subject}' должно быть от {MIN_GRADES} до {MAX_GRADES}.")

    def update_grades(self, subject: str, new_grades: List[int]) -> None:
        if subject in self.grades:
            self.grades[subject].grades = new_grades
        else:
            print(f"Предмет '{subject}' не найден у студента.")

    def get_average_grade(self, subject: str) -> Optional[float]:
        if subject in self.grades and self.grades[subject].grades:
            return self.grades[subject].get_average()
        return None

    def get_overall_average(self) -> Optional[float]:
        if not self.grades:
            return None
        total_sum = sum(grade.get_average() for grade in self.grades.values())
        return total_sum / len(self.grades)

    def get_age(self) -> int:
        today = datetime.today()
        return today.year - self.birthdate.year - (
                    (today.month, today.day) < (self.birthdate.month, self.birthdate.day))

    def display_info(self) -> None:
        """Отображение информации о студенте."""
        zodiac_sign = get_zodiac_sign(self.birthdate)
        days_lived = days_since_birth(self.birthdate)

        print(f"Студент: {self.name}")
        print(f"Дата рождения: {self.birthdate.strftime('%d.%m.%Y')}")
        print(f"Возраст: {self.get_age()} лет")
        print(f"Знак зодиака: {zodiac_sign}")
        print(f"Дней с момента рождения: {days_lived}")

        for subject, grade in self.grades.items():
            grades_str = ', '.join(map(str, grade.grades))
            avg_grade = grade.get_average()
            print(f"Предмет: {subject}, Оценки: {grades_str}, Средний балл: {avg_grade:.2f}")

        overall_average = self.get_overall_average()
        if overall_average is not None:
            print(f"Средний балл по всем предметам: {round(overall_average, 2)}")
        print("-" * 40)


class SchoolJournal:
    """Класс для управления списком студентов."""

    def __init__(self) -> None:
        self.students: List[Student] = []

    def create_student(self, name: str, birthdate: str) -> Student:
        return Student(name, birthdate)

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def get_student_by_index(self, index: int) -> Student:
        return self.students[index]

    def display_statistics(self) -> None:
        if not self.students:
            print("В журнале нет студентов.")
            return

        print(f"Всего студентов: {len(self.students)}\n")

        for student in self.students:
            student.display_info()
