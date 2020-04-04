import sys
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().strip().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for x in range(n):
    for y in range(n):
        
        if map[x][y] == 0:
            break

        nx = x + map[x][y]
        ny = y + map[x][y]

        if 0 <= nx < n:
            dp[nx][y] += dp[x][y]
        if 0 <= ny < n:
            dp[x][ny] += dp[x][y]

print(dp[-1][-1])
