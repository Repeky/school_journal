from src.components.person import Person
from typing import List, Optional, Dict
from datetime import datetime
from src.components.date_analysis import get_zodiac_sign, days_since_birth
from src.components.exceptions import (InvalidDateError,
                                       InvalidGradeError,
                                       SubjectNotFoundError,
                                       StudentNotFoundError)


class Grade:
    """Класс для хранения оценок по определенному предмету."""

    def __init__(self, subject: str, grades: List[int]) -> None:
        self.subject = subject
        self.grades = grades

    def get_average(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0.0


class Student(Person):
    """Класс для представления студента."""

    def __init__(self, name: str, birthdate_str: str) -> None:
        super().__init__(name, birthdate_str)
        try:
            self.birthdate = datetime.strptime(birthdate_str, "%d.%m.%Y")
        except ValueError:
            raise InvalidDateError(f"Некорректный формат даты: {birthdate_str}. Ожидается ДД.ММ.ГГГГ.")
        self.grades: Dict[str, Grade] = {}

    def add_grades(self, subject: str, grades: List[int]) -> None:
        MIN_GRADES = 2
        MAX_GRADES = 16

        if not isinstance(grades, list) or not all(isinstance(grade, int) for grade in grades):
            raise InvalidGradeError("Оценки должны быть списком целых чисел.")

        if not MIN_GRADES <= len(grades) <= MAX_GRADES:
            raise InvalidGradeError(
                f"Количество оценок по предмету '{subject}' должно быть от {MIN_GRADES} до {MAX_GRADES}.")

        if not all(1 <= grade <= 5 for grade in grades):
            raise InvalidGradeError("Оценки должны быть в диапазоне от 1 до 5.")
        self.grades[subject] = Grade(subject=subject, grades=grades)

    def update_grades(self, subject: str, new_grades: List[int]) -> None:
        if subject not in self.grades:
            raise SubjectNotFoundError(f"Предмет '{subject}' не найден у студента.")

        if not isinstance(new_grades, list) or not all(isinstance(grade, int) for grade in new_grades):
            raise InvalidGradeError("Оценки должны быть списком целых чисел.")

        if not all(1 <= grade <= 5 for grade in new_grades):
            raise InvalidGradeError("Оценки должны быть в диапазоне от 1 до 5.")

        self.grades[subject].grades = new_grades

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

    def get_zodiac_sign(self) -> str:
        return get_zodiac_sign(self.birthdate)

    def days_since_birth(self) -> int:
        return days_since_birth(self.birthdate)

    def display_info(self) -> None:
        zodiac_sign = self.get_zodiac_sign()
        days_lived = self.days_since_birth()

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
        try:
            return self.students[index]
        except IndexError:
            raise StudentNotFoundError(f"Студент с номером {index + 1} не найден.")

    def display_statistics(self) -> None:
        if not self.students:
            print("В журнале нет студентов.")
            return

        print(f"Всего студентов: {len(self.students)}\n")

        for student in self.students:
            student.display_info()
