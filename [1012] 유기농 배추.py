import sys
input = sys.stdin.readline

def movable(x, y, m, n, farm):
    return 0 <= x < n and 0 <= y < m and farm[x][y] == 1

def dfs(farm, stack, i, j, m, n, worms):
    while stack:
        x, y = stack.pop()

        DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for dx, dy in DELTAS:
            next_x, next_y = x + dx, y + dy
            if movable(next_x, next_y, m, n, farm):
                stack.append((next_x, next_y))
                farm[next_x][next_y] += VISITED


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().strip().split())
    farm = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().strip().split())
        farm[y][x] = 1

    stack = []
    VISITED = 100
    worms = 0
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                stack.append((i, j))
                farm[i][j] += VISITED
                worms += 1
                dfs(farm, stack, i, j, m, n, worms)

    print(worms)
