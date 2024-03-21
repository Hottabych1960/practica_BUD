import csv


def q_sort(data):
    if len(data) <= 1:
        return data
    else:
        q = data[len(data) // 2]
        data_mq = [row for row in data if row[-1] < q[-1]]
        data_eq = [q] * data.count(q)
        data_bq = [row for row in data if row[-1] > q[-1]]
        return q_sort(data_mq) + q_sort(data_eq) + q_sort(data_bq)


with open('songs.csv', 'r', encoding='utf-8') as infile:
    data = [elem for elem in csv.reader(infile, delimiter=';')]
    data0 = data.pop(0)
    lst = q_sort(data)
    for elem in lst:
        print(elem)
    k = 1
    for row in lst:
        if k < 6:
            print(f'{k} {row[2]}, {row[1]}, {row[-1]}')
            k += 1

