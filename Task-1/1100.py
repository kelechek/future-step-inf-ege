from itertools import permutations

graph = 'АБ АГ БГ ГД ДК КЕ ЕВ ВГ'.split()
matrix = '45 57 56 17 1236 35 24'.split()

print(*range(1, 8))
for title in permutations('АБВГДЕК'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
