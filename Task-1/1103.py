from itertools import permutations

graph = 'AB BE EH HC CA DA DB DG DF FC GE GH'.split()
matrix = '2347 16 158 157 348 278 146 356'.split()

print(*range(1, 9))
for title in permutations('ABCDEFGH'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
