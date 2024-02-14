n, k, q = map(int, input().split())

base = [0] * 200002

for _ in range(n):
    v_min, v_max = map(int, input().split())
    base[v_min] += 1
    base[v_max + 1] -= 1

somador = 0
for i in range(1, len(base)):
    somador += base[i]
    if somador >= k:
        base[i] = 1
    else:
        base[i] = 0

    base[i] += base[i - 1]


for _ in range(q):
    q_min, q_max = map(int, input().split())

    count = base[q_max] - base[q_min - 1]

    print(count)
