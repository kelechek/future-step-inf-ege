from itertools import permutations

graph = 'AC CB BH HD DA GA GC GE FH FE'.split()
matrix = '258 17 56 68 138 347 26 145'.split()

print(*range(1, 9))
for title in permutations('ABCDEFGH'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
