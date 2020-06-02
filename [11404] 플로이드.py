import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

def dij(i, answer):
    heap = []
    heapq.heappush(heap, (0, i))
    answer[i][i] = 0

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        if answer[i][current_node] < current_cost:
            continue

        for adjacent_cost, next_node in graph[current_node]:
            next_cost = current_cost + adjacent_cost

            if next_cost < answer[i][next_node]:
                answer[i][next_node] = next_cost
                heapq.heappush(heap, (next_cost, next_node))

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

answer = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dij(i, answer)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(answer[i][j] if answer[i][j] != INF else 0, end=' ')
    print()
