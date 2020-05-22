from collections import deque

def movable(x, y, n, m, maps):
    return 0 <= x < n and 0 <= y < m and maps[x][y] == 1  

def bfs(n, m, maps, queue):
    while queue:
        x, y = queue.popleft()

        if x == n - 1 and y == m - 1:
            return maps[x][y]

        DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for dx, dy in DELTAS:
            next_x, next_y = x + dx, y + dy
            
            if movable(next_x, next_y, n, m, maps):
                queue.append((next_x, next_y))
                maps[next_x][next_y] = maps[x][y] + 1

    return -1

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    start = (0, 0)
    queue = deque([start])
    answer = bfs(n, m, maps, queue)
                
    return answer
