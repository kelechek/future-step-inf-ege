from itertools import permutations

graph = 'AF FE EC CG GD DB BA FB ED'.split()
matrix = '256 134 267 27 16 135 34'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
