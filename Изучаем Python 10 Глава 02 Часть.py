#10 Глава
#Исключения
#блоки try-except
#Обработка исключения ZeroDivisionError
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("Вывод ошибки")
# #Использование исключений для предотвращения аварийного
# #завершения программы
# print("Введите 2 числа: ")
# print("q on exit")
#
# while True:
#     first_number=input("\n First number")
#     if first_number=='q':
#         break
#     second_number=input("\n Second number")
#     if second_number=='q':
#         break
#     try:
#         answer=int(first_number)/ int(second_number)
#     except ZeroDivisionError:
#         print("На 0 делить нельзя")
#     else:
#         print(answer)
#Обработка исключения FileNotFoundError
# filename='pi.txt'
# try:
#     with open(filename, encoding='utf-8') as f:
#         contents=f.read()
# except FileNotFoundError:
#     print(f"Извини,но я не могу открыть этот файл {filename}")
# #Анализ текста
# else:
#     word=contents.split()
#     num_word=len(word)
#     print(f"В {filename} находиться {num_word} слов")
#Работа с несколькими файлами
# def count_words(filename):
#     """Приблизительное подсчет строк в файле"""
#     try:
#         with open(filename) as f:
#             contents=f.read()
#     except FileNotFoundError:
#         pass
#         # print(f"Извини не могу открыть файл {filename}")
#     else:
#         word=contents.split()
#         num_words=len(word)
#         print(num_words)
# filenames=['pi.txt','text.txt','suck.txt','lol.txt']
# for filename in filenames:
#     count_words(filename)
#Ошибки без уведомления пользователя
#pass - для пропуска ошибки
#Упражнения
# n=input("Введите число:") это тест чтобы понять как должна работать ошибка
# m=int(n)
# print(m)
# # print("Введите 2 числа, которые я вам сложу")
# #
# # while True:
# #     first_number=input("Введите 1 число: \n")
# #     if first_number=='q':
# #         break
# #     second_number=input("Введите 2 число: \n")
# #     if second_number=='q':
# #         break
# #     try:
# #         full=float(first_number)+float(second_number)
# #     except ValueError:
# #         print(f"Извини,но будь проще и введи число, вместо {second_number}")
# #     else:
# #         print(full)
#
# print("Введите 2 числа \n")
#
# first_number=input("Введите 1 число:")
# second_number=input("Введите 2 число: ")
# try:
#     summ=float(first_number)+float(second_number)
# except ValueError:
#     print(f"Введите число, а не букву")
# else:
#     print(summ)
#
# def error(filename):
#     try:
#         with open(filename,encoding='utf-8') as f:
#             n=f.read()
#             print(n)
#     except FileNotFoundError:
#         # print(f"Извини,но файл не  открывается {filename}")
#         pass
#     else:
#         print(f"{filename }\n")
#
# filenames=['text.txt','suck.txt','dolbaeb.txt']
# for filename in filenames:
#     error(filename)
#
#
from re import search


def count_word(filename):
    try:
        with open(filename) as f:
            content=f.read()
    except FileNotFoundError:
        print(f"Файл не открывается {content}")
    else:
       search_word='lisa'
       count = content.lower().count(search_word.lower())
       if count>0:
            print(f"Нашел {count} в файле {filename}")
filenames=['text.txt','suck.txt']
for filename in filenames:
    count_word(filename)

