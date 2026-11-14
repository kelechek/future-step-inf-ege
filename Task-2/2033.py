from itertools import product, permutations


def f(w, x, y, z):
    return not ((not x or y) and not w) or not (z and not (y and w))


for i in product([0, 1], repeat=7):
    table = [
        (0, i[0], i[1], 1),
        (i[2], 1, i[3], i[4]),
        (1, 0, i[5], i[6])
    ]
    if len(table) == len(set(table)):
        for title in permutations('wxyz'):
            check = [f(**dict(zip(title, row))) for row in table] == [0, 0, 0]
            if check:
                print(*title, sep='')

