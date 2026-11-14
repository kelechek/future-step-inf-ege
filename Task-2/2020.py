from itertools import product, permutations


def f(w, x, y, z):
    return (y <= x) and not z and w


for i in product([0, 1], repeat=6):
    table = [
        (1, 0, i[0], i[1]),
        (1, 1, i[2], i[3]),
        (i[4], 1, 1, i[5])
    ]
    if len(table) == len(set(table)):
        for title in permutations('wxyz'):
            check = [f(**dict(zip(title, row))) for row in table] == [1, 1, 1]
            if check:
                print(*title, sep='')

