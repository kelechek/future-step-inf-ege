num = 343**515 - 6*49**520 + 5*49**510 - 3*7**530 - 550
cnt = 0
while num:
    if num % 7 == 6: cnt += 1
    num //= 7
print(cnt)