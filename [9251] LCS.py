import sys
input = sys.stdin.readline

a = list(input().strip())
b = list(input().strip())

aLen = len(a)
bLen = len(b)
dp = [[0] * (aLen+1) for _ in range(bLen+1)]

for i in range(1, bLen+1):
    for j in range(1, aLen+1):
        if a[j-1] == b[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[bLen][aLen])
