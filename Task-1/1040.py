from itertools import permutations

graph = 'AD DC CF FG GE EA AH HG HB BC BD'.split()
matrix = '346 348 12 127 678 15 458 257'.split()

print(*range(1, 9))
for title in permutations('ABCDEFGH'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
