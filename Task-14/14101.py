num = 1331**650 - 55*121**610 + 77*11**510 - 3*11**100 - 221

cnt = 0
while num:
    if num % 11 == int('A', 36): cnt += 1
    num //= 11

print(cnt)