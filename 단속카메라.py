# 출처: https://programmers.co.kr/learn/courses/30/lessons/42884#

def solution(routes):
    routes.sort(key=lambda x:x[0])
    cnt = 1

    left = routes[0]
    for i, right in enumerate(routes):
        if i == 0:
            continue

        if right[0] < left[0]:
            temp = left
            left = right
            right = temp

        if right[0] <= left[1]:
            left = [right[0], min(left[1], right[1])]
        else:
            cnt += 1
            left = right

    return cnt
            
        
        
