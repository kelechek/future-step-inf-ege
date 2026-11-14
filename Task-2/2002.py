from itertools import product, permutations


def f(a, b, c, d):
    return (not a and not b) or (b == c) or d


for i in product([0, 1], repeat=4):
    table = [
        (i[0], i[1], 1, i[2]),
        (1, 0, i[3], 1),
        (0, 0, 1, 1)
    ]
    if len(table) == len(set(table)):
        for title in permutations('abcd'):
            check = [f(**dict(zip(title, row))) for row in table] == [0, 0, 0]
            if check:
                print(*title, sep='')

