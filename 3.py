import csv

with open('songs.csv', 'r', encoding='utf-8') as infile:  # открываем файл
    data = [elem for elem in csv.reader(infile, delimiter=';')]  # считываю файл в список data
    data0 = data.pop(0)  # сохраняю названия столбцов
    artist = input()  # вводимое имя артиста
    while artist != '0':  #условие прекращения ввода
        f = False  # флаг, который показывает, есть ли данный артист в БД
        for row in data:
            if artist == row[1] and (not f):
                print(f'У {row[1]} найдена песня: {row[2]}')
                f = True
        if not f:
            print(f'К сожалению, ничего не удалось найти')
        artist = input()