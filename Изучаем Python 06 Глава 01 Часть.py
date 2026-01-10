# alien_0 = {'color':'green','points':5}
# print(alien_0['color'])
# print(alien_0['points'])
from Tools.scripts.texi2html import increment
from setuptools.command.alias import alias

# alien_0 = {'color':'green','points':5}
# new_points=alien_0['points']
# print(f"Ты получил {new_points} points!")

# alien_0 = {'color':'green','points':5}
# print(alien_0)
# alien_0['x_position']=0
# alien_0['y_position']=25
# print(alien_0)

# alien_0={}
# alien_0['color']='green'
# alien_0['points']=5
# print(alien_0)
#Изменение значений в словаре
# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")
#
# alien_0['color']='yellow'
# print(f"The alien is now {alien_0['color']}.")

# alien_0={'x_position':0,'y_position':25,'speed': 'fast'}
# print(f"Оригинальная позиция {alien_0['x_position']}")
# # Пришелец перемещается вправо.
# # Вычисляем величину смещения на основании текущей скорости.
# if alien_0['speed']=='slow':
#     x_increment=1
# elif alien_0['speed']=='medium':
#     x_increment=2
# else:
#     x_increment=3
# alien_0['x_position']=alien_0['x_position']+x_increment
# print(f"Новая позиция {alien_0['x_position']}")

#Удаление пар «ключ-значение»
# alien_0={'color':'green','points':5}
# print(alien_0)
#
# del alien_0['points']
# print(alien_0)
# #Словарь с однотипными объектами
# favorite_languages={
#     'jen':'python',
#     'sahar':'c',
#     'edward':'ruby',
#     'phil':'python'
# }
# languages=favorite_languages['sahar'].title()
# print(f"Любимый язык Захара-{languages}")

#Обращение к значениям методом get()
# alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points']) тут будет ошибка

# alien_0 = {'color': 'green', 'speed': 'slow'}
#
# point_value=alien_0.get('points','No point value assigned')
# print(point_value)
#Упражнения
# maxim={'first_name':'maxim','last_name':'breev','age':19,'city':'nizniy lomov'}
# print(maxim['first_name'])
# print(maxim['last_name'])
# print(maxim['age'])
# print(maxim['city'])

like_number={
    'maxim':7,
    'alex':3,
    'andrey':5,
    'dima':67,
    'egor':4
}
# for name,number in like_number.item():
#     print(f"{name}:{number}") это через цикл For
number=like_number['maxim']
print(f"Любимое число Maxima {number}")
number=like_number['alex']
print(f"Любимое число Alexa {number}")
number=like_number['andrey']
print(f"Любимое число Andrey {number}")
number=like_number['dima']
print(f"Любимое число Dima {number}")
