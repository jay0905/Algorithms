import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

def solution(x, graph):
    dists = [INF] * (n + 1)
    dists[x] = 0
    heap = []
    heapq.heappush(heap, (0, x))

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        for adjacent_dist, next_node in graph[current_node]:
            next_dist = current_dist + adjacent_dist

            if next_dist > dists[next_node]:
                continue
            else:
                dists[next_node] = next_dist
                heapq.heappush(heap, (next_dist, next_node))

    return dists

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
graph_rev = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((t, v))
    graph_rev[v].append((t, u))

path1 = solution(x, graph)
path2 = solution(x, graph_rev)
path1[0] = path2[0] = 0


for i in range(len(path1)):
    path1[i] += path2[i]

print(max(path1))
