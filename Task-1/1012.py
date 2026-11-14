from itertools import permutations

graph = 'ГД ДЖ ЖЕ ЕБ БА АВ ВГ ГЕ ГБ'.split()
matrix = '37 45 1456 236 23 347 16'.split()

print(*range(1, 8))
for title in permutations('АБВГДЕЖ'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
