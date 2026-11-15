from string import printable as alph

ans = []
for x in alph[:29]:
    num_1 = int(f'463{x}7921', 29)
    num_2 = int(f'8241{x}153', 29)
    num = num_1 + num_2
    if num % 28 == 0:
        ans.append([x, num // 28])

print(min(ans))
