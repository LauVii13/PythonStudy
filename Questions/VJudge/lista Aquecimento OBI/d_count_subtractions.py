a, b = map(int, input().split())
a, b = max(a, b), min(a, b)

count = 0
while a != b:
    if b == 0:
        count -= 1
        break
    if b == 1:
        count += a - b
        break
    count += a // b
    
    a, b = b, a % b
    
print(count)