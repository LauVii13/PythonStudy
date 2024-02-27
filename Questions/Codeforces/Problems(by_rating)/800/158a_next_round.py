n, k = map(int, input().split())

numbers = list(map(int, input().split()))

count = 0
for i in range(n):
    if numbers[i] < numbers[k - 1] or numbers[i] <= 0:
        break
    else:
        count += 1

print(count)
