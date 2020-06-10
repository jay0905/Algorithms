import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
graph = [[INF] * n for _ in range(n)]

while True:
    a,b = map(int, input().split())

    if (a, b) == (-1, -1):
        break

    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

scores = [max(graph[i]) for i in range(n)]
print(min(scores), scores.count(min(scores)))

for i in range(n):
    if scores[i] == min(scores):
        print(i + 1, end=' ')
