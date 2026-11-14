def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'


ans = []
for N in range(3, 10_000):
    R = convert(N, 3)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += convert((N % 3) * 3, 3)
    R = int(R, 3)
    if N in (4, 6):  # Проверка примеров
        print(R)
    if R <= 150:
        ans.append(N)

print(max(ans))
