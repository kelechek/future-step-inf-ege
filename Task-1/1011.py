from itertools import permutations

graph = 'BG GF FE ED DC CB AG AB AD'.split()
matrix = '234 156 17 15 246 257 36'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
