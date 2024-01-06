import math

def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

while True:
    try:
        v = input().split()
        

        r1 = int(v[0])
        x1 = int(v[1])
        y1 = int(v[2])
        r2 = int(v[3])
        x2 = int(v[4])
        y2 = int(v[5])

        if r2 > r1:
            print("MORTO")
        elif distancia(x1, y1, x2, y2) + r2 > r1:
            print("MORTO")
        else:
            print("RICO")
            
    except EOFError:
        break