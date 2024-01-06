n, x = map(int, input().split())

values = list(map(int, input().split()))

soma = 0
for e in values:
    if e <= x:
        soma += e
    
print(soma)