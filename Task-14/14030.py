ans = []
for x in range(1, 2031):
    num = 7**91 + 7**160 - x
    cnt = 0
    while num:
        if num % 7 == 0: cnt += 1
        num //= 7
    if cnt == 70:
        ans.append(x)
print(max(ans))