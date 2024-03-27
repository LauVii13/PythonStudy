from math import ceil


def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)


t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())

    divisor = a * b
    resp_x, resp_y = -1, -1
    for i in range(a + 1, c + 1):
        mdc = gcd(max(i, divisor), min(i, divisor))
        div = divisor // mdc
        x = i // mdc
        k = ceil((b + 1) / div)
        y = div * k

        if y > b and y <= d:
            resp_x, resp_y = i, y
            break

    print(resp_x, resp_y)
