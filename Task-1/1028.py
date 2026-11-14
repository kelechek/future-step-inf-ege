from itertools import permutations

graph = 'AH HC CF FG GB BD DE EA HG EB'.split()
matrix = '38 58 146 36 27 347 568 127'.split()

print(*range(1, 9))
for title in permutations('ABCDEFGH'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
