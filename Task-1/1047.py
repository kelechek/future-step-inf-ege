from itertools import permutations

graph = 'AH HB BF FG GE EA AC CH CF DE DG'.split()
matrix = '247 148 467 123 68 358 13 256'.split()

print(*range(1, 9))
for title in permutations('ABCDEFGH'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
