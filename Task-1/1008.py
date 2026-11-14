from itertools import permutations

graph = 'AB BE EG GH HA AD DC CB FE FG'.split()
matrix = '68 568 457 35 234 12 38 127'.split()

print(*range(1, 9))
for title in permutations('ABCDEFGH'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
