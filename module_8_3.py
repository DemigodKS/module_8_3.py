#пример1 
class IncorrectVinNumber(Exception):

    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.__is_valid_vin_numbers(__vin, __numbers)
        self.__is_valid_numbers(__numbers)

    def  __is_valid_vin_numbers(self, vin_number, numbers):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif (not vin_number >= 1000000 and vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')

        return True

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300000, 'т001тy')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020277, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')


#пример2

class IncorrectVinCarNumber(Exception):

    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.__is_valid_vin_car_numbers(__vin, __numbers)
        #self.__is_valid_numbers(__numbers)

    def  __is_valid_vin_car_numbers(self, vin_number, numbers):
        if not isinstance(vin_number, int):
            raise IncorrectVinCarNumber('Некорректный тип vin номер')
        elif (not vin_number >= 1000000 and vin_number <= 9999999) and len(numbers) != 6:
            raise IncorrectVinCarNumber('Неверный диапазон для vin номера, Неверная длина номера')
        elif not vin_number >= 1000000 and vin_number <= 9999999:
            raise IncorrectVinCarNumber('Неверный диапазон для vin номера')
        elif len(numbers) != 6:
            raise IncorrectVinCarNumber('Неверная длина номера')
        elif not isinstance(numbers, str):
            raise IncorrectVinCarNumber('Некорректный тип данных для номеров')
        return True

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinCarNumber as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 3000000, 'т05')
except IncorrectVinCarNumber as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 20207, 'нет номера')
except IncorrectVinCarNumber as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')






