from itertools import product, permutations


def f(w, x, y, z):
    return (not z and y and x and not w) or (not z and y and not x and not w) or (z and y and x and not w)


for i in product([0, 1], repeat=7):
    table = [
        (i[0], 1, i[1], i[2]),
        (i[3], 0, 1, i[4]),
        (0, i[5], 0, i[6])
    ]
    if len(table) == len(set(table)):
        for title in permutations('wxyz'):
            check = [f(**dict(zip(title, row))) for row in table] == [1, 1, 1]
            if check:
                print(*title, sep='')

