import math

a, b = map(int, input().split())

d = {}
if (a == 0 and b != 0) or a - b < 0:
    print(0)
elif a == b:
    print("infinity")
else:
    div = math.ceil(math.sqrt(a - b))
    cont = 0
    for i in range(1, div + 1):
        if (a - b) % i == 0:
            j = (a - b) // i

            if j > b and (not j in d):
                cont += 1
                d[j] = True
            if i > b and i < j and (not i in d):
                cont += 1
                d[i] = True

    print(cont)
