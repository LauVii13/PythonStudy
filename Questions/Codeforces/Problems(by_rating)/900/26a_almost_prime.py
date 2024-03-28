def quase_primo(v):
    divprimos = 0
    prim = 2
    while v > 1:
        if v % prim == 0:
            divprimos += 1
            
            if divprimos >= 3:
                return 0
            
            while v % prim == 0:
                v //= prim
        
        if prim != 2:
            prim+= 1
            
        prim+= 1
    
    if divprimos == 2:
        return 1
    else:
        return 0

n = int(input())
cont = 0

# como primeiro numero que tem dois divisores primos distintos é 6
for i in range(6, n + 1):
    cont += quase_primo(i)

print(cont)