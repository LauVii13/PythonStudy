t = int(input())

for _ in range(t):
    n = int(input())
    lista = [int(j) for j in input().split()]
    
    count = 0
    for e in lista:
        if e % 2 != 0:
            count += 1
    print(count)