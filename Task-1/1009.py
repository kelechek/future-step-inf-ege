from itertools import permutations

graph = 'AF FC CG GE EA FB BD DE DA'.split()
matrix = '23 145 16 27 267 357 456'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
