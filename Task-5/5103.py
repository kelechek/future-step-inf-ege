for N in range(1, 10):
    # Шаг 1
    N_bin = f'{N:b}'
    # Шаг 2
    if N % 2:
        N_bin += "1"
    else:
        N_bin += "0"
    # Шаг 3
    if N_bin.count("1") % 3:
        R_bin = '10' + N_bin[2:]
    else:
        R_bin = '11' + N_bin[2:]

    R = int(R_bin, 2)
    if R >= 26:
        print(N)
        break