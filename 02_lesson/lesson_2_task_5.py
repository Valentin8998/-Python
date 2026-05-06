month = int(input("Введите номер месяца:"))


def month_to_season(month):
    if month == 12 or 0 < month <= 3:
        return ('Зима')
    elif 2 < month <= 6:
        return ('Весна')
    elif 5 < month <= 9:
        return ('Лето')
    elif 8 < month <= 12:
        return ('Осень')
    else:
        return ('Неверно указанный месяц')


print(month_to_season(month))
