import sys
input = sys.stdin.readline

n = int(input())
boxes = list(map(int, input().strip().split()))
dp = [0] * n

for i in range(n):
    for j in range(i):
        if boxes[j] < boxes[i] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
