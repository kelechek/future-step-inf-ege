from itertools import permutations

graph = 'AF FC CH HB BE EA AB CG GD DH'.split()
matrix = '248 157 456 136 23 34 28 17'.split()

print(*range(1, 9))
for title in permutations('ABCDEFGH'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
