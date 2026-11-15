from string import printable as alph

ans = []
for x in alph[:21]:
    num_1 = int(f'82934{x}2', 21)
    num_2 = int(f'2924{x}{x}7', 21)
    num_3 = int(f'67564{x}8', 21)
    num = num_1 + num_2 + num_3
    if num % 20 == 0:
        ans.append([x, num // 20])

print(min(ans))
