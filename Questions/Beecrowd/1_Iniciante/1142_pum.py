n = int(input())

cont = 1
for i in range(n):
    for j in range(3):
        print(f"{cont} ", end = "")
        cont += 1
    print("PUM")
    cont += 1