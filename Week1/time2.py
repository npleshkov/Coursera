#h = int(input())
h = 348720


h1 = h // 3600
m = h // 60 % 60
m0 = str(m // 10)
m1 = str(m % 10)
s = h % 60
s0 = str(s // 10)
s1 = str(s % 10)

print(h1, m0 + m1, s0 + s1, sep=':')
