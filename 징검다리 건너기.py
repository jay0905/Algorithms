# 출처: https://programmers.co.kr/learn/courses/30/lessons/64062

# 0의 연속구간 체크
def zero_check(mid, stones, k):
    cnt = 0

    for stone in stones:
        if stone < mid:
            cnt += 1

            if cnt == k:
                return False
        else:
            cnt = 0

    return True

def solution(stones, k):
    start = 0
    end = 200000000
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        if zero_check(mid, stones, k):
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    return answer
