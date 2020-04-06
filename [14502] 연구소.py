from itertools import combinations
import sys
input = sys.stdin.readline

def spreadable(next_x, next_y, n, m, VISITED):
    return 0 <= next_x < n and 0 <= next_y < m and new_map[next_x][next_y] == 0 and VISITED[next_x][next_y] == True


def dfs(n, m, new_map, VISITED):
    stack = []
    stack.append((i, j))

    while stack:
        x, y = stack.pop()
        VISITED[x][y] = False

        DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for dx, dy in DELTAS:
            next_x, next_y = x + dx, y + dy
            if spreadable(next_x, next_y, n, m, VISITED):
                new_map[next_x][next_y] = 2
                stack.append((next_x, next_y))


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    maps = [list(map(int, input().strip().split())) for _ in range(n)]
    blanks = []
    safe_section = []

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                blanks.append((i, j))

    blank_combi = list(combinations(blanks, 3))

    for combi in blank_combi:
        new_map = list(map(list, maps))
        VISITED = [[True] * m for _ in range(n)]

        for x, y in combi:
            new_map[x][y] = 1

        for i in range(n):
            for j in range(m):
                if new_map[i][j] == 2 and VISITED[i][j] == True:
                    dfs(n, m, new_map, VISITED)

        zero_cnt = 0
        for row in new_map:
            zero_cnt += row.count(0)

        safe_section.append(zero_cnt)

    print(max(safe_section))
