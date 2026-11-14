from itertools import permutations

graph = 'AG GF FE ED DA AB BG BC CD'.split()
matrix = '26 147 456 236 37 134 25'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
