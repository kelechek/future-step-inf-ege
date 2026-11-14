from itertools import product, permutations


def f(w, x, y, z):
    return not ((w or not y) and x) or (y == z)


for i in product([0, 1], repeat=4):
    table = [
        (0, 1, i[0], 0),
        (1, 1, 0, i[1]),
        (i[2], 1, i[3], 0)
    ]
    if len(table) == len(set(table)):
        for title in permutations('wxyz'):
            check = [f(**dict(zip(title, row))) for row in table] == [0, 0, 0]
            if check:
                print(*title, sep='')

