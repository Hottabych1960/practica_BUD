import csv

with open('songs.csv', 'r', encoding='utf-8') as infile:  # открываем файл
    data = [elem for elem in csv.reader(infile, delimiter=';')]  # считываю файл в список data
    data0 = data.pop(0)  # сохраняю названия столбцов
    for row in data:

        if row[-1] <= '01.01.2002':

            print(f'{row[2]} - {row[1]} - {row[0]}', row[-1])
        """if row[0] == '0':
            print(row)
            d, m, g = list(map(int, row[-1].split('.')))
            dn = 1
            di = d
            ln = len(row[1])
            ls = len(row[2])
            t = abs(((dn - di) / (ln + ls)) * 10000)
"""

