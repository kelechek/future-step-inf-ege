from itertools import permutations

graph = 'AB BC CE EG GD DF FA AC ED'.split()
matrix = '346 45 16 125 247 137 56'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
