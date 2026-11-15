num = 3*625**173 + 4*125**180 + 3*25**157 + 2*5**155 + 156
cnt = 0
while num:
    if num % 25 == 0: cnt += 1
    num //= 25
print(cnt)