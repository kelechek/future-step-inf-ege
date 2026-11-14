from itertools import product, permutations


def f(w, x, y, z):
    return (x <= y) or not (w <= z)


table = [
    (1, 0, 0, 1),
    (0, 0, 0, 1),
    (1, 0, 1, 1)
]
for title in permutations('wxyz'):
    check = [f(**dict(zip(title, row))) for row in table] == [0, 0, 0]
    if check:
        print(*title, sep='')
