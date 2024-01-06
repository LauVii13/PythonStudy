x = int(input())

while True:
    z = int(input())
    if z > x:
        break

cont = 1
n = x + 1
soma = x

while True:
    cont += 1
    soma += n

    if soma > z:
        break
    n += 1

print(cont)
