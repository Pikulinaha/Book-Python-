# # #Работа со списками
# # #Перебор всего списка
# # magic=['алиса','давид','лиза']
# # for n in magic:
# #     print(n)
# #     print(f"{n.title()},это имена.")
# # print("Спасибо за внимание")
# #Упражнения
# pizzas=['Сырный цыпленок','4 Сыра','Маргарита','Мясная','Гавайская']
# for pizza in pizzas:
#     print(f"Я обожаю эту пиццу, {pizza}!")
# print("Я реально люблю все эти пиццы")
#Создание числовых списков
# for n in range(5):
#     print(n)
# numbers=list(range(1,6))
# print(numbers)
# even_numbers=list(range(2,11,2)) 2 увеличивает ход
# print(even_numbers)
#squares=[]
# for value in range(1,11): ////////
#     unsquare= value**2 ////////////
#     squares.append(unsquare) ///////     1 Вариант Кода
# print(squares) //////////////////////
# for value in range(1,11): /////////
#     squares.append(value**2)/////////// 2 Вариает кода
# print(squares)/////////////////////
# digits =[1,2,3,4,5,6,7,8,9,0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))
# squares=[value**2 for value in range(1,11)] Этому нужно будет со временем научиться,сейчас это пример чтобы не пугаться кода других программистов
# print(squares)
#Упражнения
# for n in range(1,1000001):
#     print(min(n))
# numbers=list(range(1,1000001))
# #print(numbers)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# even_numbers=list(range(1,20,2))
# print(even_numbers)
# numbers=list(range(3,31,3))
# for n in numbers:
#     print(n)
# squares=[]
# for value in range(1,11):
#     n=value**3
#     squares.append(n)
# print(squares)


# squares=[value**3 for value in range(1,11)]
# print(squares)




