from itertools import permutations

graph = 'AE EH HG GC CF FA DE DF DB BH BG'.split()
matrix = '23 168 158 578 347 27 456 234'.split()

print(*range(1, 9))
for title in permutations('ABCDEFGH'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
