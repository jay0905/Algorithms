# 출처: https://programmers.co.kr/learn/courses/30/lessons/12927

import heapq

def solution(n, works):
    works = [-work for work in works]
    heapq.heapify(works)

    for i in range(n):
        if works[0] < 0:
            heapq.heappush(works, heapq.heappop(works) + 1)
        else:
            break

    answer = sum(work**2 for work in works)
    return answer
