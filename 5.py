import csv

with open('songs.csv', 'r', encoding='utf-8') as infile:
    data = [elem for elem in csv.reader(infile, delimiter=';')]  # считываю файл в список data
    data0 = data.pop(0)  # сохраняю названия столбцов
    dic = {}  # словарь, в котором ключ - имя артиста, значение - список его песен
    for row in data:
        # если артиста нет в ключах словаря, то я завожу ключ и в значение ставлю его песню.
        # Если же артист уже в словаре, то в список песен этого артиста добавляю его песню.
        if row[1] not in dic.keys():
            dic[row[1]] = [row[2]]
        else:
            dic[row[1]].append(row[2])
    k = 0
    for key, value in sorted(dic.items(), key=lambda x: -len(x[1])):
        # на первом мете таблицы стоит unknown => мы не знаем какой именно исполнитель сделал ту песню.
        # Поэтому пропускаем даннуб строчку и выводим первые 10 из остального упорядоченного по количеству песен списка.
        if 11 > k > 0:
            print(f'{key} выпустил {len(set(value))} песен.')
        k += 1
