ans = []
for N in range(1, 10_000):
    R = f'{N:b}'
    R += str(sum(map(int, R)) % 2)
    R += str(sum(map(int, R)) % 2)
    R = int(R, 2)
    if N in (7, 12):  # Проверка примеров
        print(R)
    if R > 253:
        ans.append(N)

print(min(ans))