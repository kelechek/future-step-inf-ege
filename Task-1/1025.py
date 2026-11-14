from itertools import permutations

graph = 'AG GB BE EF FD DC CA AB FC'.split()
matrix = '246 16 57 15 347 127 356'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
