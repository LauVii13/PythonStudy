v = [int(n) for n in input().split()]
a = v[0]
b = v[1]
c = v[2]
d = v[3]

if (b > c and d > a) and (c + d > a + b) and (c >= 0 and d >= 0) and (a % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
