from itertools import product, permutations


def f(w, x, y, z):
    return not (y <= (x == w)) and (z <= x)


for i in product([0, 1], repeat=5):
    table = [
        (i[0], 1, 1, i[1]),
        (0, i[2], i[3], 0),
        (i[4], 0, 1, 0)
    ]
    if len(table) == len(set(table)):
        for title in permutations('wxyz'):
            check = [f(**dict(zip(title, row))) for row in table] == [1, 1, 1]
            if check:
                print(*title, sep='')

