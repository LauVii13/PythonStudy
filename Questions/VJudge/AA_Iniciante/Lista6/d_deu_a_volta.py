import sys

sys.setrecursionlimit(2 * 10**5 + 81)


def dfs(n, m):
    visited[n] = True
    global x
    result.append(n)

    for i in cidades[n]:
        if m == i:
            continue
        if not visited[i]:
            if dfs(i, n):
                return True
        else:
            x = i
            final.append(x)
            for j in range(len(result) - 1, -1, -1):
                final.append(result[j])
                if result[j] == x:
                    break

            print(len(final))
            print(*final)
            exit(0)
    result.pop()


x = -1

n, m = map(int, input().split())
cidades = {i + 1: [] for i in range(n)}
visited = [False for _ in range(n + 1)]

result = []
final = []

for _ in range(m):
    a, b = map(int, input().split())
    cidades[a].append(b)
    cidades[b].append(a)
# print('4')

for k in range(1, n):
    # print('check do ', k)
    if not visited[k]:
        if dfs(k, -1):
            exit()
# print('6')

if x == -1:
    print("IMPOSSIBLE")
