#Стандартная библиотека Python
# from random import randint
# print(randint(1,6))#Случайное значение в диапазоне
#
# from random import choice
# players=['Леха','Макс','Диман','Егор','Арсений']
# first_up=choice(players)
# print(first_up)
# from random import randint
# class Die:
#     def __init__(self,sides=6):
#         self.sides=sides
#     def roll_die(self):
#         result=randint(1,self.sides)
#         print(f"{self.sides} and {result}")
#         return result
# cube=Die()
# for i in range(1,11):
#     print(f"Бросок {i}: ",end="")
#     cube.roll_die()

from random import choice
number=['А','X','C','B','Y',3,4,1,5,10,12,7,0,18,20]
my_ticket=['Y','X',18,20]
a=0
won=False
print(f"Мой билет {my_ticket}")
while not won:
    a+=1

    x=[]
    for i in range(4):
        x.append(choice(number))
    if x==my_ticket:
        won=True
    if a % 100000 == 0:
        print(f"Попытка #{a:,}... ещё не выиграл")
print(f"Выиграшная комбинация {x}")
print(f"{a}")





