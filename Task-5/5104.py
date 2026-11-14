for N in range(1, 100)[::-1]:
    N_bin = f'{N:b}'
    if N % 3:
        remainder = N % 3
        remainder += 1
        remainder += 3
        N_bin += f'{remainder:b}'
    else:
        N_bin += N_bin[-3:]
    R = int(N_bin, 2)
    if R <= 416:
        print(R)
        break