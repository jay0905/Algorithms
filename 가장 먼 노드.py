# 출처: https://programmers.co.kr/learn/courses/30/lessons/49189

def dfs(computers, VISITED, start):
    stack = [start]

    while stack:
        current = stack.pop()

        if VISITED[current] == 0:
            VISITED[current] = 1

        for node in range(len(computers)):
            if computers[current][node] == 1 and VISITED[node] == 0:
                stack.append(node)
    
def solution(n, computers):
    answer = 0
    VISITED = [0 for _ in range(n)]

    idx = 0
    while 0 in VISITED:
        if VISITED[idx] == 0:
            dfs(computers, VISITED, idx)
            answer += 1
        idx += 1
    
    return answer
