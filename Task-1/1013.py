from itertools import permutations

graph = 'AG GB BF FD DC CE EA EB CF'.split()
matrix = '456 37 25 16 137 147 256'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
