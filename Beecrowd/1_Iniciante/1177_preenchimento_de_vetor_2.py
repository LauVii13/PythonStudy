vetor = []
t = int(input())

while True:
    for i in range(t):
        vetor.append(i)
        if len(vetor) >= 1000:
            break

    if len(vetor) >= 1000:
        break

for i in range(len(vetor)):
    print(f"N[{i}] = {vetor[i]}")
