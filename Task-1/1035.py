from itertools import permutations

graph = 'AB BG GE EF FA AD DF CE CD CB'.split()
matrix = '457 567 45 136 123 247 126'.split()

print(*range(1, 8))
for title in permutations('ABCDEFG'):
    if all(str(title.index(i) + 1) in matrix[title.index(j)] for i, j in graph):
        print(*title)
