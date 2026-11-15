from string import printable as alph

ans = []
for x in alph[:19]:
    num_1 = int(f'98897{x}21', 19)
    num_2 = int(f'2{x}923', 19)
    num = num_1 + num_2
    if num % 18 == 0:
        ans.append([x, num // 18])

print(max(ans))
