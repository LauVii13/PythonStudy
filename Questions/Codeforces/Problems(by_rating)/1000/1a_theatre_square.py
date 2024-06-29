n, m, a = map(int, input().split())

h, w = n // a, m // a
h = h + 1 if n % a != 0 else h
w = w + 1 if m % a != 0 else w

print(h * w)
