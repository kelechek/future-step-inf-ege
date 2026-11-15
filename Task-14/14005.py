num = 7*512**1912 + 6*64**1954 - 5*8**1991 - 4*8**1980 - 2022
cnt = 0
while num:
    if num % 8 == 7: cnt += 1
    num //= 8
print(cnt)