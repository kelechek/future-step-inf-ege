ans = []
for N in range(1, 10_000):
    R = f'{N:b}'
    R = R.replace('1', '*')
    R = R.replace('0', '1')
    R = R.replace('*', '0')
    R = '1' + R
    R += str(R.count('1') % 2)
    R = int(R, 2)
    if R > 180:
        ans.append(N)

print(min(ans))
