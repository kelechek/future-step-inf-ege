from itertools import permutations

graph = 'AF FH HC CB BD DG GA GF ED EB EH'.split()
matrix = '234 157 147 138 268 58 23 456'.split()

print(*range(1, 9))
for title in permutations('ABCDEFGH'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
