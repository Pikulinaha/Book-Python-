#Необязательные аргументы
# def get_formated_name(first_name,midle_name,last_name):
#     """Возвращает аккуратно отформатированное полное имя"""
#     full_name=f"{first_name} {midle_name} {last_name}"
#     return full_name.title()
# musician=get_formated_name('john','lee','hooker')
# print(musician)

# def get_formated_name(first_name,last_name,midle_name=''):
#     if midle_name:
#         full_name=f"{first_name} {midle_name} {last_name}"
#     else:
#         full_name=f"{first_name} {last_name}"
#     return full_name.title()
# musician=get_formated_name('john','hooker','lee')
# print(musician)
# musician=get_formated_name('jini','hookerk')
# print(musician)

#Возвращение словаря
# def build_person(first_name,last_name,age):
#     """Возвращает словарь с информацией о человеке"""
#     person={'first':first_name,'last':last_name}
#     if age:
#         person['age']= age
#     return person
# musician=build_person('jimi','hendrix', age=27)
# print(musician)

#Использование функции в цикле while
# def get_formatted_name(first_name,last_name):
#     full_name=f"{first_name} {last_name}"
#     return full_name.title()
# while True:
#     print("\nНапишите свое ФИ")
#     print("(enter 'q' on exit)")
#     f_name=input("First name: ")
#     if f_name=='q':
#         break
#     l_name=input("Last name: ")
#     if l_name=='q':
#         break
#     formatted_name=get_formatted_name(f_name,l_name)
#     print(f"Hello, {formatted_name}!")

# def city_country(city,country):
#     full=f"{city},{country}"
#     return full.title()
# mus=city_country('Santiago','Chile')
# print(mus)
# mus=city_country('Russia','Penza')
# print(mus)
# mus=city_country('France','Paris')
# print(mus)
# def make_album(executor,album,dor):
#     full_album={'ex':executor,'al':album}
#     if dor:
#         full_album['dor']= dor
#     return full_album
# music=make_album('Раковая выпохаль','Сайт','2')
# print(music)

def make_album(arist,title,track=None):
    album={
        'artist':arist.title(),
        'title':title.title()
    }
    if track:
        album['track']=track
    return album
print("\nСоздание альбома")
print("Чтобы пропустить 'q'")
while True:
    artist=input("Введите имя исполнителя: ")
    if artist.lower()=='q':
        break
    title=input("Введите название альбома: ")
    if title.lower()=='q':
        break

    track=input("Введите кол-во песен в альбоме: ")
    if track.lower()=='q':
        break
    if track:
        albumS=make_album(artist,title,track)
    else:
        albumS=make_album(artist,title)
    print(f"\nАльбом создан: {albumS} ")
