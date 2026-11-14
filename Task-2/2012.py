from itertools import product, permutations


def f(w, x, y, z):
    return ((x <= w) and ((not y) <= z)) <= ((z == x) or (w and not y))


for i in product([0, 1], repeat=5):
    table = [
        (0, i[0], 0, 0),
        (i[1], 1, 1, 1),
        (i[2], i[3], i[4], 0)
    ]
    if len(table) == len(set(table)):
        for title in permutations('wxyz'):
            check = [f(**dict(zip(title, row))) for row in table] == [0, 0, 0]
            if check:
                print(*title, sep='')

