#10 Файлы и исключения
#Чтение из файла
# with open('pi.txt') as file_object:
#     contents=file_object.read()
# print(contents)
# print(contents.rstrip())
#Чтение по строкам
# filename='pi.txt'
from fileinput import filename

# with open(filename) as file_object:
#     lines=file_object.readline()
#
# for line in lines:
#     print(line.rstrip())
#Работа с содержимым файла

# with open(filename) as file_object:
#     lines=file_object.readline()
#
# pi_string=''
# for line in lines:
#     pi_string+=line.strip()
# print(pi_string)
# print(len(pi_string))
#Большие файлы: миллион цифр
# with open(filename) as file_object:
#     lines=file_object.readline()
#
# pi_string=''
# for line in lines:
#     pi_string+=line.strip()
# print(pi_string)
# print(f"{pi_string[:52]}...")
# print(len(pi_string))
#Проверка дня рождения
# with open(filename) as file_object:
#     lines=file_object.readlines()
#
# pi_string=''
# for line in lines:
#     pi_string+=line.strip()
# birthday= input("Введите свое день рождения: ")
# if birthday in pi_string:
#     print("Ваш день рождения есть в числе Пи")
# else:
#     print("Увы нет...")


#упражнение





filename='pi.txt'
# with open(filename) as file_object:
#     con=file_object.read()
# print(con)



# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# with open(filename) as file_object:
#     lines=file_object.readlines()
# li=''
# for line in lines:
#     li+=line
# print(f"{li}")
# with open(filename) as file_object:
#     con=file_object.read()
#     con= con.replace('yes','конечно')
# print(con)
#Запись в файл
# with open(filename, 'w') as file_object:
#     file_object.write("I love sosal?\n")
# #Многострочная запись
#     file_object.write("I love CS2\n")

# #Присоединение данных к файлу
# with open(filename,'a') as file_object:
#     file_object.write("I also love coding in PyCharm\n")
#     file_object.write("I also loving coding in VsCode\n")
#Упражнение
# print("Введите имя гостя: ")
# with open(filename,'w') as file_object:
#     while True:
#         a = input("Введите свое имя: ")
#
#         if a.lower()=='quit':
#             break
#         file_object.write(f"{a}\n")
#         print(f"Привет, {a} ваше имя добавлено в список")

#Можно написать пол-ля и причину,так же вывести имя и причину можно обьединить все в одну строку в принципе
with open(filename,'a') as file_object:
    while True:
        a=input("Введите свое имя: ")


        if a.lower()=='quit':
            exit()
        b = input("Введите причину почему вы любите программировать: ")
        if b.lower()=='quit':
            exit()
        print(f"Привет {a}!")

        print("Спасибо что написали причину!<3")
        full=f"{a}: {b}\n"
        file_object.write(full)


