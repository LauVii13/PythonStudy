n = int(input())
lista = list(map(int, input().split()))

pref = [0] * (n + 1)
suf = [0] * (n + 1)

for i in range(n):
    pref[i + 1] = lista[i] + pref[i]
    suf[-i - 2] = lista[i - 1] + suf[-i - 1]

result = 0
ini = 0
fim = n

while ini <= fim:
    if pref[ini] == suf[fim]:
        result = pref[ini]
        ini += 1
        fim -= 1

    while pref[ini] < suf[fim]:
        ini += 1
    while pref[ini] > suf[fim]:
        fim -= 1

print(result)
