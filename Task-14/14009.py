from string import printable as alph

ans = []
for x in alph[:15]:
    num_1 = int(f'123{x}5', 15)
    num_2 = int(f'1{x}233', 15)
    num = num_1 + num_2
    if num % 14 == 0:
        ans.append([x, num // 14])

print(min(ans))
