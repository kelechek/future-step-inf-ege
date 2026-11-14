ans = []
for N in range(1, 13):
    R = f'{N:b}'
    if N % 2 == 0:
        R = '10' + R
    else:
        R = '1' + R + '01'
    R = int(R, 2)
    if N in (4, 5):  # Проверка примеров
        print(R)
    ans.append(R)

print(max(ans))
