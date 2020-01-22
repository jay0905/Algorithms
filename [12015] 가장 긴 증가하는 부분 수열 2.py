import sys, bisect
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
ans = [0]

def solution():
    for i in range(n):
        if arr[i] > ans[-1]:
            ans.append(arr[i])
        elif arr[i] < ans[-1]:
            num = bisect.bisect_left(ans, arr[i])
            ans[num] = arr[i]
    return len(ans)-1

print(solution())
