#Команда continue и продолжение цикла
# curent_number=0
# while curent_number<10:
#     curent_number+=1
#     if curent_number%2==0:
#         continue
#
#     print(curent_number)
#Упражнение
# topping_pizza="\n Выберите допинг для пиццы: "
#
# while topping_pizza:
#     topping=(input(topping_pizza))
#
#     if topping=='quit':
#         break
#     else:
#         print(f"В вашу пиццу добавлены: {topping}")
from itertools import repeat

# age="Введите свой возраст: "
# while age:
#     vozr=input(age)
#     vozr=int(vozr)
#     if vozr<3:
#         print(f"Для вашего возраста {vozr}-билет бесплатный")
#     elif vozr<=12:
#         print(f"Для вашего возраст {vozr}- цена билета 10$")
#     else:
#         print(f"Для вашего возраста {vozr}- цена билета 15$")
#7.6
# active=True
# topping_pizza="\n Выберите допинг для пиццы: "
#
# while active:
#     topping=(input(topping_pizza))
#
#     if topping=='quit':
#         break
#     if topping=='stop':
#         active=False
#     else:
#         print(f"В вашу пиццу добавлены: {topping}")
#Использование цикла while со списками и словарями
##Перемещение элементов между списками
# unregisted=['alica','max','alex']
# registed=[]
# while unregisted:
#     curent_user=unregisted.pop()
#
#     print(f"Прошел проверку {curent_user.title()}")
#     registed.append(curent_user)
# print("\nПодтверждены следующие пользователи:")
# for registr in registed:
#     print(f"{registr.title()}")
#Удаление всех вхождений конкретного значения из списка
# pets=['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)
# #Заполнение словаря данными, введенными пользователем
# responses={}
# polling=True
#
# while polling:
#     name=input("\nВведите имя")
#     response=input("На какую гору вы хотели бы когда-нибудь подняться?")
#
#     responses[name]=response
#
#     repeat=input("Хотите ли вы, чтобы ответил другой человек? (да/нет)")
#     if repeat =='нет':
#         polling=False
# print("\n ---Итоги Опроса---")
# for name,response in responses.items():
#     print(f"{name} он любит {response}")

# sandwich_orders=['пастрами','сырный','говяжий','пастрами','чоризо','пастрами']
# print("Пастрами больше нету")
# finished_sandwiches=[]
# while 'пастрами' in sandwich_orders:
#     sandwich_orders.remove('пастрами')
# while sandwich_orders:
#         curent=sandwich_orders.pop()
#         print(f"Я сделаю {curent}")
#
#         finished_sandwiches.append(curent)
#         print("\nСделаны следующие заказы")
# for finished in finished_sandwiches:
#     print(f"{finished.title()}")

response={}
active=True

while active:
    name=input("Введите свое имя:")
    gora=input("Где бы вы хотели провести свой отпуск мечты?")
    response[name]=gora

    repeat=input("Хотите ли спросить другого человека (да/нет)")
    if repeat=='нет':
        active=False
print("\n ---Итоги опроса---")

for name,gora in response.items():
    print(f"{name.title()} Хочет {gora.title()}")
