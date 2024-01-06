vetor = []
vetor.append(int(input()))

for i in range(9):
    vetor.append(vetor[i] * 2)

for i in range(len(vetor)):
    print(f"N[{i}] = {vetor[i]}")
