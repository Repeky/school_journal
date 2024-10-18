from src.components.school_journal import SchoolJournal
from src.components.exceptions import (InvalidDateError,
                                       InvalidGradeError,
                                       SubjectNotFoundError,
                                       StudentNotFoundError)


class JournalApp:
    """Класс для управления школьным журналом."""

    def __init__(self) -> None:
        self.journal = SchoolJournal()
        self.is_working = True

    def run(self) -> None:
        while self.is_working:
            self.print_menu()

            user_input = input('Выберите параметр: ')

            match user_input:
                case "1":
                    self.display_journal()
                case "2":
                    self.add_student_to_journal()
                case "3":
                    self.update_student_grades()
                case "4":
                    print("Выход из программы.")
                    self.is_working = False
                case _:
                    print("Некорректный ввод. Попробуйте снова.")

    def print_menu(self) -> None:
        list_parameters = [
            "Просмотр журнала",
            "Добавить студента",
            "Изменить оценку студента",
            "Выход",
        ]

        for number, parameter in enumerate(list_parameters, start=1):
            print(f'{number}. {parameter}')

    def add_student_to_journal(self) -> None:
        name = input("Введите имя студента: ")
        while True:
            birthdate = input("Введите дату рождения студента (формат ДД.ММ.ГГГГ): ")
            try:
                student = self.journal.create_student(name, birthdate)
                break
            except InvalidDateError as err:
                print(err)
                print("Пожалуйста, попробуйте снова.")

        while True:
            subject = input("Введите предмет (или 'стоп' для завершения): ")
            if subject.lower() == 'стоп':
                break

            grades_input = input("Введите оценки через запятую: ")
            try:
                grades = list(map(int, grades_input.split(',')))
                student.add_grades(subject=subject, grades=grades)
            except ValueError:
                print("Некорректный ввод оценок. Пожалуйста, введите числа, разделенные запятыми.")
            except InvalidGradeError as err:
                print(err)

        self.journal.add_student(student)
        print(f"Студент {name} успешно добавлен в журнал!")

    def update_student_grades(self) -> None:
        if not self.journal.students:
            print("В журнале нет студентов.")
            return

        print("Список студентов:")
        for idx, student in enumerate(self.journal.students, start=1):
            print(f"{idx}. {student.name}")

        try:
            student_index = int(input("Выберите номер студента для изменения оценок: ")) - 1
            student = self.journal.get_student_by_index(student_index)
        except (ValueError, StudentNotFoundError) as err:
            print(err)
            return

        subject = input("Введите предмет для изменения оценок: ")

        try:
            grades_input = input("Введите новые оценки через запятую: ")
            new_grades = list(map(int, grades_input.split(',')))
            student.update_grades(subject=subject, new_grades=new_grades)
            print(f"Оценки по предмету '{subject}' обновлены для студента {student.name}.")
        except ValueError:
            print("Некорректный ввод оценок. Пожалуйста, введите числа, разделенные запятыми.")
        except InvalidGradeError as err:
            print(err)
        except SubjectNotFoundError as err:
            print(err)

    def display_journal(self) -> None:
        self.journal.display_statistics()


if __name__ == '__main__':
    app = JournalApp()
    app.run()
