from itertools import product, permutations


def f(w, x, y, z):
    return (x or y) and not (y == z) and not w


for i in product([0, 1], repeat=4):
    table = [
        (1, i[0], 1, i[1]),
        (0, 1, i[2], 0),
        (i[3], 1, 1, 0)
    ]
    if len(table) == len(set(table)):
        for title in permutations('wxyz'):
            check = [f(**dict(zip(title, row))) for row in table] == [1, 1, 1]
            if check:
                print(*title, sep='')
