import sys
input = sys.stdin.readline

n, c = map(int, input().strip().split())
arr = [int(input()) for _ in range(n)]

def routerCnt(mid): # 간격에 따른 설치 가능한 공유기의 개수를 return하는 함수
    baseCase = arr[0]
    cnt = 1 # 설치할 공유기 수를 담는 변수. baseCase에 기본적으로 설치하므로 1에서 시작한다
    for i in range(1, n):
        if arr[i] - baseCase >= mid: # arr[i] 의 간격이 더 넓으면 설치 가능
            cnt += 1
            baseCase = arr[i]
    return cnt

def BinarySearch(c):
    start = 1
    end = arr[-1] - arr[0] # 최대 간격은 가장 큰 좌표에서 가장 작은 좌표를 뺀 것
    while start <= end:
        mid = (start + end) // 2 # mid가 간격이 된다
        router = routerCnt(mid)
        if router < c: # 이 간격에서 설치되는 공유기의 수가 c보다 작다면
            end = mid - 1 # 간격을 좁혀야 한다
        elif router >= c: # 크거나 같다면
            ans = mid  # 정답 후보이므로 ans에 값을 저장해두고
            start = mid + 1 # 간격을 넓혀야 한다.
    return ans

arr.sort()
print(BinarySearch(c))
