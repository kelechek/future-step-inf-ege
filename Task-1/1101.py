from itertools import permutations

graph = 'ЛВ ВГ ГА АБ БК КЕ ЕМ МЛ ГД ДЕ ВМ АК'.split()
matrix = '26 156 578 59 234 129 38 379 468'.split()

print(*range(1, 10))
for title in permutations('АБВГДЕКЛМ'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
