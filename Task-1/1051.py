from itertools import permutations

graph = 'AB BH HF FD DC CE EA AH GE GF GC'.split()
matrix = '567 348 278 27 168 15 134 235'.split()

print(*range(1, 9))
for title in permutations('ABCDEFGH'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
