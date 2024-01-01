n = int(input())

x = [int(i) for i in input().split()]

menor = min(x)
pos = x.index(menor)

print(f"Menor valor: {menor}")
print(f"Posicao: {pos}")
