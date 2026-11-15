num = 5*216**155 + 4*36**156 - 4*6**157 - 2023
cnt = 0
while num:
    if num % 6 == 0: cnt += 1
    num //= 6
print(cnt)