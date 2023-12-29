n = int(input())

for i in range(n):
    v = [float(x) for x in input().split()]
    media = ((v[0] * 2) + (v[1] * 3) + (v[2] * 5)) / 10
    print(f"{media:.1f}")
    