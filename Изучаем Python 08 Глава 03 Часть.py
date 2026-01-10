#Передача списка
# def greet_users(names):
#     """Вывод простого приветствия для каждого пользователя в списке"""
#     for name in names:
#         msg=f"Привет, {name.title()}"
#         print(msg)
# user_name=['hannah','ty','margot']
# greet_users(user_name)

#Изменение списка в функции

# Список моделей, которые необходимо напечатать.
# unprinted_designs=['phone case','robot pendant','dodecahedron']
# complited_models=[]
# # Цикл последовательно печатает каждую модель до конца списка.
# # После печати каждая модель перемещается в список completed_models.
# while unprinted_designs:
#     current_design=unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     complited_models.append(current_design)
# print("\nВывод подписанных моделей: ")
# for complited_model in complited_models:
#     print(complited_model)

# def print_model(unprinted_designs,complited_models):
#     """Имитирует печать моделей, пока список не станет пустым.
#  Каждая модель после печати перемещается в completed_models."""
#     while unprinted_designs:
#         current_design=unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         complited_models.append(current_design)
# def show_complited_models(completed_models):
#     """Вывод обо всех напечатанных моделей"""
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_designs=['phone case','robot pendant','dodecahedron']
# complited_models=[]
# print_model(unprinted_designs, complited_models)
# show_complited_models(complited_models)
#Запрет изменения списка в функции
#Синтаксис сегмента [:] создает копию списка для передачи функции.
# Если удаление элементов из списка unprinted_designs в print_models.py нежелательно, функцию print_models() можно вызвать так:
#print_models(unprinted_designs[:], completed_models)
#

#Передача произвольного набора аргументов

# def make_pizza(*toppings):
#     print(toppings)
# make_pizza('pepperoni')
# make_pizza('mushrooms','extra cheese','green peppers')

# def make_pizza(*toppings):
#     print("\nСделайте пиццу: ")
#     for topping in toppings:
#         print(f"- {topping}")
# make_pizza('pepperoni')
# make_pizza('mushrooms','extra cheese','green peppers')
#
# #Позиционные аргументы с произвольными наборами аргументов
# def make_pizza(size,*toppings):
#     print(f"\nСделайте пиццу {size}: ")
#     for topping in toppings:
#         print(f"- {topping}")
# make_pizza(12,'pepperoni')
# make_pizza(16,'mushrooms','extra cheese','green peppers')

#Использование произвольного набора именованных аргументов


# def build_profile(firs,last,**user_info):
#     user_info['first_name']=firs
#     user_info['last_name']=last
#     return user_info
# user_profile=build_profile('albert','enshtein',location='princeteon',field='physics')
# print(user_profile)


#Упражнения
# def burgers(*ing):
#     print("Ингридиенты бургера: \n")
#
#     for burger in ing:
#         print(f"---{burger}")
# burgers('Булка')
# burgers('Бекон','Котлета')
# burgers('Яйцо','Салат','Булка')

#
# def build_profile(firs,last,**user_info):
#     user_info['first_name']=firs
#     user_info['last_name']=last
#     return user_info
# user_profile=build_profile('Вова','Алмакаев',location='программист',field='Душа')
# print(user_profile)


def cars(mfr,model,**car_info):
    car_dict={
        'mnf': mfr.title(),
        'model':model.title()
    }
    for key,value in car_info.items():
        car_dict[key]=value
    return car_dict
car =cars('subaru', 'outback', color='blue', tow_package=True)

print("Вывод результата: \n")
for k,v in car.items():
    print(f" {k}:{v}")

