x = int(input())
y = int(input())

if y > x:
    x, y = y, x

if y % 2 != 0:
    y += 1

sum = 0
for i in range(y + 1, x, 2):
    sum += i

print(sum)