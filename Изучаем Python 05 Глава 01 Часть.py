# # #if(условие)
# # #простые условия
# # car="Bmw"
# # print(car.lower()=="bmw")
# # topping='black'
# #
# # if topping!='white':
# #     print("not white")
# #Сравнение чисел
# age=19
# print(age==19)
#
# numbs=17
#
# if numbs !=18:
#     print("Сорри тут с 18")
#
# print(numbs>21)#Можно такие условия писать
#
#
#Проверка нескольких условий
# age_0=21
# age_1=18
# print((age_0>=21) and (age_1>=21))
# print((age_0>=21) or  (age_1>=21))

#Проверка вхождения значений в список
# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# print('mushrooms' in requested_toppings)
# print('pepperoni' in requested_toppings)

#Проверка отсутствия значения в списке
banned_users = ['Андрей', 'Леша', 'Максим']
#banned_users=[user.lower() for user in banned_users]
users='андрей'
if users.title() not in banned_users:
     print(f"Здравствуйте,{users.title()},вы можете проходить!")
#тут просто я свою проверку сделал,с регистром

#Упражнения
#5.1
names='Vlad'
print("Your name Vlad? It's True")
print(names=='Vlad')

print("\nYour name Vladimir? It's False")
print(names=='Vladimir')
#Проверка равенства и неравенства строк. от части это задание 5.1
#Проверки с использованием функции lower().
names_1='Vladimir'
print(names_1.lower()=='vladimir')
#Числовые проверки равенства и неравенства, условий «больше», «меньше», «больше или равно», «меньше или равно».
age=18
print(f"Больше,меньше,равно и т.д: {age<19}")
#Проверки с ключевым словом and и or.
numb_0=18
numb_1=25
print((numb_0>17) and (numb_1>24))
print((numb_0>17) or (numb_1>30))
#• Проверка вхождения элемента в список
world=['Russia','Canada','Usa']
print(f"ВОТ:{'Russia' in world}")
