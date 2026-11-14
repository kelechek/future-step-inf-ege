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
        R += convert(N % 3 * 5, 3)
    R = int(R, 3)
    if N in (11, 12):  # Проверка примеров
        print(R)
    if R > 133:
        ans.append(R)

print(min(ans))
