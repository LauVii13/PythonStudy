n, l = map(int, input().split())

values = list(map(int, input().split()))

count = 0
for e in values:
    if e >= l:
        count += 1
    
print(count)