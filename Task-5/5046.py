ans = []
for N in range(1, 10_000):
    R = f'{N:b}'
    if N % 3 == 0:
        R += R[-3:]
    else:
        R += f'{N % 3 * 3:b}'
    R = int(R, 2)
    if N in (4, 6):  # Проверка примеров
        print(R)
    ans.append([abs(R - 130), N])

print(min(ans, key=lambda x: (x[0], -x[1])))
