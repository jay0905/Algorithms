# 출처: https://programmers.co.kr/learn/courses/30/lessons/12979

import math

def solution(n, stations, w):
    w_scope = 1 + 2*w
    cnt = 0
    
    for i in range(len(stations)):
        if i == 0:
            cnt += math.ceil((stations[i] - w - 1) / w_scope)
        else:
            cnt += math.ceil(((stations[i] - w) - (stations[i - 1] + w) - 1) / w_scope)

    if n not in stations:
        cnt += math.ceil((n - (stations[-1] + w)) / w_scope)

    return cnt
    
