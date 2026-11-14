from itertools import product, permutations


def f(w, x, y, z):
    return (not x and y and z and not w) or (not x and y and not z and not w) or (x and y and z and not w)


for i in product([0, 1], repeat=7):
    table = [
        (1, i[0], i[1], i[2]),
        (0, i[3], 1, i[4]),
        (i[5], 0, 0, i[6])
    ]
    if len(table) == len(set(table)):
        for title in permutations('wxyz'):
            check = [f(**dict(zip(title, row))) for row in table] == [1, 1, 1]
            if check:
                print(*title, sep='')

