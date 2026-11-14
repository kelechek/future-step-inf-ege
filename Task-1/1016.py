from itertools import permutations

graph = 'АБ БВ ВГ ГЖ ЖЕ ЕД ДА ДБ ЕГ'.split()
matrix = '346 57 14 137 267 15 245'.split()

print(*range(1, 8))
for title in permutations('АБВГДЕЖ'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
