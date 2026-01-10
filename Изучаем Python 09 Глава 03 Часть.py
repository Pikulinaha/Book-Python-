# Наследование
class Car():
 """Простая модель автомобиля."""
 def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
    self.fill_gas_tanks=120
 def get_descriptive_name(self):
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()
 def read_odometer(self):
    print(f"This car has {self.odometer_reading} miles on it.")
 def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
     self.odometer_reading = mileage
    else:
        print("You can't roll back an odometer!")
 def increment_odometer(self, miles):
    self.odometer_reading += miles
 def fill_gas_tank(self):
     print(f"Этот автомобиль имеет бак с размером {self.fill_gas_tanks} литров")
# class ElectricCar(Car):
#     def __init__ (self,make,model,year):
#         super().__init__(make,model,year)
#         self.battery_size = 75
#         """Инициализирует класс родителя """
#     def descrybe_battery(self):
#         """Вывод информации о мощности аккума"""
#         print(f"Этот аккумулятор имеет мощность в {self.battery_size}")
#     def fill_gas_tank(self):
#         print("У этого автомобиля нету бензобака")
# my_tesla=ElectricCar("tesla","model X",2019)
# print(my_tesla.get_descriptive_name())
# #Определение атрибутов и методов класса-потомка
# my_tesla.fill_gas_tank()
# my_tesla.descrybe_battery()
# #Переопределение методов класса-родителя
# my_car=Car("Автоваз","Калина",2012)
# print(my_car.get_descriptive_name())
# my_car.fill_gas_tank()
#Экземпляры как атрибуты
# class Battery():
#     def __init__(self,battery_size=100):
#         self.battery_size=battery_size
#     def describe_battery(self):
#         print(f"Этот аккумулятор имеет мощность {self.battery_size}")
#     def get_range(self):
#         if self.battery_size==75:
#             range=260
#         elif self.battery_size==100:
#             range=315
#         print(f"На полном заряде аккумулятора можно проехать {range}")
# class ElectricCar(Car):
#     def __init__ (self,make,model,year):
#         super().__init__(make,model,year)
#         self.battery=Battery()
#         """Инициализирует класс родителя """
# my_tesla=ElectricCar("tesla","model X",2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
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
# class IceCreamStand(Restaurant):
#     def __init__(self,flavor):
#         self.flavors=flavor
#     def show_flavors(self):
#         for flavors in self.flavors:
#             print(f"-{flavors}")
# ice_cream=["Ванильное","Шоколадное","Фисташковое"]
# spic=IceCreamStand(ice_cream)
# spic.show_flavors()
# class User():
#     def __init__(self,first_name,last_name,age,sity):
#         self.first=first_name.title()
#         self.last=last_name.title()
#         self.age=age
#         self.sity=sity
#     def describe_user(self):
#         print(self.first, self.last, self.age, self.sity)
#
#     def greet_user(self):
#         print(f"Привет, {self.first} {self.last}!")
# class Admin(User):
#     def __init__(self,privileges,first_name,last_name,age,sity):
#         super().__init__(first_name,last_name,age,sity)
#         self.privileges=privileges
#     def show_privileges(self):
#         # for n in self.privileges:
#         print(f"Вот ваши привилегии: \n {self.privileges}")
#
# admin_priv=["разрешено добавлять сообщения","разрешено удалять пользователей","разрешено банить пользователей"]
# admin=Admin(admin_priv,"Anisimov","Alex",19,"Нижний Ломов")
# admin.describe_user()
# admin.show_privileges()


class Car():
 """Простая модель автомобиля."""
 def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
    self.fill_gas_tanks=120
 def get_descriptive_name(self):
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()
 def read_odometer(self):
    print(f"This car has {self.odometer_reading} miles on it.")
 def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
     self.odometer_reading = mileage
    else:
        print("You can't roll back an odometer!")
 def increment_odometer(self, miles):
    self.odometer_reading += miles
 def fill_gas_tank(self):
     print(f"Этот автомобиль имеет бак с размером {self.fill_gas_tanks} литров")
class Battery():
    def __init__(self,battery_size=75):
        self.battery_size=battery_size
    def describe_battery(self):
        print(f"Этот аккумулятор имеет мощность {self.battery_size}")
    def get_range(self):
        if self.battery_size==75:
            range=260
        elif self.battery_size==100:
            range=315
        print(f"На полном заряде аккумулятора можно проехать {range}")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
            print("Аккумулятор обновлён до 100 кВт·ч")
        else:
            print("Аккумулятор уже имеет максимальную мощность 100 кВт·ч")
class ElectricCar(Car):
    def __init__ (self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
        """Инициализирует класс родителя """
my_tesla=ElectricCar("tesla","model X",2019)
print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

battery = Battery()  #
battery.describe_battery()
battery.get_range()
print("\nПосле апгрейда:")
battery.upgrade_battery()
battery.describe_battery()
battery.get_range()


