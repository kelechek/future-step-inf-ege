def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'


ans = []
for N in range(1, 300):
    R = convert(N, 3)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += convert(sum(map(int, R)) * 3, 3)
    R = int(R, 3)
    if N in (8, 9):
        print(R)
    if R > 208 and R % 2:
        ans.append(R)

print(min(ans))
