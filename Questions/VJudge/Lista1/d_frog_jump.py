n = int(input())

for _ in range(n):
    s = 'R'
    s += input()
    s += 'R'
    maior = 0
    count = 0
    for i in range(1, len(s)):
        count += 1
        if s[i] == 'R':
            if maior < count:
                maior = count
            count = 0
    print(maior)