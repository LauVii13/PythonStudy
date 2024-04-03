import heapq

n, m = map(int, input().split())
nos = {i + 1: [] for i in range(n)}

for _ in range(m):
    a, b = map(int, input().split())
    nos[a].append(b)
    nos[b].append(a)

fila = [1]
heapq.heapify(fila)
visited = {1}

while fila:
    x = heapq.heappop(fila)
    print(x, end=" ")
    for e in nos[x]:
        if not e in visited:
            heapq.heappush(fila, e)
            visited.add(e)
