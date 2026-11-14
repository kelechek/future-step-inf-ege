from itertools import permutations

graph = 'AC CB BH HD DA GA GC GE FH FE'.split()
matrix = '368 34 126 27 67 135 458 17'.split()

print(*range(1, 9))
for title in permutations('ABCDEFGH'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
