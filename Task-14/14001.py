num = 7*512**120 - 6*64**100 + 8**210 - 255
cnt = 0
while num:
    if num % 8 == 0: cnt += 1
    num //= 8
print(cnt)