from itertools import permutations

graph = 'АБ БВ ВЖ ЖГ ГД ДЕ ЕБ БЖ ЖД ЕЖ'.split()
matrix = '47 46 6 12567 467 2345 145'.split()

print(*range(1, 8))
for title in permutations('АБВГДЕЖ'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)