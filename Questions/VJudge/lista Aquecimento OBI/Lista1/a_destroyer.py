t = int(input())

for _ in range(t):
    n = int(input())
    l = [0] * 100
    
    a = list(map(int, input().split()))
    
    for i in a:
        l[i] += 1
    
    ordem = True
    for i in range(len(l) - 1):
        if l[i] < l[i+1]:
            ordem = False
            print('NO')
            break
    if ordem:
        print('YES')