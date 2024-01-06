n = int(input())

if n % 2 != 0:
    n -= 1

for i in range(2, n + 1, 2):
    print(f"{i}^2 = {i**2}")