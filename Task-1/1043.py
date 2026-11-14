from itertools import permutations

graph = 'AF FC CD DB BE EG GA GF BC'.split()
matrix = '24 134 267 125 47 37 356'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
