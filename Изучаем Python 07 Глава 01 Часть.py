# message=input("Напиши текст и я его повторю: \n")
# print(message)
# name=input("Введите свое имя: ")
# print(f"Приветствую, {name.title()}")
# prompt="Если вы сообщите нам, кто вы, мы сможем персонализировать сообщения, которые вы видите."
# prompt+="\nВведите свое имя: "
# name=input(prompt)
# print(f"Здравствуйте{name.title()}")
#Использование int() для получения числового ввода
# age=input("Введите свой возраст: ")
# age=int(age)
# print(age>=18)
# height=input("Размер ноги: ")
# height=int(height)
#
# if height>=48:
#     print("\nПроверка пройдена")
# else:
#     print("\nПроверка не пройдена")
#Оператор вычисления остатка
# print(6%3)
# number=input("Введите число и я вам сообщу четное или нечетное: ")
# number=int(number)
#
# if number%2==0:
#     print("Четное")
# else:
#     print("Нечет")
#Упражнения
# car=input("Какую вы хотите взять машина на прокат?\n")
# print(f"Давайте я посмотрю смогу ли я найти вам {car}")

# more=input("На сколько мест вы хотите взять столик?\n:")
# more=int(more)
# if more>8:
#     print("Придется подождать")
# else:
#     print("Стол готов")

# number=input("Введите число и я скажу кратно ли оно 10 или нет: ")
# number=int(number)
#
# if number%10==0:
#     print(f"Ваше число {number} кратно 10")
# else:
#     print(f"Ваше число {number} не кратно 10")
#Цикл while в действии
# current_number=1
# while current_number<=5:
#     print(current_number)
#     current_number+=1
#Пользователь решает прервать работу программы
# prompt="\nНапиши мне любой текст и я его повторю"
# prompt+="\n Если хочешь остановить 'quit' напиши это: "
# message=""
# while message != 'quit':
#     message=(input(prompt))
#     if message!= 'quit':
#         print(message)


# prompt="\nНапиши мне любой текст и я его повторю"
# prompt+="\n Если хочешь остановить 'quit' напиши это: "
# active=True
# while active:
#     message=input(prompt)
#
#     if message=='quit':
#         active=False
#     else:
#         print(message)

prompt="\nНапиши мне любой текст и я его повторю"
prompt+="\n Если хочешь остановить 'quit' напиши это: "
while True:
    city=input(prompt)

    if city=='quit':
        break
    else:
        print(f"Cool {city.title()}")
