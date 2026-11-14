from itertools import permutations

graph = 'АД ДЕ ЕВ ВБ БА БГ ДВ'.split()
matrix = '245 136 25 15 134 2'.split()

print(*range(1, 7))
for title in permutations('АБВГДЕ'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
