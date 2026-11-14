from itertools import permutations

graph = 'AG GF FB BD DE EA CG CB CD'.split()
matrix = '45 345 256 127 123 37 46'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
