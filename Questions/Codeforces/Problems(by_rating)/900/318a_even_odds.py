n, k = map(int, input().split())

meio = (n + 1) // 2

if k > meio:
    print((k - meio) * 2)
else:
    print((k - 1) * 2 + 1)
