출처: https://programmers.co.kr/learn/courses/30/lessons/43104

def solution(N):
    TILES = 80
    side = [0] * (TILES + 1)
    side[1], side[2] = 1, 1
    
    for i in range(3, N + 1):
        side[i] = side[i - 1] + side[i - 2]
    
    answer = (side[N] * 4) + (side[N - 1] * 2) 
    return answer
    
