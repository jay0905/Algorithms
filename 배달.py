import math
from collections import deque
# 출처: https://programmers.co.kr/learn/courses/30/lessons/12978

def bfs(start, maps, dists, K):
    queue = deque([start])
    dists[start] = 0

    while queue:
        y = queue.popleft()
        for x in range(1, len(maps)):
            if maps[y][x] != 0:
                if dists[x] > dists[y] + maps[y][x] and dists[y] + maps[y][x] <= K:
                    dists[x] = dists[y] + maps[y][x]
                    queue.append(x)

    return len([dist for dist in dists if dist <= K])
    

def solution(N, road, K):
    dists = [math.inf for _ in range(N + 1)]
    maps = [[0] * (N + 1) for _ in range(N + 1)]

    for frm, to, w in road:
        if maps[frm][to] == 0 and maps[to][frm] == 0:
            maps[frm][to], maps[to][frm] = w, w
        else:
            if maps[frm][to] > w:
                maps[frm][to], maps[to][frm] = w, w

    answer = bfs(1, maps, dists, K)
    return answer
