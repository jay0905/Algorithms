import sys
input = sys.stdin.readline

n = int(input())
cards = [0] + list(map(int, input().strip().split()))
dp = [0] * (n + 1)

for i in range(n + 1):
    for j in range(i + 1):
        dp[i] = max(dp[i], cards[j] + dp[i - j])

print(dp[n])
