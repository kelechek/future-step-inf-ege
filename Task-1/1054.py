from itertools import permutations

graph = 'AF FB BE ED DA GD GE GC CA CB'.split()
matrix = '367 346 124 237 67 125 145'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
