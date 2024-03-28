n, q = map(int, input().split())
s = [i for i in input()]

som = [0] * (n)

for i in range(1, n):
    som[i] = som[i-1]
    if s[i-1] == "A" and s[i] == "C":
        som[i] += 1
    
for _ in range(q):
    l, r = map(int, input().split())  
    print(som[r-1] - som[l-1])