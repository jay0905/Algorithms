import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
dp1 = [0 for i in range(n)] # 증가하는 부분 수열
dp2 = [0 for i in range(n)] # 감소하는 부분 수열
ans = [0 for i in range(n)] # dp1 + dp2를 저장할 배열

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp1[i] = max(dp1[j], dp1[i])
    dp1[i] += 1

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[j], dp2[i])
    dp2[i] += 1

for i in range(n):
    ans[i] = dp1[i] + dp2[i] -1

print(max(ans))
