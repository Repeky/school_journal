from abc import ABC, abstractmethod
from datetime import datetime


class Person(ABC):
    def __init__(self, name: str, birthdate: str):
        self.name = name
        self.birthdate = datetime.strptime(birthdate, "%d.%m.%Y")

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.birthdate.year

    @abstractmethod
    def display_info(self):
        pass
