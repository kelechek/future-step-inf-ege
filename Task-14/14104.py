num = 4**2022 - 6*4**522 + 5*64**510 - 3*2**330 - 100

cnt = 0
while num:
    if num % 8 == 7: cnt += 1
    num //= 8

print(cnt)