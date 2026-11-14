def convert(num):
    result = ''
    while num:
        result += str(num % 4)
        num //= 4
    return result[::-1]


res = []

for N in range(1, 1000):
    # Строим четверичную запись
    R = convert(N)
    # Если сумма цифр четверичной записи чётная
    if sum(map(int, R)) % 2 == 0:
        # 2 последние цифры
        R += R[-2:]
    # Если нечётная
    else:
        R = '2' + R + '0'
    # Переводим в десятичную
    R = int(R, 4)
    # Формируем ответ
    if R % 2 == 0 and R > 120:
        res.append(R)

print(min(res))