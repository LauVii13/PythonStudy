n = int(input())
lista = list(map(int, input().split()))

pref = [0] * (n + 1)
suf = [0] * (n + 1)

for i in range(n):
    pref[i + 1] = lista[i] + pref[i]

for i in range(n - 1, -1, -1):
    suf[i] = lista[i] + suf[i + 1]

print(pref, suf)
