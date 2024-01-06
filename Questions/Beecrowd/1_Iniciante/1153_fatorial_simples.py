n = int(input())

fat = 1
for i in range(n, 0, -1):
    fat *= i

print(fat)
