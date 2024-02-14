s = input()
n = [0, 0, 0]

for i in range(3):
    n[i] = int(s[i])

while True:   
    if n[0] * n[1] < 10 and n[0] * n[1] >= n[2]:
        break
    elif n[1] == 9:
        n[0] += 1
        n[1] = 0
        n[2] = 0
    else:
        n[1] += 1
        n[2] = 0
        
n[2] = n[0] * n[1]

result = f'{n[0]}{n[1]}{n[2]}'

print(result)