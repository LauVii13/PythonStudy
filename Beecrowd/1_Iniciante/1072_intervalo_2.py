n = int(input())

dentro = 0
fora = 0

for i in range(n):
    x = int(input())
    if x >= 10 and x <= 20:
        dentro += 1
    else:
        fora += 1

print(f'''{dentro} in
{fora} out''')