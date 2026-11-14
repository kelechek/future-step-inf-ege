ans = []
for N in range(1, 10_000):
    R = f'{N:b}'
    R += str(sum(map(int, R)) % 2)
    R += str(sum(map(int, R)) % 2)
    R = int(R, 2)
    if R > 396:
        ans.append(R)

print(min(ans))
