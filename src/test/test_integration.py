import unittest
from src.components.school_journal import SchoolJournal
from src.components.school_journal import Student
from src.components.exceptions import StudentNotFoundError


class TestIntegration(unittest.TestCase):
    def test_add_student_and_update_grades(self):
        """Тестирование полного сценария добавления студента и обновления его оценок."""
        journal = SchoolJournal()
        student = Student("Иван Иванов", "28.01.2000")
        journal.add_student(student)
        student.add_grades("Математика", [5, 4, 3])
        student.update_grades("Математика", [5, 5, 5])
        avg = student.get_average_grade("Математика")
        self.assertEqual(avg, 5.0)

    def test_student_not_found_in_journal(self):
        """Тестирование попытки получить несуществующего студента из журнала."""
        journal = SchoolJournal()
        with self.assertRaises(StudentNotFoundError):
            journal.get_student_by_index(0)


if __name__ == '__main__':
    unittest.main()
