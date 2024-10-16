import unittest
from src.components.school_journal import Student
from src.components.exceptions import InvalidDateError, InvalidGradeError, SubjectNotFoundError


class TestStudent(unittest.TestCase):
    def test_valid_student_creation(self):
        """Тестирование корректного создания объекта Student."""
        student = Student("Иван Иванов", "28.01.2000")
        self.assertEqual(student.name, "Иван Иванов")
        self.assertEqual(student.birthdate.strftime('%d.%m.%Y'), "28.01.2000")

    def test_invalid_date(self):
        """Тестирование создания студента с некорректной датой рождения."""
        with self.assertRaises(InvalidDateError):
            Student("Иван Иванов", "31.02.2000")

    def test_add_valid_grades(self):
        """Тестирование добавления корректных оценок студенту."""
        student = Student("Иван Иванов", "28.01.2000")
        student.add_grades("Математика", [5, 4, 3])
        self.assertIn("Математика", student.grades)
        self.assertEqual(student.grades["Математика"].grades, [5, 4, 3])

    def test_add_invalid_grades(self):
        """Тестирование добавления некорректных оценок студенту."""
        student = Student("Иван Иванов", "28.01.2000")
        with self.assertRaises(InvalidGradeError):
            student.add_grades("Математика", [5, "отлично", 3])

    def test_update_grades_subject_not_found(self):
        student = Student("Иван Иванов", "28.01.2000")
        with self.assertRaises(SubjectNotFoundError):
            student.update_grades("Физика", [5, 5, 5])

    def test_get_average_grade(self):
        student = Student("Иван Иванов", "28.01.2000")
        student.add_grades("Математика", [5, 4, 3])
        avg = student.get_average_grade("Математика")
        self.assertEqual(avg, 4.0)


if __name__ == '__main__':
    unittest.main()
