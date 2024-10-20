from datetime import datetime


def get_zodiac_sign(birthdate: datetime) -> str:
    zodiac_info = {
        1: (20, "Козерог", "Водолей"),
        2: (19, "Водолей", "Рыбы"),
        3: (21, "Рыбы", "Овен"),
        4: (20, "Овен", "Телец"),
        5: (21, "Телец", "Близнецы"),
        6: (21, "Близнецы", "Рак"),
        7: (23, "Рак", "Лев"),
        8: (23, "Лев", "Дева"),
        9: (23, "Дева", "Весы"),
        10: (23, "Весы", "Скорпион"),
        11: (22, "Скорпион", "Стрелец"),
        12: (22, "Стрелец", "Козерог"),
    }

    day = birthdate.day
    month = birthdate.month
    cutoff_day, prev_sign, next_sign = zodiac_info[month]

    if day < cutoff_day:
        return prev_sign
    else:
        return next_sign


def days_since_birth(birthdate: datetime) -> int:
    today = datetime.today()
    delta = today - birthdate
    return delta.days
