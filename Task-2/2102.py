from itertools import product, permutations


def f(w, x, y, z):
    return not (w <= (not (x <= y))) and ((not x) <= ((not y) == z))


for i in product([0, 1], repeat=5):
    table = [
        (i[0], 1, 1, 1),
        (i[1], i[2], 0, 0),
        (0, i[3], i[4], 0)
    ]
    if len(table) == len(set(table)):
        for title in permutations('wxyz'):
            check = [f(**dict(zip(title, row))) for row in table] == [0, 1, 1]
            if check:
                print(*title, sep='')
