def tira_s(s, t):
    t.append(s[0])
    s.pop(0)


def tira_t(t):
    v = t[-1]
    t.pop(-1)
    return v


s = [i for i in input()]
t = []
u = ""

while len(s) > 0 or len(t) > 0:
    if len(t) == 0:
        tira_s(s, t)

    if len(s) == 0 or t[-1] < s[0]:
        u += tira_t(t)
    else:
        tira_s(s, t)

print(u)
