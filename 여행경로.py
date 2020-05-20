# 출처: https://programmers.co.kr/learn/courses/30/lessons/43164#

from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)

    for start, arrive in tickets:
        routes[start].append(arrive)

    for key in routes.keys():
        routes[key].sort(reverse=True)

    stack = ["ICN"]
    answer = []
    
    while stack:
        top = stack[-1]

        if top not in routes or len(routes[top]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
        
    return answer[::-1]
