import sys
input = sys.stdin.readline

k, n = map(int, input().strip().split())
arr = [int(input()) for _ in range(k)]

# 랜선의 길이를 받아 만들 수 있는 랜선의 개수를 return하는 함수
def lanCount(mid):
    cnt = 0
    for i in range(k):
        cnt += (arr[i] // mid)
    return cnt

def binarySearch(n):
    start = 1
    end = arr[-1]
    while start <= end:
        mid = (start + end) // 2
        cnt = lanCount(mid)
        if cnt < n: # 만약 만들 수 있는 개수가 만들어야 하는 개수보다 적으면
            end = mid - 1 # 랜선의 길이를 줄여 더 많이 만들어야 함
        elif cnt >= n: # 더 크면 정답 후보이므로
            ans = mid # 정답 저장
            start = mid + 1 # 랜선의 길이를 늘일 여지가 있으므로
    return ans

arr.sort()
print(binarySearch(n))
