import json
# class Dog:
#
#     def __init__(self, name, origin):
#         self.name = name
#         self.origin = origin
#
#     @property
#     def say(self):
#         print(f"{self.name} умеет лаять")
#
# white_dog = Dog("Шурик", "Asian")
# brown_dog = Dog("Пушок", "Еврей")
#
# print(white_dog.name)
# print(brown_dog.name)
# # print(white_dog.origin)
# print(f"{white_dog.name} порода {white_dog.origin}")
#
# white_dog.say

# Класс прародитель Human
class Human:

    # метод для ввода данных
    def input_data(self):
        self.fio = input("Введите ФИО: ")
        self.number = input("Введите номер телефона: ")
        self.brithday = input("Введите дату рождения: ")

    # метод для вывода данных
    def print_data(self):
        print(self.fio)
        print(self.number)
        print(self.brithday)

    # методы для получения
    def get_fio(self):
        return self.fio

    def get_number(self):
        return self.number

    def get_brithday(self):
        return self.brithday

class Bulder(Human):

    def input_parametr(self):
        self.specialization = input("Введите специализацию строителя: ")
        self.main_tools = input("Введите основной инструмент: ")
        self.post = input("Введите должность: ")

    # Полиморфизм. Поли - много, морфизм - форма
    def print_data(self):
        print(self.fio)
        print(self.post)
        print(self.specialization)
        print(self.main_tools)
        print(self.number)
        print(self.brithday)

    def get_specialization(self):
        return self.specialization

    def get_main_tools(self):
        return self.main_tools

    def get_post(self):
        return self.post

class Obj(Bulder):
    pass

# object_1 = Human()
# object_1.input_data()
list_employee = []
for i in range(3):
    employee = Bulder()
    employee.input_data()
    employee.input_parametr()
    list_employee.append(i)
    list_employee[i] = {"ФИО":employee.fio, "Должность":employee.get_post(), "Специализация":employee.get_specialization(), "Основной инструмент":employee.get_main_tools(), "Номер телефона":employee.get_number(), "Дата рождения":employee.get_brithday()}

print(list_employee)

with open("data_file.json", "w") as write_file:
    json.dump(list_employee, write_file)
# class City:
#
#     def input_data(self):
#         self.__name_city = input("Введите название города: ")
#         self.__count_resident = int(input("Введите количество жителей: "))
#         self.__cod_phone = int(input("Введим код города: "))
#         self.__print_data()
#
#     # Инкапсулирование
#     def __print_data(self):
#         print(self.__name_city)
#         print(self.__count_resident)
#         print(self.__cod_phone)
#
#     def get_name_city(self):
#         return self.__name_city
#
#     def get_count_resident(self):
#         return self.__count_resident
#
#     def get_cod_phone_city(self):
#         return self.__cod_phone
#
# city_1 = City()
# city_1.input_data()
# city_1.get_cod_phone_city()



