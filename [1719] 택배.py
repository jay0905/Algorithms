import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

def solution(start):
    times = [INF] * (n + 1)
    times[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        current_time, current_node = heapq.heappop(heap)

        for adjacent_time, next_node in graph[current_node]:
            next_time = current_time + adjacent_time

            if next_time > times[next_node]:
                continue
            else:
                times[next_node] = next_time
                heapq.heappush(heap, (next_time, next_node))
                answer[next_node][start] = current_node

    return times

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((t, v))
    graph[v].append((t, u))

answer = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    solution(i)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print("-", end=" ")
        else:
            print(answer[i][j], end=" ")
    print()
