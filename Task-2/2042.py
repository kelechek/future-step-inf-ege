from itertools import product, permutations


def f(w, x, y, z):
    return not (y <= x) or (z <= w) or not z


for i in product([0, 1], repeat=7):
    table = [
        (i[0], 0, i[1], i[2]),
        (0, 1, i[3], i[4]),
        (1, i[5], i[6], 0)
    ]
    if len(table) == len(set(table)):
        for title in permutations('wxyz'):
            check = [f(**dict(zip(title, row))) for row in table] == [0, 0, 0]
            if check:
                print(*title, sep='')

