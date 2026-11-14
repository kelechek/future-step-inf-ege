from itertools import permutations

graph = 'AC CD DB BF FE ED DG GA AD'.split()
matrix = '37 57 147 37 26 57 12346'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
