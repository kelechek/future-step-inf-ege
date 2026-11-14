from itertools import permutations

graph = 'АГ ГД ДК КЕ ЕБ БА ВА ВБ ВД'.split()
matrix = '356 36 125 67 137 124 45'.split()

print(*range(1, 8))
for title in permutations('АБВГДЕК'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
