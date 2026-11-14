ans = []
for N in range(1, 10_000):
    R = f'{N:b}'
    if sum(map(int, R)) % 2 == 0:
        R = '1' + R[2:] + '0'
    else:
        R = '11' + R[2:] + '1'
    R = int(R, 2)
    if N in (4, 6): # Проверка примеров
        print(R)
    if R > 25:
        ans.append([R, N])

print(min(ans))
