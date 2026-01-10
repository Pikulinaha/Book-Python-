#Работа с классами и экземплярами
# class Car():
#     """Простая модель машины"""
#
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.odometer_reading=0
#
#
#     def get_discriptive_name(self):
#         """Возвращает атрибуты описания автомобиля"""
#         long_name=f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#     def read_odometer(self):
#         """Вывод о пробеге машины"""
#         print(f"Машина прошла {self.odometer_reading}")
#
#     # Изменение значения атрибута с использованием метода
#     def update_odometer(self,mileage):
#         """Устанавливает заданное значение на одометре"""
#         if mileage>=self.odometer_reading:
#             self.odometer_reading=mileage
#         else:
#             print("Скрутите пробег обратно")
# # my_new_car=Car('audi','a3',1998)
# # print(my_new_car.get_discriptive_name())
# # my_new_car.update_odometer(23)
# # my_new_car.read_odometer()
#
#
# #Изменение значения атрибута с приращением
#     def increment_odometer(self,miles):
#         """Увеличивает прирост пробега"""
#         self.odometer_reading+=miles
# my_new_car=Car('audi','a3',1998)
# print(my_new_car.get_discriptive_name())
#
# my_new_car.update_odometer(23_500)
# my_new_car.read_odometer()
#
# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()
from cgitb import reset


#Упражнения

# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#             self.name=restaurant_name
#             self.kitchen=cuisine_type
#             self.number_served=0
#     def discribe_restotane(self):
#         print(f"{self.name}")
#         print(f"{self.kitchen}")
#     def open_restaurant(self):
#         print(f"{self.name} открыт!")
#     def set_number_served(self,served):
#         self.number_served=served
#         return served
#     def increment_number_served(self,serv):
#         self.number_served+=serv
# restaurant=Restaurant("Харчевня","Русская")
#
# print(f"Посетило за час {restaurant.number_served}")
# #2
# restaurant.number_served=5
# print(f"Посетило за 2 часа {restaurant.number_served}")
# restaurant.set_number_served(10)
# print(f"Пришло посетителей {restaurant.number_served}")
# restaurant.increment_number_served(50)
# print(f"{restaurant.number_served}")

# class User():
#     def __init__(self,first_name,last_name,age,сity):
#         self.first=first_name.title()
#         self.last=last_name.title()
#         self.age=age
#         self.сity=сity
#         self.login_attemps=0
#     def describe_user(self):
#         print(self.first, self.last, self.age, self.сity)
#
#
#     def greet_user(self):
#         print(f"Привет, {self.first} {self.last}!")
#     def increment_login_attemps(self):
#         self.login_attemps+=1
#         return self.login_attemps
#     def reset_login_attemps(self):
#         self.login_attemps=0
# user_1=User("Владимир","Алмакаев",19,"Пенза")
# print(f"Пользователей посещено {user_1.login_attemps}")
# user_1.increment_login_attemps()
# user_1.increment_login_attemps()
# user_1.increment_login_attemps()
# print(f"Пользователей посещено дальше {user_1.increment_login_attemps()}")
# user_1.reset_login_attemps()
# print(f"После сброса {user_1.login_attemps}")


"""Попытался решить хоть одну задачу на leetcode,понял что у меня не развито мышление для решения подобных задач"""

