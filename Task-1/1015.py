from itertools import permutations

graph = 'АБ БД ДЕ ЕГ ГВ ВЖ ЖК КА ДГ АВ'.split()
matrix = '58 357 25 67 123 48 248 167'.split()

print(*range(1, 9))
for title in permutations('АБВГДЕЖК'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
