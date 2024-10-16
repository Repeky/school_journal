import unittest
from src.components.school_journal import SchoolJournal
from src.components.school_journal import Student
from src.components.exceptions import StudentNotFoundError


class TestSchoolJournal(unittest.TestCase):
    def test_add_student(self):
        journal = SchoolJournal()
        student = Student("Иван Иванов", "28.01.2000")
        journal.add_student(student)
        self.assertEqual(len(journal.students), 1)

    def test_get_student_by_valid_index(self):
        journal = SchoolJournal()
        student = Student("Иван Иванов", "28.01.2000")
        journal.add_student(student)
        retrieved_student = journal.get_student_by_index(0)
        self.assertEqual(retrieved_student.name, "Иван Иванов")

    def test_get_student_by_invalid_index(self):
        journal = SchoolJournal()
        with self.assertRaises(StudentNotFoundError):
            journal.get_student_by_index(0)


if __name__ == '__main__':
    unittest.main()
