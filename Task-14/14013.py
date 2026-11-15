num = 2*729**1021 - 2*243**1022 + 81**1023 - 2*27**1024 - 1025
cnt = 0
while num:
    if num % 3 == 0: cnt += 1
    num //= 3
print(cnt)