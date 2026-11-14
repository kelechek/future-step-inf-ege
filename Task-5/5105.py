for K in range(1_000, 10_000):
    K = list(map(int, str(K)))
    S = sum(K)
    M = max(K)
    N = min(K)
    P_1 = S - M
    P_2 = S - N
    if P_1 >= P_2:
        L = str(P_2) + str(P_1)

    else:
        L = str(P_1) + str(P_2)
    if L == '1318':
        print(K)
        break