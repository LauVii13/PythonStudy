n = int(input())

for i in range(n):
    x, y = [int(a) for a in input().split()]
    
    if x > y:
        x, y = y, x
    
    soma = 0
    for j in range(x + 1, y):
        if j % 2 != 0:
            soma += j
    
    print(soma)