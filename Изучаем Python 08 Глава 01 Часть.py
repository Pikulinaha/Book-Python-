# def greet_user():
#     """Выводит приветствие"""
#     print("Hello!")
# greet_user()
# def greet_user(username):
#     """Выводит приветствие"""
#     print(f"Hello!, {username.title()}!")
# greet_user('max')
"""Упражнения"""
# def display_message():
#     """Выводит название главы"""
#     print("Функции")
# display_message()

# def favorite_book(title):
#     """Название книги"""
#     print(f"Мне нравиться читать книгу,{title.title()}!!!")
# favorite_book('изучаем python')

#Позиционные аргументы
# def describe_pet(animal_type,pet_name):
#     """Вывод информации о животном"""
#     print(f"\nЯ хочу завести {animal_type}")
#     print(f"\nИ назвать {pet_name}")
# describe_pet('Кошечку','Томми')
# #Многократные вызовы функций
# describe_pet('Собачку','Бобби')
#
# #Именованные аргументы
# def describe_pet(animal_type,pet_name):
#     """Вывод информации о животном"""
#     print(f"\nЯ хочу завести {animal_type}")
#     print(f"\nИ назвать {pet_name}")
# describe_pet(animal_type='Dog',pet_name='Bobby')
# describe_pet(pet_name='harry', animal_type='hamster')

# def describe_pet(pet_name,animal_type='dog'):
#     """Вывод информации о животном"""
#     print(f"\nЯ хочу завести {animal_type}")
#     print(f"\nИ назвать {pet_name}")
# describe_pet(pet_name='willy')
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

"""Упражнения"""
# def make_shirt(size,text):
#     """Вывод размера и текста"""
#     print(f"\nРазмер: {size}")
#     print(f"\nТекст: {text}")
# make_shirt('46','OOO Tlizy')
# make_shirt(size='46',text='SOSal?')

# def make_shirt(size='L',text='I love Python'):
#     """Вывод размера и текста футболки"""
#     print(f"\n{'=' * 30}")
#     print(f"Размер : {size}")
#     print(f"Текст : {text}")
#     print(f"\n{'=' * 30}")
# make_shirt()
# make_shirt(size='M',text='Sosal?')

def describe_city(sity,country='россия'):
    print(f"{sity.title()} находиться в {country.title()}")
describe_city('Москва')
describe_city('Пенза')
describe_city(sity='Париж', country='Франция')

#Возвращаемое значение
def get_formatted_name(first_name,last_name):
    """Возвращает отформатированное полное имя"""
    full_name=f"{first_name} {last_name}"
    return full_name.title()
musician=get_formatted_name('Max','Breev')
print(musician)
