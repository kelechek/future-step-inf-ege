from string import printable as alph

ans = []
for x in alph[:13]:
    num_1 = int(f'753{x}2', 13)
    num_2 = int(f'2{x}173', 13)
    num = num_1 + num_2
    if num % 12 == 0:
        ans.append([x, num // 12])

print(min(ans))
