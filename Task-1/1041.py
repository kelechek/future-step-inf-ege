from itertools import permutations

graph = 'AF FE ED DC CB GA GF GE GD GC GB'.split()
matrix = '345 467 14 123567 147 24 245'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
