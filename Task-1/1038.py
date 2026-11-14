from itertools import permutations

graph = 'AE EC CG GF FB BD DA DF GE'.split()
matrix = '234 136 12 157 467 25 45'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
