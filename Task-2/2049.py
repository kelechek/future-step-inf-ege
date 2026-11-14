from itertools import product, permutations


def f(w, x, y, z):
    return (x and not z and not w) or (x and not z and y)


for i in product([0, 1], repeat=7):
    table = [
        (1, i[0], i[1], i[2]),
        (0, i[3], 1, i[4]),
        (i[5], i[6], 0, 0)
    ]
    if len(table) == len(set(table)):
        for title in permutations('wxyz'):
            check = [f(**dict(zip(title, row))) for row in table] == [1, 1, 1]
            if check:
                print(*title, sep='')

