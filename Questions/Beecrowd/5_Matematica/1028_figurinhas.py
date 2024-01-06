def mdc(n1, n2):
    while n2:
        n1, n2 = n2, n1%n2
    return n1

total = int(input())

for i in range(total):
    r, v = input().split()
    print(mdc(int(r), int(v)))
    