def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


n = int(input())
l = list(map(int, input().split()))
cont = 0

i = -1
while True:
    if i <= -len(l):
        break
    if gcd(max(l[i], l[i - 1]), min(l[i], l[i - 1])) != 1:
        l.insert(i, 1)
        cont += 1
        i -= 1
    i -= 1

print(cont)
for e in l:
    print(e, end=" ")
print()
