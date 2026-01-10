
#Сохранение данных

# import json
#
# numbers=[2,3,5,7,11,3]
#
# filename='numbers.json'
# with open(filename,'w') as f:
#     json.dump(numbers,f)

# filename='numbers.json'
#
# with open(filename) as f:
#     numbers=json.load(f)
# print(numbers)

#Сохранение и чтение данных, сгенерированных пользователем
# import json
#
# username=input("Как тебя зовут?")
#
# filename='numbers.json'
# with open(filename,'w') as f:
#     json.dump(username,f)
#     print(f"Я запомнил вас {username}!")

# import json
#
# filename='numbers.json'
# with open(filename) as f:
#     username=json.load(f)
#     print(f"С возвращением {username}!")

# import json
#
# #Программа загружает имя пользовтеля, если оно не загружено, то запрашивает имя
# filename='numbers.json'
# try:
#     with open(filename) as f:
#         username=json.load(f)
# except FileNotFoundError:
#     username=input("Как вас зовут?")
#     with open(filename,'w') as f:
#         json.dump(username,f)
#         print(f"Приветствую!{username.title()} я запомнил")
# else:
#     print(f"C возвращением я ждал тебя {username.title()}!")



import json

def get_stored_username():
    """Получает, хранимое имя пользователя, если оно существует"""
    filename='numbers.json'
    try:
        with open(filename) as  f:
            username=json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def def_new_user():
    username = input("Введите свое имя: ")
    filename = 'numbers.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        return username

def greet_user():
        """Приветствует пользователя"""
        username=get_stored_username()
        if username:
            inswer=input(f"Это вы {username}, yes/no").lower()
            if inswer=="yes":
                print(f"Приветствую тебя {username}")
            else:
                username=def_new_user()
                print(f"Привет,{username} я тебя запомнил")
        else:
            username=def_new_user()
            print(f"We'll remember you when you come back {username}")
greet_user()

# import json
#
# filename='numbers.json'
# try:
#     with open(filename) as f:
#         nubmer=json.load(f)
#         print(f"Ваше любимое число: {nubmer}")
# except FileNotFoundError:
#     user = input("Введите свое любимое число: ")
#     with open(filename, 'w') as f:
#         json.dump(user, f)
#         print("Хорошо я запомнил ваше число!")

