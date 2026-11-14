from itertools import permutations

graph = 'AE EB BG GD DF FA CG CF CA'.split()
matrix = '47 35 246 136 267 345 15'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
