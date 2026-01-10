# #Классы
# #Создание и использование класса
# class Dog():
#     """Простая модель собаки"""
#     def __init__(self,name,age):   метод
#         """Инициализирует имя и возраст"""
#         self.name=name   атрибут
#         self.age=age
#
#     def sit(self):
#         """Собаки садятся по команде"""
#         print(f"{self.name.title()} сидеть!")
#
#     def roll_over(self):
#         """Собака перекатывается"""
#         print(f"{self.name} перекатывается!")
# #Создание экземпляра класса
# my_dog= Dog('willie', 6)
# your_dog = Dog('lucy', 3)
# print(f"Имя моей собаки - {my_dog.name.title()}")
# print(f"Возраст моей собаки {my_dog.age}")
# my_dog.sit()
# print("-"*30)
# print(f"Имя твоей собаки - {your_dog.name.title()}")
# print(f"Возраст твоей собаки - {your_dog.age}")
# your_dog.sit()
# #Обращение к атрибутам
# #my_dog- экземпляр, name-атрибут
# #Обращение к атрибутам
# # my_dog.sit()
# # my_dog.roll_over()
# #Создание нескольких экземпляров


#Упражнения
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#             self.name=restaurant_name
#             self.kitchen=cuisine_type
#     def discribe_restotane(self):
#         print(f"{self.name}")
#         print(f"{self.kitchen}")
#     def open_restaurant(self):
#         print(f"{self.name} открыт!")
#
# restaurant=Restaurant("Харчевня","Русская")
# your_restaurant=Restaurant("Шаурмечка","Армянская")

# restaurant.open_restaurant()
# print("="*30)
# restaurant.discribe_restotane()
# print("="*30)
# print(restaurant.kitchen)
# print(restaurant.name)
# restaurant.discribe_restotane()
# print("="*50)
# your_restaurant.discribe_restotane()




class User():
    def __init__(self,first_name,last_name,age,sity):
        self.first=first_name.title()
        self.last=last_name.title()
        self.age=age
        self.sity=sity
    def describe_user(self):
        print(self.first, self.last, self.age, self.sity)

    def greet_user(self):
        print(f"Привет, {self.first} {self.last}!")
user_1=User("Владимир","Алмакаев",19,"Пенза")
user_2=User("Максим","Бреев",19,"Нижний Ломов")
user_3=User("Дима","Родников",19,"Саранск")

user_1.describe_user()
user_1.greet_user()
print("="*30)
user_2.describe_user()
user_2.greet_user()
print("="*30)
user_3.describe_user()
user_3.greet_user()
