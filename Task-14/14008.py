num = 216**1315 - 4*36**1502 + 5*36**1510 - 3*6**1331 - 253

cnt = 0
while num:
    if num % 6 == 0: cnt += 1
    num //= 6

print(cnt)