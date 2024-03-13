t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    print(10 ** (a - 1) + (10 ** (c - 1)), 10 ** (b - 1))
