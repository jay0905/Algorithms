import sys
input = sys.stdin.readline

n = int(input())
dp = [4] * 50001
dp[0] = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i - j*j >= 0:
            dp[i] = min(dp[i], dp[i - j*j] + 1)
        else:
            break

print(dp[n])
