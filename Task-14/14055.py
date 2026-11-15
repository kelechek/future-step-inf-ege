from string import printable as alph

ans = []
for x in alph[:23]:
    num_1 = int(f'761{x}035', 23)
    num_2 = int(f'338{x}932', 23)
    num = num_1 + num_2
    if num % 22 == 0:
        ans.append([x, num // 22])

print(min(ans))
