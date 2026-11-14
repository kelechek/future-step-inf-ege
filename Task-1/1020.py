from itertools import permutations

graph = 'AC CF FD DH HG GA AB BC BE ED'.split()
matrix = '56 378 26 68 17 134 258 247'.split()

print(*range(1, 9))
for title in permutations('ABCDEFGH'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
