# 출처: https://programmers.co.kr/learn/courses/30/lessons/42861

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    VISITED = [0] * n 
    VISITED[costs[0][0]] = 1

    while sum(VISITED) != n:
        for start, end, cost in costs:
            if VISITED[start] or VISITED[end]:
                if VISITED[start] and VISITED[end]:
                    continue
                else:
                    VISITED[start] = 1
                    VISITED[end] = 1
                    answer += cost
                    break
    
    return answer
