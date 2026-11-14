line = input()

syms = {'∨':'or', '∧':'and', '¬':'not ', '→':'<=', '≡':'=='}

res = ''
for i in line:
    res += syms[i] if i in syms else i

print(res)
