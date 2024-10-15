from datetime import datetime


def get_zodiac_sign(birthdate: datetime) -> str:
    day = birthdate.day
    month = birthdate.month

    zodiac_days = [20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22, 22, 20]
    zodiac_signs = [
        "Козерог", "Водолей", "Рыбы", "Овен", "Телец", "Близнецы",
        "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец", "Козерог"
    ]

    if day < zodiac_days[month - 1]:
        sign = zodiac_signs[month - 1]
    else:
        sign = zodiac_signs[month % 12]

    return sign


def days_since_birth(birthdate: datetime) -> int:
    today = datetime.today()
    delta = today - birthdate
    return delta.days
