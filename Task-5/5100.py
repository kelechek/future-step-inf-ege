def get_digits_mult(num):
    return int(str(num)[0]) * int(str(num)[1]) * int(str(num)[2])


def get_digits_sum(num):
    return int(str(num)[0]) + int(str(num)[1]) + int(str(num)[2])


for num in range(99, 1000)[::-1]:
    result = str(get_digits_mult(num)) + str(get_digits_sum(num))
    if result == '33621':
        print(num)
        break