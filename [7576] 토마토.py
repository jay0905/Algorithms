from collections import deque
import sys
input = sys.stdin.readline

def spreadable(x, y):
    return 0 <= x < n and 0 <= y < m and box[x][y] == 0

def bfs(box):
    while queue:
        x, y = queue.popleft()

        DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for dx, dy in DELTAS:
            next_x, next_y = x + dx, y + dy
            if spreadable(next_x, next_y):
                queue.append((next_x, next_y))
                box[next_x][next_y] = box[x][y] + 1

if __name__ == "__main__":
    m, n = map(int, input().strip().split())
    box = [[int(x) for x in input().strip().split()] for _ in range(n)]

    queue = deque()
    FIRST_TOMATO = 100

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i, j))
                box[i][j] = FIRST_TOMATO

    bfs(box)

    maximum = 0
    ZERO = False
    for row in box:
        maximum = max(maximum, max(row))

        if 0 in row:
            ZERO = True

    if ZERO:
        print(-1)
    else:
        print(maximum - FIRST_TOMATO)
