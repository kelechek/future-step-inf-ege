from itertools import permutations

graph = 'АБ БД ДК КЕ ЕВ ВА ГД ГК ГЕ БВ'.split()
matrix = '567 357 246 36 127 134 125'.split()

print(*range(1, 8))
for title in permutations('АБВГДЕК'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
