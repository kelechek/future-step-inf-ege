from itertools import permutations

graph = 'BC CG GE ED DB DA AF FE FG'.split()
matrix = '24 135 256 157 234 37 46'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
