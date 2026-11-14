from itertools import permutations

graph = 'AG GF FE ED DB CA CG CF CE CD CB'.split()
matrix = '234567 17 157 156 134 14 123'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
