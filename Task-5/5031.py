ans = []
for N in range(28, 10_000):
    R = f'{N:b}'
    if sum(map(int, R)) % 2 == 0:
        R = '10' + R[2:] + '0'
    else:
        R = '11' + R[2:] + '1'
    R = int(R, 2)
    ans.append(R)

print(min(ans))
