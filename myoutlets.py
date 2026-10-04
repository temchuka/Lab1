outlets = [
    {
        "name": "Павильон 1-05",
        "tenant": "ООО «Модный дом»",
        "months": ["Июль", "Август", "Сентябрь"],
        "payments": [93000, 93000, 90000]
    },
    {
        "name": "Павильон 1-12",
        "tenant": "ИП Гришин А. В.",
        "months": ["Июль", "Август", "Сентябрь"],
        "payments": [46500, 46500, 45000]
    },
    {
        "name": "Островок 2-03",
        "tenant": "ООО «Кофе Тайм»",
        "months": ["Июль", "Август", "Сентябрь"],
        "payments": [31000, 31000, 30000]
    },
    {
        "name": "Павильон 2-17",
        "tenant": "АО «ЭлектроМаркет»",
        "months": ["Сентябрь"],
        "payments": [150000]
    },
    {
        "name": "Павильон 3-08",
        "tenant": "ООО «Детский мир игрушек»",
        "months": ["Сентябрь"],
        "payments": [75000]
    },
    {
        "name": "Островок 3-01",
        "tenant": "ИП Назарова Л. С.",
        "months": ["Август", "Сентябрь"],
        "payments": [24800, 24000]
    }
]


def print_outlets(items):
    print(u"Торговая точка".ljust(16), u"Арендатор".ljust(28),
          u"Месяцы".ljust(32), u"Платежи, руб.".ljust(26))
    for item in items:
        print(item["name"].ljust(16), item["tenant"].ljust(28),
              str(item["months"]).ljust(32), str(item["payments"]).ljust(26))


def filter_by_average(items, min_average):
    """Возвращает торговые точки, средний ежемесячный платеж по которым выше заданного."""
    result = []
    for item in items:
        average = sum(item["payments"]) / len(item["payments"])
        if average > min_average:
            result.append(item)
    return result


print("Все торговые точки:")
print_outlets(outlets)
print()
try:
    threshold = float(input("Введите минимальный средний платеж: "))
except ValueError:
    print("Ошибка: необходимо ввести число.")
else:
    print("Торговые точки со средним ежемесячным платежом выше", str(threshold) + ":")
    print_outlets(filter_by_average(outlets, threshold))
