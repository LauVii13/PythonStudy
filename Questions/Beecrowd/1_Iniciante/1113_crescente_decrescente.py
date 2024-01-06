while True:
    x, y = [int(i) for i in input().split()]
    
    if x == y: break
    
    if x > y:
        print("Decrescente")
    else:
        print("Crescente")