from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
homes = [[int(x) for x in input().strip()] for _ in range(n)]

def is_there_neighbor(next_x, next_y, homes):
    return 0 <= next_x < n and 0 <= next_y < n and homes[next_x][next_y] != 0

def bfs(homes, queue, answer):
    cnt = 1
    while queue:
        x, y = queue.popleft()
        DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for dx, dy in DELTAS:
            next_x, next_y = dx + x, dy + y
            if is_there_neighbor(next_x, next_y, homes) and homes[next_x][next_y] == 1:
                homes[next_x][next_y] += VISITED
                cnt += 1
                queue.append((next_x, next_y))
    answer.append(cnt)

queue = deque()
answer = []
VISITED = 1

for i in range(n):
    for j in range(n):
        if homes[i][j] == 1:
            queue.append((i, j))
            homes[i][j] += VISITED
            bfs(homes, queue, answer)

print(len(answer))

answer.sort()
for a in answer:
    print(a)
