import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1: 
            return -1
        one = heapq.heappop(scoville) 
        two = heapq.heappop(scoville) 
        heapq.heappush(scoville, one + two*2)
        cnt += 1
    return cnt


