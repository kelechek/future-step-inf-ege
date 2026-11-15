from string import printable as alph

ans = []
for x in alph[:15]:
    num_1 = int(f'99658{x}29', 15)
    num_2 = int(f'102{x}023', 15)
    num = num_1 + num_2
    if num % 14 == 0:
        ans.append([x, num // 14])

print(max(ans))
