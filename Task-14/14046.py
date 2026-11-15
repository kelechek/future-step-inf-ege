from string import printable as alph

ans = []
for x in alph[:30]:
    num_1 = int(f'7{x}A9F', 30)
    num_2 = int(f'1B3{x}', 30)
    num = num_1 + num_2
    if num % 29 == 0:
        ans.append([x, num // 29])

print(min(ans))
