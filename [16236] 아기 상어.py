import sys, heapq
input = sys.stdin.readline

def movable(x, y, space, n, shark, VISITED):
    return 0 <= x < n and 0 <= y < n and space[x][y] <= shark and VISITED[x][y] == 0

def bfs(i, j, n, space):
    queue = []
    heapq.heappush(queue, (0, i, j))
    VISITED = [[0] * n for _ in range(n)]
    shark = 2
    eaten_fish_cnt = 0
    answer_time = 0

    while queue:
        time, x, y = heapq.heappop(queue)

        # 만약 먹을 수 있으면 먹는다
        if 0 < space[x][y] < shark:
            space[x][y] = 0
            queue = []
            VISITED = [[0] * n for _ in range(n)]
            eaten_fish_cnt += 1
            answer_time += time
            time = 0

            if eaten_fish_cnt == shark:
                shark += 1
                eaten_fish_cnt = 0

        DELTAS = ((0, 1), (-1, 0), (1, 0), (0, -1))
        for dx, dy in DELTAS:
            nx, ny = x + dx, y + dy
            n_time = time + 1
            if movable(nx, ny, space, n, shark, VISITED):
                heapq.heappush(queue, (n_time, nx, ny))
                VISITED[nx][ny] = 1

    return answer_time

if __name__ == "__main__":
    n = int(input())
    space = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                space[i][j] = 0
                print(bfs(i, j, n, space))
