from itertools import permutations

graph = 'АГ БД ВЕ ГД ДЕ ДК ДЛ КЛ'.split()
matrix = '2 13578 28 7 26 5 24 23'.split()

print(*range(1, 9))
for title in permutations('АБВГДЕКЛ'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
