# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

import random
import datetime

#Получаем список из трех случайных песен
three_songs = random.sample(my_favorite_songs, 3)

# Скорее всего числовое значение в списке (например "3.40")
# это количество минут, секунд песни
# Пишем функцию для извлечения минут:
def kol_minyt(p):
    return int(p//1)

# Пишем функцию для извлечения секунд:
def kol_sekynd(p):
    return int(round((p%1)*100, 2))

#время исполнения трех случайных песен в секундах
SS0= kol_minyt(three_songs[0][1])*60 + kol_sekynd(three_songs[0][1]) + \
kol_minyt(three_songs[1][1])*60 + kol_sekynd(three_songs[1][1]) + \
kol_minyt(three_songs[2][1])*60 + kol_sekynd(three_songs[2][1]) 

print ('Три песни звучат', round(SS0/60) ,'минут')

SS1= datetime.time(0, int(SS0/60), SS0-(int(SS0/60)*60))
print('Пункт D',SS1)



# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

songs_list = list(my_favorite_songs_dict.values())


#Получаем список из трех случайных песен
three_songs1 = random.sample(songs_list, 3)


#время исполнения трех случайных песен в секундах
SSS0= kol_minyt(three_songs1[0])*60 + kol_sekynd(three_songs1[0]) + \
kol_minyt(three_songs1[1])*60 + kol_sekynd(three_songs1[1]) + \
kol_minyt(three_songs1[2])*60 + kol_sekynd(three_songs1[2]) 

print('Пункт B')

print ('Три песни звучат', round(SSS0/60) ,'минут')

SSS1= datetime.time(0, int(SSS0/60), SSS0-(int(SSS0/60)*60))
print('Пункт D', SSS1)


# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

