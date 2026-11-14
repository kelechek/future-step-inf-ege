ans = []
for N in range(1, 10_000):
    R = f'{N:b}'
    if N % 2 == 0:
        R += R[-2:]
    else:
        R = '1' + R + '0'
    R = int(R, 2)
    if N in (10, 11):  # Проверка примеров
        print(R)
    if R < 100:
        ans.append(N)

print(max(ans))
