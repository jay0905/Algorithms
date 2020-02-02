import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
dp = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
