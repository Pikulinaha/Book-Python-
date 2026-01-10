# #Перебор словаря
# user_0={
#     'username':'efermi',
#     'first':'enrico',
#     'last': 'fermi'
# }
# for key,value in user_0.items():
#     print(f"\nКлюч: {key}")
#     print(f"Значение: {value}")
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# # for name,language in favorite_languages.items():
# #     print(f"{name.title()} favorite languages: {language.title()}")
# #Перебор всех ключей в словаре
# # for name in favorite_languages.keys():
# #     print(name.title())
# friend=['phil','sarah']
# for name in favorite_languages:
#     print(name.title())
#     if name in friend:
#         languages=favorite_languages[name].title()
#         print(f"{name} я вижу ты любишь {languages}")
#Перебор ключей словаря в определенном порядке
# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
#  }
# # for name in sorted(favorite_languages.keys()):
# #     print(f"{name.title()}, cool")
# #Перебор всех значений в словаре
# # print("Написаны языки: ")
# # for name in favorite_languages.values():
# #     print(f"{name.title()}")
# #Без повторений
# print("Написаны языки:")
# for name in set(favorite_languages.values()):
#     print(f"{name.title()}")
#Упражнения
# like_number={
#     'maxim':7,
#     'alex':3,
#     'andrey':5,
#     'dima':67,
#     'egor':4
# }
# for k,v in like_number.items():
#  print(f"Любимое число {k.title()}: {v} ")
# rivers = {
#     'Нил': 'Египет',
#     'Амазонка': 'Бразилия',
#     'Янцзы': 'Китай'
# }
# for k,v in rivers.items():
#  print(f"The {k.title()} runs through {v.title()}")
# print("\nСтраны")
# for world in rivers.values():
#  print(f"{world}-Страна")
# print("\nРеки")
# for world in rivers.keys():
#  print(f"{world}-Река")
# favorite_languages = {
#   'jen': 'python',
#   'sarah': 'c',
#   'edward': 'ruby',
#   'phil': 'python',
# }
# mans=['jen','edward','jully']
# for name in mans:
#  if name in favorite_languages:
#   l=favorite_languages[name].title()
#   print(f"{name.title()} Спасибо что прошел опрос")
#  else:
#   print(f"{name.title()} Хотите пройти опрос?")
#Вложение
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens=[alien_0,alien_1,alien_2]
# for alien in aliens:
#  print(alien)
# aliens=[]
# #Создание 30 зеленых пришельцев
# for alien_number in range(30):
#  new_alien={'color':'green','points':5,'speed':'slow'}
#  aliens.append(new_alien)
#  #Вывод первых 5
# for alien in aliens[:5]:
#    print(alien)
# print("...")
# print(f"Всего создано пришельцев: {len(aliens)}")
# aliens=[]
# #Создание 30 зеленых пришельцев
# for alien_number in range(0,30):
#  new_alien={'color':'green','points':5,'speed':'slow'}
#  aliens.append(new_alien)
# for alien in aliens[0:3]:
#  if alien['color']=='green':
#   alien['color']='yellow'
#   alien['speed']='medium'
#   alien['points']=10
# for alien in aliens[0:5]:
#  print(alien)
# print("...")
#Список в словаре
# pizza={
#  'crust':'think',
#  'toppings':['mushrooms','extra cheese']
# }
# #Описание заказа
# print(f"You ordered a {pizza['crust']}-crust pizza"
#       "with the following toppings")
# for topping in pizza['toppings']:
#  print("\t"+topping)
favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }
for name,languages in favorite_languages.items():
 if len(languages)==1:
  print(f"\n{name.title()} your favorite laguage: ")
  for language in languages:
   print(f"{language.title()}")
 else:
   print(f"\n{name.title()} your favorites languages: ")
   for language in languages:  # Этот цикл ВНУТРИ else
    print(f"{language.title()}")
