# 출처: https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import defaultdict, deque

def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    dists = [0] * (n + 1)

    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)

    dists[0] = -1
    dists[1] = -1
    queue = deque(graph[1])
    dist = 1

    while 0 in dists:
        for _ in range(len(queue)):
            current = queue.popleft()

            if dists[current] == 0:
                dists[current] = dist

                for v in graph[current]:
                    queue.append(v)

        dist += 1
        
    answer = dists.count(max(dists))
    return answer
