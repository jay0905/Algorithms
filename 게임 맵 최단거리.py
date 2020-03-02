from collections import deque

def can_go(x, y, N, M, maps):
    return 0 <= x < N and 0 <= y < M and maps[x][y] == 1

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == (N-1, M-1):
            return maps[x][y]
        
        DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for dx, dy in DELTAS:
            next_x, next_y = x + dx, y + dy
            
            if can_go(next_x, next_y, N, M, maps):
                queue.append((next_x, next_y))
                maps[next_x][next_y] = maps[x][y] + 1
                                
    return -1
