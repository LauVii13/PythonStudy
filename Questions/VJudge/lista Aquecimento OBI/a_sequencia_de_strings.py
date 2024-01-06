n = int(input())
s = []
for i in range(n):
    s.append(input())


for e in range(len(s) - 1, -1, -1):
    print(s[e])