from itertools import permutations

graph = 'AB BD DG EA BC CD CE EF DF FG'.split()
matrix = '245 136 2567 16 137 234 35'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
