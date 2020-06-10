import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
weights = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    weights[a - 1][b - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if weights[i][j] == 1 or (weights[i][k] == 1 and weights[k][j]):
                weights[i][j] = 1

for i in range(n):
    cnt = 0
    for j in range(n):
        if weights[i][j] == 0 and weights[j][i] == 0:
            cnt += 1

    print(cnt - 1)
