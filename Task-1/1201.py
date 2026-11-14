from itertools import permutations

graph = 'AB BE EG GH HC CD DF FB AD AC AG'.split()
matrix = '36 478 178 258 46 158 23 2346'.split()

print(*range(1, 9))
for title in permutations('ABCDEFGH'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
