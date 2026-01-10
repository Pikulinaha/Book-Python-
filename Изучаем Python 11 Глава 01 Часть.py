#11 Глава
#Тестирование
#Тестирование функции
# def get_formatted_name(first,last,middle=''):
#     """Строит отформатированное полное имя"""
#     if middle:
#         full_name=f"{first} {middle} {last}"
#     else:
#         full_name=f"{first} {last}"
#     return full_name.title()
# #Модульные тесты и тестовые сценарии

# def get_contry(city,country,population=''):
#     """Делает Город-Страна"""
#     if population:
#         full=f"{city}, {country} - {population}"
#     else:
#         full=f"{city}, {country}"
#     return full.title()

class AnonymousSurvey():
    """Сбор анонимных ответов на вопросы"""

    def __init__(self,question):
        """Сохраняет вопрос и готовиться к сохранению ответов"""
        self.question=question
        self.responses=[]

    def show_question(self):
        """Выводит вопрос"""
        print(self.question)

    def store_response(self,new_response):
        """Сохраняет один ответ на вопрос"""
        self.responses.append(new_response)

    def show_result(self):
        """Вывод полученных ответов"""
        print("Results: ")
        for response in self.responses:
            print(f"- {response}")







#2 file
# import unittest
# from list import get_formatted_name
#
# class NamesTestCase(unittest.TestCase):
#     """Тесты для list.py"""
#
#     def test_first_last_name(self):
#         """Имена вида 'Janis Joplin' """
#         formated_name=get_formatted_name('janis','joplin')
#         self.assertEqual(formated_name,'Janis Joplin')
#     def test_first_last_middle_name(self):
#         """Работают ли такие имена как Wolfgang Amadeus Mozart?"""
#         formated_name=get_formatted_name('wolfgang','mozart','amadeus')
#         self.assertEqual(formated_name,'Wolfgang Amadeus Mozart')
#
# if __name__ =='__main__':
#     unittest.main()
from http.client import responses

# import unittest
# from list import get_contry
#
# class NamesTestCase(unittest.TestCase):
#     """Test for list.py"""
#
#     def test_city_country(self):
#         full_name=get_contry('santiago','chile')
#         self.assertEqual(full_name,'Santiago, Chile')
#     def test_city_country_population(self):
#         full_name=get_contry('santiago', 'chile',5000)
#         self.assertEqual(full_name,'Santiago, Chile - 5000')
# if __name__ == '__main__':
#     unittest.main()


from list import AnonymousSurvey

#Определение опроса с созданием экземпляра AnonymousServey
question="На каком языке ты разговариваешь?"
my_survey=AnonymousSurvey(question)

#Вывод вопроса и сохранение ответов
my_survey.show_question()
print("Enter 'q' for exit")
while True:
    response=input('Language: ')
    if response=='q':
        break
    my_survey.store_response(response)
#Вывод результатов
print("\nСпасибо за ответы на тест")
my_survey.show_result()