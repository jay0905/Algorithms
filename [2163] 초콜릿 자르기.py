import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j == 1:
            dp[i][j] = i - 1
        else:
            dp[i][j] = dp[i][j-1] + i

print(dp[n][m])
