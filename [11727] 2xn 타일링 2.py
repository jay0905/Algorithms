import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1, 3]

for _ in range(3, n + 1):
    dp.append((dp[-2]*2 + dp[-1]) % 10007)

print(dp[n])
