ans = []
for N in range(1, 10_000):
    R = f'{N:b}'
    if N % 2 == 0:
        R += '01'
    else:
        R = '1' + R + '1'
    R = int(R, 2)
    if N in (5, 12):  # Проверка примеров
        print(R)
    if R > 156:
        ans.append(N)

print(min(ans))
