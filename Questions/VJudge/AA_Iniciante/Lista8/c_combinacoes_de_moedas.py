mod = 1000000007
n_moedas, final = map(int, input().split())
lista = [0 for _ in range(final + 1)]
lista[0] = 1
moedas = list(map(int, input().split()))

for i in range(1, final + 1):

    for m in moedas:
        if m > i:
            continue

        lista[i] = (lista[i] + lista[i - m]) % mod

print(lista[final])
