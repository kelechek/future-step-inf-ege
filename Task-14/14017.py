from string import printable as alph

ans = []
for x in alph[:15]:
    num_1 = int(f'97968{x}15', 15)
    num_2 = int(f'7{x}233', 15)
    num = num_1 + num_2
    if num % 14 == 0:
        ans.append([x, num // 14])

print(min(ans))
