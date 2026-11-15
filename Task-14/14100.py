num = 4*25**2022 - 2*5**2000 + 125**1011 - 3*5**100 - 660

cnt = 0
while num:
    if num % 5 == 4: cnt += 1
    num //= 5

print(cnt)