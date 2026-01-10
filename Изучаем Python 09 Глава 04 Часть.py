#Импортирование классов
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descryptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometr(self):
        print(f"Этот автомобиль имеет пробег {self.odometer_reading}")

    def upgrade_odometer(self,millage):
        if millage>=self.odometer_reading:
            self.odometer_reading=millage
        else:
            print("Пробег скручен")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class Battery():
    def __init__(self,battery_size=100):
        self.battery_size=battery_size

    def describe_battery(self):
        print(f"Ваша батарея имеет заряд {self.battery_size}")

    def get_range(self):
        if self.battery_size==75:
            range=260
        elif self.battery_size==100:
            range=300

        print(f"Ваша машина проедет {range} на заряде {self.battery_size}")


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
import list """Импорт всех классов из модуля"""
from list import Car """Импорт конкретного класса из модуля"""
my_beently=list.Car('volsvagen','bently',2017)
print(my_beently.get_descryptive_name())

my_tesla=list.ElectricCar('tesla','model X',2017)
print(my_tesla.get_descryptive_name())
