for N in range(1, 20)[::-1]:
    N_1 = N - N % 4
    N_bin = f'{N_1:b}'
    N_bin += str(sum(map(int, N_bin)) % 2)
    N_bin += str(sum(map(int, N_bin)) % 2)
    R = int(N_bin, 2)

    if R < 47:
        print(N)
        break