import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

answer = 0

for i in range(n):
    cnt = 0
    for j in range(n):
        cnt += graph[i][j] + graph[j][i]

    if cnt == n - 1:
        answer += 1

print(answer)
