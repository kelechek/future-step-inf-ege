# Функция для подсчета чётных цифр
def count_evens(num):
    evens = sum([1 for i in num
                 if int(i, 8) % 2 == 0])
    return evens


res = []
for N in range(10000):
    # Строим 8-ричную запись
    R = f'{N:o}'
    # Если кол-во нечётно
    if count_evens(R) % 2:
        R = R[-3:] + '46'
    # Если кол-во чётно
    else:
        R = f'{(N % 8 * 5):o}' + R
    # Переводим в десятичную
    R = int(R, 8)
    # Формируем ответ
    if N == 12:
        print(R)
        break