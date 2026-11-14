from itertools import product, permutations


def f(w, x, y, z):
    return not (x or y) and not w or not (z or w) and y


for i in product([0, 1], repeat=8):
    table = [
        (i[0], 1, i[1], i[2]),
        (i[3], i[4], 1, i[5]),
        (i[6], 1, i[7], 1)
    ]
    if len(table) == len(set(table)):
        for title in permutations('wxyz'):
            check = [f(**dict(zip(title, row))) for row in table] == [1, 1, 1]
            if check:
                print(*title, sep='')

