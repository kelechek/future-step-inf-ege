from itertools import permutations

graph = 'АБ БВ ВГ ГД ДЕ КА КБ КВ КГ КД КЕ'.split()
matrix = '25 156 45 357 123467 257 456'.split()

print(*range(1, 8))
for title in permutations('АБВГДЕК'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
