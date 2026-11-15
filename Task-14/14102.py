num = 3**333 + 3**22 - 9**111 - 9

cnt = 0
while num:
    if num % 3 == 2: cnt += 1
    num //= 3

print(cnt)