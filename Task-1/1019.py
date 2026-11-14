from itertools import permutations

graph = 'AD DB BF FC CG GA EB EF EC EG'.split()
matrix = '47 357 2567 16 236 345 123'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
