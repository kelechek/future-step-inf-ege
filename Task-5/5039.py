ans = []
for N in range(1, 100):
    R = f'{N:b}'
    if N % 3 == 0:
        R += R[-3:]
    else:
        R += f'{N % 3 * 3:b}'
    R = int(R, 2)
    if N in (4, 12):
        print(R)
    if R < 130:
        ans.append(N)

print(max(ans))
