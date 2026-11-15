from string import printable as alph

ans = []
for x in alph[:27]:
    num_1 = int(f'123{x}24', 27)
    num_2 = int(f'135{x}78', 27)
    num = num_1 + num_2
    if num % 26 == 0:
        ans.append([x, num // 26])

print(max(ans))
