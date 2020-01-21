import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

# mid 보다 작은 수의 개수를 return하는 함수
def numCount(mid):
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid//i, n)
    return cnt

def binarySearch(k):
    start = 1
    end = k
    while start <= end:
        mid = (start + end) // 2
        num = numCount(mid)
        if num < k:
            start = mid + 1
        elif num >= k:
            ans = mid
            end = mid - 1
    return ans

print(binarySearch(k))

