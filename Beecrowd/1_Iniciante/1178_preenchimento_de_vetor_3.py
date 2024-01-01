n = []
n.append(float(input()))

for i in range(1, 100):
    n.append(n[i - 1] / 2)

for i in range(len(n)):
    print(f"N[{i}] = {n[i]:.4f}")
