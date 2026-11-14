from itertools import permutations

graph = 'АВ ВЕ ЕК КД ДБ БА БВ ГД ГК ГЕ'.split()
matrix = '457 346 24 123 167 257 156'.split()

print(*range(1, 8))
for title in permutations('АБВГДЕК'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
