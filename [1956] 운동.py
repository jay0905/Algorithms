import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

def dij(i):
    heap = []
    heapq.heappush(heap, (0, i))
    table[i][i] = 0

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if current_dist > table[i][current_node]:
            continue

        for adjacent_dist, next_node in graph[current_node]:
            next_dist = current_dist + adjacent_dist

            if next_dist < table[i][next_node]:
                table[i][next_node] = next_dist
                heapq.heappush(heap, (next_dist, next_node))

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

table = [[INF] * (v + 1) for _ in range(v + 1)]

for i in range(1, v + 1):
    dij(i)

for i in range(1, v + 1):
    for j in range(1, v + 1):
        if table[i][j] == INF:
            table[i][j] = 0

candidates = []

for i in range(1, v + 1):
    for j in range(1, v + 1):
        if table[i][j] != 0 and table[j][i] != 0:
            candidates.append(table[i][j] + table[j][i])

if candidates:
    print(min(candidates))
else:
    print(-1)
