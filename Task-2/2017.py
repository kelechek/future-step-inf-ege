from itertools import product, permutations


def f(w, x, y, z):
    return not (y and not x) and not (x == z) and w


for i in product([0, 1], repeat=4):
    table = [
        (0, 0, i[0], 1),
        (0, 1, 0, 1),
        (i[1], i[2], 0, i[3])
    ]
    if len(table) == len(set(table)):
        for title in permutations('wxyz'):
            check = [f(**dict(zip(title, row))) for row in table] == [1, 1, 1]
            if check:
                print(*title, sep='')

