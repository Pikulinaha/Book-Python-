#Импортирование всего модуля
def make_pizza(size,*toppings):
    print(f"Пицца размера {size} ")
    for topping in toppings:
        print(f"----{topping}")
#Импортирование конкретных функций

# from pizza import make_pizza
#
# make_pizza(16,'pepperoni')                        это из другого файла
# make_pizza(12,'mushrooms','extra cheese')

#Назначение псевдонима для функции
# from pizza import make_pizza as mp
#
# mp(16,'pepperoni')
# mp(12,'mushrooms','extra cheese')      #Общий синтаксис назначения псевдонима выглядит так:
# from имя_модуля import имя_функции as псевдоним
#Назначение псевдонима для модуля
# import имя_модуля as псевдоним
# import pizza as p
#
# p.make_pizza(16,'pepperoni')
# p.make_pizza(12,'mushrooms','extra cheese')

#Импортирование всех функций модуля
#from pizza import *
#
# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms','extra cheese')


# unprinted_designs=['phone case','robot pendant','dodecahedron']
# complited_models=[]
# # Цикл последовательно печатает каждую модель до конца списка.
# # После печати каждая модель перемещается в список completed_models.
# while unprinted_designs:
#     current_design=unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     complited_models.append(current_design)
# print("\nВывод подписанных моделей: ")        1 файл



# from  printing_functions import *
#
# for complited_model in complited_models:
#     print(complited_models)       2 файл


# #def burgers(*ing):
#     print("Ингридиенты бургера: \n")
#
#     for burger in ing:
#         print(f"---{burger}") 1 Файл


#
# import printing_functions
# printing_functions.burgers('Булка')
#
#
# from  printing_functions import burgers
# burgers('Бекон','Котлета')
#
# from printing_functions import burgers as bg
#
# bg('Яйцо','Салат','Булка')
#
# import printing_functions as pf
#
# pf.burgers('Булка')
#
# from  printing_functions import *
# burgers('Бекон','Котлета')                        2 file 

