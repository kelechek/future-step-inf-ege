num = 3*16**2018 - 2*8**1028 - 3*4**1100 - 2**1050 - 2022
cnt = 0
while num:
    if num % 4 == 3: cnt += 1
    num //= 4
print(cnt)