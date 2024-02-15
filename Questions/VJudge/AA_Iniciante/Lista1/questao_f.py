t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    degraus = list(map(int, input().split()))
    degraus.append(0)
    testes = list(map(int, input().split()))
    
    som = 0
    
    p1 = 0
    p2 = 0
    
    outs = []
    
    while p2 < len(testes):
        if testes[p2-1] > testes[p2] and p2 != 0:
            p1 = 0
            som = 0
        while degraus[p1] <= testes[p2]:
            som += degraus[p1]
            
            if p1 < len(degraus)-1:
                p1+=1
            else:
                break
                
                
        outs.append(som)    
        p2 += 1
        
    for i in outs:
        print(i, end=" ")
    print()
    