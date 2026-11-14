from itertools import permutations

graph = 'AE EF FB BD DC CA AB GC GD'.split()
matrix = '36 567 14 367 27 124 245'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
