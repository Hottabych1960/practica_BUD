import csv

with open('songs.csv', 'r', encoding='utf-8') as infile:
    data = [elem for elem in csv.reader(infile, delimiter=';')]   # считываю файл в список data
    data0 = data.pop(0)  # сохраняю названия столбцов
    russian_artists, foreign_artists = [],[]  #списки российских и иностранных артистов соответственно
    alf1 = 'ёйцукенгшщзхъэждлорпавыфячсмитьбю'
    alf = alf1 + alf1.upper()  # русский алфвавит: строчные и заглавные буквы
    for row in data:
        if any(True if l in alf else False for l in row[1]):   # проверяю, есть ли хотя бы одна русская буква
            russian_artists.append(row[1])
        else:
            foreign_artists.append(row[1])
    russian_artists = list(set(russian_artists))
    foreign_artists = list(set(foreign_artists))
    print(f'Количество российских исполнителей: {len(russian_artists)}')
    print(f'Количество иностранных исполнителей: {len(foreign_artists)}')


with open('russian_artists.txt', 'w', encoding='utf-8') as outfile1, \
        open('foreign_artists.txt', 'w', encoding='utf-8') as outfile2:
    # открываю файлы для записи
    for name in russian_artists:
        print(name, file=outfile1)  # запись российских артистов в файл russian_artists.txt
    for name in foreign_artists:
        print(name, file=outfile2)  # запись иностранных артистов в файл foreign_artists.txt


