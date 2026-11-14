from itertools import permutations

graph = 'AC CG GB BD DE EA FG FC FE'.split()
matrix = '26 147 456 237 37 13 245'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
