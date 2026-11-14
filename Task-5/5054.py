ans = []
for N in range(17, 10_000):
    R = f'{N:b}'
    if N % 2 == 0:
        R = '10' + R
    else:
        R = '1' + R + '01'
    R = int(R, 2)
    ans.append(R)

print(min(ans))
