def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'


ans = []
for N in range(1, 10_000):
    R = convert(N, 3)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += convert(sum(map(int, R)) * 2, 3)
    R = int(R, 3)
    if N in (8, 9):  # Проверка примеров
        print(R)
    if R % 2 != 0 and R > 520:
        ans.append(R)

print(min(ans))
