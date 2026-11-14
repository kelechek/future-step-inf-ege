from itertools import permutations

graph = 'AH HF FE ED DG GA BF BH BC CG'.split()
matrix = '478 38 256 15 34 37 168 127'.split()

print(*range(1, 9))
for title in permutations('ABCDEFGH'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
