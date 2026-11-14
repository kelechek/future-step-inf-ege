ans = []
for N in range(1, 10_000):
    R = f'{N:b}'
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += f'{N % 3 * 3:b}'
    R = int(R, 2)
    if N in (9, 10):  # Проверка примеров
        print(R)
    if R >= 195:
        ans.append(R)

print(min(ans))
