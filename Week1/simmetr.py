h = int(input())

h1 = str(h // 1000)
h2 = str(h // 100 % 10)
h3 = str(h // 10 % 10)
h4 = str(h % 10)

if (h1 == h4 and h2 == h3):
    print('1')
else:
    print('2')
