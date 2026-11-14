from itertools import permutations

graph = 'AD DF FB BC CH HA EH EA EB GF GD'.split()
matrix = '567 38 248 367 168 145 14 235'.split()

print(*range(1, 9))
for title in permutations('ABCDEFGH'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
