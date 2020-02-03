import sys
input = sys.stdin.readline

n = int(input())
line = [list(map(int, input().strip().split())) for _ in range(n)]
line.sort(key = lambda x:x[0])

dp = [0]*n

for i in range(n):
    for j in range(i):
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1

print(n - max(dp))
