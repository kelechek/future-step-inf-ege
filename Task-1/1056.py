from itertools import permutations

graph = 'AF FC CB BE EA DF DB DE'.split()
matrix = '256 13 245 356 134 14'.split()

print(*range(1, 7))
for title in permutations('ABCDEF'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
