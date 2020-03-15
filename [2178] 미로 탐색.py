from collections import deque
import sys
input = sys.stdin.readline

def movable(x, y, n, m, maze):
    if x != 0 or y != 0:
        return 0 <= x < n and 0 <= y < m and maze[x][y] == 1
    return False

def bfs(maze, queue, n, m):
    while queue:
        x, y = queue.popleft()

        DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for dx, dy in DELTAS:
            next_x, next_y = x + dx, y + dy
            if movable(next_x, next_y, n, m, maze):
                queue.append((next_x, next_y))
                maze[next_x][next_y] = maze[x][y] + 1


n, m = map(int, input().strip().split())
maze = [[int(x) for x in input().strip()] for _ in range(n)]

queue = deque()

queue.append((0, 0))
bfs(maze, queue, n, m)
print(maze[n-1][m-1])
