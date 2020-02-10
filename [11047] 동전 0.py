import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
arr = [int(input()) for _ in range(n)]
cnt = 0

for i in range(1, n+1):
    while arr[n-i] <= k:
        k -= arr[n-i]
        cnt += 1
    if k == 0:
        break

print(cnt)
