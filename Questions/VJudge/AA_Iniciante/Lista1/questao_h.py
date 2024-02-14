n = int(input())
lista = list(map(int, input().split()))

sum1 = 0
sum2 = 0
ini = -1
fim = n

result = 0
while ini < fim:
    if sum1 == sum2:
        result = sum1
        ini += 1
        fim -= 1
        sum1 += lista[ini]
        sum2 += lista[fim]
    elif sum1 < sum2:
        ini += 1
        sum1 += lista[ini]
    else:
        fim -= 1
        sum2 += lista[fim]

print(result)
