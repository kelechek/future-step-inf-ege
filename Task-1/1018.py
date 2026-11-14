from itertools import permutations

graph = 'АБ БВ ВД ДЕ ЕК КГ ЕГ ГВ ЕВ АВ'.split()
matrix = '24 146 56 1267 36 23457 46'.split()

print(*range(1, 8))
for title in permutations('АБВГДЕК'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
