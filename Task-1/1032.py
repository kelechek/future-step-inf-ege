from itertools import permutations

graph = 'AB BD DF FE EC CA GD GF GC'.split()
matrix = '457 46 567 12 136 235 13'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
