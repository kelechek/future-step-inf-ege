ans = []
for N in range(1, 16):
    R = f'{N:b}'
    if sum(map(int, R)) % 2 == 0:
        R = '10' + R[2:] + '1'
    else:
        R = '11' + R[2:] + '0'
    R = int(R, 2)
    if N in (4, 6): # Проверка примеров
        print(R)
    ans.append(R)

print(max(ans))
