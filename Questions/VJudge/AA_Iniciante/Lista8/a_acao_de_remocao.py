import sys

sys.setrecursionlimit(10**6)


def calcula(i, j):
    if i > j or j < 0:
        return 0

    op1 = lista[i] + min(calcula(i + 2, j), calcula(i + 1, j - 1))
    op2 = lista[j] + min(calcula(i + 1, j - 1), calcula(i, j - 2))

    return max(op1, op2)


n = int(input())
lista = list(map(int, input().split()))
print(calcula(0, len(lista) - 1))
