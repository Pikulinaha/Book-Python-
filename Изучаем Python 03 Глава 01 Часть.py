# #Глава 3 Списки
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# # #print(bicycles[0].title())
# # print(bicycles[1])
# # print(bicycles[3])
# # print(bicycles[-1])#-вывод последнего элемента
# #Использование отдельных элементов из списка
# message=f"My first byke was a {bicycles[0].title()}"
# print(message)
#Упражнения 3.1-3.3


names=['Егор','Арсений','Ваня','Влад']
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
#-------------------------------------------------------
#message=f"Крутой парень,но не совсем {names[0]}"
#print(message)
#--------------------------------------------------
# car=['BMW','Mersedes','Toyota','Volvo']
# message=f"Я хотел бы купить себе следующую машину {car[0]}"
# print(message)
#Изменение элементов в списке
# motorcycles=['honda','yamaha','suzuki']
# print(motorcycles)
# motorcycles[0]='ducati'
# print(motorcycles)
#Добавление элементов в список
# motorcycles=['honda','yamaha','suzuki']
# print(motorcycles)
# motorcycles.append('ducati')
# print(motorcycles)
# motorcycles=[]##########################
# motorcycles.append('honda')#############
# motorcycles.append('yamaha')############ Самый популярный способ построения списков потому что данные, которые пользователь,
# print(motorcycles)###################### захочет сохранить в программе, часто становятся известными только после запуска программы
#Вставка элементов в список
# motorcycles=['honda', 'yamaha', 'suzuki']
# motorcycles.insert(2,'ducati') # метод insert позволяет вставить любой элемент в любую позицию
# print(motorcycles)
#Удаление элементов из списка
#Del
# motorcycles=['honda','yamaha','suzuki']
# print(motorcycles)
# del motorcycles[2]
# print(motorcycles)
#pop
# motorcycles=['honda','yamaha','suzuki']
# print(motorcycles)
                                                                                # если вы собираетесь просто
                                                # удалить элемент из списка, никак не используя его, выбирайте команду del; если
                                                #же вы намерены использовать элемент после удаления из списка, выбирайте метод pop().
# popped_motorcycles=motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycles)
#Извлечение элементов из произвольной позиции списка
# firs_owned=motorcycles.pop(0)
# print(f"Первый мотоцикл,который я купил {firs_owned.title()}.")
#Удаление элементов по значению
# motorcycles=['honda','yamaha','suzuki','ducati']
# print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)
#Упражнения 3.4-3.7
# names=['Егор','Арсений','Ваня','Влад']
# invitation=f"Йоу,пригоняй на вечеринку {names[0].title()}"
# print(invitation)
# invitation=f"Йоу,пригоняй на вечеринку {names[1].title()}"
# print(invitation)
# invitation=f"Йоу,пригоняй на вечеринку {names[2].title()}"
# print(invitation)
# names[3]='Саня'
# invitation=f"Йоу,пригоняй на вечеринку {names[3].title()}"
# print(invitation)
# print(names)
# names.insert(0,'Назар')
# names.insert(3,'Илья')
# names.append('Кирилл')
# print(names)
