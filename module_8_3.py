# Определим пользовательские исключения
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


# Класс Car
class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = None  # Инициализируем vin и numbers через setter (валидацию)
        self.__numbers = None
        self.__set_vin(vin)
        self.__set_numbers(numbers)

    # Приватный метод проверки VIN номера
    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        return True

    # Приватный метод проверки номеров
    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        return True

    # Сеттер для VIN номера (с валидацией)
    def __set_vin(self, vin):
        if self.__is_valid_vin(vin):
            self.__vin = vin

    # Сеттер для номеров (с валидацией)
    def __set_numbers(self, numbers):
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers


# Пример использования
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
