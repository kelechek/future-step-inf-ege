from itertools import permutations

graph = 'АБ БД ДК КЕ ЕГ ГВ ВБ ЕВ ЕД ВД'.split()
matrix = '27 1567 67 5 246 2357 1236'.split()

print(*range(1, 8))
for title in permutations('АБВГДЕК'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
