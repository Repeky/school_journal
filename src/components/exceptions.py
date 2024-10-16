class SchoolJournalError(Exception):
    """Базовый класс для исключений в школьном журнале."""
    pass


class InvalidDateError(SchoolJournalError):
    """Исключение для неверного формата даты."""
    pass


class InvalidGradeError(SchoolJournalError):
    """Исключение для неверных оценок."""
    pass


class StudentNotFoundError(SchoolJournalError):
    """Исключение, когда студент не найден."""
    pass


class SubjectNotFoundError(SchoolJournalError):
    """Исключение, когда предмет не найден у студента."""
    pass


class InvalidInputError(SchoolJournalError):
    """Исключение для неверного ввода."""
    pass
