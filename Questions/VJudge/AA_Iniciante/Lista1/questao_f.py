t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    degraus = list(map(int, input().split()))
    degraus.append(0)
    
    somatoria = list(map(lambda x: 0, degraus))
    somatoria[0] = degraus[0]

    for i in range(1, len(degraus)):
        somatoria[i] = degraus[i] + somatoria[i - 1]

        
    testes = list(map(int, input().split()))
    med = list(map(lambda x: 0, range(max(testes)+1)))
    print(med)
    
    som = 0
    
    p1 = 0
    p2 = 0
    
    outs = []
    
    while p2 < len(testes):
        if testes[p2-1] > testes[p2] and p2 != 0:
            for 
            p1 = 0
            som = 0
        while degraus[p1] <= testes[p2]:
            som += degraus[p1]
            
            if p1 < len(degraus)-1:
                p1+=1
            else:
                break
                
                
        outs.append(som)
        med[testes[p2]] = p1
        p2 += 1
        
    for i in outs:
        print(i, end=" ")
    print()
    