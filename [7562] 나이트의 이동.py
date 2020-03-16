from collections import deque
import sys
input = sys.stdin.readline

def movable(x, y, i):
    return 0 <= x < i and 0 <= y < i and VISITED[x][y] == 0

def bfs(i, queue, VISITED, target):
    while queue:
        x, y = queue.popleft()
        if (x, y) == target:
            return VISITED[x][y]

        DELTAS = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
        for dx, dy in DELTAS:
            next_x, next_y = x + dx, y + dy

            if movable(next_x, next_y, i):
                VISITED[next_x][next_y] = VISITED[x][y] + 1
                queue.append((next_x, next_y))

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        i = int(input())
        current = tuple(map(int, input().strip().split()))
        target = tuple(map(int, input().strip().split()))

        queue = deque()
        queue.append(current)
        VISITED = [[0] * i for _ in range(i)]
        print(bfs(i, queue, VISITED, target))
