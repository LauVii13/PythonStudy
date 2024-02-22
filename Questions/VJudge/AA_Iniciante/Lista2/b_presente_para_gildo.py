def tira_s(s, t):
    t.append(s[0])
    s.pop(0)


def tira_t(t, u):
    u.append(t[-1])
    t.pop(-1)


s = [i for i in input()]
t = []
u = []
