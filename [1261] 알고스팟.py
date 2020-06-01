import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

def dij(m, n, maze):
    wall_cnt = [[INF] * m for _ in range(n)]
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    wall_cnt[0][0] = 0

    while heap:
        current_cnt, x, y = heapq.heappop(heap)

        if (x, y) == (n - 1, m - 1):
            return current_cnt

        DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for dx, dy in DELTAS:
            next_x, next_y = x + dx, y + dy

            if 0 <= next_x < n and 0 <= next_y < m:
                next_cnt = current_cnt + maze[next_x][next_y]

                if next_cnt < wall_cnt[next_x][next_y]:
                    wall_cnt[next_x][next_y] = next_cnt
                    heapq.heappush(heap, (next_cnt, next_x, next_y))

m, n = map(int, input().split())
maze = [[int(x) for x in input().strip()] for _ in range(n)]

print(dij(m, n, maze))
