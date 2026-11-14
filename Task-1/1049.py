from itertools import permutations

graph = 'AH HF FE EG GB BA CB CG CD DF'.split()
matrix = '47 458 67 125 246 35 138 27'.split()

print(*range(1, 9))
for title in permutations('ABCDEFGH'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
