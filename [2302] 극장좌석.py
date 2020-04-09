import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
fixed = [int(input()) for _ in range(m)]

dp = [0, 1, 2]

for i in range(3, 41):
    dp.append(dp[i - 2] + dp[i - 1])

before_seat = 0
answer = 1
fixed.append(n + 1)

for i in range(m + 1):
    current_cnt = fixed[i] - before_seat - 1
    if current_cnt != 0:
        answer *= dp[current_cnt]
    before_seat = fixed[i]

print(answer)
