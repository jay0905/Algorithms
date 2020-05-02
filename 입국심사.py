# 출처: https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    start = 0
    end = max(times) * n 
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for time in times:
            cnt += mid // time

        if cnt >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer
