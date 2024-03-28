n = int(input())
di = {}
cont = 0
for _ in range(n):
    s = input()
    s2 = ""
    
    for i in range(len(s)-1, -1, -1):
        s2 += s[i]
        
    if di.get(s) == None and di.get(s2) == None:
        cont += 1
        di[s] = True

print(cont)