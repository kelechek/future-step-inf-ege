from itertools import product, permutations


def f(w, x, y, z):
    return not (x <= w) or (y == z) or y


for i in product([0, 1], repeat=7):
    table = [
        (i[0], 1, i[1], 0),
        (i[2], 0, 1, i[3]),
        (i[4], i[5], 0, i[6])
    ]
    if len(table) == len(set(table)):
        for title in permutations('wxyz'):
            check = [f(**dict(zip(title, row))) for row in table] == [0, 0, 0]
            if check:
                print(*title, sep='')

