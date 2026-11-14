from itertools import permutations

graph = 'AB BH HF FD DC CE EA AH GE GC GF'.split()
matrix = '247 148 578 126 38 47 136 235'.split()

print(*range(1, 9))
for title in permutations('ABCDEFGH'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
