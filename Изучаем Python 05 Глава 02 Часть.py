#Команды if
# age=17
# if age>=18:
#      print("Вы можете голосовать!")
#      print("Вы зарегестрироавлись для голосования?")
# else:
#      print("Извините,вы не можете голосовать")
#      print("Пройдите регистрацию,когда наступит 18 лет")
#age=66
# if age<4:
#      print("Ваш билет бесплатный билет")
# elif age<18:
#      print("Билет стоит 25$")
# else:
#      print("Билет стоит 40$")
# if age<4:
#      price=0
# elif age<18:
#      price=25
# else:
#      price=40
# print(f"Ваш билет стоит ${price}")

#Серии блоков elif
# if age<4:
#      price=0
# elif age<18:
#      price=25
# elif age<65:
#      price=40
# else:
#      price=20
# print(f"Ваш билет стоит ${price}")

#Отсутствие блока else
# if age<4:
#      price=0
# elif age<18:
#      price=25
# elif age<65:
#      price=40
# elif age>=65:
#      price=20
# print(f"Ваш билет стоит ${price}")

#Проверка нескольких условий
# tooppings=['mushrooms', 'extra cheese']
#
# if 'mushrooms' in tooppings:
#      print("Добавим грибы")
# if 'peperoni' in tooppings:
#      print("Добавим пеперони")
# if 'extra cheese' in tooppings:
#      print("Добавим сыр")
# print("\nВаша пицца собрана")
#Упражнения
# alien_color='red'
# if alien_color=='green':
#      print("Вы заработали 5 очков")

# alien_color='red'
# if alien_color=='green':
#      print("Вы заработали 5 очков")
# else:
#      print("Вы заработали 10 очков")

# alien_color='red'
# if alien_color=='green':
#      print("Вы заработали 5 очков")
# elif alien_color=='yellow':
#      print("Вы заработали 10 очков")
# else:
#      print("Вы заработали 15 очков")

# age=65
# if age<2:
#      a='Младенец'
# elif 2<=age<4:
#      a='Малыш'
# elif 4<=age<13:
#      a='Ребенок'
# elif 13<=age<20:
#      a='Подросток'
# elif 20<=age<65:
#      a='Взрослый'
# else:
#      a='Пожилой'
# print(f"Если вам столько лет,то вы {a}")

favorite_fruit=['apple','pineapple','peach','banana']
if 'apple' in favorite_fruit:
     print(f"Я тоже люблю этот фрукт")
if 'pizza' in favorite_fruit:
     print("Это не фрукт даже!")
if 'pineapple' in favorite_fruit:
     print("Он еще такой кислый!")
if 'peach' in favorite_fruit:
     print("Я сок сейчас с ним пью")
if 'banana' in favorite_fruit:
     print("Миньены его любят тоже")

