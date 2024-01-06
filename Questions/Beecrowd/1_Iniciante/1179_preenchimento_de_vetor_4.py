par = []
impar = []
for j in range(15):
    x = int(input())

    if x % 2 == 0:
        par.append(x)

        if len(par) == 5:
            for i in range(len(par)):
                print(f"par[{i}] = {par[i]}")
            par = []
    else:
        impar.append(x)
        if len(impar) == 5:
            for i in range(len(impar)):
                print(f"impar[{i}] = {impar[i]}")
            impar = []

for i in range(len(impar)):
    print(f"impar[{i}] = {impar[i]}")

for i in range(len(par)):
    print(f"par[{i}] = {par[i]}")
