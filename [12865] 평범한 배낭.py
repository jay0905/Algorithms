# python3으로 채점할 시 시간초과 (PyPy로 채점)

import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(n)]

weights = [ele[0] for ele in arr]
value = [ele[1] for ele in arr]

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w = weights[i-1]
        v = value[i-1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v + dp[i - 1][j - w], dp[i-1][j])

print(dp[n][k])
