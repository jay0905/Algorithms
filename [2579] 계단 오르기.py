import sys
input = sys.stdin.readline

n = int(input())
stair = [int(input()) for _ in range(n)]
dp = []

dp.append(stair[0])
dp.append(stair[0] + stair[1])
dp.append(max(stair[0] + stair[2], stair[1] + stair[2]))

for i in range(3, n):
    dp.append(max(stair[i] + dp[i-2], stair[i] + stair[i-1] + dp[i-3]))

print(dp[-1])
