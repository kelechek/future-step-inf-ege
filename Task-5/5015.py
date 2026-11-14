ans = []
for N in range(1, 10_000):
    R = f'{N:b}'
    if N % 2 == 0:
        R = '1' + R + '00'
    else:
        R += f'{sum(map(int, R)):b}'
    R = int(R, 2)
    if N in (4, 13): # Проверка примеров
        print(R)
    if R > 190:
        ans.append([R, N])

print(min(ans))
