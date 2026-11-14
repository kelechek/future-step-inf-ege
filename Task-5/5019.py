ans = []
for N in range(1, 10_000):
    R = f'{N:b}'
    if N % 3 == 0:
        R += R[-3:]
    else:
        R += f'{N % 3 * 3:b}'
    R = int(R, 2)
    if N in (4, 12):  # Проверка примеров
        print(R)
    if R <= 170:
        ans.append(R)

print(max(ans))
