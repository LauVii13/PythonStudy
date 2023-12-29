x, y = [int(i) for i in input().split()]

count = 0
for i in range(1, y + 1):
    count += 1
    if count == x:
        print(i)
        count = 0
    else:
        print(i, end=" ")
        