# 출처: https://programmers.co.kr/learn/courses/30/lessons/62049#

from collections import deque

def solution(n):
    dp = [[], [0], [0, 0, 1], [0, 0, 1, 0, 0, 1, 1]]

    if n <= 3:
        return dp[n]

    for i in range(4, n + 1):
        paper = []
        previous = deque(dp[i - 1])

        for j in range(len(previous)):
            if j % 2 == 0:
                paper.append(0)
            else:
                paper.append(1)
            paper.append(previous.popleft())
        paper.append(1)
        
        dp.append(paper)

    return dp[-1]
