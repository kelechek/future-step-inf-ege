from itertools import permutations

graph = 'АБ БГ ГЕ ЕЗ ЗД ДВ ВА ВБ ГД'.split()
matrix = '67 567 456 35 234 123 12'.split()

print(*range(1, 8))
for title in permutations('АБВГДЕЗ'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
