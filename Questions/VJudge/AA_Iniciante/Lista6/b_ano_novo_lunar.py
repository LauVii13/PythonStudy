import heapq

n, m = map(int, input().split())
nos = {i + 1: set() for i in range(n)}

for _ in range(m):
    a, b = map(int, input().split())
    nos[a].add(b)
    nos[b].add(a)

fila = []
heapq.heapify(fila)
for e in nos[1]:
    heapq.heappush(fila, e)

visited = list(map(lambda x: False, range(n + 1)))
visited[1] = True

result = "1 "


while fila:
    x = heapq.heappop(fila)

    if not visited[x]:
        visited[x] = True
        result += f"{x} "
        for e in nos[x]:
            if not visited[e]:
                heapq.heappush(fila, e)

print(result)
