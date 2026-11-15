num = 49**7 + 7**21 - 7
cnt = 0
while num:
    if num % 7 == 6: cnt += 1
    num //= 7
print(cnt)