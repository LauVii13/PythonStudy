a = []
for i in range(100):
    a.append(float(input()))

for i in range(len(a)):
    if a[i] <= 10:
        print(f"A[{i}] = {a[i]:.1f}")
