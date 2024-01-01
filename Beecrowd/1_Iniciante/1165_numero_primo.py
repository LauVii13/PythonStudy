n = int(input())

for j in range(n):
    x = int(input())

    primo = True
    for i in range(2, x):
        if x % i == 0:
            primo = False
            break
    if primo:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")
