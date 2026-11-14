from itertools import permutations

graph = 'AD DE EG GC CF FA BA BE BF'.split()
matrix = '37 367 125 56 34 247 126'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
