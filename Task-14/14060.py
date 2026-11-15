from string import printable as alph

ans = []
for x in alph[:19]:
    num_1 = int(f'76{x}79645', 19)
    num_2 = int(f'35{x}42', 19)
    num_3 = int(f'332{x}6', 19)
    num = num_1 + num_2 + num_3
    if num % 18 == 0:
        ans.append([x, num // 18])

print(max(ans))
