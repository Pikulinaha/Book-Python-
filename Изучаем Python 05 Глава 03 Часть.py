#Использование команд if со списками
#toopings=['mushrooms', 'green peppers', 'extra cheese']
from http.cookiejar import cut_port_re

# for toops in toopings:
#      print(f"Добавим вам это в пиццу {toops}")
# print("\nВаша пицца готова")

# for toops in toopings:
#      if toops=='green peppers':
#           print("Извините перца нету на данный момент")
#      else:
#           print(f"Добавим вам это в пиццу {toops}")
# print("\nВаша пицца готова")

# requested_toppings=['cheese']
# if requested_toppings:
#      for toppings in requested_toppings:
#           print(f"Добавим вам {toppings}")
#      print("\nПицца завершена")
# else:
#      print("Уверены что хотите обычную пиццу?")

# available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
#
# requested_toppings= ['mushrooms', 'french fries', 'extra cheese']
#
# for toppings in requested_toppings:
#      if toppings in available_toppings:
#           print(f"Добавим вам {toppings}")
#      else:
#           print("Извините такого у нас нету")
# print("\nВаша пицца готова")

#Упражнения
# names=['admin','Vova','Alex','Maxim','Andrey']
# for name in names:
#      if name=='admin':
#           print("Привет админ кого будем банить")
#      else:
#           print(f"Привет {name}")

# names=['admin','Vova','Alex','Maxim','Andrey']
# if names:
#      print("Список не пуст")
#      for name in names:
#           if name=='admin':
#                print("admin")
#           else:
#                print(f"Привет {name}")
#
# else:
#      print("Список пуст")

# current_users=['Vova','Alex','Maxim','Andrey','Dima']
#
# new_users=['Vova','Maxim','Egor','Nikita','Danil']
#
# current_users_lower=[user.lower() for user in current_users]
#
# for new_user in new_users:
#      if new_user.lower() in current_users_lower:
#           print(f"Имя {new_user} уже занято")
#      else:
#           print(f"{new_user} это имя доступно!")

# current_users=['Vova','Alex','Maxim','Andrey','Dima']
# new_users=['Vova','Maxim','Egor','Nikita','Danil']
# name_lower=[user.lower() for user in current_users]
#
# for name in new_users:
#      if name.lower() in name_lower:
#           print(f"{name},это Занято")
#      else:
#           print(f"{name} это свободно")

# word=[1,2,3,4,5,6,7,8,9]
# for current in word:
#      if current==1:
#           print(f"{current}st")
#      elif current==2:
#           print(f"{current}nd")
#      elif current==3:
#           print(f"{current}rd")
#      else:
#           print(f"{current}th") вот тут я потупил,и думал как лучше заполнить список,['1' и т.д ] или через range
#deepseek написал он бы решил эту задачу через range и я попытался сделать это через range
# for n in range(1,10):
#      if n==1:
#           print(f"{n}st")
#      elif n==2:
#           print(f"{n}nd")
#      elif n==3:
#           print(f"{n}rd")
#      else:
#           print(f"{n}th")
