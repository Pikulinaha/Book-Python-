# cars = ['bmw', 'audi', 'toyota', 'subaru']
# # cars.sort(reverse=True)
# print(cars)
# print("Оригинальный список: ")
# print(cars)
# print("\nВременная сортировка:")
# print(sorted(cars)) Позволяет хранить оригинальный список в исходном порядке,хотя просто сортирует его
# print("\nСнова оригинальная сортировка:")
# print(cars)
# cars.reverse()#он не сортирует, просто отзеркаливает список
# print(cars)
# print(len(cars))
#Упражнения
world=['Россия','Италия','Франция','Германия','Англия']
print(world)
print(sorted(world))
print(world)
print(sorted(world,reverse=True))
print(world)
world.reverse()
print(world)
world.reverse()
print(world)
world.sort(reverse=True)
print(world)
names=['Егор','Арсений','Ваня','Влад']
print(len(names))
#Ошибки индексирования при работе со списками
#Не стоит забывать что элементы списка начинаются с 0,а не с 1
#Так же при выводе print(car[-1]) из пустого списка будет выведена ошибка, сначала нужно его заполнить
#Если не известна ошибка со списком, то нужно попробовать вывести его длину или сам список 
