from itertools import product, permutations


def f(w, x, y, z):
    return x and (y <= z) and ((not y) <= ((not z) == w))


for i in product([0, 1], repeat=5):
    table = [
        (i[0], i[1], 0, 0),
        (i[2], 0, 0, i[3]),
        (1, i[4], 1, 1)
    ]
    if len(table) == len(set(table)):
        for title in permutations('wxyz'):
            check = [f(**dict(zip(title, row))) for row in table] == [1, 1, 0]
            if check:
                print(*title, sep='')
