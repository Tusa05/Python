from smartphone import Smartphone


# Создаем список книг (библиотеку)
catalog = [
    Smartphone("Samsung", "S24", "+7908888888"),
    Smartphone("Samsung", "S25", "+7907777777"),
    Smartphone("Samsung", "Z", "+7906666666"),
    Smartphone("POCO", "F7", "+7905555555"),
    Smartphone("POCO", "X7", "+7904444444")
]

# Печатаем библиотеку
for smartphone in catalog:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model} - "
          f"{smartphone.subscriber_number}")
