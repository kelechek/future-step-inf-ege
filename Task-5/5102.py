for N in range(1, 30)[::-1]:
    N_bin = f'{N:b}'
    len_num = len(N_bin)
    if len_num % 2 == 0:
        mid_idx = len_num // 2
        R_bin = N_bin[:mid_idx] + '1' + N_bin[mid_idx:]
    else:
        R_bin = N_bin

    R = int(R_bin, 2)
    if R <= 26:
        print(N)
        break