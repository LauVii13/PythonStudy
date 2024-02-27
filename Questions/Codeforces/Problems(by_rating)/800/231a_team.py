t = int(input())

result = 0
for _ in range(t):
    n = list(map(int, input().split()))
    if sum(n) >= 2:
        result += 1
print(result)
