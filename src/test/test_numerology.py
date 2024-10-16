import unittest
from datetime import datetime
from src.components.date_analysis import get_zodiac_sign, days_since_birth


class TestNumerology(unittest.TestCase):
    def test_get_zodiac_sign(self):
        birthdate = datetime.strptime("28.01.2000", "%d.%m.%Y")
        zodiac_sign = get_zodiac_sign(birthdate)
        self.assertEqual(zodiac_sign, "Водолей")

    def test_days_since_birth(self):
        birthdate = datetime.strptime("01.01.2000", "%d.%m.%Y")
        days = days_since_birth(birthdate)
        # Проверяем, что количество дней больше 0
        self.assertTrue(days > 0)


if __name__ == '__main__':
    unittest.main()
