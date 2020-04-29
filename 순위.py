# 출처: https://programmers.co.kr/learn/courses/30/lessons/49191

from collections import defaultdict

def solution(n, results):
    win = defaultdict(set)
    lose = defaultdict(set)

    for result in results:
        win[result[0]].add(result[1])
        lose[result[1]].add(result[0])

    for i in range(1, n + 1):
        for winner in lose[i]:
            win[winner].update(win[i])

        for loser in win[i]:
            lose[loser].update(lose[i])

    answer = 0
    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1

    return answer
