from abc import ABC, abstractmethod
from datetime import datetime
from src.components.exceptions import InvalidDateError


class Person(ABC):
    def __init__(self, name: str, birthdate: str):
        self.name = name
        try:
            self.birthdate = datetime.strptime(birthdate, "%d.%m.%Y")
        except ValueError:
            raise InvalidDateError(f"Некорректный формат даты: {birthdate}. Ожидается ДД.ММ.ГГГГ.")

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.birthdate.year

    @abstractmethod
    def display_info(self):
        pass
