while True:
    n = int(input())
    if n == 0: break
    
    matriz = [[1 for i in range(n)] for j in range(n)]
    
    tot = (n // 2) + (n % 2)
    for x in range(2, tot + 1):
        for i in range(x - 1, len(matriz) - (x - 1)):
            for j in range(x - 1, len(matriz) - (x - 1)):
                matriz[i][j] = x        

    for lin in range(len(matriz)):
        for i in range(len(matriz[lin])):
                print("%3d" %(matriz[lin][i]), end="")
                if i != len(matriz[lin]) - 1:
                    print(end=" ")
        print()
    print()