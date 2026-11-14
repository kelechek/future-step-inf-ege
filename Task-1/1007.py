from itertools import permutations

graph = 'AC CE EG GF FA BA BF DC DH HE'.split()
matrix = '68 47 45 237 368 15 248 157'.split()

print(*range(1, 9))
for title in permutations('ABCDEFGH'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
