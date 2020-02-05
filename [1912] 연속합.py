import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().strip().split()))
dp = [lst[0]]

for i in range(1, n):
    dp.append(max(dp[-1] + lst[i], lst[i]))

print(max(dp))
