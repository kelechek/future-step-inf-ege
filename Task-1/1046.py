from itertools import permutations

graph = 'AD DB BE EF FA AC CE CB'.split()
matrix = '36 456 145 236 23 124'.split()

print(*range(1, 7))
for title in permutations('ABCDEF'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
