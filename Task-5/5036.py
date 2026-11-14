ans = []
for N in range(1, 10_000):
    R = f'{N:b}'
    if not (R.count('1') % 2):
        R = '10' + R[2:] + '0'
    else:
        R = '11' + R[2:] + '1'
    R = int(R, 2)
    if N in (4, 6):
        print(R)
    if R > 480:
        ans.append(N)

print(min(ans))